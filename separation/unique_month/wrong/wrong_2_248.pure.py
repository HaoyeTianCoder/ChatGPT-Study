def unique_month(month, possible_birthdays):
    unique = 0
    for i in possible_birthdays:
        if i[0] == month:
            unique += 1
    if unique > 1:
        return False
    return True