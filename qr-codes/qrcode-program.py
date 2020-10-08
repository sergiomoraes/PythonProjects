import segno

qr = segno.make("s1bm2nd3", micro=False)
qr.designator
qr.save("WiFi-QRcode.svg", scale=5)
