
from tkinter import *

def calculate_deadweight_loss():
  """
  Calculates the deadweight loss based on price, tax, quantity before and after tax.
  Updates the result label in the window.
  """
  try:
    price_no_tax = float(price_no_tax_entry.get())
    tax = float(tax_entry.get())
    quantity_beforetax = float(quantity_beforetax_entry.get())
    quantity_aftertax = float(quantity_aftertax_entry.get())

    # Perform basic validation (check for non-negative quantities)
    if quantity_beforetax < 0 or quantity_aftertax < 0:
        result_label.config(text="Invalid Input! Quantities cannot be negative.")
        return

    quantity_difference = quantity_beforetax - quantity_aftertax
    deadweight_loss = 0.5 * (tax * quantity_difference)
    result_label.config(text=f"The deadweight loss is ${deadweight_loss:.2f}")
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Deadweight Loss Calculator")

# Labels
price_no_tax_label = Label(window, text="Price without Tax:")
tax_label = Label(window, text="Tax in $:")
quantity_beforetax_label = Label(window, text="Quantity Before Tax:")
quantity_aftertax_label = Label(window, text="Quantity After Tax:")
result_label = Label(window, text="")

# Entry fields
price_no_tax_entry = Entry(window)
tax_entry = Entry(window)
quantity_beforetax_entry = Entry(window)
quantity_aftertax_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_deadweight_loss)

# Layout the widgets
price_no_tax_label.grid(row=0, column=0)
tax_label.grid(row=1, column=0)
quantity_beforetax_label.grid(row=2, column=0)
quantity_aftertax_label.grid(row=3, column=0)
result_label.grid(row=4, columnspan=2)

price_no_tax_entry.grid(row=0, column=1)
tax_entry.grid(row=1, column=1)
quantity_beforetax_entry.grid(row=2, column=1)
quantity_aftertax_entry.grid(row=3, column=1)

calculate_button.grid(row=5, columnspan=2)

# Run the main loop
window.mainloop()
