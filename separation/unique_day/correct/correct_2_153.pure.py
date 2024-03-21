def unique_day(date, possible_birthdays):
    if len(tuple(filter(lambda x: x[1] == date ,possible_birthdays))) == 1:
        return True
    else:
        return False