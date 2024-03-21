def contains_unique_day(month, possible_birthdays):
    x = () 
    for k in range(len(possible_birthdays)):
        if possible_birthdays[k][0] == month:
            x = x + (possible_birthdays[k],)
    for l in range(len(x)):
        if unique_day(x[l][1], possible_birthdays):
            return True
        else:
            continue
    return False 