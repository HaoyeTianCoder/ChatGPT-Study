def contains_unique_day(month, possible_birthdays):
    list_d = ()
    for i in range(16,20):
        i_string = str(i)
        if unique_day(i_string, possible_birthdays) is True:
            list_d = list_d + (str(i),)
    for i in possible_birthdays:
        for j in list_d:
            if i[1] == j:
                if i[0] == month:
                    return True
    return False