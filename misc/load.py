import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class LoadingScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Loading...")
        self.geometry("800x600")
        self.configure(background='white')
        
        # Load and display the GIF
        self.gif_path = "loading.gif"
        if os.path.exists(self.gif_path):
            self.gif = Image.open(self.gif_path)
            self.gif_frames = []
            try:
                while True:
                    self.gif_frames.append(self.gif.copy())
                    self.gif.seek(len(self.gif_frames))  # Go to next frame
            except EOFError:
                pass

            # Display the first frame
            self.current_frame = 0
            self.gif_label = ttk.Label(self, image=None)
            self.gif_label.pack()

            # Center the window on the screen
            self.update_idletasks()
            width = self.winfo_width()
            height = self.winfo_height()
            x = (self.winfo_screenwidth() // 2) - (width // 2)
            y = (self.winfo_screenheight() // 2) - (height // 2)
            self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            # Play the GIF
            self.play_gif()

    def play_gif(self):
        if self.current_frame < len(self.gif_frames):
            frame = self.gif_frames[self.current_frame]
            self.current_frame += 1
            gif_image = ImageTk.PhotoImage(frame)
            self.gif_label.config(image=gif_image)
            self.gif_label.image = gif_image
            self.after(2, self.play_gif)
        else:
            # Stop the animation after one cycle and destroy the loading screen
            self.destroy()
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Face Recognition App")
        self.geometry("400x300")

        # Add a button to start the face recognition process
        self.start_button = ttk.Button(self, text="Start Recognition", command=self.start_recognition)
        self.start_button.pack(pady=50)

    def start_recognition(self):
        # Display the loading screen
        loading_screen = LoadingScreen(self)
        self.wait_window(loading_screen)

        # Simulate some time-consuming task (e.g., face recognition process)
        import time
        time.sleep(1)

        # After the task is done, destroy the loading screen
        loading_screen.destroy()

        # You can continue with your face recognition process here

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
