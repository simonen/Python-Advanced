eggs = list(map(int, input().split(", ")))
papers = list(map(int, input().split(", ")))

boxed = 0

while eggs and papers:
    egg = eggs.pop(0)
    paper = papers.pop()

    if egg == 13:
        papers.append(papers.pop(0))
        papers.insert(0, paper)

    if egg + paper in range(1, 51) and egg != 13 and egg > 0:
        boxed += 1

    if egg <= 0:
        papers.append(paper)

if boxed:
    print(f"Great! You filled {boxed} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")