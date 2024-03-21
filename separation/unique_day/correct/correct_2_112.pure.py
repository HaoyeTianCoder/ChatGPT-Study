def unique_day(day, possible_birthdays):
    checker=0
    for k in possible_birthdays:
        if k[1]==day:
          checker+=1
    return checker==1