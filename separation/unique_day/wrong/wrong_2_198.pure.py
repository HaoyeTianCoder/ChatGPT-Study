def unique_day(day, possible_birthdays):
    checker=True
    for k in possible_birthdays:
        if k[1]==day:
          checker=False
    return checker