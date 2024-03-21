def unique_day(date, possible_birthdays):
    count =0
    for i in possible_birthdays:
        if date==i[1]:
            count+=1
    return count==1