#import required modules
from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('600x400')
root.configure(bg='dimgray')
root.resizable(0, 0)

#title of the window
root.title("Message Encrypter and Decrypter")

#label
Label(root, text = 'Message Encrypter and Decrypter', font = 'arial 20 bold', bg = 'dimgray', fg = 'black').pack()
Label(root, text = 'Developed by - \n Kamal Raj, Aditya Kumar, Ashish Ranjan, Gufran Hasan, Md. Shadab Khan, Ritik Raj Kumar', font = 'arial 7 bold', bg = 'dimgray', fg = 'black').pack(side = BOTTOM)

#define variables
Text = StringVar()
private_key = StringVar()
mode = IntVar()
Result = StringVar()


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
    if(mode.get() == 1):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 2):
        Result.set(Decode(private_key.get(), Text.get()))

    with open("riki.txt", "w") as f:
        f.write(f"{Result.get()}")

#function to exit window
def Exit():
    root.destroy()

#function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("None")
    Result.set("")


'''Labels and Buttons'''

#message
Label(root, font = 'arial 12 bold', text = 'Enter Your Text :', bg = 'dimgray', fg = 'black').place(x = 50, y = 60)
Entry(root, font = 'arial 12 ', textvariable = Text, width= '38', bg = 'dimgray', fg = 'black').place(x = 200, y = 60)

#key
Label(root, font = 'arial 12 bold', text = 'Enter Key :', bg = 'dimgray', fg = 'black').place(x = 50, y = 100)
Entry(root, font = 'arial 12', textvariable = private_key , width= '38', bg = 'dimgray', fg = 'black').place(x = 200, y = 100)


#mode
Label(root, font = 'arial 12 bold', text = 'Select Mode :', bg = 'dimgray', fg = 'black').place(x = 50, y = 140)
Radiobutton(root, font = 'arial 10 bold',text="Encrypt",bg = 'dimgray', variable=mode, value=1).place(x = 200, y = 140)
Radiobutton(root, font = 'arial 10 bold',text="Decrypt",bg = 'dimgray', variable=mode, value=2).place(x = 320, y = 140)


#result button
Button(root, font = 'arial 10 bold', text = 'View Result', padx = 2, bg = 'Cyan', command = Mode).place(x = 250, y = 185)

#result label
Label(root, font = 'arial 12 bold', text = 'Encrypted/Decrypted Text:', bg = 'dimgray', fg = 'black').place(x = 200, y = 230)
Entry(root, font = 'arial 12', textvariable = Result, width= '55', bg = 'dimgray', fg = 'black').place(x = 50, y = 260)

#reset button
Button(root, font = 'arial 10 bold', text = 'Reset', width = 6, command = Reset, bg = 'Green', padx=2).place(x = 120, y = 305)

#exit button
Button(root, font = 'arial 10 bold', text= 'Exit' , width = 6, command = Exit, bg = 'Red', padx = 2, pady = 2).place(x = 400, y = 305)

root.mainloop()
