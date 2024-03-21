def unique_month(month, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if element[0] == month:
            count += 1
    if count != 1:
        return False
    return True