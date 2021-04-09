import tkinter as tk
import scrapes
import threading
import auctions
import searches
import os


def run_select_auctions_scrape():
    scrapes.scrape("select auctions")


def write_all_select_auction_data():
    scrapes.write_scrape_data_all("select auctions")

def write_A_select_auction_data():
    stuff = searches.search_for_a_grade(scrapes.select_auction_items)
    print(len(stuff))
    scrapes.copy_of_select_auction_items = stuff
    print(len(scrapes.select_auction_items))
    scrapes.write_filtered_scrape_data("select auctions")

def write_B_select_auction_data():
    stuff = searches.search_for_b_grade(scrapes.select_auction_items)
    print(len(stuff))
    scrapes.copy_of_select_auction_items = stuff
    print(len(scrapes.select_auction_items))
    scrapes.write_filtered_scrape_data("select auctions")

def write_C_select_auction_data():
    stuff = searches.search_for_c_grade(scrapes.select_auction_items)
    print(len(stuff))
    scrapes.copy_of_select_auction_items = stuff
    print(len(scrapes.select_auction_items))
    scrapes.write_filtered_scrape_data("select auctions")

    #scrapes.write_scrape_data("select auctions")

def write_apple_select_auction_data():
    stuff = searches.search_for_apple(scrapes.select_auction_items)
    print(len(stuff))
    scrapes.copy_of_select_auction_items = stuff
    print(len(scrapes.select_auction_items))
    scrapes.write_filtered_scrape_data("select auctions")

def write_samsung_select_auction_data():
    stuff = searches.search_for_samsung(scrapes.select_auction_items)
    print(len(stuff))
    scrapes.copy_of_select_auction_items = stuff
    print(len(scrapes.select_auction_items))
    scrapes.write_filtered_scrape_data("select auctions")



def write_all_auction_data():
    scrapes.write_scrape_data_all("select auctions")


class Window:
    def animated_working(self):
        animations = ['.', '..', '...', '....', '.....']
        for animation in animations:
            self.canvas.itemconfig(self.working, text="working stiff")

    def scrape_select_auction(self):
        t1 = threading.Thread(target=run_select_auctions_scrape)
        t1.start()
        while t1.is_alive():
            self.canvas.itemconfigure(self.working, text="Data Collected")
            # scrapes.scrape('select auctions')

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
        self.window.geometry("680x480")
        self.window.config(bg='light blue')
        background_img = tk.PhotoImage("images/JEGgo.png")

        # create canvas to display over window.
        self.canvas = tk.Canvas(self.window, width=660, height=460, bg='white')
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')

        self.working = self.canvas.create_text(330, 230, text="where is this")

        # self.label = tk.Label(self.canvas, text='')
        # self.label.place(relx=0.1, rely=0.5)


        # Menus
        self.auctions_menu = tk.Menu(self.menu, tearoff=0)
        self.commHub_menu = tk.Menu(self.menu, tearoff=0)
        self.export_menu = tk.Menu(self.menu, tearoff=0)
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.scrape_menu = tk.Menu(self.auctions_menu, tearoff=0)
        # cascade set for each menu
        self.menu.add_cascade(label='Auctions', menu=self.auctions_menu)
        self.menu.add_cascade(label='CommerceHUB', menu=self.commHub_menu)
        self.menu.add_cascade(label='Excel Export', menu=self.export_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)

        # options under the Auctions menu option
        self.auctions_menu.add_command(label="Scrape All")
        self.auctions_menu.add_cascade(label="Scrape", menu=self.scrape_menu)

        # self.canvas.config(xpad=50, ypad=50)
        # actions under each menu
        self.scrape_menu.add_command(label="Superior Auctions", command=self.scrape_superior_aution)
        self.scrape_menu.add_command(label="Select Mobile Auctions", command=self.scrape_select_auction)
        self.scrape_menu.add_command(label="B-Stock Supply Auctions", command=self.scrape_Bsupply_acution)

        self.export_menu.add_command(label="Export All Auctions", command=write_all_auction_data)
        self.export_menu.add_command(label="Export All Select Auctions", command=write_all_select_auction_data)
        self.export_menu.add_command(label="Export A Grade Auctions", command=write_A_select_auction_data)
        self.export_menu.add_command(label="Export B Grade Auctions", command=write_B_select_auction_data)
        self.export_menu.add_command(label="Export C Grade Auctions", command=write_C_select_auction_data)
        self.export_menu.add_command(label="Export Apple only", command=write_apple_select_auction_data)
        self.export_menu.add_command(label="Export Samsung only", command=write_samsung_select_auction_data)

        self.window.mainloop()

# window = Tk()
# window.title("Language Flash")
# window.config(padx=60, pady=60, bg=BACKGROUND_COLOR)
#
# flip_timer = window.after(3000, func=flip_card)
# front_card_image = PhotoImage(file="./images/card_front.png")
#
# back_card_image = PhotoImage(file="./images/card_back.png")
#
#
# canvas = Canvas(width=800, height=526, highlightthickness=0)
# canvas_image = canvas.create_image(400, 263, image=front_card_image)
# canvas.grid(row=0, column=0, columnspan=2)
# canvas.config(bg=BACKGROUND_COLOR)
# card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
# card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
#
# right_image = PhotoImage(file="images/right.png")
# right_button = Button(image=right_image, highlightthickness=0, command=word_learned)
# right_button.grid(row=1, column=0, pady=10)
#
# wrong_image = PhotoImage(file="images/wrong.png")
# wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_word)
# wrong_button.grid(row=1, column=1, pady=10)
#
#
# if not learned_all:
#     get_word()
# else:
#     print("Your are done!")
#
#
# window.mainloop()


