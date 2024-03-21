def contains_unique_day(month, possible_birthdays):
    birthdays_in_month = ()
    for birthday in possible_birthdays:
        if birthday[0] == month: birthdays_in_month += (birthday,)
    for birthday in birthdays_in_month:
        if unique_day(birthday[1], possible_birthdays):
            return True
    return False