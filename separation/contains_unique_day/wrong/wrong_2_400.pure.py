def contains_unique_day(month, possible_birthdays):
    def generate_unique_days(possible_birthdays):
        generate = ()
        for i in range(14, 20):
            if unique_day(str(i), possible_birthdays):
                generate += (str(i),)
        return generate
    for i in possible_birthdays:
        if i[0] == month:
            if str(i[1]) in generate_unique_days(possible_birthdays):
                return True
    return False