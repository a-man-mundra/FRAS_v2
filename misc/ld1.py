from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from load import LoadingScreen

class LoadingScreen1(Toplevel):
    def __init__(self, parent, next_window_callback):
        Toplevel.__init__(self, parent)
        self.title("Loading FRAS")
        self.geometry("800x600")
        self.configure(background='white')
        self.next_window_callback = next_window_callback
        
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
            self.after(4, self.play_gif)
        else:
            # Stop the animation after one cycle and destroy the loading screen
            self.destroy()
            # Call the callback function to open the next window
            self.next_window_callback()

class MainApplication(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Face Recognition App")
        self.geometry("400x300")

        # Start the loading screen
        self.loading_screen = LoadingScreen1(self, self.open_next_window)
        self.loading_screen.wait_visibility()  # Wait until loading screen is visible
        self.loading_screen.attributes("-topmost", True)  # Set loading screen to topmost

    # def open_next_window(self):
    #     # Open the main window
    #     self.main_window = Toplevel(self)
    #     self.main_window.title("Main Window")
    #     # Add widgets and configure the main window as needed
    #     # Example:
    #     label = Label(self.main_window, text="This is the main window")
    #     label.pack()
    #     # You can continue adding widgets or perform other actions here
    
    def open_next_window(self):
        self.new_window=Toplevel(self)
        self.app=LoadingScreen(self.new_window)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
