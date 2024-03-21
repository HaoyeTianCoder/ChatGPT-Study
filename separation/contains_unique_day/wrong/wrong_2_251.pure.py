def contains_unique_day(month, possible_birthdays):
    a =()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            a = a + (birthday,)
    for birthday in a:
        if unique_day(birthday[1], possible_birthdays):
            return True
    return False