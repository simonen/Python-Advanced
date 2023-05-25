def math_operations(*floats, **kwargs):
    floats = list(floats)
    while floats:
        kwargs['a'] += float(floats.pop(0)) if len(floats) > 0 else 0
        kwargs['s'] -= float(floats.pop(0)) if len(floats) > 0 else 0
        if len(floats) > 0:
            num = float(floats.pop(0))
        else:
            break
        kwargs['d'] /= num if num != 0 else 1 if len(floats) > 0 else 1
        kwargs['m'] *= float(floats.pop(0)) if len(floats) > 0 else 1

    result = [f"{x[0]}: {x[1]:.1f}" for x in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
