# Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.

def find_angle(time_str):
    hh, mm = time_str.split(":")

    hours = int(hh)
    minutes = int(mm)

    hours = hours % 12

    minutes_angle = minutes * 6
    hours_angle = hours * 30 + minutes * 0.5

    angle = abs(hours_angle - minutes_angle)

    return round(min(angle, 360 - angle), 3)


print(find_angle("5:33"))
print(find_angle("3:43"))


