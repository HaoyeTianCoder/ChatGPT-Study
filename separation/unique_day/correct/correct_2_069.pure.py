def unique_day(day, possible_birthdays):
    days = tuple(map(lambda x: x[1],possible_birthdays))
    count = 0
    for i in days:
        if i == day:
            count = count+1
    return count == 1