import cv2
import mediapipe as mp
import pyautogui
import math

# MediaPipe el izleme modelini başlat
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Video yakalama (kamera)
cap = cv2.VideoCapture(0)

# Ekran boyutlarını al
screen_width, screen_height = pyautogui.size()

# Tıklama durumlarını izlemek için bayraklar
left_click = False
right_click = False

while True:
    # Kameradan bir kare oku
    success, img = cap.read()
    if not success:
        break

    # Görüntüyü yatayda çevir
    img = cv2.flip(img, 1)

    # RGB'ye dönüştür
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # El izleme modelini kullanarak elleri tespit et
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # İşaret parmağı ve baş parmak ucu koordinatlarını al
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            # Görüntü boyutları
            h, w, c = img.shape
            index_x, index_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # İşaret parmağı ucu koordinatlarını ekran koordinatlarına dönüştür
            screen_x = int(screen_width * index_finger_tip.x)
            screen_y = int(screen_height * index_finger_tip.y)

            # Mouse hareketini gerçekleştir
            pyautogui.moveTo(screen_x, screen_y)

            # İşaret parmağı ve baş parmak arasındaki mesafeyi hesapla
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

            # Sağ tıklama: mesafe küçük ve sağ tıklama henüz yapılmamışsa
            if distance < 30 and not right_click:
                pyautogui.rightClick()
                right_click = True
            # Sol tıklama: mesafe küçük ve sol tıklama henüz yapılmamışsa
            elif distance < 30 and not left_click:
                pyautogui.leftClick()
                left_click = True
            # Mesafe büyükse tıklama bayraklarını sıfırla
            elif distance > 30:
                left_click = False
                right_click = False

            # Elleri çiz
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Görüntüyü göster
    cv2.imshow("El ile Mouse Kontrolü", img)

    # 'q' tuşuna basarak çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
