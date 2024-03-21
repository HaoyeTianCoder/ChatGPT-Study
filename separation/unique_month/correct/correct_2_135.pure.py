def unique_month(month, possible_birthdays):
    y = ()
    for i in range (0,len(possible_birthdays)):
        y += (possible_birthdays[i][0],)
    if y.count(month) == 1:
        return True
    else:
        return False