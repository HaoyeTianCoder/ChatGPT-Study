def contains_unique_day(month, possible_birthdays):
    tup = () 
    for k in range(len(possible_birthdays)):
        if possible_birthdays[k][0] == month:
            tup = tup + (possible_birthdays[k],)
    for l in range(len(tup)):
        if unique_day(tup[l][1], possible_birthdays):
            return True
    return False 