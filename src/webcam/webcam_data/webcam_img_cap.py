import cv2

webcam = cv2.VideoCapture(0)

img_cnt = 0

list_of_num = []
list_of_num.append(0)

while(True):
    ret, frame = webcam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        num = len(list_of_num) - 1
        img_name = "opencv_frame_{}.png".format(num)
        cv2.imwrite(img_name, frame)
        img_cnt += 1
        list_of_num.append(img_cnt)
    
    cv2.imshow('webcam', gray)
    
    # allow user to press "q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
