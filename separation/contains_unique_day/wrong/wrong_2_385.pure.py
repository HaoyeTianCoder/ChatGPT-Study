def contains_unique_day(month, possible_birthdays):
    for birthdate in possible_birthdays:
        if month == birthdate[0]:
            return unique_day(birthdate[1], possible_birthdays)