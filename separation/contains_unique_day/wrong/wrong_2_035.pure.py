def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if month==date[0]:
            if unique_day(date[1], possible_birthdays):
                return True
    return False