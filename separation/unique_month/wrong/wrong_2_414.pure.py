def unique_month(month, possible_birthdays):
    count = ()
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count = count + (possible_birthdays[i][0],)
    if len(count) < 2:
        return True
    else:
        return False