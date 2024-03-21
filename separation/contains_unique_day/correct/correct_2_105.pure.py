def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if unique_day(birthday[1],possible_birthdays):
            months = birthday[0]
            if months == month:
                return True
            else:
                continue
        else:
            continue
    return False