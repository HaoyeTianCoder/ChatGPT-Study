def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if month == i[0]:
            result = result + 1
    if result == 1:
        return True
    else:
        return False