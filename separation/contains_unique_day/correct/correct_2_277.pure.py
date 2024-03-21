def contains_unique_day(month, possible_birthdays):
    newtuple = ()
    for i in possible_birthdays:
        if month== i[0]:
            newtuple = newtuple + (i,)
    for j in newtuple:
        if unique_day(j[1], possible_birthdays) == True:
            return True
    else:
        return False