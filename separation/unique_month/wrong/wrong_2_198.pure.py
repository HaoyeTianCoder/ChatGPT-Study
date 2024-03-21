def unique_month(day, possible_birthdays):
    checker=True
    for k in possible_birthdays:
        if k[0]==day:
          checker=False
    return checker