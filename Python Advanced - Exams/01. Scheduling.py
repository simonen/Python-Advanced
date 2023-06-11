jobs = list(map(int, input().split(", ")))
index = int(input())

cycles = 0

while True:
    job_index = jobs.index(min(jobs))
    job = jobs[job_index]

    cycles += job
    jobs[job_index] = 1000000

    if index == job_index:
        print(cycles)
        break
