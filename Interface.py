from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from run_encryption import *
import os
import time

root = tk.Tk()
root.title("Gavrik OSIS BSUIR 2021")
root.geometry("600x600")
root.config(background="#263D42")
root.resizable(0, 0)
apps = []
key = ''

filetypes = (("all files", "*.*"), ("executables", "*.exe"), ("picture", "*.png"), ("picture", "*.jpg")
             , ("text", "*.txt"), ("doc", "*.docx"), ("pdf", "*.pdf")
             , ("text_rtf", "*.rtf"), ("code_files", "*.py"))


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    answer = messagebox.askyesno(title="Question", message="Do you want to encrypt the partition?")
    if answer:
        filename = filedialog.askdirectory(title="Select file")
        apps.clear()
        apps.append(filename)
    else:
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=filetypes)
        apps.clear()
        apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
    print(apps[0])


def run_apps():
    answer = messagebox.askyesno(title="ATTENTION",
                                 message="If the file is not encrypted, you can lose access to it forever.Do you want "
                                         "to continue?")
    if answer:
        if is_error("Disk path not specified", apps):
            return
        else:
            if is_error("operation cannot be performed. (key is empty)", enter_key.get()):
                return
            else:
                #decrypt_disk(apps[0], enter_key.get())
                #time.sleep(30)
                #print("here 1")
                os.startfile(apps[0])
                #time.sleep(50)
                #print("here 2")
                #encrypt_disk(apps[0], enter_key.get())
    else:
        return




def encode_disk():
    if is_error("Disk path not specified", apps):
        return
    else:
        generated_key_label['fg'] = "red"
        generated_key_label['text'] = "Remember key: "
        key = generate_random_string(2)
        generated_key_label['text'] += key
        print(key)
        print(apps[0])
        encrypt_disk(apps[0], key)


def decode_disk():
    answer = messagebox.askyesno(title="ATTENTION",
                                 message="If the file is not encrypted, you can lose access to it forever.Do you want "
                                         "to continue?")
    if answer:
        if is_error("operation cannot be performed. (key is empty)", enter_key.get()):
            return
        else:
            if is_error("Disk path not specified", apps):
                return
            else:
                answer = messagebox.askyesno(title="Question", message="ATTENTION! Make sure you entered the correct "
                                                                       "password, continue?")
                if answer:
                    print(enter_key.get())
                    print(apps[0])
                    decrypt_disk(apps[0], enter_key.get())
                else:
                    return
    else:
        return


def is_error(error_description, check_argument):
    if not check_argument:
        messagebox.showerror("Error", error_description)
        return True
    else:
        return False


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.03)

generated_key_label = Label(root, text="Generated key: ", width=82, height=2, bg="white")
generated_key_label.place(x=10, y=450)

enter_key = Entry(root)
enter_key.place(x=10, y=495, height=35, width=580)

openFile = tk.Button(root, text="Open File", height=2, width="15", fg="white", activebackground="white", bg="#263D42",
                     command=addApp)
openFile.place(x=10, y=540)

runApps = tk.Button(root, text="Run Apps", fg="white", height=2, width="15", activebackground="white", bg="#263D42",
                    command=run_apps)
runApps.place(x=170, y=540)

decodeDisk = tk.Button(root, text="Decode disk", height=2, width="15", activebackground="white", fg="white",
                       bg="#263D42", command=decode_disk)
decodeDisk.place(x=320, y=540)

decodeDisk = tk.Button(root, text="Encode disk", height=2, width="15", activebackground="white", fg="white",
                       bg="#263D42", command=encode_disk)
decodeDisk.place(x=475, y=540)

root.mainloop()

#GCXxiwlJeSHgkoyi
