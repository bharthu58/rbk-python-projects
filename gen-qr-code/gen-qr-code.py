import qrcode as QR

def create(content, filename):
    img = QR.make(content)
    img.save(filename)
    return f"here is your file saved at {filename}"
   
cntnt = """BEGIN:VCARD
VERSION:3.0
N:Ramanna;Bharathkumar
FN:Bharathkumar Ramanna
NICKNAME:Bharath
ORG:UBS Securities LLC
TITLE:Executive Director
TEL;TYPE=WORK,VOICE:7323978315
TEL;TYPE=CELL:7323978315
EMAIL:bharthu.code@gmail.com
URL:https://bharthu58.github.io
END:VCARD"""

result = create(cntnt, "rbk_vcard_qr.png")  # info, filename
print(result)