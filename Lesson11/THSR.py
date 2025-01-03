import requests
import json
from bs4 import BeautifulSoup
payload = {"SearchType": "S",
           "Lang": "TW",
    	   "StartStation": "NanGang",
           "EndStation": "ZuoYing",
           "OutWardSearchDate": "2023/05/06",   #記得更改日期
           "OutWardSearchTime": "20:00"
           }
res = requests.post("https://www.thsrc.com.tw/TimeTable/Search",data = payload)

soup = BeautifulSoup(res.text,"html.parser")
train_dict = json.loads(soup.text)
for item in train_dict['data']['DepartureTable']['TrainItem']:
    trainNumber = item['TrainNumber']
    DepartureTime = item['DepartureTime']
    DestinationTime = item['DestinationTime']

    print('車次:'+trainNumber, '出發時間:'+DepartureTime, '抵達時間:'+DestinationTime)

        

