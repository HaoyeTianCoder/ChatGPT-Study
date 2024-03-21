def unique_month(month, possible_birthdays):
    new = ()
    for i in range (len(possible_birthdays)):
        new = new + (possible_birthdays[i][0],)
    if new.count(month) == 1:
        return True
    else:
        return False