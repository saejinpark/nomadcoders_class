import requests
from bs4 import BeautifulSoup

def get_super_blands():
    alba_url = "https://www.alba.co.kr/"

    bland_list = []


    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser")
    super_brand = soup.find("div", {"id": "MainSuperBrand"})
    super_brand_ul = super_brand.find("ul", {"class": "goodsBox"})
    super_brand_ul_li = super_brand_ul.find_all("li", {"class": "impact"})
    for i in super_brand_ul_li:
        bland_list.append({
            "title": i.find("strong").string,
            "url": i.find("a").attrs['href'],
        })
        
    return bland_list