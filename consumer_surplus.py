from tkinter import *

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
  """
  Prints the calculated consumer surplus with a message.

  Args:
      consumer_surplus: The calculated consumer surplus.
  """

  result_label.config(text=f"The consumer surplus is ${consumer_surplus:.2f}")

def get_user_input(label_text, entry_var):
  """
  Prompts the user for input using a label and entry field,
  performs basic validation, and returns the value.
  """
  try:
    value = float(entry_var.get())
    return value
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")
    return None  # Indicate error

def calculate_and_display():
  """
  Gets user input, calculates consumer surplus, and displays the result.
  """
  price = get_user_input("Equilibrium Price:", price_entry)
  quantity = get_user_input("Equilibrium Quantity:", quantity_entry)
  price_when_q_0 = get_user_input("Price at Q=0:", price_q0_entry)

  if price is not None and quantity is not None and price_when_q_0 is not None:
    # All inputs valid, proceed with calculation
    consumer_surplus = calculate_consumer_surplus(price, quantity, price_when_q_0)
    print_result(consumer_surplus)

# Create the main window
window = Tk()
window.title("Consumer Surplus Calculator")

# Labels
price_label = Label(window, text="Equilibrium Price:")
quantity_label = Label(window, text="Equilibrium Quantity:")
price_q0_label = Label(window, text="Price at Q=0:")
result_label = Label(window, text="")

# Entry fields
price_entry = Entry(window)
quantity_entry = Entry(window)
price_q0_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_and_display)

# Layout the widgets
price_label.grid(row=0, column=0)
quantity_label.grid(row=1, column=0)
price_q0_label.grid(row=2, column=0)
result_label.grid(row=3, columnspan=2)

price_entry.grid(row=0, column=1)
quantity_entry.grid(row=1, column=1)
price_q0_entry.grid(row=2, column=1)

calculate_button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()
