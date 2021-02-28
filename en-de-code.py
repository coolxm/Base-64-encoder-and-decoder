import base64
from datetime import datetime

def decode(input1):
    afbeelding1 = open(input1, "rb")
    image_read1 = afbeelding1.read()
    image_64_decode1 = base64.decodebytes(image_read1)

    print(image_64_decode1)
    return(image_64_decode1)

def encode(input1):
    afbeelding1 = open(input1, "rb")
    image_read1 = afbeelding1.read()
    image_64_encode1 = base64.encodebytes(image_read1)

    print(image_64_encode1)
    return(image_64_encode1)

def write(image_64_decode1):
    now = datetime.now()
    dtstring = now.strftime("%H%M%S")
    name1 = "decoded" + dtstring + "1.jpg"

    print(name1)

    text1 = open(name1, "wb")

    n = text1.write(image_64_decode1)
    text1.close()

def onStart():
    func = input("encoden or decoden")
    input = input("welke 2 bestanden wil je" + func)
    
    if input == "encoden":
        resp = encode(input)
    elif input == "decoden":
        resp = decode(input)
    else:
        return False

    write(resp)
    return "done"

print (onStart())
        