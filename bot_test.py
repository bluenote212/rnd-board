import json, requests

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'consumerKey': 'IuAF6mCrW4FiTxWF6bmm',
    'Authorization': 'Bearer AAABAXONcN0Ch9T4YmhyDiRG+1ilvRZoM1MoutdUZLzV6++m3h+/fipKAlD0I1OKCbAJFWhuiQV07ldyuY1M3qu0pVEKqWcrhPdK5k2PKp2Xo42bfFsPleMt8D0+ZHqJVGrXPdw3JheNM5hkVqpzEc0l24vlpymIeLTg74+aEUFa+SpI6mjkbP5vJwD5kR8auewDnQgmuE1cwdBVlveJq2ZDC7ohbAF29Hfd/Wmc75h72LAC3W1Zea+4LF/UpKoBnSxCmqSInyWmyYwAJ5HBrPp/9PdoxB5SqRma2aFswhmwvaR/6AClqjmuAKdGlcgA+DertSmLCCer7i2iNXxNimgqXsrvEAHQQpLwtrv8IGdcV/sf'
}

url = 'https://apis.worksmobile.com/r/kr1llsnPeSqSR/message/v1/bot/1809717/message/push' #1:1 메시지 Request URL

body1 = {
        "accountId": "bluenote212@telechips.com",
        "content": {
                "type": "button_template",
                "contentText": "안녕하세요 R&D 물어봇 입니다.\n아래에서 궁금한 항목을 선택해 주세요.",
                "actions": [
                        {
                                "type": "uri",
                                "label": "R&D Notice",
                                "uri": "https://wiki.telechips.com:8443/pages/viewpage.action?pageId=108817910"
                        },
                        {
                                "type": "message",
                                "label": "Project",
                                "postback": "ButtonTemplate_Project"
                        },
                        {
                                "type": "message",
                                "label": "System",
                                "postback": "ButtonTemplate_System"
                        }
                        ]
                }
        }

body2 = {
    'botNo': '1809717',
    'accountId': 'bluenote212@telechips.com',
    'content': {
        'type': 'text',
        'text': '아직도 모르니'
     }
}

r = requests.post(url, data=json.dumps(body1), headers=headers)
