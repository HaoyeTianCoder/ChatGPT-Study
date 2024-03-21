def unique_day(day, possible_birthdays):
    index = 1
    for days in tuple(map(lambda x:x[1], possible_birthdays)):
        if day == days:
            index = index*(-1)
            if index == 1:
                return False
    return True