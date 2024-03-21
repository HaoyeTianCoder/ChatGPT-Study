def unique_month(month, possible_birthdays):
    result = 0
    for bday in possible_birthdays:
        if bday[0] == month:
            result += 1
    return result == 1