import os 
import qrcode 

def main():

    data = input("Podaj link, do ktorego chcesz wygenerowac QR Code: ")


    if data: 

        dir_path = os.path.dirname(os.path.realpath(__file__))

        qr = qrcode.QRCode(version = 1, box_size=10, border = 5)

        qr.add_data(data)

        qr.make(fit=True)
        img = qr.make_image()

        img.save(f"{dir_path}/qr-codes/myqrcode.png")

        print("Kod QR został zapisany w folderze qr-codes")
        
    

    else: 
        print("Nie podano linka!")
        main()
    
main()