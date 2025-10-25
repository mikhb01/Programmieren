# *args     = allows you to pass mulitple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. postitional, 2. default, 3. keyword, 4. ARBITARY

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# print(add(1, 2, 3, 4, 5))

# print(add(1, 2, 3))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Leon", "Michael", "Lengert")


# def print_address(**kwargs):
#     for key in kwargs.items():
#         print(key)


# print_address(street="Weserstraße 3", 
#               city="Bremen", 
#               state="Bremen", 
#               zip="21783")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake Street",
            #    apt="100", 
            pobox="PO box #1001",
               city="Detroit",
               state="MI", 
               zip="54321")