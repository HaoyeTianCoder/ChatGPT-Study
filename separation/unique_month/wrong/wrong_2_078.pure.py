def unique_month(month, possible_birthdays):
    total = 0
    for i in possible_birthdays:
        if i[0] == month:
            total += 1
    if total > 1:
        return False
    return True