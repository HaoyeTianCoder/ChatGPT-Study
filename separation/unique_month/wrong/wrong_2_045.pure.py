def unique_month(month, possible_birthdays):
    count=0
    for birthday_month in possible_birthdays:
        if month in birthday_month[0]:
            count+=1
    if count==1:
        return True
    else:
        return False