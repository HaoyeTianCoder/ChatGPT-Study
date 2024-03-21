def contains_unique_day(month, possible_birthdays):
    monies = ()
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            monies += (possible_birthdays[i][1],)
    for i in range(len(monies)):
        if unique_day(monies[i], possible_birthdays):
            return True
    return False 