import cv2
import argparse
import numpy as np
 
 
def callback(value):
    pass
 

def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)
 
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
 
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)
def get_arguments():
    ap = argparse.ArgumentParser()
    #ap.add_argument('-f', '--filter', required=False,
    #                help='Range filter. RGB or HSV')
    ap.add_argument('-w', '--webcam', required=False,
                    help='Use webcam', action='store_true')
    
    args = vars(ap.parse_args())
    args['webcam'] = True
    #if not args['filter'].upper() in ['RGB', 'HSV']:
    #    ap.error("Please speciy a correct filter.")
 
    return args

def get_trackbar_values(range_filter):
    values = list()
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values


def main():
    args = get_arguments()
 
    #range_filter = args['filter'].upper()

    range_filter = 'HSV'
 
    camera = cv2.VideoCapture(0)
 
    #setup_trackbars(range_filter)
 
    while True:
        
        if args['webcam']:
            ret, image = camera.read()
 
            if not ret:
                break
 
            if range_filter == 'RGB':
                frame_to_thresh = image.copy()
            else:
                frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
        #v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
 
        #thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        thresh = cv2.inRange(frame_to_thresh, (14, 175, 17), (155, 255, 255))
        kernel = np.ones((5,5),np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
 
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
 
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
            # only proceed if the radius meets a minimum size
            if radius > 20:
                print(radius)
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(mask, (int(x), int(y)), int(radius),(200, 240, 255), 2)
                cv2.circle(mask, center, 3, (3, 200, 255), -1)
                cv2.putText(mask,"centroid", (center[0]+10,center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
                cv2.putText(mask,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
 
        # show the frame to our screen
        cv2.imshow("Original", (cv2.flip(image,1)))
        #cv2.imshow("Thresh", (cv2.flip(thresh,1)))
        cv2.imshow("Mask",(cv2.flip(mask,1)))
 
        if cv2.waitKey(1) & 0xFF is 27:
            break
 
 
if __name__ == '__main__':
    main()