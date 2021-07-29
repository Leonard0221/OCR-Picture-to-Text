from PIL import Image
import pytesseract as pt
import tkinter as tk
import tkinter.filedialog as filedialog

class GUI(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Pic To Words")

        self.img_path = tk.StringVar()

        self.frame = tk.Frame(self)
        self.frame.pack(padx=10, pady=10)

        self.lbl_file = tk.Label(self.frame, text="Picture")
        self.lbl_file.grid(row=0, column=0)
        
        self.txt_file = tk.Entry(self.frame, width=50, textvariable=self.img_path)
        self.txt_file.grid(row=0, column=1, sticky=tk.W)
        
        self.btn_file = tk.Button(self.frame, text="Choose", command=self.sel_img_file)
        self.btn_file.grid(row=0, column=1, sticky=tk.E)
        
        self.lbl_txt = tk.Label(self.frame, text="Text")
        self.lbl_txt.grid(row=1, column=0)
        
        self.txt_exract = tk.Text(self.frame)
        self.txt_exract.grid(row=1, column=1)
        
        self.btn_extract = tk.Button(self.frame, text="Import Text", command=self.extract_text)
        self.btn_extract.grid(row=2, column=1, sticky=tk.W+tk.E)
    def sel_img_file(self):
        self.img_path.set(filedialog.askopenfilename(title="Import Image", initialdir="."))
    def extract_text(self):
        if self.img_path:
            img = Image.open(self.img_path.get())
            text = pt.image_to_string(img)
            self.txt_exract.delete(1.0, tk.END)
            self.txt_exract.insert(tk.END, text)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
