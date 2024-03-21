def contains_unique_day(month, possible_birthdays):
    birthdays_month = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            birthdays_month += (birthday,)
    for birthday in birthdays_month:
        if unique_day(birthday[1], birthdays_month):
            return True
    return False  