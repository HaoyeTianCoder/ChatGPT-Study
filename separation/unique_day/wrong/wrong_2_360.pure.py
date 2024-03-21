def unique_day(day, possible_birthdays):
    count = ()
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count = count + (possible_birthdays[i][1],)
    if len(count) < 2:
        return True
    else:
        return False