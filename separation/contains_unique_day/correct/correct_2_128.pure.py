def contains_unique_day(month, possible_birthdays):
    truth_holder = False
    for birthday in possible_birthdays:
        if birthday[0] != month:
            continue
        else:
            truth_holder = truth_holder or unique_day(birthday[1], possible_birthdays)
    return truth_holder