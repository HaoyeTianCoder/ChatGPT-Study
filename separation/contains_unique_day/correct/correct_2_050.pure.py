def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0]==month:
            if unique_day(birthday[1], possible_birthdays)==True:
                return True
                break
    return False