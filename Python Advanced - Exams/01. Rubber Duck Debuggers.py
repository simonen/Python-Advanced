time_table = list(map(int, (input().split())))
tasks = list(map(int, input().split()))

ducks = {'Darth Vader Ducky': range(61),
         'Thor Ducky': range(61, 121),
         'Big Blue Rubber Ducky': range(121, 181),
         'Small Yellow Rubber Ducky': range(181, 240)}

awards = {'Darth Vader Ducky': 0,
          'Thor Ducky': 0,
          'Big Blue Rubber Ducky': 0,
          'Small Yellow Rubber Ducky': 0}

while time_table:
    value = time_table[0] * tasks[-1]

    for k, v in ducks.items():
        if value in v:
            awards[k] += 1
            time_table.pop(0)
            tasks.pop()
            break
    else:
        tasks[-1] -= 2
        time_table.append(time_table.pop(0))

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(*[f"{k}: {v}" for k, v in awards.items()], sep='\n')
