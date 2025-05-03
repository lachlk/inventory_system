from customtkinter import *
from app import App

def main():
    root = CTk()
    root.title("Inventory Management System")
    root.geometry("800x600")
    app = App(root)
    root.mainloop()
if __name__ == "__main__":
    main()