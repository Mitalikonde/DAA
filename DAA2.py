class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)

    # Initialize result array and tracking variables
    result = [None] * max_deadline
    job_count = 0
    total_profit = 0

    # Iterate through sorted jobs
    for job in jobs:
        # Find a free slot for this job, starting from the last possible slot
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if result[j] is None:
                result[j] = job.id
                job_count += 1
                total_profit += job.profit
                break

    # Print the scheduled jobs and the total profit
    print("Scheduled Jobs:", [job for job in result if job is not None])
    print("Total Profit:", total_profit)

# Input number of jobs
n = int(input("Enter the number of jobs: "))
jobs = []

# Input job details
for i in range(n):
    id = input("Enter job ID: ")
    deadline = int(input(f"Enter deadline for job {id}: "))
    profit = int(input(f"Enter profit for job {id}: "))
    jobs.append(Job(id, deadline, profit))

# Perform job sequencing
job_sequencing(jobs)
