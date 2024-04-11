from tkinter import *

def calculate_tax_revenue():
  """
  Calculates the tax revenue based on price without tax, tax rate, and quantity.
  Updates the result label in the window.
  """
  try:
    price_no_tax = float(price_no_tax_entry.get())
    tax = float(tax_entry.get())
    quantity_at = int(quantity_entry.get())
    tax_revenue = tax * quantity_at
    result_label.config(text=f"The tax revenue generated is ${tax_revenue:.2f}")
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Tax Revenue Calculator")

# Labels
price_no_tax_label = Label(window, text="Price without Tax:")
tax_label = Label(window, text="Tax in $:")
quantity_label = Label(window, text="Quantity after Tax is Imposed:")
result_label = Label(window, text="")

# Entry fields
price_no_tax_entry = Entry(window)
tax_entry = Entry(window)
quantity_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_tax_revenue)

# Layout the widgets
price_no_tax_label.grid(row=0, column=0)
tax_label.grid(row=1, column=0)
quantity_label.grid(row=2, column=0)
result_label.grid(row=3, columnspan=2)

price_no_tax_entry.grid(row=0, column=1)
tax_entry.grid(row=1, column=1)
quantity_entry.grid(row=2, column=1)

calculate_button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()
