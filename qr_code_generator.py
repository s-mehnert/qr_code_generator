import qrcode
import os
from matplotlib.colors import is_color_like
from qrcode.main import GenericImage


def create_qrcode(data: str, color: str) -> GenericImage:
    """
    function to build a qr code
    :param data:
    :param color:
    :return:
    """
    qr = qrcode.QRCode(version=1, box_size=8, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    return img


def is_filename_valid(name: str) -> bool:
    """
     helper function to check if file name entered is valid
    :param name: name of the
    :return:
    """
    if len(name) == 0:
        return False
    for char in name:
        if char in '\\/:*?"<>| ':
            return False
    return True

# asking for user input


print("\n\nWelcome to the QR Code Generator")

data = input("\n\nDATA --- Please enter the text or link you would like to encode into a QR Code.\n\n> ")

color = input("\n\nCOLOR --- What color should the QR Code have?\n\nYou can input the color using keywords (red, blue, green) or hex codes (e.g. #ba0048).\nNote that the background will always be white.\n\n> ")

if not is_color_like(color):
    print(f"\n!!!   Sorry, --- {color}--- is not a valid color. The QR code will be created in black.")
    color = "black"

name = input("\n\nFILENAME --- Under which name should the PNG file be saved?\n\n> ")

while not is_filename_valid(name):
    print(f"\n!!!   Sorry, --- {name} --- is not a valid file name. \n\nPlease note that the following characters are not allowed: \\/:*?<>| as well as the space character\nValid: test_code --> Not valid: test code")
    name = input("\nPlease enter a new file name.\n> ")

qrc = create_qrcode(data, color)
location = os.getcwd() + "/" + name + ".png"

qrc.save(location)

print(f"\n\nThe QR Code has been successfully created. \nIt can be found at:\n\n{location}\n")
