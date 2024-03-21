def unique_day(day, possible_birthdays):
    count = 0
    days = map(lambda x:x[1], possible_birthdays)
    for i in days:
        if i == day:
            count += 1
    if count != 1:
        return False
    return True