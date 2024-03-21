def unique_month(month, possible_birthdays):
    a = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            a = a + 1
    if a == 1:
        return True
    else:
        return False