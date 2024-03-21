def contains_unique_day(month, possible_birthdays):
    has_unique_day = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            if unique_day(birthday[1], possible_birthdays):
                has_unique_day = 1
                break
    if has_unique_day:
        return True
    else:
        return False