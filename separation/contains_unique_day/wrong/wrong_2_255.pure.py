def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if unique_day(date[1], possible_birthdays) and date[0] == month:
            return True
    else:
        return False