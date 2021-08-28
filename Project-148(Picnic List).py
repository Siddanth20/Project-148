from tkinter import*
import random

root=Tk()
root.title("Picnic Bag")
root.geometry("400x400")

display_items_label=Label(root)
display_random_item_label=Label(root)

Listed_items= ['Extra Clothes','Water Bottle','Snacks','Book','Pencil','First Aid Box']


def List():
   random_number = random.randint(0,5)
   display_items_label["text"]="Picnic List : "+str(Listed_items)
   display_random_item_label["text"]="Put Item no"+str(random_number)
   
btn=Button(root,text="Picnic List",command=List)
   
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

display_items_label.place(relx=0.5,rely=0.4,anchor=CENTER)
display_random_item_label.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()