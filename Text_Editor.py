from Tkinter import *
import tkFileDialog
import Tkinter as tk
root=Tk()
global c
global dat
global data
c=0
def appear(data):
	l=0
	dat = ""
	for i in data:
		b = len(i)
		x = "%-68s"%i[:b-1]+ "|%d:%d|\n"%(l, l+len(i)-2)
		dat+=x
		if (l<= c <=l+len(i)-2):
			for j in range(c-l):
				dat+=" "
			dat+="^\n"
		l += len(i)-1
	text.insert("1.0", dat)



def saveas():
	x =""
	for i in data :
		x+=i

	savelocation = tkFileDialog.asksaveasfilename()
	try:
		file1=open(savelocation, "w+")
	except:
		return
	file1.write(x)
	file1.close()
button=Button(root,text="Save",command=saveas)
button.grid()
def openfilename():
	global text
	openlocation = tkFileDialog.askopenfilename()
	try:
		f=open(openlocation,"rw")
	except:
		return
	global data
	data=f.readlines()
	print data
	appear(data)
def callback():
	global c
	c =  int(e.get())
	appear(data)




text=Text(root)
text.grid()



def quit():
	root.destroy()

def erase():
	l=0
	daat = ""
	global data
	for i in data:
		b = len(i)
		if (l<= c <=l+len(i)-2):
			x = "%s\n"%(i[:c-l]+i[c-l+1:b-1])
		else:
			x = "%s\n"%i[:b-1]
		daat+=x
		l += b-1
	data=daat.split('\n')
	print data
	y=[]
	for i in data:
		
		y.append(i+'\n')
	data  =y
	print data
	appear(data)



def insert():
	z = e1.get()
	l=0
	daat = ""
	global data
	for i in data:
		b = len(i)
		if (l<= c <=l+len(i)-2):
			x = "%s\n"%(i[:c-l+1]+z+i[c-l+1:b-1])
		else:
			x = "%s\n"%i[:b-1]
		daat+=x
		l += b-1
	data=daat.split('\n')
	print data
	y=[]
	for i in data:
		
		y.append(i+'\n')
	data  =y
	print data
	appear(data)

e1 = Entry()
e1.grid(row=7,column=1)
ins = Button( text="Insert", width=70, command=insert)
ins.grid(row=7)
e = Entry()
e.grid(row=5,column=1)
b = Button( text="move", width=70, command=callback)
b.grid(row=5)
instruktionBtn = Button(root, text='open file', command=openfilename)
instruktionBtn.grid()
er= Button(root, text='Erase', command=erase)
er.grid()

n = Button(root, text='Quit', command=quit)
n.grid()
root.mainloop()

