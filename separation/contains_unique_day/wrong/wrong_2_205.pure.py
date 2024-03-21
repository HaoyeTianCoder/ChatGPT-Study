def contains_unique_day(month, possible_birthdays):
    temp=()
    for i in possible_birthdays:
        if i[0]==month:
            temp=temp+(i,)
    for i in temp:
        if unique_day(i[1],possible_birthdays):
            return True
    return False