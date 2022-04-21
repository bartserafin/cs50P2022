def coke_machine(amount_due):

    insert_coin = 0
    inserted_coins = 0
    inital_amount_due = amount_due
    list_coins = [1, 2, 5, 10, 25, 50]

    while amount_due >= insert_coin:
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))
        if insert_coin not in list_coins:
            continue
        inserted_coins += insert_coin
        amount_due -= insert_coin

    change_owed = inserted_coins - inital_amount_due
    print(f"Change Owed: {change_owed}")


coke_machine(50)