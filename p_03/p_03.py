#! /usr/bin/python3

def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount percent and calculate final price
    """
    final_price = int(price * (1 - discount))

    assert (
      0 < final_price <= price, "A Assertion Error Raised"
    )
    return final_price


print(apply_discount(1000, 1.2))
