import tkinter as tk
from tkinter import messagebox

class InformationManagementExpertSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Information Management Expert System")
        
        self.facts = {}
        
        self.label = tk.Label(master, text="Welcome to the Information Management Expert System", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.add_fact_label = tk.Label(master, text="Add Information:")
        self.add_fact_label.pack()
        
        self.fact_entry = tk.Entry(master, width=40)
        self.fact_entry.pack()

        self.category_label = tk.Label(master, text="Add Category:")
        self.category_label.pack()
        
        self.category_entry = tk.Entry(master, width=40)
        self.category_entry.pack()

        self.add_button = tk.Button(master, text="Add Information", command=self.add_fact)
        self.add_button.pack()
        
        self.retrieve_label = tk.Label(master, text="Retrieve Data:")
        self.retrieve_label.pack()
        
        self.category_retrieve_entry = tk.Entry(master, width=40)
        self.category_retrieve_entry.pack()
        
        self.retrieve_button = tk.Button(master, text="Retrieve Data", command=self.retrieve_data)
        self.retrieve_button.pack()

        self.delete_fact_label = tk.Label(master, text="Delete an Information:")
        self.delete_fact_label.pack()

        self.fact_to_delete_entry = tk.Entry(master, width=40)
        self.fact_to_delete_entry.pack()

        self.delete_button = tk.Button(master, text="Delete Information", command=self.delete_fact)
        self.delete_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_program)
        self.exit_button.pack()
    
    def add_fact(self):
        fact = self.fact_entry.get()
        category = self.category_entry.get()
        
        if category not in self.facts:
            self.facts[category] = []
        
        self.facts[category].append(fact)
        messagebox.showinfo("Success", "Information added successfully!")
        
        self.fact_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
    
    def retrieve_data(self):
        category = self.category_retrieve_entry.get()
        
        if category in self.facts:
            data = "\n".join(self.facts[category])
            messagebox.showinfo("Data for category '{}'".format(category), data)
        else:
            messagebox.showinfo("Error", "No data found for this category.")
        
        self.category_retrieve_entry.delete(0, tk.END)

    def delete_fact(self):
        fact_to_delete = self.fact_to_delete_entry.get()

        found = False
        for category, facts in self.facts.items():
            if fact_to_delete in facts:
                facts.remove(fact_to_delete)
                found = True
                break
        
        if found:
            messagebox.showinfo("Success", "Fact deleted successfully!")
        else:
            messagebox.showerror("Error", "Fact not found!")

        self.fact_to_delete_entry.delete(0, tk.END)    

    def exit_program(self):
        self.master.destroy()    

def main():
    root = tk.Tk()
    app = InformationManagementExpertSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

