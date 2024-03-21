def contains_unique_day(month, possible_birthdays):
    contains = ()
    for date in possible_birthdays:
        if month in date and unique_day(date[1],possible_birthdays):
            return True
    return False