workers = input().split()
nectar = input().split()
process = input().split()

honey = 0
while workers and nectar:
    bee = workers.pop(0)
    juice = nectar.pop()
    if int(bee) == 0 and int(juice) == 0:
        continue
    if int(juice) >= int(bee):
        op = process.pop(0)
        honey += abs(eval(f"{int(bee)} {op} {int(juice)}"))
    else:
        workers.insert(0, bee)

print(f"Total honey made: {honey}")
if workers:
    print(f"Bees left: {', '.join(workers)}")
if nectar:
    print(f"Nectar left: {', '.join(nectar)}")