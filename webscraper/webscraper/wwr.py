import requests
from bs4 import BeautifulSoup
def wwr_get_jobs(word):
    categories = {}
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    jobs = soup.find_all("section", {"class", "jobs"})
    for job in jobs:
        category = job.find("h2").find("a").get_text()
        categories[category] = []
        features = job.find_all("li", {"class", "feature"})
        for feature in features:
            try:
                feature_body = feature.find_all("a")[1]
                company = feature_body.find("span", {"class", "company"}).string
                title = feature_body.find("span", {"class", "title"}).string
                date = feature_body.find("span", {"class", "date"}).string
                time = feature_body.find_all("span", {"class", "company"})[1].string
                local = feature_body.find_all("span", {"class", "company"})[2].string
                url = feature_body.attrs["href"]
                feature_data = {}
                feature_data["no"] = len(categories[category]) + 1
                feature_data["category"] = category
                feature_data["company"] = company
                feature_data["title"] = title
                feature_data["date"] = date
                feature_data["time"] = time
                feature_data["local"] = local
                feature_data["url"] = "https://weworkremotely.com" + url
                categories[category].append(feature_data)
            except:
                pass
    return categories

def wwr_get_jobs_tr(categories):
  conversion = [];
  for i in categories:
    for j in categories[i]:
      conversion.append(j)
  return conversion