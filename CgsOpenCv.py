from PIL import Image
import cv2
import pytesseract
import os
import json
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Tried google vision OCR did not work. 
#from google.cloud import vision

# Set the environment variable for authentication
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Mota\Desktop\Code\CODGODSTATS\CODGODSTATS\gv\sapient-notch-453122-d0-b20d6fe66a01.json'
#db = client['sample_mflix']
#stats = db['users']
#print(stats[0])
#print(stats.find_one({"name":"Varys"}))
#document = {"name": "John", "age": 30, "city": "New York"}

#stats.update_one({"name": "Bob"}, {"$set": {"email": "bob@bob.bob"}})

#if not stats.find_one({'name':'Jas'}):
    #stats.insert_one({'name':'Jas'})

#if not stats.find_one({'name':'Ram'}):
    #stats.insert_one({'name':'Ram'})
#stats.insert_one({'name':'Jas'})
#stats.insert_one({'name':'Ram'})

#We are going to get off clan tags and everything after # then call this to get the value and put that in it.
nameDict = {"[BRATIGunna": "Gunna", "UnbanSniper": "Faker","Poggers": "Faker", "[dSIFaker": "Faker","Faker": "Faker","Gunna": "Gunna","barter6": "barter6","Walt": "Walt","McGangBanger": "Jag","mayo": "Mayo","BuuhDeshh": "BuuhDeshh","4PocketsFull": "4PocketsFull","Sarpanch": "Sarpanch","TwitchItsWhips": "Aceous","Woo": "Woo","LastAirbender": "LastAirbender","GonnaGetGot": "GonnaGetGot","Aceous": "Aceous"}

def calculate_darkness(image_path):
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')

    # Get pixel values and convert them to a list
    pixel_values = list(image.getdata())

    # Calculate the average pixel value
    average_brightness = sum(pixel_values) / len(pixel_values)

    # Calculate darkness (normalized to a range of 0 to 1)
    darkness = 1 - (average_brightness / 255)

    return darkness

def getMapName(image_path):
    #Coords to get map name.
    x, y, w, h = 290, 45, 125, 45

    image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
    retval, image =cv2.threshold(image1, 150 ,255 ,cv2.THRESH_BINARY)

    croppedImage = image[y:y+h, x:x+w]
    allLettersAnd6 = r'--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ6'

    text = pytesseract.image_to_string(croppedImage,lang= 'Hitmarker', config= allLettersAnd6)
    #cv2.imshow('imgage',croppedImage)
    #cv2.waitKey(0)
    return text

def getTopTeamScore(image_path):
    #Coords to get map name.
    x, y, w, h = 1458, 210, 40, 60

    image1= cv2.imread(image_path,1) #,cv2.IMREAD_GRAYSCALE
    retval, image1 =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

    croppedImage = image1[y:y+h, x:x+w]
    numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

    text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)
    cv2.imshow('imgage',croppedImage)
    cv2.waitKey(0)

    return text

def getBottomTeamScore(image_path):
    
    text =""
    playerNum = getPlayerNumbers(image_path)
    if playerNum == 4:
        x, y, w, h = 1465, 660, 40, 60

        image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
        retval, image =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

        text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)

    elif playerNum == 5:
        x, y, w, h = 1450, 710, 40, 60

        image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
        retval, image =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

        text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)


    if playerNum == 6:
        x, y, w, h = 1450, 764, 55, 55

        image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
        retval, image =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

        text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)

    if text =="" and playerNum == 4:
        x, y, w, h = 1450, 710, 40, 60

        image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
        retval, image =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

        text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)

    if text =="" and playerNum == 5:
        x, y, w, h = 1450, 764, 55, 55

        image1= cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
        retval, image =cv2.threshold(image1, 125 ,255 ,cv2.THRESH_BINARY)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=0123456'

        text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)
    #cv2.imshow('imgage',croppedImage)
    #cv2.waitKey(0)
    return text

def getPlayerNumbers(image_path):
    x, y, w, h = 75, 258, 260, 35

    image= cv2.imread(image_path,1)

    croppedImage = image[y:y+h, x:x+w]
    numConfig = r'--psm 6 -c tessedit_char_whitelist=345678'

    tmpPNum = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)
    #cv2.imshow('imgage',croppedImage)
    #cv2.waitKey(0)

    my_int = int(tmpPNum[0])


    return my_int

# 813 =6 760 = 5 707 =4 
def getBottomPlayerNumbers(image_path):
    topPlayers = getPlayerNumbers(image_path)
    if topPlayers == 4:
        y = 706
    if topPlayers == 5:
        y = 759
    if topPlayers == 6:
        y = 812

    x, w, h = 75, 260, 35

    image= cv2.imread(image_path,1)

    croppedImage = image[y:y+h, x:x+w]
    numConfig = r'--psm 6 -c tessedit_char_whitelist=345678'

    tmpPNum = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)

    if tmpPNum =="":
        y += 52
        image= cv2.imread(image_path,1)

        croppedImage = image[y:y+h, x:x+w]
        numConfig = r'--psm 6 -c tessedit_char_whitelist=345678'

        tmpPNum = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= numConfig)
        #cv2.imshow('imgage',croppedImage)
    my_int = int(tmpPNum[0])


    return my_int


def getPlayerName(image_path,x,y,w,h):

    image= cv2.imread(image_path,1)

    croppedImage = image[y:y+h, x:x+w]
    nameConfig = r'--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789[]#'

    text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= nameConfig)
   
    #print(text)
    scrap2 = text.split('#')[0].strip()
    scrap2 = re.sub(r'\[.*?\]', '', scrap2)
    #print(scrap2)
    #cv2.imshow('imgage',croppedImage)
    #cv2.waitKey(0)
    return text

def getPlayerStats(image_path,x,y,w,h):

    image1 = cv2.imread(image_path,0) #,cv2.IMREAD_GRAYSCALE
    retval, image =cv2.threshold(image1, 114 ,255 ,cv2.THRESH_BINARY)

    croppedImage = image[y:y+h, x:x+w]
    #croppedImage = cv2.bitwise_not(croppedImage)
    statsConfig = r'--psm 6 -c tessedit_char_whitelist=0123456789'
    
    text = pytesseract.image_to_string(croppedImage,lang= 'HitmarkerCL', config= statsConfig)
    #print(text)
    #invertedImage = cv2.bitwise_not(croppedImage)
    #cv2.imshow('imgage',invertedImage)
    #cv2.waitKey(0)

    #_, buffer = cv2.imencode('.png', invertedImage)
    #croppedImageBytes = buffer.tobytes()
    
    #client = vision.ImageAnnotatorClient()

    #image = vision.Image(content=croppedImageBytes)

    #response = client.text_detection(image=image)
    #texts = response.text_annotations
    #print(texts[0].description.strip())
    #numbersOnly = re.sub(r'\D', '', texts[0].description.strip())
    #print(numbersOnly)

    return text

def generateMapData(image_path,team1,team2):
    #team1 = getTopTeamScore(image_path)
    #team2 = getBottomTeamScore(image_path)
    #print(team1,team2)
    try:
        mapname = getMapName(image_path)
    except Exception as e:
        mapname =" "

    if team1 > team2:
        tmp = "team1"
    else:
        tmp = "team2"
    return {
        "number": getMapNumber(image_path),
        "map": mapname[:-1],
        "team_1_captain": "",
        "team_2_captain":  "",
        "team_1_rounds_won": team1,
        "team_2_rounds_won": team2,
        "winner": tmp,
        "date": image_path[26:36],
        "time": image_path[37:43],
        "players": []
    }

def getMapNumber(image_path):
    folder_path = 'Codscoreboards'
    file_names = os.listdir(folder_path)
    index = file_names.index(image_path[15:])
    return index+1

def addPlayers(map_data, players):
    if 'players' in map_data:
        map_data['players'].append(players)
    else:
        print("hello")
        map_data['players'] = players

    return map_data

# Create function that makes a list, name, score, kills, plants, defuses, deaths.
# Then pass that list to this function
def createPlayerList(image_path,x,y,w,h,x2,y2,w2,h2):
    tmp = getPlayerName(image_path,x,y,w,h)
    name = tmp.split('#')[0].strip()
    name = re.sub(r'\[.*?\]', '', name)
    name = nameDict.get(name)
    playerList = []
    playerList.append(name)
    tmp = getPlayerStats(image_path,x2,y2,w2,h2)
    stats= tmp.split()
    playerList.append(stats)

    return playerList



def createPlayer(imagePath,playerList,team,team1,team2):
    stats= [int(item) for item in playerList[1]]

    if len(stats)> 4:
        deaths = stats[4]
    else:
        deaths = "error"
    if len(stats)> 3:
        defuses = stats[3]
    else:
        defuses = 0

    if len(stats)> 2:
        plants = stats[2]
    else:
        plants = 0

    if len(stats)> 1:
        kills = stats[1]
    else:
        kills = "error"

    if len(stats)> 0:
        score = stats[0]
    else:
        score = "error"
    
    if team == "team1":
        roundsW = team1
        roundsL = team2
    if team == "team2":
        roundsL = team1
        roundsW = team2

    if plants == 4 and defuses == 4:
        plants = 0
        defuses = 0

    if defuses == 4:
        defuses = 0

    player = {
            "name": playerList[0],
            "team": team,
            "stats": {
                "score": score,
                "kills": kills,
                "plants": plants,
                "defuses": defuses,
                "deaths": deaths,
                "rounds_won": roundsW,
                "rounds_lost": roundsL,
            }
        }

    return player