def unique_month(month, possible_birthdays):
    count = 0
    for x in possible_birthdays:
        if month in x:
            count += 1
    return count == 1