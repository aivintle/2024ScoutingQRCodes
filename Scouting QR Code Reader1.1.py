import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from pyzbar.pyzbar import decode

class QRCodeReaderApp:
    def __init__(self, cameraStream):
        self.toggleImage = True
        self.window = tk.Tk()
        self.window.title("QR Code Reader App")

        # Create four subself.frames
        self.top_left_frame = tk.Frame(self.window)
        self.top_right_frame = tk.Frame(self.window)
        self.bottom_left_frame = tk.Frame(self.window)
        self.bottom_right_frame = tk.Frame(self.window)

        # Arrange the self.frames
        self.top_left_frame.grid(row=0, column=0)
        self.top_right_frame.grid(row=0, column=1)
        self.bottom_left_frame.grid(row=1, column=0)
        self.bottom_right_frame.grid(row=1, column=1)

        # Add a label above the video stream
        self.stream_label = tk.Label(self.top_left_frame, text="Camera Stream")
        self.stream_label.pack()

        # Add a label in the bottom right self.frame for QR code text
        self.qr_text_label = tk.Label(self.bottom_right_frame, text="")
        self.qr_text_label.pack()

        # Add Accept and Reject buttons in the top right self.frame
        self.accept_button = tk.Button(self.top_right_frame, text="Accept", command=self.accept)
        self.reject_button = tk.Button(self.top_right_frame, text="Reject", command=self.reject)

        # Initially hide the buttons
        self.accept_button.pack_forget()
        self.reject_button.pack_forget()

        # Add a menu with options to exit the program and change the camera stream
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quitProgram)
        self.file_menu.add_command(label="Change Camera Stream", command=self.change_stream)

        # Initialize the camera stream (0 is usually the built-in webcam)
        self.cap = cv2.VideoCapture(cameraStream)

        self.update_frame()

        # Start the app
        self.window.mainloop()

    def change_stream(self):
        # This function should contain the logic to change the camera stream
        pass

    def accept(self):
        # This function should contain the logic when the Accept button is pressed
        self.toggleImage = True
        self.file = open('ScoutingAppOutput.txt', 'a')
        self.file.write("\n" + self.qrCode)
        self.file.close()
        print(self.qrCode)

    def reject(self):
        # This function should contain the logic when the Reject button is pressed
        self.toggleImage = True

    def update_frame(self):
        try:
            # Capture self.frame-by-self.frame
            if(self.toggleImage):
                self.ret, self.frame = self.cap.read()

            # Convert the image from OpenCV BGR format to PIL Image format
            cv_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)

            # When a QR code is detected by the camera, draw a region of interest around the QR code on the image and read the QR code
            codes = decode(pil_image)
            for code in codes:
                x, y, w, h = code.rect
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                self.data = code.data.decode().replace(";", "\t")
                # NOTE: Decode don't decode to u-128 as that will crash is a single quote is in the comment
                self.qr_text_label.config(text=self.data)
                self.qrCode = self.data
                self.accept_button.pack()
                self.reject_button.pack()
                self.toggleImage = False

            # Convert PIL Image to Tkinter PhotoImage and show it in a label
            tk_image = ImageTk.PhotoImage(image=pil_image)
            self.stream_label.config(image=tk_image)
            self.stream_label.image = tk_image

            # Call this function again after 10 milliseconds to continuously update the self.frame
            self.window.after(10, self.update_frame)
        except:
            print("Something bad happended, I'm not sure what but let's ignore it.")

    def quitProgram(self):
        quit()

## Start at zero, go to 1, 2, etc. until code works.
cameraStream = 1
app = QRCodeReaderApp(cameraStream)
