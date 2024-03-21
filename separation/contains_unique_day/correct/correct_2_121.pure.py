def contains_unique_day(month, possible_birthdays):
    dayi = ()
    result = False
    for i in possible_birthdays:
        if month == i[0]:
            dayi += (i[1],)
    for j in dayi:
        result = result or unique_day(j, possible_birthdays)
    return result