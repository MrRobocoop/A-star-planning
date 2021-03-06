import cv2
import numpy as np
import copy
import glob

def crossProduct(one, two, point):
    y = two[1]-one[1]
    x = two[0]-one[0]
    vec = np.array([x,y,0])
    p = np.array([point[0]-one[0],point[1]-one[1],0])
    pro = np.cross(vec,p)
    if pro[2] < 0 :
        return -1
    elif pro[2] == 0:
        return -1
    else :
        return 1

images = glob.glob('*.jpg')

for im in images:
    img = cv2.imread(im)

    cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = cv2.medianBlur(cimg,13)

    ret,thresh1 = cv2.threshold(cimg,40,255,cv2.THRESH_BINARY)
    t2 = copy.copy(thresh1)
    image, contours, hierarchy = cv2.findContours(t2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, contours, -1, (0,255,0), 3)

    x, y  = thresh1.shape

#    print x, y

    arr = np.zeros((x, y, 3), np.uint8)
    final_contours = []
    for i in range(len(contours)):
        cnt = contours[i]
        if cv2.contourArea(cnt) > 1000 and cv2.contourArea(cnt) < 7000:
            final_contours.append(cnt)
            hull = cv2.convexHull(cnt, clockwise=True, returnPoints= True)
            print hull
            break
            for i in range(len(hull)):
        #        print hull[i]
                start = tuple(hull[i, 0])
                end = tuple(hull[(i+1) % len(hull), 0])
                cv2.line(img, start, end, [0, 255, 0], 1)
            cv2.fillConvexPoly(arr, hull, [255, 255, 255])


    cv2.imshow('image',img)
    cv2.imshow('image2', arr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()