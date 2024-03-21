def unique_month(month, possible_birthdays):
    n=0
    for tup in possible_birthdays:
        if tup[0]==month:
            n+=1
    if n==1:
        return True           
    return False