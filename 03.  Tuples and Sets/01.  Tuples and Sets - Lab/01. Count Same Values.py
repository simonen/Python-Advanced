occ = []
nums = input().split()
for i in nums:
    if i not in occ:
        occ.append(i)
        print(f"{float(i):.1f} - {nums.count(i)} times")