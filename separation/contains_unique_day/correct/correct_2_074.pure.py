def contains_unique_day(month, possible_birthdays):
    counter = 0
    result = False
    for i in possible_birthdays:
        if month == i[0]:
            result = result or unique_day(i[1], possible_birthdays)
    return result