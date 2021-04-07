import requests


url = "https://rnd-board.telechips.com/rest/test"
r = requests.post(url, verify=False)


print(r.text)