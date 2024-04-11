from tkinter import *

def calculate_elasticity_of_demand(initial_quantity, final_quantity, initial_income, final_income):
  """Calculates the elasticity of demand using the midpoint formula.
  Args:
      initial_quantity: The initial quantity demanded.
      final_quantity: The final quantity demanded.
      initial_income: The initial income.
      final_income: The final income.
  Returns:
      The elasticity of demand (rounded to 2 decimal places).
  """

  # Calculate percentage changes using the midpoint formula
  percentage_change_income = ((final_income - initial_income) / ((initial_income + final_income) / 2)) * 100
  percentage_change_quantity = ((final_quantity - initial_quantity) / ((initial_quantity + final_quantity) / 2)) * 100

  # Calculate elasticity using the percentage changes
  elasticity_of_demand = percentage_change_quantity / percentage_change_income
  return round(elasticity_of_demand, 2)

def get_user_input():
  """
  Prompts the user for input through GUI entry fields and returns the values.
  """
  initial_income = float(initial_income_entry.get())
  initial_quantity = float(initial_quantity_entry.get())
  final_income = float(final_income_entry.get())
  final_quantity = float(final_quantity_entry.get())

  
  return initial_quantity, final_quantity, initial_income, final_income

def elasticity_type(elasticity):
  """
  Analyzes the elasticity value and displays the good's type based on income elasticity.
  """
  if elasticity > 1:
    result_label.config(text=f"The income elasticity is {elasticity:.2f}. Therefore the good is a luxury.")
  elif elasticity > 0:
    result_label.config(text=f"The income elasticity is {elasticity:.2f}. Therefore the good is normal.")
  elif elasticity < 0:
    result_label.config(text=f"The income elasticity is {elasticity:.2f}. Therefore the good is inferior.")
  else:
    result_label.config(text=f"The income elasticity is {elasticity:.2f}. Therefore the good is sticky.")

def calculate_elasticity():
  """
  Calls functions to get user input, calculate elasticity, and display the result.
  """
  try:
    initial_quantity, final_quantity, initial_income, final_income = get_user_input()
    elasticity_of_demand = calculate_elasticity_of_demand(initial_quantity, final_quantity, initial_income, final_income)
    elasticity_type(elasticity_of_demand)
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Income Elasticity of Demand Calculator")

# Labels
initial_income_label = Label(window, text="Initial Income:")
initial_quantity_label = Label(window, text="Initial Quantity:")
final_income_label = Label(window, text="Final Income:")
final_quantity_label = Label(window, text="Final Quantity:")
result_label = Label(window, text="")

# Entry fields
initial_income_entry = Entry(window)
initial_quantity_entry = Entry(window)
final_income_entry = Entry(window)
final_quantity_entry = Entry(window)
# Button
calculate_button = Button(window, text="Calculate", command=calculate_elasticity)

# Layout the widgets
initial_income_label.grid(row=0, column=0)
initial_quantity_label.grid(row=1, column=0)
final_income_label.grid(row=2, column=0)
final_quantity_label.grid(row=3, column=0)

initial_income_entry.grid(row=0, column=1)
initial_quantity_entry.grid(row=1, column=1)
final_income_entry.grid(row=2, column=1)
final_quantity_entry.grid(row=3, column=1)

calculate_button.grid(row=4, columnspan=2)
result_label.grid(row=5, columnspan=2)

# Run the main loop
window.mainloop()
