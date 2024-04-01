import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk

registered_users = {}  # Dictionary to store registered usernames and passwords
search_entry = None  # Global variable for search entry
recipes = []  # List to store recipes

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the username exists and the password matches
    if entered_username in registered_users and registered_users[entered_username] == entered_password:
        messagebox.showinfo("Login Successful", "Welcome, " + entered_username + "!")
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_main_window():
    main_window = tk.Toplevel(root)
    main_window.title("Main Window")
    main_window.configure(background="#03A89E")  # Set background color

    # Add interface elements for the main window here
    label = tk.Label(main_window, text="Welcome to the Recipe Manager!", background="#03A89E", fg="white")
    label.pack(pady=10)

    # Add search bar
    search_frame = tk.Frame(main_window, background="#03A89E")
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Search:", background="#03A89E", fg="white")
    search_label.grid(row=0, column=0)

    global search_entry
    search_entry = tk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1)

    search_button = tk.Button(search_frame, text="Search", command=search_recipe)
    search_button.grid(row=0, column=2)

    # Add button to add recipe
    add_recipe_button = tk.Button(main_window, text="Add Recipe", command=add_recipe)
    add_recipe_button.pack(pady=10)

    # Add button to show recipes
    show_recipes_button = tk.Button(main_window, text="Show Recipes", command=show_recipes)
    show_recipes_button.pack(pady=5)

def search_recipe():
     search_query = search_entry.get().lower()
     show_recipes(search_query=search_query)
    
def add_recipe():
    add_recipe_window = tk.Toplevel(root)
    add_recipe_window.title("Add Recipe")
    add_recipe_window.configure(background="#03A89E")

    def save_recipe():
        name = recipe_name_entry.get()
        ingredients = recipe_ingredients_text.get("1.0", tk.END).strip()
        instructions = recipe_instructions_text.get("1.0", tk.END).strip()

        if name and ingredients and instructions:
            recipe = {"name": name, "ingredients": ingredients, "instructions": instructions}
            recipes.append(recipe)
            messagebox.showinfo("Recipe Saved", "Recipe saved successfully!")
            add_recipe_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    recipe_name_label = tk.Label(add_recipe_window, text="Recipe Name:")
    recipe_name_label.grid(row=0, column=0, padx=10, pady=5)

    recipe_name_entry = tk.Entry(add_recipe_window)
    recipe_name_entry.grid(row=0, column=1, padx=10, pady=5)

    recipe_ingredients_label = tk.Label(add_recipe_window, text="Ingredients:")
    recipe_ingredients_label.grid(row=1, column=0, padx=10, pady=5)

    recipe_ingredients_text = tk.Text(add_recipe_window, width=30, height=5)
    recipe_ingredients_text.grid(row=1, column=1, padx=10, pady=5)

    recipe_instructions_label = tk.Label(add_recipe_window, text="Instructions:")
    recipe_instructions_label.grid(row=2, column=0, padx=10, pady=5)

    recipe_instructions_text = tk.Text(add_recipe_window, width=30, height=5)
    recipe_instructions_text.grid(row=2, column=1, padx=10, pady=5)

    save_button = tk.Button(add_recipe_window, text="Save Recipe", command=save_recipe)
    save_button.grid(row=3, columnspan=2, padx=10, pady=10)

def show_recipes(search_query=None):
    show_recipes_window = tk.Toplevel(root)
    show_recipes_window.title("Recipes")
    show_recipes_window.configure(background="#03A89E")  

    tree_frame = tk.Frame(show_recipes_window, background="#03A89E")
    tree_frame.pack(expand=True, fill="both")

    tree = ttk.Treeview(tree_frame, columns=("Name"), show="headings")
    tree.heading("Name", text="Name")

    # Filter recipes based on search query
    filtered_recipes = recipes
    if search_query:
        filtered_recipes = [recipe for recipe in recipes if search_query in recipe["name"].lower()]

    for recipe in filtered_recipes:
        tree.insert("", "end", values=(recipe["name"]))

    tree.pack(expand=True, fill="both")

def register():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    # Check if the username is not empty and password is at least 6 characters
    if new_username and len(new_password) >= 6:
        registered_users[new_username] = new_password  # Store the new username and password
        messagebox.showinfo("Registration Successful", "Registration successful!")
    else:
        messagebox.showerror("Registration Failed", "Invalid username or password")

def show_registration_window():
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration")
    registration_window.geometry("300x150")  # Set the size of the registration window

    new_username_label = tk.Label(registration_window, text="New Username:")
    new_username_label.grid(row=0, column=0, padx=10, pady=5)
    global new_username_entry
    new_username_entry = tk.Entry(registration_window)
    new_username_entry.grid(row=0, column=1, padx=10, pady=5)

    new_password_label = tk.Label(registration_window, text="New Password:")
    new_password_label.grid(row=1, column=0, padx=10, pady=5)
    global new_password_entry
    new_password_entry = tk.Entry(registration_window, show="*")
    new_password_entry.grid(row=1, column=1, padx=10, pady=5)

    register_button = tk.Button(registration_window, text="Register", command=register)
    register_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Ionio Recipe Manager")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, background="#03A89E")
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

logo_img = ImageTk.PhotoImage(file="Image.png")
logo_widget = tk.Label(frame1, image=logo_img, background="#03A89E")
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(
    frame1,text="Ionio Recipe \n Manager",
    background="#03A89E",
    fg="white",
    font=("TkMenuFont", 24)
).pack()

# Create labels and entry widgets for username and password
username_label = tk.Label(frame1, text="Username:")
username_label.pack(pady=(30, 5))

username_entry = tk.Entry(frame1)
username_entry.pack(pady=5)

password_label = tk.Label(frame1, text="Password:")
password_label.pack()

password_entry = tk.Entry(frame1, show="*")
password_entry.pack(pady=5)

# Create a login button
login_button = tk.Button(frame1, text="Login", command=login)
login_button.pack(pady=10)

# Create a register button
register_button = tk.Button(frame1, text="Register", command=show_registration_window)
register_button.pack(pady=5)

root.mainloop()  # Start the GUI

