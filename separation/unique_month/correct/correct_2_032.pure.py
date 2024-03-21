def unique_month(month, possible_birthdays):
    count = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[0] == month:
            count += 1
        continue
    if count == 1:
        return True
    return False