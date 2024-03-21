def unique_day(date, possible_birthdays):
    if int(date) in possible_birthdays[1]: 
        return False
    else:
        return True