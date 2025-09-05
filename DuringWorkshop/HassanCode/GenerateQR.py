import qrcode
import cv2
import numpy as np

# Générer le QR code avec qrcode
img = qrcode.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
img.save("qr_temp.png")

# Charger l'image avec OpenCV
qr_img = cv2.imread("qr_temp.png")

# Afficher l'image
cv2.imshow("QR Code", qr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
