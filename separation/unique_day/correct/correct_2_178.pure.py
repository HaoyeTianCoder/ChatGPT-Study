def unique_day(day, possible_birthdays):
    number=0
    for i in possible_birthdays:
        if i[1]==day:
            number+=1
    return number==1