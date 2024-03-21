def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        months,day=date
        if unique_day(day, possible_birthdays):
            return months==month