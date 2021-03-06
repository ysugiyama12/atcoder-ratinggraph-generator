import json
import urllib.request
from datetime import datetime as dt
from pprint import pprint

base_url = "https://atcoder.jp/users/"
def getJsonData(username, inputs):
    if username == "":
        return ""
    json_data = []
    url = base_url + username + "/history/json"
    req = urllib.request.Request(url)
    raw_data = []
    with urllib.request.urlopen(req) as res:
        status_code = res.getcode()
        if status_code != 200:
            return ""
        body = res.read()
        raw_data = json.loads(body)
    
    for rd in raw_data:
        if rd['IsRated'] == True:
            tdatetime = dt.strptime(rd["EndTime"], "%Y-%m-%dT%H:%M:%S+09:00")
            timestamp = tdatetime.timestamp()
            "abc098.contest.atcoder.jp"
            StandingsUrl = rd["ContestScreenName"].replace(".contest.atcoder.jp", "")
            StandingsUrl = "/contests/" + StandingsUrl + "/standings?watching=" + username
            if rd["ContestName"] in inputs:
                rd["NewRating"] = inputs[rd["ContestName"]]
            data = {
                "StandingsUrl": StandingsUrl,
                "EndTime": timestamp,
                "NewRating": int(rd["NewRating"]),
                "OldRating": rd["OldRating"],
                "Place": rd["Place"],
                "ContestName": rd["ContestName"]
            }
            json_data.append(data)
    # if len(json_data) == 0:
    #     return ""
    # pprint(json_data)


    

    return json_data
