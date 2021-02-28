import base64
from datetime import datetime

print("welke 2 bestanden wil je encoden")
input1 = input()
input2 = input()

afbeelding1 = open(input1, "rb")
afbeelding2 = open(input2, "rb")

image_read1 = afbeelding1.read()
image_read2 = afbeelding2.read()

image_64_encode1 = base64.encodebytes(image_read1)
image_64_encode2 = base64.encodebytes(image_read2)

now = datetime.now()
dtstring = now.strftime("%H%M%S")
name1 = "encoded" + dtstring + "1.txt"
name2 = "encoded" + dtstring + "2.txt"

print(name1, name2)

text1 = open(name1, "wb")
text2 = open(name2, "wb")

n = text1.write(image_64_encode1)
text1.close()
n = text2.write(image_64_encode2)
text2.close()