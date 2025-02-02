import qrcode
data="http://mazidmohammad.pythonanywhere.com"
qr=qrcode.make(data)
qr.save("C:\\Users\\USER\\Desktop\\final project\\mazidatlas.png")
print("QR successfull")
