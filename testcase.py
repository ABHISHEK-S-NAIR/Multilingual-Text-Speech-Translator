from tkinter import *                          # * imports everything from the module tkinter
from tkinter import ttk,messagebox             # ttk is a module that is used to style the tkinter widgets.
                                               # messagebox module is used to display the message boxes in the python applications
import googletrans  # Googletrans is a python library that implementS Google Translate API.(installed externally)
import textblob                                #library used for processing text data.(installed externally)
                                               #(spelling correction, part of speech tagging, and text classification)
root=Tk()                                      #creates root window(main drawing board on which the things are being done)
root.title('Google Translator')                #provides title to the root window
root.geometry('1080x400')                      #provides geometory the root window i.e length=1080 and breadth=400

def label_change():
    #get() : Returns the entry’s current text as a string.
    c=combo1.get()  #gets the current value from combo1 
    c1=combo2.get()
    #configure():to access an object's attributes after its initialisation.
    label1.configure(text=c)   #label1 is configured to display the current text of c1 
    label2.configure(text=c1)   #label2 is configured to display the current text of c2
    root.after(1000,label_change) #labelchange is executed 1000ms after the labelchange is called



def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror('googletrans','Please Try Again!!!')








#google translate icon on left most
image_icon=PhotoImage(file="C:\\Users\\aayan\\OneDrive\\Desktop\\PESU_SEM_1\\CSProject\\download.png")   #image_icon object created 
root.iconphoto(False,image_icon)               #sets image as the icon of titlebar

#arrow image in between
arrow_image=PhotoImage(file="C:\\Users\\aayan\\OneDrive\\Desktop\\PESU_SEM_1\\CSProject\\arrow4.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)







language=googletrans.LANGUAGES                           #dictionary containing all the languages in googletrans pointing to variable language
languageV=list(language.values())                        #variable languageV  created containing list of all the values taken from language
lang1=language.keys()                                    #variable lang1 created containing list of all the keys taken from language


#creating left language selection widget(combo1)
#Combobox is a combination of Listbox and an entry field.
#It is one of the Tkinter widgets where it contains a down arrow to select from a list of options
combo1=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo1.place(x=110,y=20)
combo1.set('ENGLISH')

#creating normal display widget label1 below combo1,widget=label1
#Label is a widget that is used to implement display boxes where you can place text or images.
label1=Label(root,text='ENGLISH',font='segoe 30 bold',bg='white',width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

#creates a frame widget below label1,widget=f1
#Frame widget is used to organize the group of widgets. It acts like a container which can be used to hold the other widgets.
f1=Frame(root,bg='Black',bd=5)
f1.place(x=10,y=118,width=440,height=210)

#creating text widget overlapping frame widget,widget=text1
#Text Widget is used where a user wants to insert multiline text fields.
text1=Text(f1,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

#creating scrollbar and intergrating it with text widget overlapped upon fram widget,widget=scrollbar1
#scrollbar widget is used to scroll down the content
scrollbar1=Scrollbar(f1)                       
scrollbar1.pack(side='right',fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)











#creating right language selection widget(combo2)
#Combobox is a combination of Listbox and an entry field.
#It is one of the Tkinter widgets where it contains a down arrow to select from a list of options
combo2=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo2.place(x=730,y=20)
combo2.set('SELECT LANGUAGE')

#creating normal display widget label2 below combo2,widget=label2
#Label is a widget that is used to implement display boxes where you can place text or images.
label2=Label(root,text='SELECT LANGUAGE',font='segoe 30 bold',bg='white',width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

#creates a frame widget below label1,widget=f2
#Frame widget is used to organize the group of widgets. It acts like a container which can be used to hold the other widgets.
f2=Frame(root,bg='Black',bd=5)
f2.place(x=620,y=118,width=440,height=210)

#creating text widget overlapping frame widget,widget=text2
#Text Widget is used where a user wants to insert multiline text fields.
text2=Text(f2,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

#creating scrollbar and intergrating it with text widget overlapped upon fram widget,widget=scrollbar2
#scrollbar widget is used to scroll down the content
scrollbar2=Scrollbar(f2)                       
scrollbar2.pack(side='right',fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)












#Translate Button Creation
#command option associates the button’s action with a function or a method of a class.
#When you click or press the button, it’ll automatically invoke a callback function
translate=Button(root,text='Translate',font='Roboto 15 bold italic',
                 activebackground='purple',cursor='hand2',bd=5,
                 bg='red',fg='white',command=translate_now)
translate.place(x=480,y=250)









label_change()

root.configure(bg='white')                     #provides background colour i.e. white in this case
root.mainloop()                                #mainloop method is what keeps the root window visiblele until you press the close button 






'''
Error in Python can be of two types i.e. Syntax errors and Exceptions.
Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program.

    Some of the common Exception Errors are :
        IOError: if the file can’t be opened
        KeyboardInterrupt: when an unrequired key is pressed by the user
        ValueError: when the built-in function receives a wrong argument
        EOFError: if End-Of-File is hit without reading any data
        ImportError: if it is unable to find the module
    
        
    Try Except in Python:
        Try and Except statement is used to handle these errors within our code in Python.
        The try block is used to check some code for errors i.e the code inside the try block will execute when there is no error in the program.
        Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

    Syntax: 
        try:
            # Some Code
        except:
            # Executed if error in the
            # try block
    
    How try() works?
        #First, the try clause is executed i.e. the code between try.
        #If there is no exception, then only the try clause will run, except clause is finished.
        #If any exception occurs, the try clause will be skipped and except clause will run.
        #If any exception occurs, but the except clause within the code doesn’t handle it,
         it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
        #A try statement can have more than one except clause
'''

#Code 1: No exception, so the try clause will run. 
'''
# Python code to illustrate
# working of try() 

def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)

#Output:
#Yeah ! Your answer is : 1
'''
#Code 2: There is an exception so only except clause will run. 
'''
# Python code to illustrate
# working of try() 
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)

#Output:
#Sorry ! You are dividing by zero
'''



 
