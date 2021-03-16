import tkinter as tk
import scrapes
import os


class Window:
    def scrape_select_auction(self):
        scrapes.scrape('select auctions')

    def scrape_superior_aution(self):
        print("superior auction selected")

    def scrape_Bsupply_acution(self):
        print("B-supply action")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Jeggy')
        self.window.iconbitmap(".\images\jeggo_4Bf_icon.ico")
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.window.geometry("700x500")
        self.window.config(bg='light blue')
        background_img = tk.PhotoImage("images/JEGgo.png")

        # create canvas to display over window.
        self.canvas = tk.Canvas(self.window, width=660, height=460, bg='white')
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')

        self.label = tk.Label(self.canvas, text='progress')
        self.label.place(relx=0.1, rely=0.5)

        # Menus
        self.auctions_menu = tk.Menu(self.menu, tearoff=0)
        self.commHub_menu = tk.Menu(self.menu, tearoff=0)
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.scrape_menu = tk.Menu(self.auctions_menu, tearoff=0)
        # cascade set for each menu
        self.menu.add_cascade(label='Auctions', menu=self.auctions_menu)
        self.menu.add_cascade(label='CommerceHUB', menu=self.commHub_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)

        # options under the Auctions menu option
        self.auctions_menu.add_command(label="Scrape All")
        self.auctions_menu.add_cascade(label="Scrape", menu=self.scrape_menu)

        # self.canvas.config(xpad=50, ypad=50)

        self.scrape_menu.add_command(label="Superior Auctions", command=self.scrape_superior_aution)
        self.scrape_menu.add_command(label="Select Mobile Auctions", command=self.scrape_select_auction)
        self.scrape_menu.add_command(label="B-Stock Supply Auctions", command=self.scrape_Bsupply_acution)

        self.auctions_menu.add_command(label="Open")

        self.window.mainloop()

