import tkinter as tk
from tkinter import messagebox
import json

class Card:
    def __init__(self, name, rarity, WUBRG)
        self.name = name
        self.rarity = rarity
        self.WUBRG = WUBRG

class CardManager:
    def __init__(self):
        self.cards = []
        self.load_data()

    def load_data(self):
        try:
            with open("cards_data.json", "r") as file:
                data = json.load(file)
                self.cards = [Card(**card_data) for card_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            pass

    def save_data(self):
        with open("cards_data,json", "w") as file:
            data = [{"name": card.name, "rarity": card.rarity, "WUBRG": card.WUBRG} for card in self.cards]
            json.dump(data, file, indent=2)

class CardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic the Gathering Card Manager")

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Card Name: ")
        self.name_entry = tk.Entry(self.root)

        self.rarity_label = tk.Label(self.root, text="Rarity: ")
        self.rarity_entry = tk.Entry(self.root)

        self.WUBRG_label = tk.Label(self.root, text="WUBRG: ")
        self.WUBRG_entry = tk.Entry(self.root)

        self.create_button = tk.Button(self.root, text="Create")
        self.search_button = tk.Button(self.root, text="Search")
        self.update_button = tk.Button(self.root, text="Update")
        self.delete_button = tk.Button(self.root, text="Delete")
        self.display_all_button = tk.Button(self.root, text="Display All")

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        self.rarity_label.grid(row=1, column=0)
        self.rarity_entry.grid(row=1, column=1)

        self.WUBRG_label.grid(row=2, column=0)
        self.WUBRG_entry.grid(row=2, column=1)

        self.create_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.display_all_button.grid(row=7, column=0, columnspan=2, pady=10)
    