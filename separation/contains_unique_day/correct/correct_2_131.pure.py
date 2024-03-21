def contains_unique_day(month, possible_birthdays):
    birthday_days_in_month = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            birthday_days_in_month += (birthday[1],)
    day_counter = 0
    for day in birthday_days_in_month:
        if unique_day(day, possible_birthdays):
            return True
    return False 