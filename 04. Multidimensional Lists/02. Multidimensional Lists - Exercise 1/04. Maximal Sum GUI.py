import tkinter as tk
from math import inf

DEFAULT_COLOR = "lavender"
EVEN_COLOR = "mistyrose"
# Initiate App
root = tk.Tk()
root.title("Matrix")
# root.geometry("600x600")
game_area = tk.Frame(root, bg="steelblue")
game_area.grid(padx=10, pady=10)
board_frame = tk.LabelFrame(game_area, text="Board", font=("JetBrainsMono", 14, "bold"), relief="flat", bd=2,
                            padx=6, pady=6, borderwidth=2, bg="steelblue", fg="white")
board_frame.grid(row=0, column=0, padx=(0, 8), sticky="n")

matrix = [
    list(map(int, "1 5 5 2 4".split())),
    list(map(int, "2 1 4 14 3".split())),
    list(map(int, "3 7 11 2 8".split())),
    list(map(int, "4 8 12 16 4".split())),
    ]

# Backend Logic

def block_sum(block: list):
    return sum(sum(row) for row in block)

def sub_matrix_coords(start_row: int, start_col: int, height: int, width: int):
    coords = []
    for row in range(start_row, start_row + height):
        coords.append([(row, col) for col in range(start_col, start_col + width)])
    return coords

def window_size(sub_rows, sub_cols, s, clamp: bool):
    if clamp:
        bucket_height = min(s, sub_rows)
        bucket_width = min(s, sub_cols)
        return bucket_height, bucket_width
    if sub_rows < s or sub_cols < s:
        raise ValueError("Window size must be <= matrix dimensions")
    return s, s

def read_from_coords(matrix, coords):
    res = []
    for b in coords:
        res.append([matrix[x][y] for x, y in b])
    return res

def max_sum_coords(matrix, s: int, clamp):
    sub_rows = len(matrix)
    sub_cols = len(matrix[0])
    height, width = window_size(sub_rows, sub_cols, s, clamp)
    best_row, best_col = 0, 0
    best_sum = -inf
    for row in range(sub_rows - height + 1):
        for col in range(sub_cols - width + 1):
            block_coords = sub_matrix_coords(row, col, height, width)
            block = read_from_coords(matrix, block_coords)
            curr_sum = block_sum(block)
            if curr_sum > best_sum:
                best_sum = curr_sum
                best_row, best_col = row, col

    max_sum = best_sum
    return sub_matrix_coords(best_row, best_col, height, width), max_sum

editing = {"widget": None, "label": None, "row": None, "col": None}

def commit_edit(cancel=False):
    """Commit whatever is currently being edited (or cancel)."""
    if editing["widget"] is None:
        return

    entry = editing["widget"]
    label = editing["label"]
    row, col = editing["row"], editing["col"]

    # Clear state FIRST so re-entrant calls can't double-fire
    editing["widget"] = None
    editing["label"] = None
    editing["row"] = None
    editing["col"] = None

    if not cancel:
        raw = entry.get().strip()
        try:
            matrix[row][col] = int(raw)
        except ValueError:
            pass  # keep old value on bad input

    label.config(text=str(matrix[row][col]))
    label.grid(row=row, column=col, padx=1, pady=1)
    entry.destroy()

    # Auto-update AFTER the matrix is written
    if not cancel:
        update_submatrix()

def start_edit(event, row, col):
    # If another cell is mid-edit, commit it first
    if editing["widget"] is not None:
        if editing["row"] == row and editing["col"] == col:
            commit_edit()

            return

    label = event.widget
    label.grid_forget()

    # NOTE: parent is board_frame, so it lives in the grid
    entry = tk.Entry(board_frame, width=6, justify="center",
                     font=("JetBrainsMono", 14, "bold"))
    entry.insert(0, str(matrix[row][col]))
    entry.grid(row=row, column=col, padx=1, pady=1)
    entry.focus_set()
    entry.select_range(0, tk.END)

    editing.update(widget=entry, label=label, row=row, col=col)

    entry.bind("<Return>",   lambda e: commit_edit())
    entry.bind("<FocusOut>", lambda e: commit_edit() if editing["widget"] is entry else None)
    entry.bind("<Escape>",   lambda e: commit_edit(cancel=True))

size = 3

ROWS, COLS = len(matrix), len(matrix[0])
labels = [[None] * COLS for _ in range(ROWS)]
sub_labels = [[None] * size for _ in range(size)]

def grid(array: list):
    ROWS = len(array)
    COLS = len(array[0])
    for r in range(ROWS):
        for c in range(COLS):
            ch = matrix[r][c]
            lbl = tk.Label(board_frame, text=f"{ch}", width=6, height=3,
                           font=("JetBrainsMono", 14, "bold"), relief="flat", bd=1, bg=DEFAULT_COLOR)
            lbl.grid(row=r, column=c, padx=1, pady=1)
            lbl.bind("<Button-1>", lambda ev, r=r, c=c: start_edit(ev, r, c))
            labels[r][c] = lbl

### Board loop

grid(matrix)

### Submatrix

bottom_frame = tk.LabelFrame(game_area, text="Submatrix", font=("JetBrainsMono", 14, "bold"), relief="flat", bd=2, padx=6,
                           pady=6, bg="steelblue", fg="white")
bottom_frame.grid(row=ROWS+1, column=0, sticky="nsew")

coords = max_sum_coords(matrix, size, True)[0]

for i, b in enumerate(coords):
    for c_in_b, (r, c) in enumerate(b):
        ch = matrix[r][c]
        lbl = tk.Label(bottom_frame, text=f"{ch}", width=6, height=3,
                       font=("JetBrainsMono", 14, "bold"), relief="flat", bd=1,
                       bg=DEFAULT_COLOR)
        lbl.grid(row=i, column=c_in_b, padx=1, pady=1)   # ← fixed positions
        sub_labels[i][c_in_b] = lbl

def update_submatrix():
    coords, total = max_sum_coords(matrix, size, True)
    for i, b in enumerate(coords):
        for j, (r, c) in enumerate(b):
            sub_labels[i][j].config(text=str(matrix[r][c]))
    if "Max" in stats:
        stats["Max"].config(text=total)
    color_sum(EVEN_COLOR)

side_frame = tk.LabelFrame(game_area, text="Stats", font=("JetBrainsMono", 14, "bold"), relief="flat", bd=2, padx=6,
                           pady=6, bg="steelblue", fg="white")
side_frame.grid(row=0, column=1, sticky="n")

stats = {}
for i, name in enumerate(["Max",]):
    tk.Label(side_frame, text=name, anchor="w", width=8, bg="steelblue", fg="white").grid(row=i, column=0, sticky="w")
    stats[name] = tk.Label(side_frame, text="—", anchor="w", width=8, bg="steelblue", fg="white", pady=1)
    stats[name].grid(row=i, column=1, sticky="w")

def even_nums(n: int):
    if n % 2 == 0:
        return "lavender"
    return "mistyrose"

def reset_color(n):
    return "lavender"

colors = {"evens": even_nums, "reset": reset_color}

def color_grid(color):
    for r in range(ROWS):
        for c in range(COLS):
            if color == DEFAULT_COLOR:
                labels[r][c].config(bg=color)   # Update the label instead of recreating it

def color_sum(color):
    color_grid(DEFAULT_COLOR)
    coords = max_sum_coords(matrix, size, True)[0]
    for b in coords:
        for r, c in b:
            labels[r][c].config(bg=color)

def matrix_stats():
    max_sum = max_sum_coords(matrix, size, True)[1]
    stats["Max"].config(text=max_sum)

tk.Button(
    side_frame,
    text="Max Window",
    command=lambda: color_sum(EVEN_COLOR), font=("JetBrainsMono", 10), relief="flat", padx=1, pady=3, bg="steelblue",
    fg="white"
).grid(row=3, column=0, columnspan=2, sticky="nsew")

tk.Button(
    side_frame,
    text="Reset",
    command=lambda: color_grid(DEFAULT_COLOR), font=("JetBrainsMono", 10), relief="flat", padx=1, pady=3, bg="steelblue",
    fg="white"
).grid(row=4, column=0, columnspan=2, sticky="nsew", pady=3)

tk.Button(
    side_frame,
    text="Calculate Max",
    command=lambda: matrix_stats(), font=("JetBrainsMono", 10), relief="flat", padx=1, pady=3, bg="steelblue",
    fg="white"
).grid(row=5, column=0, columnspan=2, sticky="nsew", pady=3)

tk.Button(
    side_frame,
    text="Update Submatrix",
    command=lambda: update_submatrix(), font=("JetBrainsMono", 10), relief="flat", padx=1, pady=3, bg="steelblue",
    fg="white"
).grid(row=6, column=0, columnspan=2, sticky="nsew", pady=3)

root.mainloop()