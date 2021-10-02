def toHours(minutes, seconds):
    hours = minutes/60 + seconds/3600
    return hours

print(toHours(73,54))

def toHours(seconds, minutes=100):
    hours = minutes/60 + seconds/3600
    print(hours)

toHours(73)

toHours(54,73)

print(type(toHours(54,73)))
