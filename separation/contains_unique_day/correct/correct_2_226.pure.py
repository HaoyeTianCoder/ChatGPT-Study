def contains_unique_day(month, possible_birthdays):
    for a in possible_birthdays:
        if unique_day(a[1],possible_birthdays):
            if month == a[0]:
                return True
    return False