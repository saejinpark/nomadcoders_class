import requests
from bs4 import BeautifulSoup
def remoteok_get_jobs(word):
    url = f"https://remoteok.com/remote-{word}-jobs"
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    db = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table")
    jobs = table.find_all("tr", {"class", "job"})
    for i in jobs:
        job = {}
        name = i.find("h3").get_text(strip=True)
        title = i.find("h2").get_text(strip=True)
        tooltip = i.find("div", {"class", "tooltip"}).string
        location = i.find("div", {"class", "location"}).string
        temp = i.find_all("td", {"class", "tags"})
        tags = ""
        for j in temp:
            for k in j.find_all("a"):
                tags += "#" + k.get_text(strip=True)
        time = i.find("time").get_text(strip=True)
        url = "https://remoteok.com" + i.find("a").attrs["href"]
        job["no"] = len(db) + 1
        job["name"] = name
        job["title"] = title
        job["tooltip"] = tooltip
        job["location"] = location
        job["tags"] = tags
        job["time"] = time
        job["url"] = url
        db.append(job)
    return db