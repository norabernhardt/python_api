import requests
import lockdown
import writingJson
import trend

limit=10000
url = requests.get ("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()
y=response[-1]

# print(type(y))
# print(y["Confirmed"])
# print(y["Active"])
# print(y["Date"])

cases=response[-1]["Confirmed"] 
print(cases)
active=response[-1]["Active"] - response[-8]["Active"]
print(active)

print(trend.calculateTrend(response))
print(lockdown.calculateLockdown(response,limit))


