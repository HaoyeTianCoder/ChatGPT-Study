def unique_day(day, possible_birthdays):
    n=0
    for tup in possible_birthdays:
        if tup[1]==day:
            n+=1
    if n==1:
        return True           
    return False