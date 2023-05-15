def subtract(collection_f):
    res = collection_f[0]
    for i in range(1, len(collection_f)):
       res -= collection_f[i]

    return res


def multiply(collection_f):
    res = 1
    for i in range(0, len(collection_f)):
       res *= collection_f[i]

    return res


def divide(collection_f):
    res = collection_f[0]
    for i in range(1, len(collection_f)):
       res //= collection_f[i]

    return res


string = input().split()

nums = []
operators = '-+*/'
operator = []
string2 = []

for i in string:
    if i in operators:
        operator.append(i)
        string2.append(tuple(nums))
        nums = []
    else:
        nums.append(int(i))


result = 0
for j in range(len(string2)):
    if operator[j] == "-":
        if j == 0:
            result = subtract(string2[j])
            continue
        result -= sum(string2[j])
    elif operator[j] == "+":
        result += sum(string2[j])
    elif operator[j] == "*":
        if j == 0:
            result = multiply(string2[j])
            continue
        result *= multiply(string2[j])
    elif operator[j] == "/":
        if j == 0:
            result = divide(string2[j])
            continue
        result //= multiply(string2[j])

print(result)