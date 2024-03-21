def contains_unique_day(month, possible_birthdays):
    birthdays = tuple(filter(lambda x: x[0] == month ,possible_birthdays))
    for i in birthdays:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    else:
        return False 