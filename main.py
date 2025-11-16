import cv2
import numpy as np

WINDOW_NAME = "Vehicle Communication Display"
WIDTH, HEIGHT = 1000, 1000
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX

state = {
    "text": ""
}

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        state["text"] = f"Go around me."
    elif event == cv2.EVENT_RBUTTONDOWN:
        state["text"] = f"Thank you."
    elif event == cv2.EVENT_MBUTTONDOWN:
        state["text"] = f"Emergency ahead."
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        state["text"] = f""
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        state["text"] = f""
    elif event == cv2.EVENT_MBUTTONDBLCLK:
        state["text"] = f""

def draw_frame():
    img = np.full((HEIGHT, WIDTH, 3), BG_COLOR, dtype=np.uint8)
    # draw instructions and current state
    cv2.putText(img, state["text"], (200, 500), FONT, 2.5, (50, 50, 200), 2, cv2.LINE_AA)
    return img

def main():
    cv2.namedWindow(WINDOW_NAME)
    cv2.setMouseCallback(WINDOW_NAME, mouse_callback)

    while True:
        frame = draw_frame()
        cv2.imshow(WINDOW_NAME, frame)
        key = cv2.waitKey(20) & 0xFF
        if key == 27 or key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()