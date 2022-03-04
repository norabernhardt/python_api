import requests
import writingJson
#"https://api.covid19api.com/total/country/germany/status/confirmed?from=2022-03-01T00:00:00Z&to=2022-03-04T00:00:00Z")

url = requests.get ("https://api.covid19api.com/live/country/switzerland/status/confirmed")
response = url.json()
y=response[-1]

#print(type(y))
# print(y["Confirmed"])
# print(y["Active"])
# print(y["Date"])

cases=response[-1]["Confirmed"] - response[-8]["Confirmed"]
print(cases)
active=response[-1]["Active"] - response[-8]["Active"]
print(active)




