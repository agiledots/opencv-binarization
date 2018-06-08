import os
import shutil
import cv2
import utils


video = cv2.VideoCapture("videos/001.mp4")
fps = video.get(cv2.CAP_PROP_FPS)

text_folder = os.path.join(".", "text")
shutil.rmtree(text_folder, ignore_errors=True)
os.mkdir(text_folder)

seq = 0

while (video.isOpened()):
    seq = seq + 1

    # Read first frame.b  b
    ok, image = video.read()
    if not ok:
        print('Cannot read video file')
        break

    image = utils.frame_resize(image, 0.3)

    # Display result
    cv2.imshow("original", image)

    if seq % 5 != 0:
        continue

    # ------------------------------
    GrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 中值滤波
    GrayImage = cv2.medianBlur(GrayImage, 5)
    ret, th1 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY)
    # 3 为Block size, 5为param1值
    th2 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 3, 5)
    th3 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 3, 5)

    cv2.imshow("tracking", th3)

    filename = "{:0>5d}.txt".format(seq)
    filename = os.path.join(text_folder, filename)

    text = ""
    for xAxis in th3:
        for dot in xAxis:
            if dot == 255:
                text = text + " "
            else:
                text = text + utils.random_char()

        text = text + "\r\n"
    utils.write_file(filename, text)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        print(th3)
        break

video.release()
cv2.destroyAllWindows()
