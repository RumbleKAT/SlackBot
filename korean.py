import requests
from bs4 import BeautifulSoup

def getKorean(query):
    url = 'http://stdweb2.korean.go.kr/search/List_dic.jsp'
    headers = {
        'content-type': 'application/x-www-form-urlencoded' 
    }

    payload = {
        'PageRow': 10, 
        'Table': 'words|word', 
        'Gubun': 0, 
        'SearchPart': 'Simple', 
        'SearchText': query
    }
    response = requests.post(url=url, data=payload, headers=headers)
    html = response.text
    result = []

    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.select('p[class="exp"]'):
        data = tag.text.strip()
       
    return data