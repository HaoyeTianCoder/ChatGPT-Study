def unique_month(month, possible_birthdays):
    days = ()
    for birthday in possible_birthdays:
        if birthday[0] != month:
            continue
        elif birthday[0] not in days:
            days += (birthday[0],)
        else:
            return False
    return True