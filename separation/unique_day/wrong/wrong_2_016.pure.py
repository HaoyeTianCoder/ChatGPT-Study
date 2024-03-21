def unique_day(day, possible_birthdays):
    days = map(lambda x: x[1], possible_birthdays)
    times = 0
    for i in days:
        if i==day:
            times = times+1
        else:
            continue
    if times>1:
        return False
    else:
        return True