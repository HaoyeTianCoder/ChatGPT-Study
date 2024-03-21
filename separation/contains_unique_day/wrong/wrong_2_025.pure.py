def contains_unique_day(month, possible_birthdays):
    for bday in possible_birthdays:
        if bday[0] == month:
            if unique_day(bday[1], possible_birthdays) == True:
                return True
    return False