def calculateLockdown(data, limit):
    thisWeeksLimit=data[-1]["Active"]-data[-7]["Active"]

    if thisWeeksLimit >= limit:
        lockdown = True
    else:
        lockdown = False

    return lockdown