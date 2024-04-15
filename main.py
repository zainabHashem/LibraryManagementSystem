import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, book_id, name, author, copies):
        self.id = book_id
        self.name = name
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Book ID: {self.id}, Name: {self.name}, Author: {self.author}, Copies: {self.copies}"

books = {}

def add_book_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Book")

    book_id_entry = tk.Entry(add_window)
    book_id_label = tk.Label(add_window, text="Enter Book ID:")
    book_id_label.grid(row=0, column=0)
    book_id_entry.grid(row=0, column=1)

    name_entry = tk.Entry(add_window)
    name_label = tk.Label(add_window, text="Enter Name of book:")
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1)

    author_entry = tk.Entry(add_window)
    author_label = tk.Label(add_window, text="Enter Name of Author:")
    author_label.grid(row=2, column=0)
    author_entry.grid(row=2, column=1)

    copies_entry = tk.Entry(add_window)
    copies_label = tk.Label(add_window, text="Enter Number of Copies:")
    copies_label.grid(row=3, column=0)
    copies_entry.grid(row=3, column=1)

    submit_button = tk.Button(add_window, text="Submit", bg="lightgreen",activebackground="blue",
                              font=("Arial", 11, "bold"), command=lambda: add_book(book_id_entry.get(), name_entry.get(), author_entry.get(), copies_entry.get()))
    submit_button.grid(row=4, columnspan=2)

def add_book(book_id, name, author, copies):
    if not book_id or not name or not author or not copies:
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        try:
            copies = int(copies)
            if copies <= 0:
                raise ValueError
            if book_id in books:
                raise KeyError
            books[book_id] = Book(book_id, name, author, copies)
            messagebox.showinfo("Success", "Book added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for copies.")
        except KeyError:
            messagebox.showerror("Error", "Book ID already exists. Enter a different Book ID.")

def view_all_window():
    view_window = tk.Toplevel(root)
    view_window.title("View All Books")
    if books:
        for idx, (book_id, book) in enumerate(books.items(), start=1):
            label_text = f"{idx}. {book}"
            tk.Label(view_window, text=label_text).pack()
    else:
        tk.Label(view_window, text="No books available. Please add books to our library.").pack()

def update_book_window():
    update_window = tk.Toplevel(root)
    update_window.title("Update Book")

    book_id_entry = tk.Entry(update_window)
    book_id_label = tk.Label(update_window, text="Enter Book ID:")
    book_id_label.grid(row=0, column=0)
    book_id_entry.grid(row=0, column=1)

    name_entry = tk.Entry(update_window)
    name_label = tk.Label(update_window, text="Enter Name of book:")
    name_label.grid(row=1, column=0)
    name_entry.grid(row=1, column=1)

    author_entry = tk.Entry(update_window)
    author_label = tk.Label(update_window, text="Enter Name of Author:")
    author_label.grid(row=2, column=0)
    author_entry.grid(row=2, column=1)

    copies_entry = tk.Entry(update_window)
    copies_label = tk.Label(update_window, text="Enter Number of Copies:")
    copies_label.grid(row=3, column=0)
    copies_entry.grid(row=3, column=1)

    submit_button = tk.Button(update_window, text="Submit", bg="lightgreen",activebackground="blue", 
                              font=("Arial", 11, "bold"), command=lambda: update_book(book_id_entry.get(), name_entry.get(), author_entry.get(), copies_entry.get()))
    submit_button.grid(row=4, columnspan=2)

def update_book(book_id, name, author, copies):
    if book_id in books:
        try:
            copies = int(copies)
            if copies <= 0:
                raise ValueError
            books[book_id].name = name
            books[book_id].author = author
            books[book_id].copies = copies
            messagebox.showinfo("Success", "Book updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for copies.")
    else:
        messagebox.showerror("Error", "Book ID not found.")

def delete_book_window():
    def delete_confirm():
        book_id = book_id_entry.get()
        if book_id in books:
            del books[book_id]
            messagebox.showinfo("Success", "Book deleted successfully.")
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "Book ID not found.")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Book")

    book_id_entry = tk.Entry(delete_window)
    book_id_label = tk.Label(delete_window, text="Enter Book ID:")
    book_id_label.pack()
    book_id_entry.pack()

    submit_button = tk.Button(delete_window, text="Delete", bg="lightgreen",activebackground="blue",
                              font=("Arial", 11, "bold"), command=delete_confirm)
    submit_button.pack()

def check_book_window():
    check_window = tk.Toplevel(root)
    check_window.title("Check Book")

    book_id_entry = tk.Entry(check_window)
    book_id_label = tk.Label(check_window, text="Enter Book ID:")
    book_id_label.pack()
    book_id_entry.pack()

    submit_button = tk.Button(check_window, text="Check", bg="lightgreen",activebackground="blue",
                              font=("Arial", 11, "bold"), command=lambda: check_book(book_id_entry.get()))
    submit_button.pack()

def check_book(book_id):
    if book_id in books:
        messagebox.showinfo("Book Details", str(books[book_id]))
    else:
        messagebox.showerror("Error", "Book ID not found.")

def on_exit():
  if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
      root.destroy()
    
root = tk.Tk()
root.title("Library Management System")

window_width = 800
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.config(bg="lightblue")

menu_label = tk.Label(root, text="Menu:", font=("Arial", 20, "bold"), bg="lightblue")
menu_label.pack()
options = [
  ("Add Book", add_book_window),
  ("Display Books", view_all_window),
  ("Update Book", update_book_window),
  ("Delete Book", delete_book_window),
  ("Check a Book", check_book_window),
  ("Exit", on_exit)
]

for text, command in options:
  tk.Button(root, text=text, command=command, bg="lightgreen",
            activebackground="blue", borderwidth=3,
            font=("Arial", 11, "bold")).pack()
root.protocol("WM_DELETE_WINDOW", on_exit)  # Handle window close button
root.mainloop()