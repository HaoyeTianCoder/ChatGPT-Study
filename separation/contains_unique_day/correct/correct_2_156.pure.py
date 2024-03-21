def contains_unique_day(month, possible_birthdays):
    tupleofdays=()
    for elements in possible_birthdays:
        if elements[0]==month:
            tupleofdays += (elements[1],)
    for elements in tupleofdays:
        if unique_day(elements,possible_birthdays):
            return True
    return False