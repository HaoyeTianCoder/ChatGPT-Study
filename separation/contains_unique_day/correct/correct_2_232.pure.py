def contains_unique_day(month, possible_birthdays):
    result = ()
    for birthdays in possible_birthdays:
        if birthdays[0] == month:
            result = result + (birthdays,)
    for birthdayss in result:
        if unique_day(birthdayss[1], possible_birthdays):
            return True
    return False