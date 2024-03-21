def contains_unique_day(month, possible_birthdays):
    dates=()
    for date in possible_birthdays:
        months,day=date
        if unique_day(day, possible_birthdays):
            return month==months