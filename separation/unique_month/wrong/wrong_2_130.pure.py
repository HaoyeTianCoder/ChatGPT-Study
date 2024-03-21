def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[0] == month:
            counter = counter + 1
    if counter > 1:
        return False
    else:
        return True