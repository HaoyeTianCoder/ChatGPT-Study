def unique_day(date, possible_birthdays):
    if date in possible_birthdays[1:]: 
        return False
    else:
        return True