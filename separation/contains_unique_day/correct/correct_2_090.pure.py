def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if month in i:
            if unique_day(i[1],possible_birthdays):
                return True
    return False