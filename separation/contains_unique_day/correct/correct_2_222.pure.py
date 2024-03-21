def contains_unique_day(month, possible_birthdays):
    for x in possible_birthdays:
        if x[0]==month:
            if unique_day(x[1], possible_birthdays):
                return True
            else:
                continue
        else:
            continue
    return False