# Get size
def get_size():
    res = input(
        "What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res == "a":
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print(
            "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        return get_size()


# Drink type
def get_drink_type():
    res = input(
        "What type of drink would you like? \n[a]Brewed Coffee \n[b] Mocha \n[c] Latte \n")
    if res == "a":
        return 'Brewed Coffee'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return order_latte()
    else:
      print(
          "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
      return get_drink_type()

# Order Latte
def order_latte():
    res = input(
        "What type of milk for your latter? \n[a]2% milk \n[b] Non-fat milk \n[c] Soy milk \n")
    if res == "a":
        return 'latte'
    elif res == 'b':
        return 'Mocha'
    elif res == 'c':
        return 'Latte'
    else:
        print(
            "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        return order_latte()


def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print("Alright, that\'s a {} {}!".format(size, drink_type))
    name = input('Can I get your name please? \n> ')
    print("Thanks, {}! Your drink will be ready shortly".format(name))
coffee_bot()
