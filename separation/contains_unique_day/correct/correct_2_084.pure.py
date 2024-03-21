def contains_unique_day(month, possible_birthdays):
    for k in possible_birthdays:
        if month == k[0] and unique_day(k[1], possible_birthdays)==True:
            return True
    return False