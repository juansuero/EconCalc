from tkinter import *

def display_result(elasticity, change_quantity):
  """
  Calculates the percentage change in price and displays it in a new window.
  """
  percentage_change_price = round((change_quantity / elasticity), 2)
  result_text = f"The percentage change in price is: {percentage_change_price}%"

  # Create the result window
  window = Tk()
  window.title("Result (Price Change)")

  # Label for displaying the result
  result_label = Label(window, text=result_text)
  result_label.pack()

  # Run the main loop for the result window
  window.mainloop()

def get_input():
  """
  Prompts the user for elasticity and percentage change in quantity,
  performs basic validation, and closes the input window.
  """
  try:
    elasticity = float(elasticity_entry.get())
    change_quantity = float(change_quantity_entry.get())
    window.destroy()  # Close the input window
    display_result(elasticity, change_quantity)  # Call the local function
  except ValueError:
    error_label.config(text="Invalid Input! Please enter numbers.")

# Create the input window
window = Tk()
window.title("Enter Values (Elasticity & Change in Quantity)")

# Labels
elasticity_label = Label(window, text="Elasticity of Demand (negative):")
change_quantity_label = Label(window, text="Change in Quantity (%):")
error_label = Label(window, text="")

# Entry fields
elasticity_entry = Entry(window)
change_quantity_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=get_input)

# Layout the widgets
elasticity_label.grid(row=0, column=0)
change_quantity_label.grid(row=1, column=0)

elasticity_entry.grid(row=0, column=1)
change_quantity_entry.grid(row=1, column=1)

error_label.grid(row=2, columnspan=2)
calculate_button.grid(row=3, columnspan=2)

# Run the main loop for the input window
window.mainloop()

