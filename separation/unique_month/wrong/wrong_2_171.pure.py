def unique_month(month, possible_birthdays):
    result = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(result) == 1:
        return True  
    else:
        return False