import requests
import cases
import active
import lockdown
import writingJson
import trend

limit=10000
url = requests.get ("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()


print(cases.totalCases(response))
print(active.activeCases(response))
print(trend.calculateTrend(response))
print(lockdown.calculateLockdown(response,limit))


