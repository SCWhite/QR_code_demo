import qrcode

#version
#https://www.keyence.com/ss/products/auto_id/barcode_lecture/basic_2d/qr/
#set to "None" and use "fit" to let it choose automatically

#error_correction
#ERROR_CORRECT_L / ERROR_CORRECT_M / ERROR_CORRECT_Q /ERROR_CORRECT_H

#box_size
#how many pixels each"box" of the QR code is.

#border 
#controls how many boxes thick the border should be

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
text = "Some data is put in here, maybe a url ? or some testing text. you can fund python lib in: https:\/\/pypi.org\/project\/qrcode\/"
qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")
