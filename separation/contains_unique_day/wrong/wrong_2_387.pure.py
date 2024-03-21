def contains_unique_day(month, possible_birthdays):
    counter = 0
    for birthdate in possible_birthdays:
        if month == birthdate[0]:
            tp = unique_day(birthdate[1], possible_birthdays)
            if tp == True:
                counter += 1
    if counter >= 1:
        return True
    else:
        return False