from PIL import ImageGrab
from PIL import Image
from PIL import UnidentifiedImageError
from pyzbar.pyzbar import decode
import subprocess
import pyperclip
import plyer
import sys
import io

def linux_grabimage():
    try:
        byte_img = subprocess.check_output(["xclip","-se","c","-t","image/png","-o"])
    except subprocess.CalledProcessError:
        return None
    stream = io.BytesIO(byte_img)
    try:
        img = Image.open(stream)
    except UnidentifiedImageError:
        return None
    return img

def other_grabimage():
    img = ImageGrab.grabclipboard()
    return img

bind = False
cur_os = sys.platform
args = sys.argv
appname = "QRscanner"

if len(args) == 2:
    if args[1] == "-bind":
        bind = True

if cur_os.startswith("linux"):
    qrcode_img = linux_grabimage()
else:
    qrcode_img = other_grabimage()

if qrcode_img is not None:   
    decoded = decode(qrcode_img)

    string = "\n".join([i.data.decode() for i in decoded])
    
    if string:
        pyperclip.copy(string)
        
        print("Decoded data copied to clipboard!")
        if bind:
            plyer.notification.notify(app_name=appname, title="Decoded data copied to clipboard!", message=string)
    else:
        print("No QR code found in clipboard image.")
        if bind:
            plyer.notification.notify(app_name=appname, title="No QR code found in clipboard image.", message="Try again with other image.")
else:
    print("No image data found in clipboard!")
    if bind:
        plyer.notification.notify(app_name=appname, title="No image data found in clipboard!", message="Copy an image to clipboard before use.")
