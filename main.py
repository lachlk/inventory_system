from tkinter import Tk
from app import App

def main():
    root = Tk()
    root.title("Inventory Management System")
    root.state('zoomed')
    root.minsize(800, 600)
    app = App(root)
    root.mainloop()
if __name__ == "__main__":
    main()