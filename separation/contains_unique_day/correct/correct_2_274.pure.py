def contains_unique_day(month, possible_birthdays):
    for elem in possible_birthdays:
        birthmonth = elem[0]
        if birthmonth == month:
            if unique_day(elem[1], possible_birthdays) == True:
                return True
    return False