def calculateTrend(data):
    thisWeeksActive=data[-1]["Active"]-data[-7]["Active"]
    lastWeeksActive=data[-8]["Active"]-data[-15]["Active"]

    if thisWeeksActive > lastWeeksActive:
        print("UP")
        trend = "UP"
    elif thisWeeksActive == lastWeeksActive:
        print("SAME")
        trend = "SAME"
    else:
        print("DOWN")
        trend = "DOWN"

    return trend