def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if date[0] == month:
            day = date[1]
            if unique_day(day, possible_birthdays):
                return True
            else:
                continue
    return False