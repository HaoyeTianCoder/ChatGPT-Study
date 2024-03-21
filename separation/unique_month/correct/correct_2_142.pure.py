def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if i[0] == month:
            result += 1
        elif i[0] != month:
            result += 0
    if result == 1:
        return True
    else:
        return False