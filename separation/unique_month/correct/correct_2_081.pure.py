def unique_month(month, possible_birthdays):
    count = 0
    for k in possible_birthdays:
        if k[0] == month:
            count = count + 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False