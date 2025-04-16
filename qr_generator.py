import qrcode  #necessary package for qrcode generation 
data="https://github.com/Mazid2003"   #assign any website link to a variable 
qr=qrcode.make(data)  
#make a methode in qrcode package which is used to create the qrcode 
qr.save("C:\\Users\\USER\\Desktop\\final project\\mazidatlas.png")
#save is a method which is used to store the qrcode for the given website
print("QR successfull")
