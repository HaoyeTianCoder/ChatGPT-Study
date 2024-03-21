def unique_month(month, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if month == bday[0]:
            count += 1
    return count == 1