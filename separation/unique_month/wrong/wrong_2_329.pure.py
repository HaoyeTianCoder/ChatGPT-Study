def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if month in date:
            counter+=1
        if counter>1:
            return False 
    return True