text = list(input())

symbols = []
for i in sorted(text):
    if i not in symbols:
        print(f"{i}: {text.count(i)} time/s")
        symbols.append(i)
