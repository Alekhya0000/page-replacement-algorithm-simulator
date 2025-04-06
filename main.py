# main.py

import tkinter as tk
from tkinter import messagebox
from fifo import fifo_algorithm
from lru import lru_algorithm
from optimal import optimal_algorithm

class PageReplacementSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulator")
        self.root.geometry("700x600")
        self.root.configure(bg="#1a1a1a")
        
        # Title
        self.title_label = tk.Label(root, text="Page Replacement Simulator", 
                                  font=("Arial", 20, "bold"), fg="#00ff00", bg="#1a1a1a")
        self.title_label.pack(pady=10)
        
        # Frame Size Input
        self.frame_label = tk.Label(root, text="Enter Number of Frames (2-5):", 
                                  font=("Arial", 12), fg="#ffffff", bg="#1a1a1a")
        self.frame_label.pack(pady=5)
        self.frame_entry = tk.Entry(root, font=("Arial", 12), width=10, bg="#333333", fg="#ffffff")
        self.frame_entry.pack()
        
        # Page Reference Input
        self.page_label = tk.Label(root, text="Enter Page References (comma separated):", 
                                 font=("Arial", 12), fg="#ffffff", bg="#1a1a1a")
        self.page_label.pack(pady=5)
        self.page_entry = tk.Entry(root, font=("Arial", 12), width=30, bg="#333333", fg="#ffffff")
        self.page_entry.pack()
        
        # Algorithm Selection
        self.algo_label = tk.Label(root, text="Select Algorithm:", 
                                 font=("Arial", 12), fg="#ffffff", bg="#1a1a1a")
        self.algo_label.pack(pady=5)
        self.algo_var = tk.StringVar(value="FIFO")
        self.algo_menu = tk.OptionMenu(root, self.algo_var, "FIFO", "LRU", "Optimal")
        self.algo_menu.config(font=("Arial", 12), bg="#333333", fg="#ffffff")
        self.algo_menu.pack()
        
        # Buttons
        self.simulate_btn = tk.Button(root, text="Simulate", command=self.simulate,
                                    font=("Arial", 12, "bold"), bg="#ff4444", fg="#ffffff")
        self.simulate_btn.pack(pady=10)
        
        self.clear_btn = tk.Button(root, text="Clear", command=self.clear_fields,
                                 font=("Arial", 12, "bold"), bg="#4444ff", fg="#ffffff")
        self.clear_btn.pack(pady=5)
        
        # Result Display
        self.result_text = tk.Text(root, height=20, width=80, font=("Arial", 10), 
                                 bg="#333333", fg="#00ff00")
        self.result_text.pack(pady=10)
        
    def simulate(self):
        try:
            frames = int(self.frame_entry.get())
            if frames < 2 or frames > 5:
                messagebox.showerror("Error", "Frames must be between 2 and 5!")
                return
            
            page_string = self.page_entry.get()
            pages = [int(p.strip()) for p in page_string.split(",")]
            if not pages:
                messagebox.showerror("Error", "Please enter page references!")
                return
                
            self.result_text.delete(1.0, tk.END)
            algo = self.algo_var.get()
            
            if algo == "FIFO":
                output, page_faults = fifo_algorithm(frames, pages)
            elif algo == "LRU":
                output, page_faults = lru_algorithm(frames, pages)
            elif algo == "Optimal":
                output, page_faults = optimal_algorithm(frames, pages)
                
            self.display_results(algo, output, page_faults, len(pages))
                
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Use numbers for frames and comma-separated numbers for pages.")
    
    def display_results(self, algo, output, page_faults, total_pages):
        self.result_text.insert(tk.END, f"{algo} Algorithm Simulation:\n")
        self.result_text.insert(tk.END, "-" * 60 + "\n")
        for line in output:
            self.result_text.insert(tk.END, line + "\n")
        self.result_text.insert(tk.END, "-" * 60 + "\n")
        self.result_text.insert(tk.END, f"Total Page Faults: {page_faults}\n")
        self.result_text.insert(tk.END, f"Page Fault Rate: {page_faults/total_pages*100:.2f}%\n")
        
        if page_faults < total_pages // 2:
            self.result_text.insert(tk.END, "Nice one! Low faults! 🚀\n")
        else:
            self.result_text.insert(tk.END, "Ouch! High faults this time! 😬\n")
    
    def clear_fields(self):
        self.frame_entry.delete(0, tk.END)
        self.page_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.algo_var.set("FIFO")

def main():
    root = tk.Tk()
    app = PageReplacementSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
