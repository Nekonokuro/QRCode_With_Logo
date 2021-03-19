import qrcode
from PIL import Image



def qr_code_link(picture,url):
    #logo
    logo_pic=picture
    logo=Image.open(logo_pic)
    width_base=75
    width_percent=(width_base/float(logo.size[0]))
    size=int((float(logo.size[1])*float(width_percent)))
    logo=logo.resize((width_base,size),Image.ANTIALIAS)
    link_code = url
    #link for QR code
    code_specs = qrcode.QRCode(version=1,box_size=10,border=5)
    code_specs.add_data(link_code)
    code_specs.make(fit=True)
    code_image = code_specs.make_image(fill="black", back_color="white").convert("RGB")
    logo_position=((code_image.size[0]-logo.size[0]) // 2, (code_image.size[1]-logo.size[1]) // 2)
    code_image.paste(logo,logo_position)
    code_image.save("GitQR.png")

qr_code_link("gitpic.png","https://github.com/Nekonokuro")



