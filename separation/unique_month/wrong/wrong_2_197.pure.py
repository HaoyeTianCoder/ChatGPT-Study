def unique_month(month, possible_birthdays):
    x = 0
    for birthday in possible_birthdays:
        if month in birthday:
            x += 1
    if x > 1:
        return False
    else:
        return True