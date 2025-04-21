import tkinter as tk
from tkinter import messagebox

def clear_form():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    for entry in mark_entries:
        entry.delete(0, tk.END)
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.config(state='disabled')

def generate_result():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()

    if not name or not roll:
        messagebox.showwarning("Missing Info", "Please fill Name and Roll No.")
        return

    try:
        marks = [float(e.get()) for e in mark_entries]
        if any(m < 0 or m > 100 for m in marks):
            raise ValueError

        total = sum(marks)
        percent = total / 5

        # Grade logic
        if percent >= 90:
            grade = 'A+'
        elif percent >= 80:
            grade = 'A'
        elif percent >= 70:
            grade = 'B'
        elif percent >= 60:
            grade = 'C'
        elif percent >= 50:
            grade = 'D'
        else:
            grade = 'F'

        result = "Pass" if percent >= 33 else "Fail"

        result_display = f"""🎓 Student Result Card 🎓
-------------------------------
Name       : {name}
Roll No.   : {roll}
-------------------------------
Total Marks: {total}/500
Percentage : {percent:.2f}%
Grade      : {grade}
Result     : {result}
"""
        result_text.config(state='normal')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result_display)
        result_text.config(state='disabled')

    except ValueError:
        messagebox.showerror("Invalid Marks", "Please enter valid marks (0-100 only).")

# ==== GUI Setup ====
root = tk.Tk()
root.title("📝 Student Result Generator")
root.geometry("450x600")
root.configure(bg="#f4f4f4")

tk.Label(root, text="Student Result Generator", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

form_frame = tk.Frame(root, bg="#f4f4f4")
form_frame.pack(pady=10)

# Name & Roll No
tk.Label(form_frame, text="Student Name:", bg="#f4f4f4").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Roll No:", bg="#f4f4f4").grid(row=1, column=0, sticky="w", pady=5)
roll_entry = tk.Entry(form_frame, width=30)
roll_entry.grid(row=1, column=1, pady=5)

# Subject Marks
mark_entries = []
for i in range(5):
    tk.Label(form_frame, text=f"Subject {i+1} Marks:", bg="#f4f4f4").grid(row=i+2, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, width=30)
    entry.grid(row=i+2, column=1, pady=5)
    mark_entries.append(entry)

# Buttons
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Generate Result", command=generate_result, bg="#28a745", fg="white", width=20).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_form, bg="#dc3545", fg="white", width=10).grid(row=0, column=1, padx=10)

# Result Display
result_text = tk.Text(root, height=10, width=50, font=("Courier", 10), bg="#fff")
result_text.pack(pady=10)
result_text.config(state='disabled')

root.mainloop()
