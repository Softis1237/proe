
import tkinter as tk
from tkinter import messagebox

class AppGUI:
    def __init__(self, root, profile_manager):
        self.root = root
        self.profile_manager = profile_manager
        self.root.title("App")

        self.label = tk.Label(root, text="Profile Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.button = tk.Button(root, text="Create Profile", command=self.create_profile)
        self.button.pack()

    def create_profile(self):
        name = self.entry.get()
        if name:
            profile = self.profile_manager.create_profile(name)
            messagebox.showinfo("Success", f"Created profile {profile['name']}")
        else:
            messagebox.showerror("Error", "Profile name cannot be empty.")

if __name__ == "__main__":
    from profile_manager import ProfileManager
    root = tk.Tk()
    manager = ProfileManager()
    gui = AppGUI(root, manager)
    root.mainloop()
