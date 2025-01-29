import requests, json
from datetime import datetime

url = "https://api.opendota.com/api/players/383671716/matches?limit=1000"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
windays = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}
loosedays = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}
for i in data:
    date = i['start_time']
    is_radiant = True if i['player_slot'] < 128 else False
    radiant_win = i['radiant_win']
    readable_time = datetime.utcfromtimestamp(date)
    rd = readable_time.strftime("%Y-%m-%d %H:%M:%S")
    weekday = readable_time.weekday()

    if is_radiant and radiant_win:
        windays[str(weekday)] += 1
    elif not is_radiant and not radiant_win:
        loosedays[str(weekday)] += 1
    elif is_radiant and not radiant_win:
        loosedays[str(weekday)] += 1
    elif not is_radiant and radiant_win:
        windays[str(weekday)] += 1

windays_ret = {
    "monday": windays["0"],
    "tuesday": windays["1"],
    "wednesday": windays["2"],
    "thursday": windays["3"],
    "friday": windays["4"],
    "saturday": windays["5"],
    "sunday": windays["6"]
}

loosedays_ret = {
    "monday": loosedays["0"],
    "tuesday": loosedays["1"],
    "wednesday": loosedays["2"],
    "thursday": loosedays["3"],
    "friday": loosedays["4"],
    "saturday": loosedays["5"],
    "sunday": loosedays["6"]
}

print("Windays")
print(json.dumps(windays_ret))
print("Loosedays")
print(json.dumps(loosedays_ret))

def request():
    pass