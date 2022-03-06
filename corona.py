import requests
import modules.cases as cases
import modules.active as active
import modules.lockdown as lockdown
import modules.trend as trend
from modules.writingJson import writingJsonFile
import json

url = requests.get ("https://api.covid19api.com/live/country/barbados/status/confirmed")
response = url.json()
limit=10000

cases = (cases.totalCases(response))
active = (active.activeCases(response))
trend = (trend.calculateTrend(response))
lockdown = (lockdown.calculateLockdown(response,limit))

writingJsonFile(json.dumps({"Cases": cases, "Active": active, "Trend": trend, "Lockdown": lockdown}))
