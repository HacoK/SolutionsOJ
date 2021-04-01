if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        raw_input = [int(x) for x in input().split()]
        jobs = []
        for i in range(N):
            jobs.append((raw_input[i*3],raw_input[i*3+1],raw_input[i*3+2]))
        job_count = 0
        job_profit = 0

        ddls = [x[1] for x in jobs]
        for ddl in range(max(ddls),0,-1):
            cur_jobs = []
            for job in jobs:
                if job[1] >= ddl:
                    cur_jobs.append(job)
            if len(cur_jobs) != 0:
                job_count += 1
                max_job = max(cur_jobs,key=lambda job:job[2])
                job_profit += max_job[2]
                jobs.remove(max_job)
        
        print(job_count,job_profit)