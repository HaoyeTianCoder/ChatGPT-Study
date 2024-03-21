def unique_day(day, possible_birthdays):
    x = ()
    for i in range (0,len(possible_birthdays)):
        x += (possible_birthdays[i][-1],)
    if x.count(day) == 1:
        return True
    else:
        return False