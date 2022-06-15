import requests
import json

url ='https://youtubeclassifier.herokuapp.com/api'

import requests, json
r = requests.post( 
    url,
    data = json.dumps(['VỀ SÀI GÒN MUA CAMERA & TỔ CHỨC SINH NHẬT BẤT NGỜ CHO BẠN'],
    ensure_ascii=False).encode('utf-8'))
print(r.json())