def unique_month(month, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        if month == x[0]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False