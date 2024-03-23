likes_sweet = input("Do you like your coffee sweet? (yes/no)")
likes_milk = input("Do you prefer milk in your coffee? (yes/no)")
if likes_sweet == "yes" and likes_milk =="yes":
    print("How about a caramel latte")
elif likes_sweet == "no" and likes_milk == "yes":
    print("An Americano with a dash of milk!")
elif likes_sweet == "yes" and likes_m