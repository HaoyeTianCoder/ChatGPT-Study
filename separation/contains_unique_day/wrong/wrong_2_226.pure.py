def contains_unique_day(month, possible_birthdays):
    for bday in possible_birthdays:
        if month == bday[0]:
            if unique_day(bday[1], possible_birthdays):
                return True
    return False 