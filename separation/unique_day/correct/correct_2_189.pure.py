def unique_day(day, possible_birthdays):
    dates = map(lambda x: x[1], possible_birthdays)
    counter = 0
    for date in dates:
        if day == date:
            counter += 1
    if counter == 1:
        return True
    else:
        return False