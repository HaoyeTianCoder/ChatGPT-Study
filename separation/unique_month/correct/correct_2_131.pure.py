def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        birthday_month = birthday[0]
        if month == birthday_month:
            counter += 1
    if counter == 1:
        return True
    else:
        return False