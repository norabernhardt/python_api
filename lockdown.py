def calculateLockdown(data, limit):
    thisWeeksLimit=data[-1]["Active"]-data[-7]["Active"]

    if thisWeeksLimit >= limit:
        print("true")
        lockdown = True
    else:
        print("false")
        lockdown = False

    return lockdown