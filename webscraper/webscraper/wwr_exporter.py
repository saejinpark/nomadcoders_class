import csv
def wwr_save_to_file(word, jobs):
    for i in jobs.keys():
        file = open(f"./data/wwr/wwr_{word}_{i}.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["no","category", "company", "title", "date", "time", "local", "url"])
        for job in jobs[i]:
            list_job = list(job.values())
            writer.writerow(list_job)