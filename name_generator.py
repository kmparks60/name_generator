import tkinter as tk
import random
import requests

class NameGenerator:
	def __init__(self, main):
		self.main = main
		main.title("Name Generator")

		self.label = tk.Label(main, text="Enter a letter:", font=("Arial", 20))
		self.label.pack()

		self.entry = tk.Entry(main, font=("Arial", 20))
		self.entry.pack()

		self.entry.bind("<Return>", self.generate_name)

		self.generate_button = tk.Button(main, text="Generate", command=self.generate_name, font=("Arial", 20), fg="red")
		self.generate_button.pack()

		self.generate_button = tk.Button(main, text="Randomize \u21BB", command=self.generate_random_name, font=("Arial", 20), fg="purple")
		self.generate_button.pack()

		self.result_label = tk.Label(main, text="", font=("Arial", 20), fg="royal blue")
		self.result_label.pack()

		main.geometry("450x250")

	def generate_name(self, event=None):
		letter= self.entry.get().strip().lower()
		if len(letter) != 1 or not letter.isalpha():
			self.result_label.config(text="Please enter a single letter.")
			return
		
		names = self.generate_names(letter)
		if names:
			self.result_label.config(text=random.choice(names))
		else:
			self.result_label.config(text="No names found for that letter.")

	def generate_random_name(self):
		names = self.generate_names("")
		if names:
			self.result_label.config(text=random.choice(names))
		else:
			self.result_label.config(text="No names found.")

	def generate_names(self, letter):
		names = []
		with open("first_names.txt", "r") as file:
			for name in file:
				if name.strip().lower().startswith(letter):
					names.append(name.strip().capitalize())
		return names
		
root = tk.Tk()
app = NameGenerator(root)
root.mainloop()
