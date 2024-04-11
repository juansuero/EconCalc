from tkinter import *

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

  # **Modify for elasticity of supply:**
  # Since supply responds to price changes, we reverse the signs
  elasticity_of_supply = abs(percentage_change_quantity / -percentage_change_price)

  return round(elasticity_of_supply, 2)

def elasticity_type(elasticity):
  if elasticity > 1:
    return f"The elasticity is {elasticity:.2f}. Therefore supply is elastic."
  elif elasticity < 1:
    return f"The elasticity is {elasticity:.2f}. Therefore supply is inelastic."
  else:
    return f"The elasticity is {elasticity:.2f}. Therefore supply is unit elastic."

def calculate_elasticity():
  try:
    initial_price = float(initial_price_entry.get())
    initial_quantity = float(initial_quantity_entry.get())
    final_price = float(final_price_entry.get())
    final_quantity = float(final_quantity_entry.get())

    # Call the modified function for elasticity of supply
    elasticity = calculate_elasticity_of_supply(initial_quantity, final_quantity, initial_price, final_price)
    elasticity_text = elasticity_type(elasticity)

    # Display the result
    result_label.config(text=f"Elasticity: {elasticity_text}")
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

window = Tk()
window.title("Elasticity of Supply Calculator")

# Labels
initial_price_label = Label(window, text="Initial Price:")
initial_quantity_label = Label(window, text="Initial Quantity:")
final_price_label = Label(window, text="Final Price:")
final_quantity_label = Label(window, text="Final Quantity:")
result_label = Label(window, text="")

# Entry fields
initial_price_entry = Entry(window)
initial_quantity_entry = Entry(window)
final_price_entry = Entry(window)
final_quantity_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate Elasticity of Supply", command=calculate_elasticity)

# Layout the widgets
initial_price_label.grid(row=0, column=0)
initial_quantity_label.grid(row=1, column=0)
final_price_label.grid(row=2, column=0)
final_quantity_label.grid(row=3, column=0)

initial_price_entry.grid(row=0, column=1)
initial_quantity_entry.grid(row=1, column=1)
final_price_entry.grid(row=2, column=1)
final_quantity_entry.grid(row=3, column=1)

calculate_button.grid(row=4, columnspan=2)
result_label.grid(row=5, columnspan=2)

# Run the main loop
window.mainloop()

