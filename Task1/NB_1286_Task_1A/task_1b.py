'''
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This script is to implement Task 1B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
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
# Filename:			task_1b.py
# Functions:		applyPerspectiveTransform, detectMaze, writeToCsv
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, csv)               ##
##############################################################
import numpy as np
import cv2
import csv
##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################

#this function will return weight of the box

def weight( points , img) :                   #points r the 2d numpy aarray containging co ordinates of point 
    i1 = points[0][0]
    j1 = points[0][1]

    i2 = points[1][0]                          #extracting points from array 
    j2 = points[1][1]

    i4 = points[2][0]
    j4 = points[2][1]

    i3 = points[3][0]
    j3 = points[3][1]

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 #to convert image into binary image 
    ret, img  = cv2.threshold(imgray, 127, 255, 0)
    length , height   = img.shape

    Ans = 0 
    a = 0                                   #starting points a,b,c,d so that one weight should not add twice 
    b = 0 
    c = 0 
    d = 0 
    ans = [] 

	# now for check in the middle of each side of box we will check 10 pixels back,forth or up,down for black pixel 
	# and we will add image according to that  
    for _ in range(-10 , 10 ) :

        if ( a== 0 and j1 >= 0 and j1 < 15)    or     ( a== 0 and ( (j1+j2)//2 + _ > 0 and (j1+j2)//2 + _ < height   ) and (img[ (j1+j2)//2 + _ , (i1+i2)//2  ] == 0    )) :
            Ans = Ans + 2              #Adding weight         2         as it is closed at        up         side 
            a = 1                      #so this 2 should not add again 
            ans.append(2)

        if ( b == 0 and i1 >= 0 and i1 < 15 )  or   ( b==0 and  (  (i1+i3)//2 + _ > 0 and (i1+i3)//2 + _ < length  ) and ( img[ (j1+j3)//2  , (i1+i3)//2 + _   ] ==0   )) :
            Ans = Ans + 1              #Adding weight        1         as it is closed at          left        side
            b = 1                                 
            ans.append(1)
            #cv.circle(img1,(  (i1+i3)//2 + _ , (j1+j3)//2      ), 2 , (0,0,255), -1)

        if ( c == 0 and j3 <= height and j3 >= height - 10) or  (c==0  and ( (j3+j4)//2 + _ > 0 and  (j3+j4)//2 + _ < height  ) and  (  img[ (j3+j4)//2 + _  , (i3+i4)//2    ] ==0    ))   :
            Ans = Ans + 8              #Adding weight          8           as it is closed at       down       side        
            c = 1 
            ans.append(8)
            #cv.circle(img1,(  (i3+i4)//2 , (j3+j4)//2 + _     ), 2 , (0,0,255), -1)
            
        if ( d ==0 and i4 <= length and i4 >= length - 10 ) or (d==0  and ( (i2+i4)//2 + _ > 0 and ( (i2+i4)//2 + _ < length  )) and   (  img[  (j2+j4)//2   , (i2+i4)//2 + _  ] == 0   ))     :      
            Ans = Ans + 4              #Adding weight         4          as it is closed at       right       side
            d= 1                                         
            ans.append(4)
            #cv.circle(img1,( (i2+i4)//2 + _  , (j2+j4)//2    ), 2 , (0,0,255), -1)
            
    return Ans , ans 






##############################################################


def applyPerspectiveTransform(input_img):

	"""
	Purpose:
	---
	takes a maze test case image as input and applies a Perspective Transfrom on it to isolate the maze

	Input Arguments:
	---
	`input_img` :   [ numpy array ]
		maze image in the form of a numpy array
	
	Returns:
	---
	`warped_img` :  [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Example call:
	---
	warped_img = applyPerspectiveTransform(input_img)
	"""

	warped_img = None

	##############	ADD YOUR CODE HERE	##############
	
	img = input_img 

	imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(imgray, 127, 255, 0)               #converting image into binary 

	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)      #finding counters 

	max = 0                        #to find maximum perimeter 
	Ans = 0                        #to remember square 
	for _ in contours :
		area = cv2.contourArea(_)                           #to get area of conter 
		perimeter = cv2.arcLength(_,True)                   # to get perimeter of conter 
		
		# this will check if the given counter is square 
		#by checking one of its properties 
		check = area - (perimeter//4)**2           
		if check > -10000 and check < 10000 and area > max :
			max = area                                              #taking largest square 
			#print(area) 
			Ans = _ 

	
	x , y , w , h = cv2.boundingRect(Ans)            
	img = img[ y:y+h , x:x+w]                               #croping image 
	                                                        #getting required square 
	
	
	warped_img = img 
	
	

	##################################################

	return warped_img


def detectMaze(warped_img):

	"""
	Purpose:
	---
	takes the warped maze image as input and returns the maze encoded in form of a 2D array

	Input Arguments:
	---
	`warped_img` :    [ numpy array ]
		resultant warped maze image after applying Perspective Transform
	
	Returns:
	---
	`maze_array` :    [ nested list of lists ]
		encoded maze in the form of a 2D array

	Example call:
	---
	maze_array = detectMaze(warped_img)
	"""

	maze_array = []

	##############	ADD YOUR CODE HERE	##############
	
	img = warped_img 

	length , height , ____ = img.shape
	i = 0
	j = 0

	array_main = [] 

	#this will divide the image into 10 squares
	#co ordinates of that square will be send to weight function to calculate weight 
	for _ in range(10) :
		i1 = 0
		j1 = j 
		array_sub = [] 
		for __ in range(10) :

			# co ordinates of square _,__ 
			pts = np.array([[ i1              ,  j1                     ],
							[ i1 + (length/10) ,  j1         ],
							[ i1 + (length/10)  ,  j1 + (height/10)         ],
							[ i1              ,  j1  + (height/10)                   ]], 
							np.int32)

			_m_ = weight( pts  , img)  #sending this co ordinates to get weight 
			mmm = 0
			for _1 in _m_[1] :
				mmm = mmm + _1
			array_sub.append(mmm )                #calculating weight 

			i1 = i1 + (length/10)                  #to move right 

		array_main.append(array_sub)                

		j = j + (height/10)                       #to move downwords 

	
	maze_array = array_main

	
	
	##################################################

	return maze_array


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
def writeToCsv(csv_file_path, maze_array):

	"""
	Purpose:
	---
	takes the encoded maze array and csv file name as input and writes the encoded maze array to the csv file

	Input Arguments:
	---
	`csv_file_path` :	[ str ]
		file path with name for csv file to write
	
	`maze_array` :		[ nested list of lists ]
		encoded maze in the form of a 2D array
	
	Example call:
	---
	warped_img = writeToCsv('test_cases/maze00.csv', maze_array)
	"""

	with open(csv_file_path, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(maze_array)


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
# 
# Function Name:    main
#        Inputs:    None
#       Outputs:    None
#       Purpose:    This part of the code is only for testing your solution. The function first takes 'maze00.jpg'
# 					as input, applies Perspective Transform by calling applyPerspectiveTransform function,
# 					encodes the maze input in form of 2D array by calling detectMaze function and writes this data to csv file
# 					by calling writeToCsv function, it then asks the user whether to repeat the same on all maze images
# 					present in 'test_cases' folder or not. Write your solution ONLY in the space provided in the above
# 					applyPerspectiveTransform and detectMaze functions.

if __name__ == "__main__":

	# path directory of images in 'test_cases' folder
	img_dir_path = 'test_cases/'

	# path to 'maze00.jpg' image file
	file_num = 0
	img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

	print('\n============================================')
	print('\nFor maze0' + str(file_num) + '.jpg')

	# path for 'maze00.csv' output file
	csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
	
	# read the 'maze00.jpg' image file
	input_img = cv2.imread(img_file_path)

	# get the resultant warped maze image after applying Perspective Transform
	warped_img = applyPerspectiveTransform(input_img)

	if type(warped_img) is np.ndarray:

		# get the encoded maze in the form of a 2D array
		maze_array = detectMaze(warped_img)

		if (type(maze_array) is list) and (len(maze_array) == 10):

			print('\nEncoded Maze Array = %s' % (maze_array))
			print('\n============================================')
			
			# writes the encoded maze array to the csv file
			writeToCsv(csv_file_path, maze_array)

			cv2.imshow('warped_img_0' + str(file_num), warped_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		
		else:

			print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
			exit()
	
	else:

		print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
		exit()
	
	choice = input('\nDo you want to run your script on all maze images ? => "y" or "n": ')

	if choice == 'y':

		for file_num in range(1, 10):
			
			# path to image file
			img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

			print('\n============================================')
			print('\nFor maze0' + str(file_num) + '.jpg')

			# path for csv output file
			csv_file_path = img_dir_path + 'maze0' + str(file_num) + '.csv'
			
			# read the image file
			input_img = cv2.imread(img_file_path)

			# get the resultant warped maze image after applying Perspective Transform
			warped_img = applyPerspectiveTransform(input_img)

			if type(warped_img) is np.ndarray:

				# get the encoded maze in the form of a 2D array
				maze_array = detectMaze(warped_img)

				if (type(maze_array) is list) and (len(maze_array) == 10):

					print('\nEncoded Maze Array = %s' % (maze_array))
					print('\n============================================')
					
					# writes the encoded maze array to the csv file
					writeToCsv(csv_file_path, maze_array)

					cv2.imshow('warped_img_0' + str(file_num), warped_img)
					cv2.waitKey(0)
					cv2.destroyAllWindows()
				
				else:

					print('\n[ERROR] maze_array returned by detectMaze function is not complete. Check the function in code.\n')
					exit()
			
			else:

				print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
				exit()

	else:

		print('')

