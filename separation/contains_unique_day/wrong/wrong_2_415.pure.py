def contains_unique_day(month, possible_birthdays):
    bday=()
    for i in possible_birthdays:
        if month==i[0]:
            bday+=(i,)
    for i in bday:
        if unique_day(i[1],possible_birthdays):
            return True
    else:
        return False