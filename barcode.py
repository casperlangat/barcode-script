import qrcode

# Data to encode in the QR code
data = "Nairobi Terminus to Mombasa Terminus\nSeat 25, Coach 3\nFirst Class"

# Generate the QR Code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code as an image
img = qr.make_image(fill_color="black", back_color="#ADD8E6")
img.save("ticket_qr_code.png")

print("QR code generated and saved as ticket_qr_code.png")
