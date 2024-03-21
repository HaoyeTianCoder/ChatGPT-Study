def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(x, possible_birthdays):
                return True
            else:
                return False