from tkinter import Tk
from controllers.data_manager import DataManager
from app import App


def main():
    root = Tk()
    root.title("Inventory Management System")
    root.state('zoomed')
    root.minsize(800, 600)

    app = App(root)
    data_manager = DataManager('data/items.json')

    root.mainloop()


if __name__ == "__main__":
    main()
