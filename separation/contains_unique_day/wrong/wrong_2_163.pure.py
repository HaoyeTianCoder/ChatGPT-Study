def contains_unique_day(month, possible_birthdays):
    birthdays=()
    for i in possible_birthdays:
        if i[0]==month:
            birthdays+=(i,)
    for j in birthdays:
        if unique_day(j[1], possible_birthdays):
            return True
    return False