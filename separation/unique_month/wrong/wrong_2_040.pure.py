def unique_month(month, possible_birthdays):
    num = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            num += 1
    return num == 1