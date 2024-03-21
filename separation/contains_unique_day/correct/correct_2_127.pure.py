def contains_unique_day(month, possible_birthdays):
    temp = [x for x in possible_birthdays if x[0] == month]
    temp = tuple(temp)
    counter = 0
    for x in temp:
        if unique_day(x[1], possible_birthdays):
            counter += 1
    if counter > 0:
        return True
    else:
        return False