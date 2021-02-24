import tkinter as tk


class Window:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Jeggy')
        self.window.iconbitmap(".\images\jeggo_4Bf_icon.ico")
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.window.geometry("700x500")
        # Menus
        self.auctions_menu = tk.Menu(self.menu, tearoff=0)
        self.commHub_menu = tk.Menu(self.menu, tearoff=0)
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        # cascade set for each menu
        self.menu.add_cascade(label='Auctions', menu=self.auctions_menu)
        self.menu.add_cascade(label='CommerceHUB', menu=self.commHub_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        # options under the Auctions menu option
        self.auctions_menu.add_command(label="New Scrape")
        self.auctions_menu.add_command(label="Open")
        self.window.mainloop()
