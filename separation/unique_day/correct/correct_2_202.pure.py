def unique_day(day, possible_birthdays):
    new = ()
    for i in range (len(possible_birthdays)):
        new = new + (possible_birthdays[i][1],)
    if new.count(day) == 1:
        return True
    else:
        return False