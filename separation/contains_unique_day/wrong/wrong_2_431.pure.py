def contains_unique_day(month, possible_birthdays):
    new_tuple = ()
    for i in possible_birthdays:
        if i[0] == month:
            new_tuple += (i,)
        if len(new_tuple)>1:
            return False
        else:
            return unique_day(new_tupl[0][1], possible_birthdays)