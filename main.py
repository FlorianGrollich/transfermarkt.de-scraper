import requests
from bs4 import BeautifulSoup
from match import Match

cookies = {
    '_sp_v1_uid': '1:768:277e6701-fad8-4b57-988e-60071a92cd11',
    '_sp_v1_data': '2:579034:1679617272:0:1:-1:1:0:0:_:-1',
    '_sp_v1_ss': '1:H4sIAAAAAAAAAItWqo5RKimOUbKKxsrIAzEMamN1YpRSQcy80pwcILsErKC6lgwJpVgAEA5-UnQAAAA^%^3D',
    '_sp_su': 'false',
    'TMSESSID': 'aa232e798770111f6aba3b9c7a6f08c6',
    'consentUUID': '9fd32c25-19e1-463a-b1d3-20bce2f3403e_17',
    '_sp_v1_opt': '1:login^|true:last_id^|11:',
    '_sp_v1_csv': '',
    '_sp_v1_lt': '1:',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Accept': '*/*',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Proxy-Authorization': 'Basic NXdEQXpUaUxRTWU3ZGFBZ0U5NkFFV0xqOm1kTmRUWE02Z0ZNTnN4anRRZ1J2N2R2eg==',
    'Connection': 'keep-alive',
    'Referer': 'https://www.transfermarkt.de/spielbericht/index/spielbericht/3839434',
    # 'Cookie': '_sp_v1_uid=1:768:277e6701-fad8-4b57-988e-60071a92cd11; _sp_v1_data=2:579034:1679617272:0:1:-1:1:0:0:_:-1; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKxsrIAzEMamN1YpRSQcy80pwcILsErKC6lgwJpVgAEA5-UnQAAAA^%^3D; _sp_su=false; TMSESSID=aa232e798770111f6aba3b9c7a6f08c6; consentUUID=9fd32c25-19e1-463a-b1d3-20bce2f3403e_17; _sp_v1_opt=1:login^|true:last_id^|11:; _sp_v1_csv=; _sp_v1_lt=1:',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

r = requests.get('https://www.transfermarkt.de/spielbericht/index/spielbericht/3839434', cookies=cookies, headers=headers)


soup = BeautifulSoup(r.content, 'html.parser')

all_players = soup.find_all('span', {'class': 'aufstellung-rueckennummer-name'})

match = Match()

# Starting Team
for i,a in enumerate(soup.select("span.aufstellung-rueckennummer-name a")):
    link = a.get('href')
    split_link = link.split('/')
    if i > 10:
        match.startingTeam2.append(split_link[4])
    else:
        match.startingTeam1.append(split_link[4])

# Bench
tables = soup.find_all('table', {'class': 'ersatzbank'})

print(match.benchTeam1)
print(match.benchTeam2)