def contains_unique_day(month, possible_birthdays):
    for j in possible_birthdays:
        if month != j[0]:
            continue
        else:
            if unique_day(j[1],possible_birthdays):
                return True
    return False