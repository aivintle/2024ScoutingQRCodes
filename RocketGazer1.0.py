import tkinter as tk
from pandastable import Table, TableModel
import pandas as pd

class SheetViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sheet Viewer")
        self.configure(background = "black")
        self.geometry("500x400")
        self.startVariables()
        self.getDataframes()
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.Statistics()

    def startVariables(self):
	# Instantiate all variables used here
        pass

    def getDataframes(self):
        self.raw_dataframe = 

    def MatchRawData(self):
        self.s1_frame = tk.Frame(self)
        self.s1_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.s1_frame.configure(background = "black")

        self.s1_data = tk.Frame(self)

        self.s1_data = StatisticsPicklist(self.s1_data, self.raw_dataframe)

        self.SheetSwap(self.s1_frame)

    def Statistics(self):
        self.s2_frame = tk.Frame(self)
        self.s2_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.s2_frame.configure(background = "black")

        self.SheetSwap(self.s2_frame)

    def SheetSwap(self, frame):
        self.sheets_frame = tk.Frame(frame)
        self.sheets_frame.grid(row = 0, column = 0, sticky = "new")

        self.s1_swapTo_button = tk.Button(self.sheets_frame, text = "Match Raw Data", command = lambda: self.swapTo_s1(frame))
        self.s2_swapto_button = tk.Button(self.sheets_frame, text = "Statistics", command = lambda: self.swapTo_s2(frame))

        self.s1_swapTo_button.grid(row = 0, column = 0)
        self.s2_swapto_button.grid(row = 0, column = 1)

    def swapTo_s1(self, frame):
        frame.grid_forget()
        print("Swap to s1")
        self.MatchRawData()

    def swapTo_s2(self, frame):
        frame.grid_forget()
        print("Swap to s2")
        self.Statistics()

    def clearFrame(self):
        try:
            self.s1_dataframe.grid_forget()
        except:
            print("Delete fail")
            pass
        try:
            self.s2_data.grid_forget()
        except:
            pass

class StatisticsPicklist(tk.Frame):
    def __init__(self, parent, matchRawData):
        tk.Frame.__init__(self, parent)
        self.configure(background = "white")

def main(): 
    app = SheetViewer()
    app.mainloop()

if __name__ == '__main__':
    main()
