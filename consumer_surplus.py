def calculate_consumer_surplus(price, quantity, price_when_q_0):
    """
    Calculates the consumer surplus based on price, quantity, and price at Q=0.
    Args:
        price: The equilibrium price.
        quantity: The equilibrium quantity.
        price_when_q_0: The price at which quantity is zero.
    Returns:
        The consumer surplus (rounded to two decimal places).
    """
    height = price_when_q_0 - price
    base = quantity
    consumer_surplus = 0.5 * height * base
    return round(consumer_surplus, 2)

def print_result(consumer_surplus):
    print(f"The consumer surplus is ${consumer_surplus:.2f}")

# Prompt the user for inputs
price = float(input("Enter the equilibrium price: "))
quantity = float(input("Enter the equilibrium quantity: "))
price_when_q_0 = float(input("Enter the price at Q=0: "))

# Calculate and print the consumer surplus
result = calculate_consumer_surplus(price, quantity, price_when_q_0)
print_result(result)
