def unique_day(day, possible_birthdays):
    days = tuple(map(lambda x: x[1], possible_birthdays))
    count = 0
    for temp_day in days:
        if temp_day == day:
            count+=1
    return True if count == 1 else False