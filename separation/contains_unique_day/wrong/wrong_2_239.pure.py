def contains_unique_day(month, possible_birthdays):
    value=()
    for i in possible_birthdays:
        if i[0]==month:
            value+=(i,)
    for i in value:
        if unique_day(i[1],possible_birthdays):
            return True
    return False