def contains_unique_day(month, possible_birthdays):
    for x in possible_birthdays:
        if month == x[0]:
            if unique_day(x[-1],possible_birthdays):
                return True
    return False