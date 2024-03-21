def unique_month(month, possible_birthdays):
    count = 0
    for tup in possible_birthdays:
        if tup[0] == month:
            count+=1
    return count == 1