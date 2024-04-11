from tkinter import *

def calculate_sinking_fund_factor():
  """
  Calculates the sinking fund factor (uniform series) based on future value, interest rate, and number of years.
  Updates the result label in the window.
  """
  try:
    future_value = float(future_value_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100  # Convert percentage to decimal
    number_years = float(number_years_entry.get())

    # Ensure valid positive values for present value and number of years
    if future_value <= 0 or number_years <= 0:
        result_label.config(text="Invalid Input! Present value and number of years must be positive.")
        return

    annuity = future_value * interest_rate / (((1 + interest_rate) ** number_years)-1)
    result_label.config(text=f"The Annuity is ${annuity:.2f}")  # Display factor, not future value
  except ValueError:
    result_label.config(text="Invalid Input! Please enter numbers.")

# Create the main window
window = Tk()
window.title("Sinking Fund Factor - Uniform Series Calculator")

# Labels
future_value_label = Label(window, text="Future Value:")
interest_rate_label = Label(window, text="Interest Rate (%):")
number_years_label = Label(window, text="Number of Years:")
result_label = Label(window, text="")

# Entry fields
future_value_entry = Entry(window)
interest_rate_entry = Entry(window)
number_years_entry = Entry(window)

# Button
calculate_button = Button(window, text="Calculate", command=calculate_sinking_fund_factor)

# Layout the widgets
future_value_label.grid(row=0, column=0)
interest_rate_label.grid(row=1, column=0)
number_years_label.grid(row=2, column=0)
result_label.grid(row=3, columnspan=2)

future_value_entry.grid(row=0, column=1)
interest_rate_entry.grid(row=1, column=1)
number_years_entry.grid(row=2, column=1)

calculate_button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()