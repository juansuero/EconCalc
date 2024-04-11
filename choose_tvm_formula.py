import tkinter as tk

def choose_tvm_formula():
    print('This program helps you choose the right TVM formula to use (out of the 6 ones we have)')

    while True:
        try:
            what_looking_for = input('What are you looking for? Input one of the following: Present Value, Future Value, Annuity) ').title()
            if what_looking_for not in ['Present Value', 'Future Value', 'Annuity']:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please try again.')

    while True:
        try:
            single_or_series = input('Is it a single payment or a series of payments? Input one of the following: Single, Series) ').title()
            if single_or_series not in ['Single', 'Series']:
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please try again.')

    if what_looking_for == 'Future Value' and single_or_series == 'Single':
        print('You should use the Single Payment - Compound Amount Factor formula')
    elif what_looking_for == 'Future Value' and single_or_series == 'Series':
        print('You should use the Uniform Series - Compound Amount Factor formula')
    elif what_looking_for == 'Present Value' and single_or_series == 'Single':
        print('You should use the Single Payment - Present Worth Factor formula')
    elif what_looking_for == 'Present Value' and single_or_series == 'Series':
        print('You should use the Uniform Series - Present Worth Factor formula')
    elif what_looking_for == 'Annuity' and single_or_series == 'Series':
        while True:
            try:
                pv_or_fv = input('Do you know the Present Value or the Future Value? Input Present Value or Future Value) ').title()
                if pv_or_fv not in ['Present Value', 'Future Value']:
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. Please try again.')

        if pv_or_fv == 'Present Value':
            print('You should use the Uniform Series - Capital Recovery Factor formula')
        elif pv_or_fv == 'Future Value':
            print('You should use the Uniform Series - Sinking Fund Factor formula')

def on_submit():
    what_looking_for = radio_var.get()
    single_or_series = check_var.get()

    if what_looking_for == 1 and single_or_series == 1:
        result_label.config(text='You should use the Single Payment - Compound Amount Factor formula')
    elif what_looking_for == 1 and single_or_series == 2:
        result_label.config(text='You should use the Uniform Series - Compound Amount Factor formula')
    elif what_looking_for == 2 and single_or_series == 1:
        result_label.config(text='You should use the Single Payment - Present Worth Factor formula')
    elif what_looking_for == 2 and single_or_series == 2:
        result_label.config(text='You should use the Uniform Series - Present Worth Factor formula')
    elif what_looking_for == 3 and single_or_series == 2:
        pv_or_fv = check_var2.get()

        if pv_or_fv == 1:
            result_label.config(text='You should use the Uniform Series - Capital Recovery Factor formula')
        elif pv_or_fv == 2:
            result_label.config(text='You should use the Uniform Series - Sinking Fund Factor formula')

root = tk.Tk()
root.title('TVM Formula Selector')

# Radio buttons for what the user is looking for
radio_var = tk.IntVar()
radio_var.set(1)

radio_frame = tk.Frame(root)
radio_frame.pack()

present_value_radio = tk.Radiobutton(radio_frame, text='Present Value', variable=radio_var, value=1)
present_value_radio.pack()

future_value_radio = tk.Radiobutton(radio_frame, text='Future Value', variable=radio_var, value=2)
future_value_radio.pack()

annuity_radio = tk.Radiobutton(radio_frame, text='Annuity', variable=radio_var, value=3)
annuity_radio.pack()

# Check buttons for single or series
check_var = tk.IntVar()
check_var.set(1)

check_frame = tk.Frame(root)
check_frame.pack()

single_check = tk.Checkbutton(check_frame, text='Single', variable=check_var, onvalue=1, offvalue=0)
single_check.pack()

series_check = tk.Checkbutton(check_frame, text='Series', variable=check_var, onvalue=2, offvalue=0)
series_check.pack()

# Check buttons for annuity options
check_var2 = tk.IntVar()
check_var2.set(1)

check_frame2 = tk.Frame(root)
check_frame2.pack()

present_value_check = tk.Checkbutton(check_frame2, text='Present Value', variable=check_var2, onvalue=1, offvalue=0)
present_value_check.pack()

future_value_check = tk.Checkbutton(check_frame2, text='Future Value', variable=check_var2, onvalue=2, offvalue=0)
future_value_check.pack()

# Submit button
submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.pack()

# Result label
result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()

choose_tvm_formula()