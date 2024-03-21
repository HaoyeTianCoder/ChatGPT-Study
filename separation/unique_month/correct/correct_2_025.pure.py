def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        counter += 1 if month == birthday[0] else 0
    return (counter == 1)