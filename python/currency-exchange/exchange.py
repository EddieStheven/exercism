def exchange_money(budget, exchange_rate):

    return float(budget) / float(exchange_rate)

print(exchange_money(127.5, 1.2))

def get_change(budget, enchanging_value):

    return float(budget) - float(enchanging_value)

print(get_change(127.5, 120))

def get_value_of_bills(denomination, number_of_bills):

    return int(denomination) * int(number_of_bills)

print(get_value_of_bills(5, 128))

def get_number_of_bills(amount, denomination):

    return float(amount) // int(denomination)

print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(amount, denomination):

    return float(amount) % int(denomination)

print(get_leftover_of_bills(127.5, 20))