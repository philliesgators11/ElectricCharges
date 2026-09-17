for i in range(4):
    kw_hours = int(input("Enter the KW hours used: "))
    if kw_hours <= 1000:
        amount = kw_hours * 7.633 / 100
    else:
        amount = (1000 * 7.633 / 100) + ((kw_hours - 1000) * 9.259 / 100)
    print("Amount owed is $" + str(amount))