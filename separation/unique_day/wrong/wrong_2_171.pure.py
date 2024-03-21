def unique_day(day, possible_birthdays):
    result = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(result) == 1:
        return True  
    else:
        return False