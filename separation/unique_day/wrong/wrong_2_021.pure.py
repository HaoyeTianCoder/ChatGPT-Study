def unique_day(day, possible_birthdays):
    possible_days = tuple(map(lambda x: x[1], possible_birthdays))
    counter = 0
    for possible_day in possible_days:
        if day == possible_day:
            counter = counter + 1
    if counter == 1:
        return True
    elif counter > 1:
        return False
    else:
        return "Not a day in possible_birthdays"