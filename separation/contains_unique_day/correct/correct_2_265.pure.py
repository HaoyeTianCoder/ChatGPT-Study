def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if get_month(i) == month and unique_day(get_day(i), possible_birthdays):
            return True
        else:
            continue
    return False 