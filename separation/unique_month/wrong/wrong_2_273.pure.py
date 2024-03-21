def unique_month(month, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if i[1]==month: num+=1
    return num==1