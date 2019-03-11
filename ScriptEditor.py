
from tkinter import *

import os
import subprocess

#MAIN
finestra=Tk()
finestra.title("Execucio d'scrips en el temps")
finestra.minsize(500,300)

f=Frame(finestra)
f.pack()

f1=Frame(finestra)
f2=Frame(finestra)
f3=Frame(finestra)
f4=Frame(finestra)
f5=Frame(finestra)
f6=Frame(finestra)
f7=Frame(finestra)
f8=Frame(finestra)
f08=Frame(finestra)
f9=Frame(finestra)

nom=" "
errsved=0
outsved=0

#BOTO SORTIR
b=Button(finestra,text='Sortir',command=finestra.quit)
b.pack(side=BOTTOM,anchor=W)


#TEXT DE CWD


cwd = os.getcwd()
e = Entry(f1,justify=CENTER)
e.delete(0,END)
e.insert(0,cwd)


#BOTO ESCOLLIR DIRECTORY
def wd():
    x=tkFileDialog.askdirectory()
    e.configure(state='normal')
    e.delete(0,END)
    e.insert(0,x)
    e.configure(state='readonly')


e.configure(state='readonly')
bt=Button(f1,text='Escollir directori de treball',command=wd)
bt.pack(side=LEFT)
e.pack(fill=X)
f1.pack(fill=X,side=TOP,anchor=W)


e2 = Entry(f2)
e2.delete(0,END)

t1=Text(f4)
sb=Scrollbar(f4,orient=VERTICAL,command=t1.yview)
sb.pack(side=RIGHT,fill=Y)
t1['yscrollcommand']=sb.set

t1.pack(fill='both',expand=True)

#OBRIR SCRIPT
def opens():
	global errsves
	global outsves
	global nom 
	errsves=0
	outsves=0
	nom=tkFileDialog.askopenfilename(defaultextension=".sh")
	e2.delete(0,END)
	e2.insert(0,os.path.basename(os.path.normpath(nom)))
	f=open(nom,"r")
	data=f.read()
	t1.delete("0.0",END)
	t1.insert("0.0",data)
	f.close()

#Guardar script
def saves():
	x=t1.get("0.0",END)
	f=open(nom,"w")
	f.write(x)
	f.close()
#Guardar scrip amb nom diferent
def savenews():
	nom=e2.get()
	x=t1.get("0.0",END)
	f=open(nom,"w")
	f.write(x)
	f.close()

b1=Button(f2,text="Obrir Script",command=opens)
b2=Button(f2,text="Guardar l'Script",command=saves)
b3=Button(f3,text="Guardar en un nou script",command=savenews)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
e2.pack(fill=X)


b3.pack()

f2.pack(side=TOP,anchor=W,fill=X)
f3.pack(side=TOP,anchor=W)
f4.pack(side=TOP,anchor=W,fill='both',expand=True)


#LABEL ARGUMENTS ENTRY BOX STDOUT STDERR




l1=Label(f5,text="Arguments d'entrada :")
e3=Entry(f5)

checkOut=0
checkErr=0

def check1():
	global checkOut
	checkOut=(checkOut+1)%2

def check2():
	global checkErr
	checkErr=(checkErr+1)%2
	

cb1 = Checkbutton(f5, text = "Genera stdout", command=check1)
cb2 = Checkbutton(f5, text = "Genera stderr",command=check2)

l1.pack(side=LEFT)
cb2.pack(side=RIGHT)
cb1.pack(side=RIGHT)
e3.pack(fill=X)

f5.pack(anchor=W,side=TOP,fill=X)



#mostrar stdout
def vout():
	x=os.path.basename(os.path.normpath(nom))
	if outsved==1:
		x=x+".out"
		f=open(x,"r")
		data=f.read()
		tkMessageBox.showinfo("Stdout",data)
	else:
		tkMessageBox.showinfo("Error","No s'ha guardat cap sortida per al fitxer "+x+".out")

#mostrar stderr
def verr():
	x=os.path.basename(os.path.normpath(nom))
	if outsved==1:
		x=x+".err"
		f=open(x,"r")
		data=f.read()
		tkMessageBox.showinfo("Stderr",data)
	else:
		tkMessageBox.showinfo("Error","No s'ha guardat cap error per al fitxer "+x+".err")

b3=Button(f6,text="Veure Stdout",command=vout)
b4=Button(f6,text="Veure Stderr",command=verr)

b4.pack(side=RIGHT)
b3.pack(side=RIGHT)

f6.pack(anchor=E,side=TOP)

#Executa immediatament
def run1():
	global checkOut
	global checkErr
	global errsved
	global outsved
	x=os.path.basename(os.path.normpath(nom))
	y="./"+x+" "+e3.get()
	if checkOut==1 or checkErr==1:
		if checkOut==1:
			f1=x+".out"
			y=y+" > "+f1
			outsved=1
		if checkErr==1:
			f2=x+".err"
			y=y+" 2> "+f2
			errsved=1

		os.system(y)
	else:
		
		os.system(y)

l2=Label(f7,text="Executa immediatament")
b5=Button(f7,text="Run",command=run1)
b5.pack(side=RIGHT)
l2.pack(side=RIGHT)

f7.pack(anchor=E,side=TOP)


#Executa amb retard

l03=Label(f08,text="Executa d'aqui a ")
formato1=Entry(f08,width=5)
l04=Label(f08,text=" segons")


def run02():
	global checkOut
	global checkErr
	global errsved
	global outsved
	
	x=os.path.basename(os.path.normpath(nom))
	y="./"+x+" "+e3.get()
	if checkOut==1 or checkErr==1:
		if checkOut==1:
			f1=x+".out"
			y=y+" > "+f1
			outsved=1
		if checkErr==1:
			f2=x+".err"
			y=y+" 2> "+f2
			errsved=1
		
		p="sleep "+formato1.get()+" \n"+y
		os.system("echo '"+p+"' > command.sh")
		z=os.getcwd()+"/command.sh"
		os.system("echo '"+z+"'")
		os.system("chmod 777 command.sh")
		os.system("./command.sh &")	
		#os.system(y)
	else:
		p="sleep "+formato1.get()+" \n"+y
		os.system("echo '"+p+"' > command.sh")
		z=os.getcwd()+"/command.sh"
		os.system("echo '"+z+"'")
		os.system("chmod 777 command.sh ")
		os.system("./command.sh &")	
		#os.system(y)



b06=Button(f08,text="Run",command=run02)

b06.pack(side=RIGHT)
l04.pack(side=RIGHT)
formato1.pack(side=RIGHT)
l03.pack(side=RIGHT)

f08.pack(anchor=E,side=TOP)

#Executa hora i mm

l3=Label(f8,text="Executa un cop amb format ")
formato=Entry(f8,width=15)
l4=Label(f8,text="de 'at'")


def run2():
	global checkOut
	global checkErr
	global errsved
	global outsved

	x=os.path.basename(os.path.normpath(nom))
	y="echo "+""""./"""+x+" "+e3.get()
	t=formato.get()

	if checkOut==1 or checkErr==1:
		if checkOut==1:
			f1=x+".out"
			y=y+" > "+f1
			
		if checkErr==1:
			f2=x+".err"
			y=y+" 2> "+f2
			
		y=y+"""" | at """+t
		os.system(y)
	else:
		y=y+"""" | at """+t
		os.system(y)



b6=Button(f8,text="Run",command=run2)

b6.pack(side=RIGHT)
l4.pack(side=RIGHT)
formato.pack(side=RIGHT)
l3.pack(side=RIGHT)

f8.pack(anchor=E,side=TOP)

#Executa cada dia a mm hh dM Mes dS

l6=Label(f9,text="Programa cada dia a les")
e6=Entry(f9,width=3)
e7=Entry(f9,width=3)
e8=Entry(f9,width=3)
e9=Entry(f9,width=3)
e10=Entry(f9,width=3)
labelo=Label(f9,text=" crontab")

def run3():
	global checkOut
	global checkErr
	global errsved
	global outsved
	os.system("crontab -l > my-crontab")
	x=os.path.basename(os.path.normpath(nom))
	y="/"+x+" "+e3.get()
	t=e6.get()+" "+e7.get()+" "+e8.get()+" "+e9.get()+" "+e10.get()+" "
	os.system('echo '+t)
	if checkOut==1 or checkErr==1:

		if checkOut==1:
			f1=x+".out"
			y=y+" > "+os.getcwd()+"/"+f1
			outsved=1

		if checkErr==1:
			f2=x+".err"
			y=y+" 2> "+os.getcwd()+"/"+f2
			errsved=1

		di=e.get()+y
		job=t+di+"\n"
		os.system('echo "'+job+'" >> my-crontab')
		os.system("crontab my-crontab")
		os.system("rm *-cron*")			#Borrem el fitxer my-crontab 
		
		
	else:
		di=e.get()+y
		job=t+di+"\n"
		os.system('echo "'+job+'" >> my-crontab')
		os.system("crontab my-crontab")
		os.system("rm *-cron*")			#Borrem el fitxer my-crontab 
		
		
		

b7=Button(f9,text="Run",command=run3)

b7.pack(side=RIGHT)
labelo.pack(side=RIGHT)
e10.pack(side=RIGHT)
e9.pack(side=RIGHT)
e8.pack(side=RIGHT)
e7.pack(side=RIGHT)
e6.pack(side=RIGHT)
l6.pack(side=RIGHT)

f9.pack(anchor=E,side=TOP)

f10=Frame(finestra)

l7=Label(f10,text="mm  ")
l8=Label(f10,text="hh  ")
l9=Label(f10,text="dM ")
l10=Label(f10,text="Mes ")
l11=Label(f10,text="dS ")
l12=Label(f10,text="             ")

l12.pack(side=RIGHT)
l11.pack(side=RIGHT)
l10.pack(side=RIGHT)
l9.pack(side=RIGHT)
l8.pack(side=RIGHT)
l7.pack(side=RIGHT)

f10.pack(anchor=E,side=TOP)

finestra.mainloop()
