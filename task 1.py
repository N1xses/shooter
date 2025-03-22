from customtkinter import *

window = CTk()
window.geometry("400x400")

txt = CTkTextbox(window, width=380, height=280)
txt.pack(pady=10)
ent = CTkEntry(window, width=360 )
ent.pack(pady=10)
click = CTkButton(window, text="Клік", width=360)
click.pack()
window.mainloop()