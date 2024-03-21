def unique_month(month, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if month == element[0]:
            count += 1
    if count > 1:
        return False
    else:
        return True