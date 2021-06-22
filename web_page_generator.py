import webbrowser
from tkinter import *

#________________________________________________________CREATE GUI__________________________________________________________

win = Tk()
v = StringVar()
e=Entry(win,textvariable = v)
e.pack()


#create frame to contain the widgets
f = Frame(win)

# create button that initiates the creation of the page
create_page_button = Button(f,text="Create Page")

# place the created button
create_page_button.pack(pady=10)

# label the button to instruct user
l = Label(win, text="Click below to create page")

# position the lable above the button.
l.pack()
f.pack() 

#____________________________________________CREATE FUNCTION TO ASSIGN TO BUTTON______________________________________________


def create_page():
    global output
    output = v.get()
    fh = open("summer_sale.html", "w") # create file and return error if it exists
    fh.write(
        """<html>
            <body>
                <h1>""" + output + 
            
                """</h1>
            </body>

        </html>""")

    fh.close()

    # store file path in variable for readability
    summer_sale = "C:\\Users\\bearf_000\\Desktop\\GitHub\\Python\\Python-Projects\\summer_sale.html"

    # Use webbrowser module to open new tab
    webbrowser.open_new_tab(summer_sale)




#_______________________________________________ASSIGN FUNCTION TO BUTTON__________________________________________________

create_page_button.configure(command=create_page)  


    #________________________________________________________SANDBOX__________________________________________________________

    # set the body of the text
    # initiates process of making new page

    ## def user_input():
    ##user_input = input(name of function?)

    ### Once the code below is entered into a function, ????

    ###assigns the function to the button

