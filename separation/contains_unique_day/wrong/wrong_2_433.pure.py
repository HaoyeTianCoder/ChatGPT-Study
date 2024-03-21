def contains_unique_day(month, possible_birthdays):
    new_tuple = ()
    for i in possible_birthdays:
        if i[0] == month:
            new_tuple += (i,)
    print(new_tuple)
    for i in range(0,len(new_tuple)):
        if unique_day(new_tuple[i][1], possible_birthdays):
            return True
    return False