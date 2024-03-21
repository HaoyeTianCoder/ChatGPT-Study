def contains_unique_day(month, possible_birthdays):
    count=()
    for i in possible_birthdays:
        if i[0]==month:
            count=count+i
    for j in count:
        if unique_day(j[1], possible_birthdays):
            return True
    return False