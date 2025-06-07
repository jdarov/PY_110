DEGREE = "\u00B0"

def dms(angle):
    angle = float(angle)
    degrees = int(angle)
    
    minutes_raw = (angle - degrees)*60
    minutes = int(minutes_raw)
    seconds = int((minutes_raw-minutes)*60 + 0.5)

    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        degrees += 1
    
    return f"{int(angle)}{DEGREE}{minutes:02d}'{seconds:02d}\""

# All of these examples should print True
# print(dms(30) == "30°00'00\"")
# print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
# print(dms(93.034773) == "93°02'05\"")
# print(dms(0) == "0°00'00\"")
# print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # -1°00'00"
print(dms(400))  # 400°00'00"
print(dms(-40))  # -40°00'00"
print(dms(-420)) # -420°00'00"