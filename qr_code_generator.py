import qrcode
import os
from matplotlib.colors import is_color_like

def create_qrcode(data: str, color: str, file_path: str) -> None:
    """
    Creates a QR code with the given data and color, and saves it to the specified file path.

    :param data: The data to encode in the QR code.
    :param color: The color of the QR code.
    :param file_path: The file path to save the QR code image.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white")
    img.save(file_path)

def get_valid_filename(prompt: str) -> str:
    """
    Repeatedly prompts the user for a filename until a valid one is entered.

    :param prompt: The prompt to display to the user.
    :return: A valid filename.
    """
    while True:
        name = input(prompt)
        if not name or any(char in '\\/:*?"<>| ' for char in name):
            print("Invalid filename. Please avoid these characters: \\/:*?\"<>| and spaces.")
        else:
            return name

def get_valid_color(prompt: str) -> str:
    """
    Prompts the user for a color and validates it. Returns 'black' if the input is not a valid color.

    :param prompt: The prompt to display to the user.
    :return: A valid color.
    """
    color = input(prompt)
    if not is_color_like(color):
        print(f"Invalid color '{color}'. Defaulting to black.")
        return "black"
    return color

def main():
    print("\nWelcome to the QR Code Generator\n")

    data = input("DATA --- Please enter the text or link to encode into a QR Code:\n> ")
    color = get_valid_color("\nCOLOR --- Enter the QR Code color (keywords like red or hex codes like #ba0048):\n> ")
    filename = get_valid_filename("\nFILENAME --- Enter the filename to save the QR Code as (without extension):\n> ")
    file_path = os.path.join(os.getcwd(), f"{filename}.png")

    create_qrcode(data, color, file_path)

    print(f"\nThe QR Code has been successfully created and saved to:\n{file_path}\n")

if __name__ == "__main__":
    main()
