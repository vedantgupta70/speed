from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title(" Internet Speed ")
sp.geometry("500x500")
sp.config(bg="Black")

lab = Label(sp,text="Internet Speed Testing",font=("Time New Roman",20,"bold","italic"))
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Time New Roman",20,"bold","italic"))
lab.place(x=60,y=130,height=50,width=380)


lab_down = Label(sp,text="00",font=("Time New Roman",20,"bold","italic"))
lab_down.place(x=60,y=200,height=50,width=380)


lab = Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold","italic"))
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time New Roman",20,"bold","italic"))
lab_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Time New Roman",20,"bold","italic"),relief=RAISED,bg="Red",fg="White",command=speedCheck)
button.place(x=60,y=460,height=50,width=380)




sp.mainloop()
