def contains_unique_day(month, possible_birthdays):
    T_or_F = False
    for i in possible_birthdays:
        if i[0] == month and unique_day(i[1], possible_birthdays):
            T_or_F = T_or_F or True
    return T_or_F