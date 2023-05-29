food = list(map(int, input().split(", ")))
stamina = list(map(int, input().split(", ")))

conquered = []
days = 7
peaks = [
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
]

while days and peaks and food:
    portion = food.pop()
    stam = stamina.pop(0)
    if portion + stam >= peaks[0][1]:
        peak = peaks.pop(0)
        conquered.append(peak[0])

    days -= 1

if peaks:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
else:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')

if conquered:
    print('Conquered peaks:', *conquered, sep='\n')
