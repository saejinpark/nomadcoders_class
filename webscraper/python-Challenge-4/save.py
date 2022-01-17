import csv


def save_to_file(company, Announcements):
    file = open(".//data//" + company["title"].replace('/', '_') + ".csv", mode="w",
                newline='', encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["local", "title", "paragraph", "data", "pay"])
    for i in Announcements:
        writer.writerow(list(i.values()))
