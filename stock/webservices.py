import json

import requests

headers = {

}
def trade_info(date):
    print("date", str(date))
    date = str(date).replace("-","")
    url = "http://cdn.tsetmc.com/api/Trade/GetTradeHistory/65883838195688438/" + str(date) + "/false"
    response = requests.request("GET", url, data={}, headers=headers)
    print("-------response ")
    res = json.loads(response.text)
    return response.text, res
