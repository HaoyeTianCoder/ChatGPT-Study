def contains_unique_day(month, possible_birthdays):
    for possible_birthday in possible_birthdays:
        if month == possible_birthday[0] and unique_day(possible_birthday[1], possible_birthdays):
            return True
    return False