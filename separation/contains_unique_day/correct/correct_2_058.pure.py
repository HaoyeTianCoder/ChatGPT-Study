def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if unique_day(birthday[1], possible_birthdays):
            birthday_month = birthday[0]
            if month == birthday_month:
                return True
    return False