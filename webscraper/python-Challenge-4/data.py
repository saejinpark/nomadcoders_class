import requests
from bs4 import BeautifulSoup
from save import save_to_file

def make_data(blands):
    for bland in blands:
        data = []
        result = requests.get(bland["url"])
        soup = BeautifulSoup(result.text, "html.parser")
        NormalInfo = soup.find("div", {"id": "NormalInfo"})
        NormalInfo_tr = NormalInfo.find_all("tr", {"class" != "summaryView"})
        for i in NormalInfo_tr:
            try:
                data.append({
                    "local": i.find("td", {"class": "local"}).get_text(),
                    "title": i.find("td", {"class": "title"}).find("span", {"class": "company"}).string,
                    "paragraph": i.find("td", {"class": "title"}).find("span", {"class": "title"}).string,
                    "data": i.find("td", {"class": "data"}).string,
                    "pay": i.find("td", {"class": "pay"}).get_text(),
                })
            except:
                pass
        save_to_file(bland, data)