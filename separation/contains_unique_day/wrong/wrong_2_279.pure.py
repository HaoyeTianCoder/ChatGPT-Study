def contains_unique_day(month, possible_birthdays):
    for day in possible_birthdays:
        if unique_day(day[1], possible_birthdays) == True and month == day[0]:
            return True
    else:
        return False