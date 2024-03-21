def unique_month(month, possible_birthdays):
    count  = 0
    for possible_birthday in possible_birthdays:
        if month == possible_birthday[0]:
            count += 1
    return count == 1