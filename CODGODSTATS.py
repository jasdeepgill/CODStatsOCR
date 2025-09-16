from pickle import TRUE
import cv2
import pytesseract
import os
import json

from PIL import Image
from CgsOpenCv import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#load array with readFiles.txt
readFiles=[]

with open('readFiles.txt','r') as file:
    for line in file:
        readFiles.append(line.strip())

#Create fName array with all none read files in folder. 
fName=[]
directory ='Codscoreboards'

contents = os.listdir(directory)
for x in contents:
    if x not in readFiles:
        fName.append(directory + '/' + x)


#tmpJson = generateMapData(test)
#print("hello")
#print(tmpJson)
#print("map name is")
#print(getMapName(test))
#print(getPlayerNumbers(test))
#print(getBottomPlayerNumbers(test))
#print("Top team score is")
#print(getTopTeamScore(test))
#print("bottom team score is")
#print(getBottomTeamScore(test))


#we have done 120 to 147.
#103, 120
# 102 skipping for now, dark images I will make new coords for they seem to be pretty close
#91, 102
# skipping 90

# Combine 07-13 002247 and 002554
#Combine 08-08 224130 and 224843
# Loop to rename data to name of image and not numbers
#for i in range(0,1,1):
    #test = fName[i]
    #jsonName = test.split('/')
    #print(jsonName[1])
    #jsonName = jsonName[1]
    #fileName1= f"data/{i+1}.json"
    #fileName2=f"data/{jsonName}.json"
    #print(fileName1, fileName2)
    #os.rename(fileName1,fileName2)




# START HERE
# So this loop, loops the folder of images. So 0 is the first image.
# It calls functions from CgsOpenCv.py.
# Use visual studio 2022 then just press start. #

# OCT 3 trained model some more on 2 0 and 8s. 
#176 to 224
# 155 to 210.
# 210 to 300.
#
for i in range(304, 400, 1):
    test = fName[i]
    
    #These are the coords for a 2k resolution image. 
    #They zoom in on the first player in the image.
    #First numbers for name second for stats.
    x,y,w,h,x2,y2,w2,h2 = 208, 384, 320, 50,808, 390, 690, 40
    # Read the image
    img = cv2.imread(test)

    # This is just for lobby screenshots.
    darkNum= calculate_darkness(test)
    #if darkNum < 0.874:
        #print(darkNum , test)
        #continue

    if darkNum > 0.874:
        x2= 710
        w2= 755
    
    # Get image dimensions
    height, width, channels = img.shape
    
    print("DATA for ",test)
    team1Nums = int(input("Enter team1 numbers: "))
    team2Nums = int(input("Enter team2 numbers: "))
    team1 = int(input("Enter team1 rounds won: "))
    team2 = int(input("Enter team2 round won: "))

    
    jsonName = test.split('/')
    print(jsonName[1])
    jsonName = jsonName[1]
    #mapNum = getMapNumber(test)
    filePath = f"data/{jsonName}.json"

    # If image is not 2k resolution not going to work so we just skip. 
    if height < 1400 or team1Nums>6 or team2Nums >6:
        print("image skipped",test)
        print("image skipped",test)
        print("image skipped",test)
        mapJson = generateMapData(test,team1,team2)
        with open(filePath,'x') as json_file:
            json.dump(mapJson, json_file, indent=4)

        print("created ", filePath)
        continue

    tmp = TRUE


    topPlayers = team1Nums

    botPlayers = team2Nums
    botPlayers +=1

    mostPlayers = max(team1Nums,team2Nums)

    team = "team1"
    mapJson = generateMapData(test,team1,team2)
   
    #x,y,w,h,x2,y2,w2,h2 = 208, 384, 320, 50,808, 390, 690, 40
    while(tmp):

        pList = createPlayerList(test,x,y,w,h,x2,y2,w2,h2)

    
        playerData = createPlayer(test,pList,team,team1,team2)

        mapJson = addPlayers(mapJson, playerData)
        y +=53
        y2 +=53
        if topPlayers > 0:
            topPlayers -= 1
            print(topPlayers)
        if topPlayers == 0:

            if mostPlayers == 4:
            
                y = 835
                y2 = 835
            if mostPlayers == 5:
                y = 887
                y2 = 887
            if mostPlayers == 6:
                y = 939
                y2 = 939
            topPlayers -=1
            team ="team2"
        if topPlayers < 0:
            botPlayers -=1

        if botPlayers == 0:
            tmp = False

    with open(filePath,'x') as json_file:
        json.dump(mapJson, json_file, indent=4)
    #print(mapJson)
    print("created ", filePath)

#print(getPlayerStats(test,808, 395, 690, 30))
#print(getPlayerName(test,208, 438, 320, 50))
#print(getPlayerStats(test,808, 448, 680, 30))
#print(getPlayerName(test,208, 492, 320, 50))
#print(getPlayerStats(test,808, 502, 680, 30))
#print(getPlayerName(test,208, 546, 320, 50))
#print(getPlayerName(test,208, 600, 320, 50))
#print(getPlayerName(test,208, 654, 320, 50))
#54 pixels the height of each box




#image = cv2.imread(cgs,1)
#image1= cv2.imread(fName[12],0) #,cv2.IMREAD_GRAYSCALE
#retval, image =cv2.threshold(image1, 50 ,255 ,cv2.THRESH_BINARY)
#breakValue= True

#while breakValue:



#Coords to get map name.
#x, y, w, h = 200, 18, 125, 50

#rounds won top
#x, y, w, h = 1000, 140, 40, 50

#rounds won bottom if G convert to 6
#x, y, w, h = 990, 485, 40, 50

#zoom in on top team name
#x, y, w, h = 120, 260, 320, 31

#zoom in on top team score
#x, y, w, h = 520, 260, 500, 31

#zoom in on top team player 2
#x, y, w, h = 120, 300, 882, 31

#zoom in on top team player 3
#x, y, w, h = 120, 340, 882, 31


#zoom in on bottom team player 1 name only
#x, y, w, h = 120, 610, 320, 31

#zoom in on bottom team player 1 stats only
#x, y, w, h = 520, 610, 500, 31

#zoom in on bottom team player 5 name only
#x, y, w, h = 120, 755, 320, 31

#zoom in on bottom team player 6 name only
#x, y, w, h = 120, 786, 320, 31

#zoom in on top team player numbers
#x, y, w, h = 188, 260, 31, 31

#rounds won bottom for 5 players for only image 9
#x, y, w, h = 990, 485, 40, 50
#rounds won bottom for 4 players
#x, y, w, h = 1450, 660, 40, 60
#rounds won bottom for 5 players
#x, y, w, h = 1450, 710, 40, 60
#rounds won bottom for 6 players
#x, y, w, h = 1450, 760, 40, 55




#cropped_region = image[y:y+h, x:x+w]

#allLettersNums = r'--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789[]#'
#numbersOnly = r'--psm 6 -c tessedit_char_whitelist=0123456'
#text = pytesseract.image_to_string(cropped_region,lang= 'Hitmarker', config= numbersOnly)

#print(text)
#with open('test11.2.txt','a') as file:
    #file.write(fName[11])
    #file.write('\n')
    #file.write(text)


#test = pytesseract.image_to_boxes(image)
#print(test)

#cv2.imshow('imgage',cropped_region)
#cv2.waitKey(0)


#So get darkness of image 0.8924822711150928 0.8553478115638616 first number is for lobby scoreboard second is for dark map scoreboard.
#lobbySB = []
# This gives us the 9 lobby scoreboards
#with open('readFiles.txt','a') as file:
    
    #for fimg in fName:
        #tmpFileName = fimg
        #tmpDark = calculate_darkness(tmpFileName)
        #if tmpDark > 0.875:
            #lobbySB.append(fimg)
            #if fimg not in readFiles:
                #file.write(fimg)
                #file.write('\n')
            

# We might use above code.



# #img = cv2.imread('Codscoreboards/Screenshot 2024-07-08 1.png', 1)

# Specify the folder path and the output text file path
#folder_path = 'Codscoreboards'
#output_file_path = 'fileList.txt'

# List all files in the folder
#file_names = os.listdir(folder_path)
#print(len(file_names))
#currently 146 images
# We are going to write a number to a file indcated how many files we have scanned
# And then we will check that file and start from that number.
#  index = names.index(search_name)
#with open(output_file_path, 'w') as file:
    #for name in file_names:
        #file.write(name + '\n')