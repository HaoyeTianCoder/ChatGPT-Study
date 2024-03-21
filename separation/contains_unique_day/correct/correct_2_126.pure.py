def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(i[1], possible_birthdays) == True:
                return True
    else:
        return False