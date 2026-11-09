rows, cols = map(int, input().split())
string = input()

new_string = string * (rows * cols // len(string) + 1)
direction = 1

for i in range(0, rows * cols, cols):
    print(new_string[i: i + cols][::direction])
    direction *= -1
