from tkinter import *

def calculate_capital_recovery_factor():
  """
  Calculates the capital recovery factor based on present value, interest rate, and number of years.
  Updates the result label in the window.
  """
  try:
    present_value = float(present_value_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100  # Convert percentage to decimal
    number_years = float(number_years_entry.get())

    # Ensure valid positive values for present value and number of years
    if present_value <= 0 or number_years <= 0:
        result_label.config(text="Invalid Input! Present value and number of years must be positive.")
        return

    annuity = present_value * (interest_rate * ((1 + interest_rate) ** number_years)) / (((1 + interest_rate) ** number_years) - 1)
    result_label.config(text=f"The Annuity is ${annuity:.2f}")  # Display factor, not present_value
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Capital Recovery Calculator")

# Labels
present_value_label = Label(window, text="Annuity:")
interest_rate_label = Label(window, text="Interest Rate (%):")
number_years_label = Label(window, text="Number of Years:")
result_label = Label(window, text="")

# Entry fields
present_value_entry = Entry(window)
interest_rate_entry = Entry(window)
number_years_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_capital_recovery_factor)

# Layout the widgets
present_value_label.grid(row=0, column=0)
interest_rate_label.grid(row=1, column=0)
number_years_label.grid(row=2, column=0)
result_label.grid(row=3, columnspan=2)

present_value_entry.grid(row=0, column=1)
interest_rate_entry.grid(row=1, column=1)
number_years_entry.grid(row=2, column=1)

calculate_button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()