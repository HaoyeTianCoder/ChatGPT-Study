def unique_month(month, possible_birthdays):
    count = 0
    for mon in possible_birthdays:
        if mon[0] == month:
            count += 1
    return count == 1