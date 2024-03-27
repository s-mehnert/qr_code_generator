import qrcode
import os

# function to build a qr code

def create_qrcode(data, color):
    qr = qrcode.QRCode(version=1, box_size=8, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    return img

# helper function to check if file name entered is valid

def name_valid(name):
    if len(name) == 0:
        return False
    for char in name:
        if char in '\\/:*?"<>| ':
            return False
    return True

# asking for user input

print("\nWelcome to the QR Code Generator\n")

data = input("\nPlease enter the text or link you would like to encode into a QR Code.\n> ")
color = input("\nWhat color shoud the QR Code have?\nThe available options are: \n\n\tblack \n\tblue \n\tred \n\tbrown \n\tgreen \n\nNote that the background will always be white.\n> ")
name = input("\nGreat, the QR Code will shortly be generated.\nUnder which name should the PNG file be saved?\n> ")

while not name_valid(name):
    print("\nSorry, that is not a valid file name. \nPlease note that the following characters are not allowed: \\/:*?<>| as well as the space character\nCorrect: test_code --> Wrong: test code")
    name = input("Please enter a new file name.\n> ")

qrc = create_qrcode(data, color)
location = os.getcwd() + "/" + name + ".png"

qrc.save(location)

print("\nThe QR Code has been successfully created. It can be found in the same directory as the QR Code Generator File.")
