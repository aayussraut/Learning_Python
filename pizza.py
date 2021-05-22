def make_pizza(size,*toppings):
    """Summarize the pizza we are baout to make."""
    print("\n Making a "+str(size)+"-inch pizza with following toppings:")
    
    for topping in toppings:
        print("- "+topping)