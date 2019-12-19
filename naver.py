import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

request = requests.get(url).text
soup = BeautifulSoup(request, 'html.parser')
sel = "#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k"
search = soup.select(sel)

for item in search :
    print(item.text)