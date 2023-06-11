jobs = list(map(int, input().split(", ")))
index = int(input())

cycles = 0
is_done = False

while jobs:
    job_index = jobs.index(min(jobs))
    job = jobs[job_index]

    if index == job_index:
        is_done = True

    cycles += job
    jobs[job_index] = 1000000

    if is_done:
        break

print(cycles)