def contains_unique_day(month, possible_birthdays):
    tf=False 
    for i in possible_birthdays:
        if i[0]==month:
            tf=tf or unique_day(i[1],possible_birthdays)
    return tf