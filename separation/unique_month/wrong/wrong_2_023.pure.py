def unique_month(month, possible_birthdays):
    count = 0
    for birthdays in possible_birthdays:
        if birthdays[0] == month:
            count +=1
            if count == 2:
                return False
    return True