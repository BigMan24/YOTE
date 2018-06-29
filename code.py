# imports from libraries
from appJar import gui
import webbrowser

# defines the button being pressed
def press(button):
# controls button events
    if button == "Cancel":
# closes the program
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        username = (usr)
        password = (pwd)
        if username == "user" and password == "password":
            webbrowser.open('https://www.youtube.com/watch?v=kJQP7kiw5Fk')
        else:
            app.infoBox('title', 'Incorrect Username or Password', parent=None)


# names the gui window, and sets the size
app = gui("Login Window", "400x200")
app.setBg("White")
app.setFont(18)
# adds names
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
# adds buttons and names to the buttons
app.addButtons(["Submit", "Cancel"], press)
app.setFocus("Username")
# start the program
app.go()
