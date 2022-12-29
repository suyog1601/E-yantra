'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1A - Part 1 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a_part1.py
# Functions:		scan_image
# 					[ Comma separated list of functions in this file ]
# Global variables:	shapes
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################






##############################################################


def scan_image(img_file_path):

    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }
    
    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes

    ##############	ADD YOUR CODE HERE	##############
    shapes = {}

    img = cv2.imread(img_file_path)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,60,0])
    upper_blue = np.array([131,255,255])

    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,120])
    upper_red = np.array([10,255,255])

    mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
    mask2 = cv2.inRange(hsv,lower_green,upper_green)
    mask3 = cv2.inRange(hsv,lower_red,upper_red)

    _,thresh1 = cv2.threshold(mask1, 230, 255, cv2.THRESH_BINARY)
    _,thresh2 = cv2.threshold(mask2, 230, 255, cv2.THRESH_BINARY)
    _,thresh3 = cv2.threshold(mask3, 230, 255, cv2.THRESH_BINARY)

    contour1,heir1 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour2,heir2 = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour3,heir3 = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cont in contour3:
        color = 'red'
        approx = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont, True), True)
        M = cv2.moments(cont)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        hull = cv2.convexHull(cont)
        area = cv2.contourArea(cont)
        a = []
        a.append(color)

        if(len(approx) == 3):
            area = area + 700
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Triangle'] = a
        elif(len(approx) == 4):
            x, y, w, h = cv2.boundingRect(approx)
            aspectratio = float(w)/h
            e = 2.718281828459045
            s = (e**(aspectratio*1j)).imag
            c = (e**(aspectratio*1j)).real
            angle = s/c
            if angle < -1:
                if aspectratio >= 2.00:
                    area = area + 700
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Parallelogram'] = a
                else:
                    area = area + 1000
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rhombus'] = a
            else:
                if aspectratio >= 0.95 and aspectratio <= 1.07:
                    area = area + 1500
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Square'] = a
                else:
                    area = area + 1200
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rectangle'] = a
        elif(len(approx) == 5):
            area = area + 900
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Pentagon'] = a
        elif(len(approx) == 6):
            area = area + 850
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Hexagon'] = a
        else:
            area = area + 1600
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Circle'] = a

    for cont in contour2:
        color = 'green'
        approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
        M = cv2.moments(cont)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        hull = cv2.convexHull(cont)
        area = cv2.contourArea(cont)
        a = []
        a.append(color)

        if (len(approx) == 3):
            area = area + 700
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Triangle'] = a
        elif (len(approx) == 4):
            x, y, w, h = cv2.boundingRect(approx)
            aspectratio = float(w) / h
            e = 2.718281828459045
            s = (e ** (aspectratio * 1j)).imag
            c = (e ** (aspectratio * 1j)).real
            angle = s / c
            if angle < -1:
                if aspectratio >= 2.00:
                    area = area + 700
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Parallelogram'] = a
                else:
                    area = area + 1000
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rhombus'] = a
            else:
                if aspectratio >= 0.95 and aspectratio <= 1.07:
                    area = area + 1500
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Square'] = a
                else:
                    area = area + 1200
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rectangle'] = a
        elif (len(approx) == 5):
            area = area + 900
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Pentagon'] = a
        elif (len(approx) == 6):
            area = area + 850
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Hexagon'] = a
        else:
            area = area + 1600
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Circle'] = a

    for cont in contour1:
        color = 'blue'
        approx = cv2.approxPolyDP(cont, 0.01 * cv2.arcLength(cont, True), True)
        M = cv2.moments(cont)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        hull = cv2.convexHull(cont)
        area = cv2.contourArea(cont)
        a = []
        a.append(color)

        if (len(approx) == 3):
            area = area + 700
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Triangle'] = a
        elif (len(approx) == 4):
            x, y, w, h = cv2.boundingRect(approx)
            aspectratio = float(w) / h
            e = 2.718281828459045
            s = (e ** (aspectratio * 1j)).imag
            c = (e ** (aspectratio * 1j)).real
            angle = s / c
            if angle < -1:
                if aspectratio >= 2.00:
                    area = area + 700
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Parallelogram'] = a
                else:
                    area = area + 1000
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rhombus'] = a
            else:
                if aspectratio >= 0.95 and aspectratio <= 1.07:
                    area = area + 1500
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Square'] = a
                else:
                    area = area + 1200
                    a.append(area)
                    a.append(cx)
                    a.append(cy)
                    shapes['Rectangle'] = a
        elif (len(approx) == 5):
            area = area + 900
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Pentagon'] = a
        elif (len(approx) == 6):
            area = area + 850
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Hexagon'] = a
        else:
            area = area + 1600
            a.append(area)
            a.append(cx)
            a.append(cy)
            shapes['Circle'] = a
	
	

	##################################################
    
    return shapes


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    the function first takes 'Sample1.png' as input and runs scan_image function to find details
#                   of colored (non-white) shapes present in 'Sample1.png', it then asks the user whether
#                   to repeat the same on all images present in 'Samples' folder or not

if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in '+ curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'
    
    # path to 'Sample1.png' image file
    file_num = 1
    img_file_path = img_dir_path + 'Sample' + str(file_num) + '.png'

    print('\n============================================')
    print('\nLooking for Sample' + str(file_num) + '.png')

    if os.path.exists('Samples/Sample' + str(file_num) + '.png'):
        print('\nFound Sample' + str(file_num) + '.png')
    
    else:
        print('\n[ERROR] Sample' + str(file_num) + '.png not found. Make sure "Samples" folder has the selected file.')
        exit()
    
    print('\n============================================')

    try:
        print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
        shapes = scan_image(img_file_path)

        if type(shapes) is dict:
            print(shapes)
            print('\nOutput generated. Please verify.')
        
        else:
            print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
            exit()

    except Exception:
        print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
        exit()

    print('\n============================================')

    choice = input('\nWant to run your script on all the images in Samples folder ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = 2
        
        for file_num in range(file_count):

            # path to image file
            img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'

            print('\n============================================')
            print('\nLooking for Sample' + str(file_num + 1) + '.png')

            if os.path.exists('Samples/Sample' + str(file_num + 1) + '.png'):
                print('\nFound Sample' + str(file_num + 1) + '.png')
            
            else:
                print('\n[ERROR] Sample' + str(file_num + 1) + '.png not found. Make sure "Samples" folder has the selected file.')
                exit()
            
            print('\n============================================')

            try:
                print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                shapes = scan_image(img_file_path)

                if type(shapes) is dict:
                    print(shapes)
                    print('\nOutput generated. Please verify.')
                
                else:
                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                    exit()

            except Exception:
                print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                exit()

            print('\n============================================')

    else:
        print('')
