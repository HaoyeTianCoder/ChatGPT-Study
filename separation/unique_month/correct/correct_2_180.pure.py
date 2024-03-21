def unique_month(month, possible_birthdays):
    number=0
    for i in possible_birthdays:
        if i[0]==month:
            number+=1
    return number==1