def unique_month(month, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[0] == month:
            result = result + 1
    if result != 1:
        return False
    else:
        return True