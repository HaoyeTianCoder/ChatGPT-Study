def unique_day(day, possible_birthdays):
    days = 0 
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            days = days + 1
    if days == 1:
        return True
    else:
        return False 