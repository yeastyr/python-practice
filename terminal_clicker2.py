import tkinter as tk
from tkinter import ttk

total_clicks = 0
prestige_total = 0
click_base = 1
click_multiplier = 1
total_upgrade = 0



# Main window

root = tk.Tk()
root.title("Terminal Clicker 2!!!!")
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)

style = ttk.Style()
style.theme_use("clam")
root.config(bg="#ffffff")

def upgrade_price():
    return int(50 * (1.25 ** total_upgrade))

def prestige_price():
    return int((10000 * (2.5 ** prestige_total)))

def per_click_total():
    return click_base * (click_multiplier * (2 ** prestige_total))


def refresh():
    counter.config(text=int(total_clicks))
    per_click.config(text=f"Per click: {per_click_total()}")
    upgrade_button.config(text=f"Upgrade! {upgrade_price()}")
    prestige_button.config(text=f"Prestige! Price: {prestige_price()}")


def prestige():
    global total_upgrade, total_clicks, prestige_total, click_base
    prestige_calculation = prestige_price()
    if total_clicks >= prestige_calculation:
        print("Prestiged")  
        click_base = 1
        total_clicks = 0
        total_upgrade = 0
        prestige_total = prestige_total + 1  
        refresh()
    else:
        print("Not enough money")


def upgrade():
    global total_clicks, total_upgrade, click_base
    upgrade_calculation = upgrade_price()
    if total_clicks >= upgrade_calculation :
        print("Upgraded")
        click_base = click_base + 1
        total_upgrade = total_upgrade + 1
        total_clicks = total_clicks - upgrade_calculation
        refresh()
    else:
        print("Not enough money")


def click(): 
    global total_clicks
    total_clicks += per_click_total()
    refresh()


# Main button
style.map("button.TButton", background=[("pressed", "#ffffff"), ("active", "#c2bebe")])
style.configure(
    "button.TButton", 
    font=("Comic Sans MS", 25, "bold"), 
    background="#ffffff", 
    foreground="#000000",
    relief="solid",
    borderwidth=1.5,
    bordercolor="#000000",
)

# Upgrade button
style.map("upgrade_button.TButton", background=[("pressed", "#ffffff"), ("active", "#c2bebe")])
style.configure(
    "upgrade_button.TButton", 
    font=("Comic Sans MS", 25, "bold"), 
    background="#ffffff", 
    foreground="#000000",
    relief="solid",
    borderwidth=1.5,
    bordercolor="#000000",
)

# Prestige button
style.map("prestige_button.TButton", background=[("pressed", "#ffffff"), ("active", "#c2bebe")])
style.configure(
    "prestige_button.TButton", 
    font=("Comic Sans MS", 25, "bold"), 
    background="#ffffff", 
    foreground="#000000",
    relief="solid",
    borderwidth=1.5,
    bordercolor="#000000",
)

# Total click - counter
style.configure(
    "counter.TLabel", 
    font=("Comic Sans MS", 35, "bold"), 
    background="#ffffff", 
    foreground="#000000",
)

# Per click - counter
style.configure(
    "per_click.TLabel", 
    font=("Comic Sans MS", 15, "bold italic"), 
    background="#ffffff", 
    foreground="#000000"
)


button = ttk.Button(
    root, 
    text="Click", 
    style="button.TButton",
    command=click,
)
button.place(relx=0.5, rely=0.6, anchor="center")

upgrade_button = ttk.Button(
    root,
    text=f"Upgrade! {upgrade_price()}",
    style="upgrade_button.TButton",
    command=upgrade,
)
upgrade_button.place(relx=0.5, rely=0.75, anchor="center")

prestige_button = ttk.Button(
    root,
    text=f"Prestige! Price: {prestige_price()}",
    style="prestige_button.TButton",
    command=prestige,
)
prestige_button.place(relx=0.5, rely=0.9, anchor="center")

counter = ttk.Label(
    root, 
    text=total_clicks, 
    style="counter.TLabel",
    anchor="center",
)
counter.place(relx=0.5, rely=0.25, anchor="center")

per_click = ttk.Label(
    root,
    text=f"Per click: {per_click_total()}",
    style="per_click.TLabel",
    anchor="center",
)
per_click.place(relx=0.5, rely=0.32, anchor="center")

root.mainloop()