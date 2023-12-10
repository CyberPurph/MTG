import tkinter as tk
from tkinter import messagebox
import json

class Card:
    def __init__(self, name, rarity, WUBRG):
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

    def create_card(self, name, rarity, WUBRG):
        card = Card(name, rarity, WUBRG)
        self.cards.append(card)
        messagebox.showinfo("Success", "Card Added Successfully")

    def display_all_cards(self):
        return self.cards
    
    def search_card(self, key_attribute, non_key_attribute):
        found_cards = [card for card in self.cards if getattr(card, key_attribute, None) == non_key_attribute]
        return found_cards
    
    def update_card(self, name, new_rarity, new_WUBRG):
        for card in self.cards:
            if card.name == name:
                card.rarity = new_rarity
                card.WUBRG = new_WUBRG
                messagebox.showinfo("Success", f"{name} updated successfully" )
                break
    
    def delete_card(self, name):
        self.cards = [card for card in self.cards if card.name != name]
        messagebox.showinfo("Success", f"{name} deleted successfully")

class CardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic the Gathering Card Manager")

        self.card_manager = CardManager()
        
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Card Name: ")
        self.name_entry = tk.Entry(self.root)

        self.rarity_label = tk.Label(self.root, text="Rarity: ")
        self.rarity_entry = tk.Entry(self.root)

        self.WUBRG_label = tk.Label(self.root, text="WUBRG: ")
        self.WUBRG_entry = tk.Entry(self.root)

        self.create_button = tk.Button(self.root, text="Create", command=self.create_card)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_card)
        self.update_button = tk.Button(self.root, text="Update", command=self.update_card)
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_card)
        self.display_all_button = tk.Button(self.root, text="Display All", command=self.display_all_cards)

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
    
    def create_card(self):
        name = self.name_entry.get()
        rarity = self.rarity_entry.get()
        WUBRG = self.WUBRG_entry.get()

        if name and rarity and WUBRG:
            self.card_manager.create_card(name, rarity, WUBRG)
            self.card_manager.save_data()
        else:
            messagebox.showerror("Error", "Please fill in all boxes")

    def search_card(self):
        key_attribute = "name"
        non_key_attribute = self.name_entry.get()

        if non_key_attribute:
            found_cards = self.card_manager.search_card(key_attribute, non_key_attribute)
            self.display_results(found_cards)
        else:
            messagebox.showerror("Error", "Please enter either Rarity or WUBRG")

    def update_card(self):
        name = self.name_entry.get()
        new_rarity = self.rarity_entry.get()
        new_WUBRG = self.WUBRG_entry.get()

        if name and new_rarity and new_WUBRG:
            self.card_manager.update_card(name, new_rarity, new_WUBRG)
            self.card_manager.save_data()
        else:
            messagebox.showerror("Error", "Please enter a card name")

    def delete_card(self):
        name = self.name_entry.get()

        if name:
            self.card_manager.delete_card(name)
            self.card_manager.save_data()
        else:
            messagebox.showerror("Error", "Please enter a card name you want to delete")

    def display_all_cards(self):
        all_cards = self.card_manager.display_all_cards()
        self.display_results(all_cards)

    def display_results(self, cards):
        result_text = ""
        for card in cards:
            result_text += f"Name: {card.name}, Rarity: {card.rarity}, WUBRG: {card.WUBRG}\n"
        messagebox.showinfo("Results", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CardApp(root)
    root.mainloop()