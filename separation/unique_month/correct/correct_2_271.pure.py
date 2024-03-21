def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if month == i[0]:
            result = result + 1
        else:
            continue 
    if result == 1:
        return True
    else:
        return False