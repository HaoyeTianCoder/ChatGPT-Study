def unique_month(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            count+=1
    return count==1