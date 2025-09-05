import cv2

# Ouvre la webcam (0 = caméra par défaut)
cap = cv2.VideoCapture(0)

# Crée un détecteur de QR code
detector = cv2.QRCodeDetector()

print("📷 Lecture QR en cours... Appuie sur 'q' pour quitter.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection et décodage
    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None:
        # Dessine le cadre autour du QR code
        for i in range(len(bbox)):
            pt1 = tuple(map(int, bbox[i][0]))
            pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
            cv2.line(frame, pt1, pt2, color=(0, 255, 0), thickness=2)

        if data:
            print(f"✅ QR Code détecté : {data}")
            cv2.putText(frame, data, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Affiche la vidéo
    cv2.imshow("Lecteur QR Code", frame)

    # Quitte si on appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère les ressources
cap.release()
cv2.destroyAllWindows()
