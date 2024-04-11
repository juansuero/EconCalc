from tkinter import *

def display_result(elasticity, change_price):
  """
  Calculates the percentage change in price and displays it in a new window.
  """
  percentage_change_quantity = round((change_price * elasticity), 2)
  result_text = f"The percentage change in quantity is: {percentage_change_quantity}%"

  # Create the result window
  window = Tk()
  window.title("Result (Quantity Change)")

  # Label for displaying the result
  result_label = Label(window, text=result_text)
  result_label.pack()

  # Run the main loop for the result window
  window.mainloop()

def get_input():
  """
  Prompts the user for elasticity and percentage change in price,
  performs basic validation, and closes the input window.
  """
  try:
    elasticity = float(elasticity_entry.get())
    change_price = float(change_price_entry.get())
    window.destroy()  # Close the input window
    display_result(elasticity, change_price)  # Call the local function
  except ValueError:
    error_label.config(text="Invalid Input! Please enter numbers.")

# Create the input window
window = Tk()
window.title("Enter Values (Elasticity & Change in Price)")

# Labels
elasticity_label = Label(window, text="Elasticity of Demand (negative):")
change_price_label = Label(window, text="Change in Price (%):")
error_label = Label(window, text="")

# Entry fields
elasticity_entry = Entry(window)
change_price_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=get_input)

# Layout the widgets
elasticity_label.grid(row=0, column=0)
change_price_label.grid(row=1, column=0)

elasticity_entry.grid(row=0, column=1)
change_price_entry.grid(row=1, column=1)

error_label.grid(row=2, columnspan=2)
calculate_button.grid(row=3, columnspan=2)

# Run the main loop for the input window
window.mainloop()
