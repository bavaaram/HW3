#! /usr/bin/python3

def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """
    final_price = int(price * (1 - discount))
    if not (0 < final_price <= price):
        print("The Discount Rate is not Valid! ")
    else:
        print(final_price)


apply_discount(1000, 0.2)
