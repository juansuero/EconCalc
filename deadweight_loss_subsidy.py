
from tkinter import *

def calculate_deadweight_loss():
  """
  Calculates the deadweight loss based on price, subsidy, quantity before and after subsidy.
  Updates the result label in the window.
  """
  try:
    price_no_subsidy = float(price_no_subsidy_entry.get())
    subsidy = float(subsidy_entry.get())
    quantity_beforesubsidy = float(quantity_beforesubsidy_entry.get())
    quantity_aftersubsidy = float(quantity_aftersubsidy_entry.get())

    # Perform basic validation (check for non-negative quantities)
    if quantity_beforesubsidy < 0 or quantity_aftersubsidy < 0:
        result_label.config(text="Invalid Input! Quantities cannot be negative.")
        return

    quantity_difference = quantity_beforesubsidy - quantity_aftersubsidy
    deadweight_loss = 0.5 * (-subsidy * quantity_difference)
    result_label.config(text=f"The deadweight loss is ${deadweight_loss:.2f}")
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Deadweight Loss Calculator")

# Labels
price_no_subsidy_label = Label(window, text="Price without Subsidy:")
subsidy_label = Label(window, text="Subsidy in $:")
quantity_beforesubsidy_label = Label(window, text="Quantity Before Subsidy:")
quantity_aftersubsidy_label = Label(window, text="Quantity After Subsidy:")
result_label = Label(window, text="")

# Entry fields
price_no_subsidy_entry = Entry(window)
subsidy_entry = Entry(window)
quantity_beforesubsidy_entry = Entry(window)
quantity_aftersubsidy_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_deadweight_loss)

# Layout the widgets
price_no_subsidy_label.grid(row=0, column=0)
subsidy_label.grid(row=1, column=0)
quantity_beforesubsidy_label.grid(row=2, column=0)
quantity_aftersubsidy_label.grid(row=3, column=0)
result_label.grid(row=4, columnspan=2)

price_no_subsidy_entry.grid(row=0, column=1)
subsidy_entry.grid(row=1, column=1)
quantity_beforesubsidy_entry.grid(row=2, column=1)
quantity_aftersubsidy_entry.grid(row=3, column=1)

calculate_button.grid(row=5, columnspan=2)

# Run the main loop
window.mainloop()