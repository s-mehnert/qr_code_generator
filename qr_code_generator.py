import qrcode

# data = "test data"
# test_img = qrcode.make(data)
# test_img.save("C:/Users/Peafly/Documents/Projects/Coding/projects/weekly_projects/qr_code_generator__python/test_qrcode.png")

# data_2 = "test again"
# qr = qrcode.QRCode(version = 1, box_size = 8, border = 5)
# qr.add_data(data_2)
# qr.make(fit=True)
# img_2 = qr.make_image(fill_color="green", back_color="white")
# img_2.save("C:/Users/Peafly/Documents/Projects/Coding/projects/weekly_projects/qr_code_generator__python/green_qrcode.png")

# linkedin_link = "https://www.linkedin.com/in/smehnert/"
# qr_li = qrcode.QRCode(version=1, box_size=10, border=5)
# qr_li.add_data(linkedin_link)
# qr_li.make(fit=True)
# img_li = qr_li.make_image(fill_color="#295D8A", back_color="white")
# img_li.save("C:/Users/Peafly/Documents/Projects/Coding/projects/weekly_projects/qr_code_generator__python/linkedin_qrcode.png")

# create function to build a qr code

def create_qrcode(data, color):
    qr = qrcode.QRCode(version=1, box_size=8, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    return img

def name_valid(name):
    if len(name) == 0:
        return False
    for char in name:
        if char in '\\/:*?"<>| ':
            return False
    return True

# create input logic

print("\nWelcome to the QR Code Generator")

data = input("\nPlease enter the text or link you would like to encode into a QR Code.\n> ")
color = input("\nWhat color shoud the QR Code have?\nThe available options are: \nblack \nblue \nred \nbrown \ngreen \n\nNote that the background will always be white.\n> ")
name = input("\nGreat, the QR Code will shortly be generated.\nUnder which name should the PNG file be saved?\n> ")

while not name_valid(name):
    print("\nSorry, that is not a valid file name. \nPlease note that the following characters are not allowed: \\/:*?<>| as well as the space character\nCorrect: test_code --> Wrong: test code")
    name = input("Please enter a new file name.\n> ")

qrc = create_qrcode(data, color)
location = "C:/Users/Peafly/Documents/Projects/Coding/projects/weekly_projects/qr_code_generator__python/" + name + ".png"

qrc.save(location)

print("\nThe QR Code has been successfully created. It can be found in the same directory as the QR Code Generator Python File.")

# testing

# qrc = create_qrcode("Hello there", "blue")
# qrc.save("C:/Users/Peafly/Documents/Projects/Coding/projects/weekly_projects/qr_code_generator__python/new_qrcode.png")
