def calculateTrend(data):
    thisWeeksActive=data[-1]["Active"]-data[-7]["Active"]
    lastWeeksActive=data[-8]["Active"]-data[-15]["Active"]

    if thisWeeksActive > lastWeeksActive:
        trend = "UP"
    elif thisWeeksActive == lastWeeksActive:
        trend = "SAME"
    else:
        trend = "DOWN"
    return trend