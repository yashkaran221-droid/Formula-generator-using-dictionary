import tkinter as tk
from tkinter import ttk, messagebox

# --- Step 1: Dictionary Data (instead of SQL database) ---
formulas = {
    "Physics": {
        "Electric Charges & Fields": {
            "Coulomb’s Law": "F = (1 / (4πε₀)) * (q₁q₂ / r²)"
        },
        "Current Electricity": {
            "Ohm’s Law": "V = IR"
        },
        "Moving Charges & Magnetism": {
            "Magnetic Force": "F = q(v × B)"
        },
        "Electromagnetic Induction": {
            "Faraday’s Law": "ε = - dΦ/dt"
        },
        "Alternating Current": {
            "Impedance in AC": "Z = √(R² + (X_L - X_C)²)"
        }
    },

    "Chemistry": {
        "Solid State": {
            "Density of Unit Cell": "ρ = (Z * M) / (a³ * N_A)"
        },
        "Solutions": {
            "Raoult’s Law": "P₁ = X₁ * P₁⁰"
        },
        "Electrochemistry": {
            "Nernst Equation": "E = E° - (RT/nF) * lnQ"
        },
        "Chemical Kinetics": {
            "Rate Law": "r = k[A]^m[B]^n"
        },
        "Surface Chemistry": {
            "Adsorption": "x/m = k * p^(1/n)"
        }
    },

    "Maths": {
        "Relations & Functions": {
            "Inverse of Function": "f⁻¹(f(x)) = x"
        },
        "Matrices": {
            "Determinant of 2x2 Matrix": "|A| = ad - bc"
        },
        "Determinants": {
            "Cramer’s Rule": "x = Δx/Δ,  y = Δy/Δ"
        },
        "Integrals": {
            "Integration of xⁿ": "∫xⁿ dx = xⁿ⁺¹ / (n+1) + C"
        },
        "Probability": {
            "Addition Theorem": "P(A ∪ B) = P(A) + P(B) - P(A ∩ B)"
        }
    }
}

# --- Step 2: Functions ---

def update_chapters(event=None):
    subject = subject_var.get()
    chapter_menu['values'] = list(formulas[subject].keys())
    chapter_menu.set('')

def show_all():
    subject = subject_var.get()
    if not subject:
        messagebox.showerror("Error", "Please select a subject first.")
        return
    output_text.delete(1.0, tk.END)
    for chapter, topics in formulas[subject].items():
        output_text.insert(tk.END, f"📘 {chapter}\n")
        for topic, formula in topics.items():
            output_text.insert(tk.END, f"  • {topic}: {formula}\n")
        output_text.insert(tk.END, "\n")

def show_formula():
    subject = subject_var.get()
    chapter = chapter_var.get()
    if not subject or not chapter:
        messagebox.showerror("Error", "Please select both subject and chapter.")
        return
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"📘 {chapter}\n\n")
    for topic, formula in formulas[subject][chapter].items():
        output_text.insert(tk.END, f"• {topic}: {formula}\n")

# --- Step 3: GUI Setup ---

root = tk.Tk()
root.title("Class 12 Formula Viewer")
root.geometry("600x400")
root.resizable(False, False)

# Labels
tk.Label(root, text="Subject:", font=("Arial", 12)).pack(pady=5)
subject_var = tk.StringVar()
subject_menu = ttk.Combobox(root, textvariable=subject_var, values=list(formulas.keys()), state="readonly", width=30)
subject_menu.pack()
subject_menu.bind("<<ComboboxSelected>>", update_chapters)

tk.Label(root, text="Chapter:", font=("Arial", 12)).pack(pady=5)
chapter_var = tk.StringVar()
chapter_menu = ttk.Combobox(root, textvariable=chapter_var, state="readonly", width=30)
chapter_menu.pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Button(frame, text="Show All Formulas", command=show_all, bg="#4CAF50", fg="white", width=18).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Show Formula by Chapter", command=show_formula, bg="#2196F3", fg="white", width=22).grid(row=0, column=1, padx=10)

# Output box
output_text = tk.Text(root, height=10, width=70, wrap="word", font=("Consolas", 10))
output_text.pack(padx=10, pady=10)

root.mainloop()
