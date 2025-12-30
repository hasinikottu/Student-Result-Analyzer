import tkinter as tk
from tkinter import messagebox
import csv
import os

# ---------------- DATA ----------------
students = []
FILE_NAME = "students.csv"
dark_mode = False

# ---------------- LOGIC ----------------
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

def clear_fields():
    for e in [roll_entry, name_entry, m1_entry, m2_entry, m3_entry]:
        e.delete(0, tk.END)

def save_to_csv():
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll", "Name", "Total"])
        for s in students:
            writer.writerow([s["roll"], s["name"], s["total"]])

def load_from_csv():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                "roll": row["Roll"],
                "name": row["Name"],
                "total": int(row["Total"])
            })

def add_student():
    try:
        roll = roll_entry.get().strip()
        name = name_entry.get().strip()
        m1 = int(m1_entry.get())
        m2 = int(m2_entry.get())
        m3 = int(m3_entry.get())

        if not roll or not name:
            raise ValueError

        total = m1 + m2 + m3
        avg = total / 3
        grade = calculate_grade(avg)
        result = "Pass" if avg >= 60 else "Fail"

        students.append({
            "roll": roll,
            "name": name,
            "total": total
        })

        save_to_csv()
        messagebox.showinfo(
            "🎉 Student Added",
            f"Name: {name}\nTotal: {total}\nGrade: {grade}\nResult: {result}"
        )
        clear_fields()

    except ValueError:
        messagebox.showerror("❌ Error", "Please enter valid inputs")

def show_rank_list():
    if not students:
        messagebox.showwarning("⚠️ No Data", "No student records available")
        return

    ranked = sorted(students, key=lambda x: x["total"], reverse=True)

    text = "🏆 RANK LIST\n\nRank  Roll  Name        Total\n"
    text += "-" * 35 + "\n"

    for i, s in enumerate(ranked, start=1):
        text += f"{i:<5} {s['roll']:<5} {s['name']:<12} {s['total']}\n"

    messagebox.showinfo("Rank List", text)

def view_all_students():
    if not students:
        messagebox.showwarning("⚠️ No Data", "No student records available")
        return

    win = tk.Toplevel(root)
    win.title("All Students")
    win.geometry("420x300")

    text = tk.Text(win, font=("Segoe UI", 10))
    text.pack(fill="both", expand=True)

    text.insert("end", "Roll   Name        Total\n")
    text.insert("end", "-" * 30 + "\n")

    for s in students:
        text.insert("end", f"{s['roll']:<6} {s['name']:<12} {s['total']}\n")

    text.config(state="disabled")

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#0f172a" if dark_mode else "#eef2f7"
    card_bg = "#020617" if dark_mode else "white"
    fg = "white" if dark_mode else "#1f2937"
    entry_bg = "#1e293b" if dark_mode else "#f1f5f9"

    root.configure(bg=bg)
    card.configure(bg=card_bg)
    header.configure(bg="#020617" if dark_mode else "#6366f1")

    for lbl in labels:
        lbl.configure(bg=card_bg, fg=fg)
    for ent in entries:
        ent.configure(bg=entry_bg, fg=fg, insertbackground=fg)

# ---------------- UI ----------------
root = tk.Tk()
root.title("Student Result Analyzer")
root.geometry("650x650")
root.configure(bg="#eef2f7")
root.resizable(False, False)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg="#6366f1", height=90)
header.pack(fill="x")

tk.Label(
    header,
    text="🎓 Student Result Analyzer",
    bg=header["bg"],
    fg="white",
    font=("Segoe UI", 22, "bold")
).pack(pady=(18, 0))

tk.Label(
    header,
    bg=header["bg"],
    fg="#e0e7ff",
    font=("Segoe UI", 11)
).pack()

# ---------------- CARD ----------------
card = tk.Frame(root, bg="white", padx=30, pady=25)
card.pack(pady=30)

labels = []
entries = []

def make_label(text, r):
    l = tk.Label(card, text=text, bg="white", fg="#1f2937",
                 font=("Segoe UI", 10, "bold"))
    l.grid(row=r, column=0, sticky="w")
    labels.append(l)

def make_entry(r):
    e = tk.Entry(card, width=35, font=("Segoe UI", 10),
                 relief="flat", bg="#f1f5f9")
    e.grid(row=r, column=0, pady=(0, 12))
    entries.append(e)
    return e

make_label("Roll Number", 0)
roll_entry = make_entry(1)

make_label("Student Name", 2)
name_entry = make_entry(3)

make_label("Subject 1 Marks", 4)
m1_entry = make_entry(5)

make_label("Subject 2 Marks", 6)
m2_entry = make_entry(7)

make_label("Subject 3 Marks", 8)
m3_entry = make_entry(9)

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(card, bg="white")
btn_frame.grid(row=10, column=0, pady=10)

tk.Button(btn_frame, text="➕ Add Student", bg="#4f46e5",
          fg="white", width=16, relief="flat",
          font=("Segoe UI", 10, "bold"),
          command=add_student).grid(row=0, column=0, padx=6)

tk.Button(btn_frame, text="🏆 Rank List", bg="#22c55e",
          fg="white", width=16, relief="flat",
          font=("Segoe UI", 10, "bold"),
          command=show_rank_list).grid(row=0, column=1, padx=6)

tk.Button(btn_frame, text="📋 View All", bg="#0ea5e9",
          fg="white", width=16, relief="flat",
          font=("Segoe UI", 10, "bold"),
          command=view_all_students).grid(row=1, column=0, padx=6, pady=6)

tk.Button(btn_frame, text="🌙 Dark Mode", bg="#334155",
          fg="white", width=16, relief="flat",
          font=("Segoe UI", 10, "bold"),
          command=toggle_theme).grid(row=1, column=1, padx=6, pady=6)

# ---------------- FOOTER ----------------
tk.Label(
    root,
    text="GUI-Based Python Mini Project",
    bg=root["bg"],
    fg="#6b7280",
    font=("Segoe UI", 9)
).pack(pady=12)

load_from_csv()
root.mainloop()
