def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            count = count + 1
    if count == 1:
        return True
    else:
        return False