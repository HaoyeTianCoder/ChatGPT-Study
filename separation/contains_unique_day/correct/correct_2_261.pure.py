def contains_unique_day(month, possible_birthdays):
    total,i = (), 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][0] == month:
            total += (possible_birthdays[i],)
        i += 1
    for x in total:
        if unique_day(x[1], possible_birthdays) == True:
            return True
    return False