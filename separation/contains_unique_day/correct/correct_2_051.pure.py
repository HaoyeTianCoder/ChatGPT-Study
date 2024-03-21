def contains_unique_day(month, possible_birthdays):
    result = ()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            result += (unique_day(birthday[1], possible_birthdays),)
    if any(result):
        return True
    return False