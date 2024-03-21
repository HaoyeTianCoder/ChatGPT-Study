def unique_month(month, possible_birthdays):
    counter = 0
    for birthdate in possible_birthdays:
        if month == birthdate[0]:
            counter += 1
    if counter > 1:
        return False
    else:
        return True