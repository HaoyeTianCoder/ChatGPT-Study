def contains_unique_day(month, possible_birthdays):
    day = filter(lambda x: x[0]== month, possible_birthdays)
    for item in tuple(day):
        if unique_day(item[1],possible_birthdays) == True:
            return True
        else:
            continue
    return False 