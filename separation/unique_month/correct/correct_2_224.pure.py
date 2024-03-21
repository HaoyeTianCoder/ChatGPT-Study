def unique_month(month, possible_birthdays):
    bag = []
    for months in possible_birthdays:
        if months[0] == month:
            bag.append(month)
    n = len(bag)
    if n == 1:
        return True
    else:
        return False