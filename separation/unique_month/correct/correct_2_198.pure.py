def unique_month(month, possible_birthdays):
    appearance = 0
    for i in possible_birthdays:
        if i[0] == month:
            appearance += 1
    if appearance == 1:
        return True
    return False