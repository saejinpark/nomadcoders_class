import csv
def remoteok_save_to_file(word, jobs):
    file = open(f"./data/remoteok/remoteok_{word}_jobs.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["no", "name", "title", "tooltip", "location", "tags", "time"])
    
    for job in jobs:
        list_job = list(job.values())
        print(list_job)
        writer.writerow(list_job)
