def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if birthday[0]== month:
            counter = counter + 1
    if counter <= 1:
        return True
    else:
        return False