import cv2 as cv
NOP = 0 #number of points selected
points = [[1,1], [1,1]]
def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN: 
        print(x, ' ', y)
        points[NOP][0] = x
        points[NOP][1] = y
        NOP = NOP + 1
        print("Number of selected pixels is: " + NOP)

GUI = cv.imread('/home/zeyad/VScode/.vscode/41.jpg')
cv.imshow('image', GUI)
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()