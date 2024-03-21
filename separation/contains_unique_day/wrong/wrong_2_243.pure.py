def contains_unique_day(month, possible_birthdays):
    condition = False
    for month_day in possible_birthdays:
        if month == month_day[0]:
            condition = unique_day(month_day[1],possible_birthdays)
    return condition