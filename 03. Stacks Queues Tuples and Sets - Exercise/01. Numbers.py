seq1 = set(map(int, input().split()))
seq2 = set(map(int, input().split()))

funcs = {"Add First": lambda s, y: s.update(y),
        "Add Second": lambda s, y: s.update(y),
        "Remove First": lambda s, y: s.difference_update(y),
        "Remove Second": lambda s, y: s.difference_update(y),
        "Check Subset": lambda x, y: x.issubset(y) or y.issubset(x)}

for _ in range(int(input())):
    line = input().split()
    comm = " ".join(line[:2])
    args = set(map(int, line[2::]))
    seq_n = seq1 if line[1] == "First" else seq2
    if comm == "Check Subset":
        print(funcs[comm](seq1, seq2))
    else:
        funcs[comm](seq_n, args)

print(", ".join(map(str, sorted(seq1))))
print(", ".join(map(str, sorted(seq2))))