def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if month in i:
            result = result + 1
    if result > 1:
        return False
    elif result == 0:
        return False
    else:
        return True