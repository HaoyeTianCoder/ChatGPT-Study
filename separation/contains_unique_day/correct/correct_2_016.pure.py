def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if unique_day(date[1], possible_birthdays) == True and month == date[0]:
            return True
    return False       