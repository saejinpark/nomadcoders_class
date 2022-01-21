import requests
from bs4 import BeautifulSoup

def so_get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def so_extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find("h3", {
        "class": "mb4"
    }).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(
        strip=True).strip("•").strip(" \r").strip("\n")
    job_id = html['data-jobid']
    return {
        'title': title,
        'company': company,
        'location': location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def so_extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = so_extract_job(result)
            job["no"] = len(jobs)+1
            jobs.append(job)
    return jobs


def so_get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
    last_page = so_get_last_page(url)
    jobs = so_extract_jobs(last_page, url)
    return jobs
