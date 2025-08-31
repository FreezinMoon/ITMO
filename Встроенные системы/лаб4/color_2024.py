import cv2
import numpy as np


access_code = ['R', 'G', 'B', 'R']

rect_size = 100
h_sensitivity = 20


def color_detect(hsv_roi):

    lower_red_1 = np.array([0 - h_sensitivity, 50, 50])
    upper_red_1 = np.array([0 + h_sensitivity, 255, 255])
    lower_red_2 = np.array([180 - h_sensitivity, 50, 50])
    upper_red_2 = np.array([180, 255, 255])

    mask_red_1 = cv2.inRange(hsv_roi, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsv_roi, lower_red_2, upper_red_2)
    mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

    lower_green = np.array([60 - h_sensitivity, 50, 50])
    upper_green = np.array([60 + h_sensitivity, 255, 255])
    mask_green = cv2.inRange(hsv_roi, lower_green, upper_green)

    lower_blue = np.array([120 - h_sensitivity, 50, 50])
    upper_blue = np.array([120 + h_sensitivity, 255, 255])
    mask_blue = cv2.inRange(hsv_roi, lower_blue, upper_blue)

    total_pixels = rect_size * rect_size
    red_rate = np.count_nonzero(mask_red) / total_pixels
    green_rate = np.count_nonzero(mask_green) / total_pixels
    blue_rate = np.count_nonzero(mask_blue) / total_pixels

    if red_rate > green_rate and red_rate > blue_rate and red_rate > 0.3:
        return 'R'
    elif green_rate > red_rate and green_rate > blue_rate and green_rate > 0.3:
        return 'G'
    elif blue_rate > red_rate and blue_rate > green_rate and blue_rate > 0.3:
        return 'B'
    else:
        return 'N'


def process(frame):

    height, width, channels = frame.shape
    spacing = 20
    total_width = 4 * rect_size + 3 * spacing
    start_x = int((width - total_width) / 2)
    start_y = int((height - rect_size) / 2)

    rects = []
    for i in range(4):
        x1 = start_x + i * (rect_size + spacing)
        y1 = start_y
        x2 = x1 + rect_size
        y2 = y1 + rect_size
        rects.append(((x1, y1), (x2, y2)))
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_colors = []
    for (p1, p2) in rects:
        roi = hsv_frame[p1[1]:p2[1], p1[0]:p2[0]]
        c = color_detect(roi)
        detected_colors.append(c)

    if detected_colors == access_code:
        status_text = "Access Granted"
        color = (0, 255, 0)
    else:
        status_text = "Access Denied"
        color = (0, 0, 255)

    cv2.putText(frame, status_text, (start_x, start_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    return frame


print('Press ESC to Quit')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 180)
    processed_frame = process(frame)
    cv2.imshow('Access Control', processed_frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:  # ESC для выхода
        print('Good Bye!')
        break

cap.release()
cv2.destroyAllWindows()
