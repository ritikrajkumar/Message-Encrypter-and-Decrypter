#import required modules
import base64
from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfile

#initialize window
root = Tk()
root.geometry('600x400')
root.configure(bg = 'dimgray')
root.resizable(0, 0)

#title of the window
root.title("Message Encrypter and Decrypter")

#window labels
Label(root, text = 'Message Encrypter and Decrypter', font = 'arial 20 bold', bg = 'dimgray', fg = 'ghostwhite').pack()
Label(root, text = 'Developed by - Ritik Raj Kumar', font = 'arial 8 bold', bg = 'dimgray', fg = 'ghostwhite').pack(side = BOTTOM)

#define variables
Text = StringVar()
private_key = StringVar()
mode = IntVar()
Result = StringVar()
textfile = StringVar()


'''Define Functions'''

#function to encode
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    while True:
        if Text.get() == "":
            mb.showwarning('Warning', 'Enter Your Text!')
            break

        elif private_key.get() == "":
            mb.showwarning('Error', 'Enter Password')
            break
            
        if mode.get() == 0: 
            mb.showwarning('Error!', 'Select Mode')
            break

        elif mode.get() == 1:
            Result.set(Encode(private_key.get(), Text.get()))
            mb.showinfo('Success', 'Encryption Successful!')
            break

        elif mode.get() == 2:
            Result.set(Decode(private_key.get(), Text.get()))
            mb.showinfo('Success', 'Decryption Successful!')
            break


#function to exit window
def Exit():
    root.destroy()

#function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("0")
    Result.set("")
    textfile.set("")

#function to load a text file file
def choosefile():

    #shows an "Open" dialog box and return the path to the selected file
    file1 = askopenfilename(title = "Select a text file", filetypes = (("text files", "*.txt"),)) 
    file1 = open(file1)
    data = file1.read()
    Text.set(data)

#function to save the result in .txt format
def savefile():
    while True:
        if Result.get() == "":
            mb.showinfo('Warning!', 'First Encrypt or Decrypt Text1')
            break
        tf = asksaveasfile(
            mode = 'w', title = "Save Result", defaultextension = ".txt")
        tf.write(f"{Result.get()}")
        break
   
'''Labels and Buttons'''

#message
Label(root, font = 'arial 12 bold', text = 'Enter Your Text :', bg = 'dimgray', fg = 'ghostwhite').place(x = 50, y = 60)
file3 = Entry(root, font = 'arial 12 ', textvariable = Text, width= '38', bg = 'dimgray', fg = 'ghostwhite').place(x = 200, y = 60)

#key/password
Label(root, font = 'arial 12 bold', text = 'Enter Password :', bg = 'dimgray', fg = 'ghostwhite').place(x = 50, y = 100)
Entry(root, font = 'arial 12', textvariable = private_key , width= '38', bg = 'dimgray', fg = 'ghostwhite').place(x = 200, y = 100)


#mode
Label(root, font = 'arial 12 bold', text = 'Select Mode :', bg = 'dimgray', fg = 'ghostwhite').place(x = 50, y = 140)
Radiobutton(root, font = 'arial 10 bold', text = "Encrypt", bg = 'dimgray', variable = mode, value = 1).place(x = 200, y = 140)
Radiobutton(root, font = 'arial 10 bold', text = "Decrypt", bg = 'dimgray', variable = mode, value = 2).place(x = 300, y = 140)


#result button
Button(root, font = 'arial 10 bold', text = 'View Result', padx = 2, bg = 'Cyan', command = Mode).place(x = 255, y = 180)

#save file button
Button(root, font = 'arial 10 bold', text = 'Save Result', padx = 2, bg = 'ghostwhite', command = savefile).place(x = 110, y = 220)

#choose file button
Button(root, font = 'arial 10 bold', text = 'Select File', padx = 2, bg = 'ghostwhite', command = choosefile).place(x = 400, y = 220)

#Encrypted/Decrypted Text
Label(root, font = 'arial 12 bold', text = 'Encrypted/Decrypted Text :', bg = 'dimgray', fg = 'ghostwhite').place(x = 200, y = 260)
Entry(root, font = 'arial 12', textvariable = Result, width= '55', bg = 'dimgray', fg = 'ghostwhite').place(x = 50, y = 290)

#reset button
Button(root, font = 'arial 10 bold', text = 'Reset', width = 6, command = Reset, bg = 'Green', padx=2).place(x = 120, y = 340)

#exit button
Button(root, font = 'arial 10 bold', text= 'Exit' , width = 6, command = Exit, bg = 'Red', padx = 2, pady = 2).place(x = 410, y = 340)

#main
root.mainloop()