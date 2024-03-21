def contains_unique_day(month, possible_birthdays):
    singledays = tuple(filter((lambda x: unique_day(x[1], possible_birthdays)), possible_birthdays))
    for i in singledays:
        if i[0] == month:
            return True
    return False