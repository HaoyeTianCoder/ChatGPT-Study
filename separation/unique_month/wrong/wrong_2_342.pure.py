def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            count = count + 1
    if count>1:
        return False
    else:
        return True