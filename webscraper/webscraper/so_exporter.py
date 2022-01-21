import csv

def so_save_to_file(word, jobs):
  file = open(f"./data/so/so_{word}_jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["No","title", "company", "location", "link"])
  for job in jobs:
    list_job = list(job.values())
    writer.writerow(list_job[-1:] + list_job[:-1])
  return