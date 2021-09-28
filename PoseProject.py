import cv2
import time
import PoseModule as pm
import matplotlib.pyplot as plt
import mimetypes
mimetypes.init()


def media_type(file):
    mimestart = mimetypes.guess_type(file)[0]
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
    return mimestart


file = input("Enter file name : ")
if file == "0" or media_type(file)=="video":
    if file =="0":
        file=0


    cap = cv2.VideoCapture(file)
    detector = pm.poseDetector()
    pTime = 0
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Pose Detector", img)
        # imS = cv2.resize(img, (451, 750))  # Resize image
        # cv2.imshow("output", imS)
        cv2.waitKey(1)

elif media_type(file)=="image":
    cap = cv2.imread(file)
    detector = pm.poseDetector()

    img = detector.findPose(cap)
    lmList = detector.findPosition(cap)
    print(lmList)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()



