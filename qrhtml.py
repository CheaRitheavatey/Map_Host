import qrcode
import qrcode.constants

# url of the index.html
url = ""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url).make(fit=True)

# make img qrcode
img = qr.make_image().save("QR_Map.png")
print("QR code saved as QR_Map.png")