def contains_unique_day(month, possible_birthdays):
    for day in possible_birthdays:
        if month == day[0]:
            if unique_day(day[1], possible_birthdays):
                return True
        else:
            continue
    return False