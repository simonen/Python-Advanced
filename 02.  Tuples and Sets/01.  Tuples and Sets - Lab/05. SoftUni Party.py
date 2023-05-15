guests = set()

for _ in range(int(input())):
    code = input()
    if len(code) == 8:
        guests.add(code)

command = input()

while command != "END":

    if command in guests:
        guests.remove(command)

    command = input()

print(len(guests))
[print(i) for i in sorted(guests)]
