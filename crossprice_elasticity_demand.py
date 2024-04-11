from tkinter import *

def calculate_cross_elasticity(initial_quantity_a, final_quantity_a, initial_price_b, final_price_b):
  """Calculates the cross-price elasticity of demand using the midpoint formula.
  Args:
    initial_quantity_a: The initial quantity demanded of good A.
    final_quantity_a: The final quantity demanded of good A.
    initial_price_b: The initial price of good B.
    final_price_b: The final price of good B.
  Returns:
    The cross-price elasticity of demand (rounded to 2 decimal places).
  """

  # Calculate percentage changes using the midpoint formula
  percentage_change_price = ((final_price_b - initial_price_b) / ((initial_price_b + final_price_b) / 2)) * 100
  percentage_change_quantity = ((final_quantity_a - initial_quantity_a) / ((initial_quantity_a + final_quantity_a) / 2)) * 100

  # Calculate cross-price elasticity
  cross_elasticity = percentage_change_quantity / percentage_change_price

  return round(cross_elasticity, 2)

def elasticity_type(elasticity):
  if elasticity > 0:
    return f"The cross-price elasticity is {elasticity:.2f}. Therefore goods A and B are substitutes."
  elif elasticity < 0:
    return f"The cross-price elasticity is {elasticity:.2f}. Therefore goods A and B are complements."
  else:
    return f"The cross-price elasticity is {elasticity:.2f}. Therefore goods A and B are unrelated."

def calculate_elasticity():
  try:
    initial_price_b = float(initial_price_b_entry.get())
    initial_quantity_a = float(initial_quantity_a_entry.get())
    final_price_b = float(final_price_b_entry.get())
    final_quantity_a = float(final_quantity_a_entry.get())

    # Call the function for cross-price elasticity
    elasticity = calculate_cross_elasticity(initial_quantity_a, final_quantity_a, initial_price_b, final_price_b)
    elasticity_text = elasticity_type(elasticity)

    # Display the result
    result_label.config(text=f"Elasticity: {elasticity_text}")
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Cross-Price Elasticity Calculator")

# Labels
initial_price_b_label = Label(window, text="Initial Price of Good B:")
initial_quantity_a_label = Label(window, text="Initial Quantity of Good A:")
final_price_b_label = Label(window, text="Final Price of Good B:")
final_quantity_a_label = Label(window, text="Final Quantity of Good A:")
result_label = Label(window, text="")

# Entry fields
initial_price_b_entry = Entry(window)
initial_quantity_a_entry = Entry(window)
final_price_b_entry = Entry(window)
final_quantity_a_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate Elasticity", command=calculate_elasticity)

# Layout the widgets
initial_price_b_label.grid(row=0, column=0)
initial_quantity_a_label.grid(row=1, column=0)
final_price_b_label.grid(row=2, column=0)
final_quantity_a_label.grid(row=3, column=0)

initial_price_b_entry.grid(row=0, column=1)
initial_quantity_a_entry.grid(row=1, column=1)
final_price_b_entry.grid(row=2, column=1)
final_quantity_a_entry.grid(row=3, column=1)

calculate_button.grid(row=4, columnspan=2)
result_label.grid(row=5, columnspan=2)

window.mainloop() 
