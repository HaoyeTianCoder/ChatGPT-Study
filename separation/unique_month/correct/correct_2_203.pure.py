def unique_month(month, possible_birthdays):
    counter = 0
    for item in possible_birthdays:
        if item[0] == month:
            counter = counter + 1
    if counter != 1:
        return False
    return True