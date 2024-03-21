def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if month in i:
            count += 1
    if count > 1:
        return False
    return True