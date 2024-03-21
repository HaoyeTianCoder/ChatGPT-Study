def contains_unique_day(month, possible_birthdays):
    count = ()
    for birthdays in possible_birthdays:
        if birthdays[0] == month:
            count += (birthdays,)
    for sub_birthday in count:
        if unique_day(sub_birthday[1], possible_birthdays):
            return True
    return False 