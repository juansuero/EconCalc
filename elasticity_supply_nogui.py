def calculate_elasticity_of_supply(initial_quantity, final_quantity, initial_price, final_price):
  """Calculates the elasticity of supply using the midpoint formula.
  Args:
      initial_quantity: The initial quantity supplied.
      final_quantity: The final quantity supplied.
      initial_price: The initial price.
      final_price: The final price.
  Returns:
      The elasticity of supply (rounded to 2 decimal places).
  """

  # Calculate percentage changes using the midpoint formula
  percentage_change_price = ((final_price - initial_price) / ((initial_price + final_price) / 2)) * 100
  percentage_change_quantity = ((final_quantity - initial_quantity) / ((initial_quantity + final_quantity) / 2)) * 100

  # Calculate elasticity using the percentage changes
  elasticity_of_supply = abs(percentage_change_quantity / percentage_change_price)

  return round(elasticity_of_supply, 2)

def get_user_input():
  initial_price = float(input("Enter the initial price: "))
  initial_quantity = float(input("Enter the initial quantity: "))
  final_price = float(input("Enter the final price: "))
  final_quantity = float(input("Enter the final quantity: "))
  return initial_quantity, final_quantity, initial_price, final_price

def elasticity_type(elasticity):
  if elasticity > 1:
    print(f"The elasticity is {elasticity:.2f}. Therefore supply is elastic.")
  elif elasticity < 1:
    print(f"The elasticity is {elasticity:.2f}. Therefore supply is inelastic.")
  else:
    print(f"The elasticity is {elasticity:.2f}. Therefore supply is unit elastic.")

def main():
  initial_quantity, final_quantity, initial_price, final_price = get_user_input()
  elasticity_of_supply = calculate_elasticity_of_supply(initial_quantity, final_quantity, initial_price, final_price)
  elasticity_type(elasticity_of_supply)

if __name__ == "__main__":
  main()