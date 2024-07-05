from Listening_Functions import Listen_English
from Listening_Functions import Listen_Hindi
from Speaking_Functions import Speak_Os

from datetime import datetime
from pyautogui import click
from time import sleep
from PIL import Image
import pyaudio
import struct
import math
import pyttsx3
import os
import smtplib
import pywhatkit
import psutil
import pyautogui
from bs4 import BeautifulSoup
from pypdf import PdfReader
from keyboard import press 
from keyboard import press_and_release
from plyer import notification
from keyboard import write
import webbrowser
from requests import get
import pyautogui
import speedtest
from googletrans import Translator
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import webbrowser
import geocoder
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from time import sleep
import json
import wolframalpha



def Firstwish():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        Speak_Os("Good Morning Sir!")
    elif hour>=12 and hour<18:
        Speak_Os("Good Afternoon Sir!")
    else:
        Speak_Os("Good Evening Sir!")
    Speak_Os("Your AI Assistant EMILLY will be ready shortly!")
    Speak_Os("You can click the Mic Icon to proceed and the Close Icon to return back!")

def openWebsite():
    Speak_Os("which website you want to be redirected?")
    websiteName = Listen_English()
    Speak_Os(f"redirecting you to {websiteName}")
    if 'youtube' in websiteName:
        open("m.youtube.com")
    elif 'chrome' in websiteName:
        open("https:\\www.google.com\\")
    elif 'stack overflow' in websiteName: 
        open("stackoverflow.com")
    elif 'university portal' in websiteName:
        vtop = "https:\\vtop.vitbhopal.ac.in\\vtop\\initialProcess"
        open(vtop)

def Lights_Automation():
    Speak_Os("Activating Smart Lights")
    Speak_Os("Now please mention the command")
    Home_control = Listen_English()
    if "turn on" in Home_control :
        click(x=747, y=1046)
        sleep(1)
        click(x=1369, y=198)
        sleep(1)                        
    elif "turn off" in Home_control :
        click(x=1369, y=198)
        sleep(1)
    elif "increase brightness" in Home_control:
        click(x=1167, y=206)
        sleep(7)
        click(x=1374, y=546)
        sleep(1)
    elif "decrease brightness" in Home_control:
        click(x=991, y=550)
        sleep(1)
    elif "red" in Home_control:
        click(x=1193, y=127)
        sleep(1)
        click(x=1252, y=452)
        sleep(1)      
    elif "yellow" in Home_control:
        click(x=1229, y=387)
        sleep(1)
    elif "green" in Home_control:
        click(x=1147, y=380)
        sleep(1)
    elif "blue" in Home_control:
        click(x=1134, y=483)
        sleep(1)
    elif "pink" in Home_control:
        click(x=1203, y=508)
        sleep(1)

def SpaceNews(Date):
    Api_Key = "D14SM3N1gRBGuMVhROsEskgbVWvwwp1YtfBbC5W7"
    Speak_Os("Gathering news for the given dates.")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Parameters = {'date':str(Date)}
    r = get(Url,params = Parameters)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    Path_1 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\" + str(FileName)
    img = Image.open(Path_1)
    img.show()
    Speak_Os(f"Title : {Title}")
    Speak_Os(f"According To Nasa : {Info}")

def MarsImage():
    Api_Key = "D14SM3N1gRBGuMVhROsEskgbVWvwwp1YtfBbC5W7"
    name = 'curiosity' 
    Speak_Os("enter the date for capture:")
    date = str(input("enter the date-:20xx-12-31\n"))
    Api_ = str(Api_Key)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"
    r = get(url)
    Data = r.json()
    Photos = Data['photos'][:1]
    try:
        for index , photo in enumerate(Photos):
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_of_photo = photo['earth_date']
            img_url = photo['img_src']
        p = get(img_url)
        img = f'{index}.jpg'
        with open(img,'wb') as f:
            f.write(p.content)
        Path_1 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\" + str(img)
        img = Image.open(Path_1)
        img.show()
        Speak_Os(f"These Images are extracted from: {full_camera_name} on: {date_of_photo}.")
    except:
        Speak_Os("Sorry Unable to extract images at the moment!")

def ISS_Tracker():
    Speak_Os("Tracking international space station.")
    url = "http://api.open-notify.org/iss-now.json"
    r = get(url)
    Data = r.json()
    dt = Data['timestamp']
    lat = Data['iss_position']['latitude']
    lon = Data['iss_position']['longitude']
    Speak_Os("International space station tracked here are its cordinates.")
    Speak_Os(f"At passwordInput Date-Time: {dt}")
    Speak_Os(f"Latitude was: {lat}")
    Speak_Os(f"Longitude was: {lon}")

def SpaceObjects(start_date,end_date):
    Api_Key = "D14SM3N1gRBGuMVhROsEskgbVWvwwp1YtfBbC5W7"
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    Speak_Os(f"Total Objects discovered Between {start_date} and {end_date} Is : {Total_Astro}")
    Speak_Os("Extacted Data For Those objects Are Listed Below.") 
    for body in neo[start_date]: 
        id = body['id']
        name = body['name']
        absolute = body['absolute_magnitude_h']
        print(id,name,absolute)

def SorlarBodies(body):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/"
    r = get(url)
    Data = r.json()
    bodies = Data['bodies']
    Number = len(bodies)
    Speak_Os(f"{body} is among {Number} Solar objects.")
    url2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
    rrr = get(url2)
    Data2 = rrr.json()
    mass = Data2['mass']['massValue']
    volume = Data2['vol']['volValue']    
    density = Data2['density']
    gravity = Data2['gravity']
    escape = Data2['escape']
    Speak_Os(f"The Physical data for {body}  is as follows:")
    Speak_Os(f"mass of {body} is {mass} sextillion tonnes.")
    Speak_Os(f"Volume of {body} is {volume} trillion cubic kilometers.")
    Speak_Os(f"Body density of {body} is {density} gram per centimeter cube.")
    Speak_Os(f"Gravitational force of {body} is {gravity} meters per second squared.")
    Speak_Os(f"Escape velocity of {body} is {escape} meters per second.")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('clashaniket321@gmail.com', 'uwoycsnhtujtzjme')
    server.sendmail("clasaniket321@gmail.com", to, content)
    server.close()      
    Speak_Os("your email sent to the recipient.")

def whatsApp_Automation():
    Speak_Os("whatsapp automated.")
    Speak_Os("Please mention the command.")
    command = Listen_English()
    if 'message rohit' in command:
        Speak_Os("please dictate the message to be sent.")
        whatsApp_message = Listen_English()
        print(whatsApp_message)
        Speak_Os("Please tell time in hours.")
        hour = int(input())
        Speak_Os("Please tell time in minutes.")
        min = int(input())
        pywhatkit.sendwhatmsg("+919101012700",whatsApp_message,hour,min,10)
        Speak_Os("Your message has been sent!")
    elif 'message shubham' in command:
        Speak_Os("please dictate the message to be sent.")
        whatsApp_message = Listen_English()
        print(whatsApp_message)
        Speak_Os("Please tell time in hours.")
        hour = int(input())
        Speak_Os("Please tell time in minutes.")
        min = int(input())
        pywhatkit.sendwhatmsg("+919461996705",whatsApp_message,hour,min,10)
        Speak_Os("Your message has been sent!")
    elif 'message multiple contact' in command:
        Speak_Os("please dictate the message to be sent.")
        whatsApp_message = Listen_English()
        print(whatsApp_message)
        open_chat =  "https://web.whatsapp.com/send?photo=" + "&text=" + whatsApp_message
        open(open_chat)
    elif "message with number" in command:
        Speak_Os("Please input whatsapp number of the recipient.")
        whatsApp_number = input("enter recipient number:-\n")
        Speak_Os("please dictate the message to be sent.")
        whatsApp_message = Listen_English()
        Speak_Os("Please tell time in hours.")
        hour = int(input())
        Speak_Os("Please tell time in minutes.")
        min = int(input())
        pywhatkit.sendwhatmsg(whatsApp_number,whatsApp_message,hour,min,10)
        Speak_Os("Your message has been sent pls save this contact for future refernce!")
    elif "whatsapp call" in command:
        click(x=807, y=1044)
        sleep(1)
        Speak_Os("please mention the contact")
        contact = Listen_English()
        write(contact)
        sleep(1)
        click(x=941, y=265)
        sleep(1)
        click(x=1706, y=96)
    elif "new whatsapp message" in command:
        click(x=807, y=1044)
        sleep(1)
        Speak_Os("please mention the contact")
        contact = Listen_English()
        write(contact)
        sleep(1)
        click(x=865, y=238)
        sleep(1)
        click(x=1391, y=980)
        sleep(1)
        Speak_Os("dictate the message to be sent")
        message = Listen_English()
        write(message)
        sleep(1)
        click(x=1866, y=974)
    elif "open chat" in command:
        click(x=807, y=1044)
        sleep(1)
        Speak_Os("please mention the contact")
        contact = Listen_English()
        write(contact)
        sleep(1)
        click(x=875, y=243)
        Speak_Os("your chat is opened")
    elif "voice message" in command:
        click(x=807, y=1044)
        sleep(1)
        Speak_Os("please mention the contact")
        contact = Listen_English()
        write(contact)
        sleep(1)
        click(x=865, y=238)
        sleep(1)
        click(x=1391, y=980)
        sleep(1)
        click(x=1867, y=980)
        sleep(7)
        click(x=1867, y=980)
        sleep(1)
        Speak_Os("your voice message has been sent")

def OpenApps():
    Speak_Os("which app would you like to use?")    
    appName = Listen_English()
    Speak_Os("Ok Sir , Wait A Second!")
    if 'code' in appName:
        os.startfile("C:\\Users\\anike\\OneDrive\\Desktop\\Visual Studio Code.lnk")
    elif 'microsoft teams' in appName:
        os.startfile("C:\\Users\\anike\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk")
    elif 'hill climb racing' in appName:
        os.startfile("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\Hill Climb Racing.lnk")
    Speak_Os("Your application has Been opened Sir!")

def Temperature():
    search = "temperature in noida"
    url = f"https://www.google.com/search?q={search}"
    r = get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    Speak_Os(f"The Temperature Outside Is {temperature} ")
    Speak_Os("Do I Have To Tell You Another Place Temperature ?")
    next = Listen_English()
    if 'yes tell' in next:
        Speak_Os("Tell Me The Name Of tHE Place.")
        name = Listen_English()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak_Os(f"The Temperature in {name} is {temperature} ")
    else:
        Speak_Os("no problem sir.")

def Notepad():
    Speak_Os("Ok. Dictate Me The Notes.")
    time = datetime.now().strftime("%H:%M")
    filename = str(time).replace(":","-") + "-note.txt"
    writes = Listen_English()
    with open(filename,"w") as f:
        f.write(writes)
    path_1 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\" + str(filename)
    os.startfile(path_1)

def CSE3006_Computer_Networks_BL2022235000368():
    Link_Monday_C11 = "https://teams.microsoft.com/l/meetup-join/19%3aqBIzXJMv524o8ihxQk6CyMNojpwPxOQ6vKPdA076PiM1%40thread.tacv2/1666342232893?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%226b708ec4-68bc-46f0-bec4-e863a78b7b97%22%7d"
    Link_wenesday_C12  = "https://teams.microsoft.com/l/meetup-join/19%3aqBIzXJMv524o8ihxQk6CyMNojpwPxOQ6vKPdA076PiM1%40thread.tacv2/1666342298423?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%226b708ec4-68bc-46f0-bec4-e863a78b7b97%22%7d"
    Link_Friday_C13 = "https://teams.microsoft.com/l/meetup-join/19%3aqBIzXJMv524o8ihxQk6CyMNojpwPxOQ6vKPdA076PiM1%40thread.tacv2/1666342344057?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%226b708ec4-68bc-46f0-bec4-e863a78b7b97%22%7d"
    Speak_Os("please tell the meeting slot.")
    slot = Listen_English()
    Speak_Os("joining the class")
    if "monday" in slot:
        webbrowser.open(Link_Monday_C11)
        sleep(2)
        click(x=1072, y=277)
        sleep(2)
        click(x=1488, y=749)
    elif "wenesday" in slot:
        webbrowser.open(Link_wenesday_C12)
        sleep(2)
        click(x=1072, y=277)
        sleep(2)
        click(x=1488, y=749)
    elif "friday" in slot:
        webbrowser.open(Link_Friday_C13)
        sleep(2)
        click(x=1072, y=277)
        sleep(2)
        click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def  E21_E22_E23_DS_AA_Winter2023():
    Speak_Os("joining the class")
    Link = "https://teams.microsoft.com/l/meetup-join/19%3a_04xDmcNbtLLiYpmLXDBjLAqZC_jc2HhGlboBQ9xgyU1%40thread.tacv2/1667300711366?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%22b0336b43-b463-4124-b072-ea5257b64cfb%22%7d"
    webbrowser.open(Link)
    sleep(2)
    click(x=1072, y=277)
    sleep(2)
    click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def B21_B22_B23_MAT3003_ProbabilityStatisticsAndReliability_DrBHUMIKACHOKSI():
    Link_Thursday = "https://teams.microsoft.com/l/meetup-join/19%3a22p1-YfrfZyxHE_BDBlAMdhMRMjcbqQe7gzWT-RM-wI1%40thread.tacv2/1670491357653?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%225a368410-6d67-4669-ad17-a0fcdd3c6634%22%7d"
    Link_Mon_Wed = "https://teams.microsoft.com/l/meetup-join/19%3a22p1-YfrfZyxHE_BDBlAMdhMRMjcbqQe7gzWT-RM-wI1%40thread.tacv2/1667194253316?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%225a368410-6d67-4669-ad17-a0fcdd3c6634%22%7d"
    Speak_Os("please tell the meeting slot.")
    slot = Listen_English()
    Speak_Os("joining the class")
    if "monday" in slot:
        webbrowser.open(Link_Mon_Wed)
        sleep(2)
        click(x=1072, y=277)
        sleep(2)
        click(x=1488, y=749)
    elif "thursday" in slot:
        webbrowser.open(Link_Thursday)
        sleep(2)
        click(x=1072, y=277)
        sleep(2)
        click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def Computational_Linguistics_F11_F12_CL_2021():
    Speak_Os("joining the class")
    Link = "https://teams.microsoft.com/l/meetup-join/19%3aXn5bMFWW1RC28xUQJ5p5jUuHMg2PRj1ukRRBp3oB-jo1%40thread.tacv2/1667282690035?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%2207272774-4a61-4865-9e9b-62e5bc3f1519%22%7d"
    webbrowser.open(Link)
    sleep(2)
    click(x=1072, y=277)
    sleep(2)
    click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def SensorsAndIOT_B11_B12():
    Speak_Os("joining the class")
    Link = "https://teams.microsoft.com/l/meetup-join/19%3aodYAWvkmSNQcT_PSgsKqRLo368EViK0avauT30v5IEI1%40thread.tacv2/1669175920050?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%22f59bd6ee-db34-4b4f-adb0-83e80fedb0a7%22%7d"
    webbrowser.open(Link)
    sleep(2)
    click(x=1072, y=277)
    sleep(2)
    click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def DSN2099_Project_Exhibition_II():
    Speak_Os("joining the class")
    Link = "https://teams.microsoft.com/l/meetup-join/19%3aT1-_D9vd4Cp4Mi_aDiE-dLEcjsdoyhApUxn8gYRsm1U1%40thread.tacv2/1672119301657?context=%7b%22Tid%22%3a%2209bd1956-edda-4e9a-9543-7c7aa2cf4e81%22%2c%22Oid%22%3a%2237b0f459-ac82-45c2-91f6-8b6211ca1599%22%7d"
    webbrowser.open(Link)
    sleep(2)
    click(x=1072, y=277)
    sleep(2)
    click(x=1488, y=749)
    Speak_Os("your class has been joined you would be soon taken in the room.")

def TextReader():
    Speak_Os("please tell the name of the book you want to hear!")      
    book_name = Listen_English()
    if "new book" in book_name:
        book = open("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\new books.pdf",'rb')
        pdf_reader = PdfReader(book)
        total_pages = len(pdf_reader.pages)
        Speak_Os(f"this book has passwordInput total {total_pages} pages.")
        Speak_Os("please tell from which page you want to hear?")
        numPage = int(input("Enter the page number:-"))
        page = pdf_reader.pages[numPage]
        text = page.extract_text()
        os.startfile("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\NonTaskingPaths\\new books.pdf")
        Speak_Os(text)

def CloseApps():
    Speak_Os("tell the name of the application")
    query = Listen_English()
    Speak_Os("Ok Sir , Wait A second!")
    if 'chrome' in query:
        os.system("TASKKILL /f /im Chrome.exe")
    elif 'code' in query:
        os.system("TASKKILL /F /im code.exe")
    elif 'whatsapp' in query:
        os.system("TASKKILL /f /im whatsapp.exe")
    elif 'spotify' in query:
        os.system("TASKKILL /f /im spotify.exe")
    elif 'notepad' in query:
        os.system("TASKKILL /F /im Notepad.exe")
    Speak_Os("Your application has been closed!")

def TimeTable():
    FiveTo6 = '''
    Good morning sir, its 5:00 Am
    You Have To Get Up starting your day will be Positive.
    you have to be ready before 6:00 am.
    '''
    SixTo9 = '''
    Sir its 6:00 Am 
    You Have To complete your
    assignments before 9:00 Am.
    '''
    NineTo12 = '''
    Sir its 9:00 Am in This Time,
    You Have to complete pending Lectures.
    from 9:00 Am To 12:00 Pm.
    '''
    TwelveTo15 = '''
    TEST ALERT-Sir the daily test is available now
    You Have to complete the presheduled hourly
    test between 12:00 Pm To 3:00 Pm .
    '''
    FifteenTo21 = '''
    Sir its 3:00 Pm In This Time ,
    You Have to do Programming for your undertaken projects.
    you can have rest after 9:00 Pm .
    '''
    TwentyOneTo5 = '''
    Sir its 9:00 pm now you can have rest,
    you can have dinner then Sleep.
    9:00 Pm To 10:00 Pm .
    '''
    hour = int(datetime.now().strftime("%H"))
    if hour>=5 and hour<6:
        Speak_Os(FiveTo6)
    elif hour>=6 and hour<9:
        Speak_Os(SixTo9)
    elif hour>=9 and hour<12:
        Speak_Os(NineTo12)
    elif hour>=12 and hour<15:
        Speak_Os(TwelveTo15)
    elif hour>=15 and hour<21:
        Speak_Os(FifteenTo21)
    elif hour>=21 and hour<5:
        Speak_Os(TwentyOneTo5)

def YoutubeAutomation():
    Speak_Os("youtube automation started what is your Command ?")
    command = Listen_English()
    if 'execute start' in command:
        press('space bar')
    elif 'execute stop' in command:
        press('space bar')
    elif 'execute restart' in command:
        press('0')  
    elif 'execute mute' in command:
        press('m')
    elif 'execute undo mute' in command:
        press('m')
    elif 'execute skip' in command:
        press('l')
    elif 'execute back' in command:
        press('j')
    elif 'execute full screen' in command:
        press('f')
    elif 'execute cinema mode' in command:
        press('t')
    elif 'increase speed' in command:
        press_and_release('SHIFT + .')
    elif 'decrease speed' in command:
        press_and_release('SHIFT + ,')
    elif 'next video' in command:
        press_and_release('SHIFT + n')    
    Speak_Os("Done Sir")

def ChromeAutomation():
    Speak_Os("Chrome Automation started what is your command.")
    command = Listen_English()
    if 'close this tab' in command:
        press_and_release('ctrl + w')
    elif 'open new tab' in command:
        press_and_release('ctrl + t')
    elif 'open new window' in command:
        press_and_release('ctrl + n')
    elif 'show history' in command:
        press_and_release('ctrl + h')
    elif 'download' in command:
        press_and_release('ctrl + j')
    elif 'bookmark' in command:
        press_and_release('ctrl + d')
        press('enter')
    elif 'incognito' in command:
        press_and_release('Ctrl + Shift + n')
    elif 'switch tab' in command:
        tab = command.replace("switch tab ", "")
        Tab = tab.replace("to","")    
        num = Tab
        bb = f'ctrl + {num}'
        press_and_release(bb)
    elif 'open' in command:
        name = command.replace("open ","")
        NameA = str(name)
        if 'youtube' in NameA:
            webbrowser.open("https://www.youtube.com/")
        elif 'instagram' in NameA:
            webbrowser.open("https://www.instagram.com/")
        else:
            string = "https://www." + NameA + ".com"
            string_2 = string.replace(" ","")
            webbrowser.open(string_2)

def CoronaVirus(Country):
    countries = str(Country).replace(" ","")
    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result = get(url)
    soups = BeautifulSoup(result.text)
    corona = soups.find_all('div',class_ = 'maincounter-number')
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases , Death , recovored = Data
    Speak_Os(f"Total Cases reported in {Country} till date are : {cases}")
    Speak_Os(f"Unfortunate deaths reported in {Country} till date are : {Death}")
    Speak_Os(f"Recovered patients in {Country} till date are : {recovored}")  

def screenshot():
    Speak_Os("Ok input the file name to save the screenshot.")
    path = input("enter file name: \n")
    path1name = path + ".png"
    path1 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\ScreenShots\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile(path1)
    Speak_Os("your screenshot has been saved in ScreenShots folder in C drive you can now access it.")

def WindowsAutomation():
    Speak_Os("windows automation started please tell the command")
    Wquery = Listen_English()
    if 'home screen' in Wquery:
        press_and_release('windows + m')
    elif 'minimize' in Wquery:
        press_and_release('windows + m')
    elif 'show start' in Wquery:
        press('windows')
    elif 'open setting' in Wquery:
        press_and_release('windows + i')
    elif 'open search' in Wquery:
        press_and_release('windows + s')
    elif 'screen shot' in Wquery:
        press_and_release('windows + SHIFT + s')
    elif 'restore windows' in  Wquery:
        press_and_release('Windows + Shift + M')
    else:
        Speak_Os("Sorry , No Command has been Found!")

def InternetSpeed():
    Speak_Os("what type of speed you want to know")
    testType = Listen_English()
    Speak_Os("checking speed")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correct_downloading = int(downloading/800000)
    uploading = speed.upload()
    correct_uploading = int(uploading/800000)
    if "downloading" in testType:
        Speak_Os(f"the downloading speed is {correct_downloading} MBP S")
    elif "uploading" in testType:
        Speak_Os(f"the uploading speed is {correct_uploading} MBP S")
    elif "both" in testType:
        Speak_Os(f"the downloading speed is {correct_downloading} MBP S")
        Speak_Os(f"the uploading speed is {correct_uploading} MBP S")

def Fridge_Automation():
    Speak_Os("Activating Home Automation")
    Speak_Os("enter the command")
    Home_control = Listen_English()
    if "increase temperature of fridge" in Home_control :
        click(x=765, y=1068)
        sleep(1)
        click(x=604, y=548)
        sleep(1)
        click(x=1583, y=373)
        sleep(1)
        click(x=1177, y=619)
        sleep(1)
        click(x=1417, y=786)
        sleep(1)
        click(x=1414, y=491)
    elif "increase temperature of freezer" in Home_control :
        click(x=765, y=1068)
        sleep(1)
        click(x=604, y=548)
        sleep(1)
        click(x=1619, y=504)
        sleep(1)
        click(x=1178, y=601)
        sleep(1)
        click(x=1417, y=786)
        sleep(1)
        click(x=1414, y=491)
    if "decrease temperature of fridge" in Home_control :
        click(x=765, y=1068)
        sleep(1)
        click(x=604, y=548)
        sleep(1)
        click(x=1583, y=373)
        sleep(1)
        click(x=1178, y=714)
        sleep(1)
        click(x=1417, y=786)
        sleep(1)
        click(x=1414, y=491)
    elif "decrease temperature of freezer" in Home_control :
        click(x=765, y=1068)
        sleep(1)
        click(x=604, y=548)
        sleep(1)
        click(x=1619, y=504)
        sleep(1)
        click(x=1178, y=714)
        sleep(1)
        click(x=1417, y=786)
        sleep(1)
        click(x=1414, y=491)
    Speak_Os("your command has been completed.")

def TransLater():
    Speak_Os("tell me the line to translate.")
    line = Listen_Hindi()
    translated_Line = Translator()
    result = translated_Line.translate(line)
    Text = result.text
    Speak_Os(f"The tanslated line is {Text}")

def YoutubeVideoDownloader():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")
    Speak_Os("Please imput the Video Url Here!")
    Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
    link = StringVar()
    Label(root,text = "Input youtube video URL here-:",font = 'arial 15 bold').place(x=160,y=60)
    Entry(root,width = 70,textvariable = link).place(x=32,y=90)
    def VideoDownloader():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)
    Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)
    root.mainloop()
    Speak_Os("Downloaded the youtube video.")

def My_Location():
    Speak_Os("cheaking your location through ip address")
    ip_add = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    home = "https://www.google.co.in/maps/place/Noida,+Uttar+Pradesh/@28.52213,77.2617397,11z/data=!3m1!4b1!4m5!3m4!1s0x390ce5a43173357b:0x37ffce30c87cc03f!8m2!3d28.5355161!4d77.3910265?hl=en"
    webbrowser.open(home)
    Speak_Os(f"Sir, you are currently in {state, country}.")

def PlaceLocator():
    Speak_Os("enter the name of the place:")
    Place = input("enter the name of the place-:\n")
    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place , addressdetails= True)
    target_latlon = location.latitude , location.longitude
    webbrowser.open(url=Url_Place)
    location = location.raw['address']
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}
    current_location = geocoder.ip('me')
    current_Location = current_location.latlng
    distance = str(great_circle(current_Location,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    Speak_Os(target)
    Speak_Os(f"Sir, {Place} is {distance} Kilometre Away From Your Location.")

def HiddenFiles():
    manage = Listen_English()
    if "hide folder" in manage:
        os.system("attrib +h /s /d")
        Speak_Os("your folder has been hidden.")
    elif "show folder" in manage:
        os.system("attrib -h /s /d")
        Speak_Os("your folder is visible now.")

def Battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    Speak_Os(f"The system battery is at {percentage} percentage.")

def Volume(query):
    if "increase" in query:
        pyautogui.press("volumeup")
    elif "decrease" in query:
        pyautogui.press("volumedown")
    elif "mute audio" in query:
        pyautogui.press("volumemute")
    Speak_Os("volume adjusted.")

def NewsHeadlines():
    business = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    entertainment = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    health = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    science = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    sports = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    technology = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    # india = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    usa = "https://newsapi.org/v2/top-headlines?country=us&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    china = "https://newsapi.org/v2/top-headlines?country=cn&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    russia = "https://newsapi.org/v2/top-headlines?country=ru&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    apple = "https://newsapi.org/v2/everything?q=apple&from=2023-02-08&to=2023-02-08&sortBy=popularity&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    tesla = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-09&sortBy=publishedAt&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    wallStreet = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f3f9e2767a6c42be9b50c49316c5a1bd"
    busigness_news = get(business).text
    entertainment_news = get(entertainment).text
    health_news = get(health).text
    science_news = get(science).text
    sports_news = get(sports).text
    tech_news = get(technology).text
    # indian_news = get(india).text
    usa_news = get(usa).text
    russia_news = get(russia).text
    china_news = get(china).text
    apple_news = get(apple).text
    tesla_news = get(tesla).text
    wallstreet_news = get(wallStreet).text
    news1 = json.loads(busigness_news )
    news2 = json.loads(entertainment_news)
    news3 = json.loads(health_news)
    news4 = json.loads(science_news)
    news5 = json.loads(sports_news)
    news6 = json.loads(tech_news)
    # news7 = json.loads(indian_news)
    news8 = json.loads(usa_news)
    news9 = json.loads(russia_news)
    news10 = json.loads(china_news)
    news11= json.loads(apple_news)
    news12 = json.loads(tesla_news)
    news13 = json.loads(wallstreet_news)
    art1 = news1["articles"]
    art2 = news2["articles"]
    art3 = news3["articles"]
    art4 = news4["articles"]
    art5 = news5["articles"]
    art6 = news6["articles"]   
    # art7 = news7["articles"]   
    art8 = news8["articles"]  
    art9 = news9["articles"]    
    art10 = news10["articles"]   
    art11 = news11["articles"]    
    art12 = news12["articles"]
    art13 = news13["articles"]
    Speak_Os("The top trending news Headlines for the week are as follows:")
    for articles in art1:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art2:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art3:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art4:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art5:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art6:
        article = articles["title"]
        Speak_Os(article)
        break
    # for articles in art7:
    #     article = articles["title"]
    #     Speak_Os(article)
    #     break
    for articles in art8:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art9:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art10:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art11:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art12:
        article = articles["title"]
        Speak_Os(article)
        break
    for articles in art13:
        article = articles["title"]
        Speak_Os(article)
        break

def WolfRamAlpha(query):
    apikey = "LYL87K-2YWTXY2KJ7"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        Speak_Os("Sorry unable to calculte expression at the moment.")

def Calculator(query):
    mathematical_expression = str(query)
    mathematical_expression = mathematical_expression.replace("into","*")
    mathematical_expression = mathematical_expression.replace("plus","+")
    mathematical_expression = mathematical_expression.replace("minus","-")
    mathematical_expression = mathematical_expression.replace("divided by","/")
    Final = str(mathematical_expression)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        Speak_Os(result)
    except:
        Speak_Os("Sorry unable to calculte expression at the moment.")

def Terminator():
    Speak_Os("Are You sure you want to shutdown the system. Input the security Hotward to terminate the entire system.")
    shutdown = input("Input Hotward 'Santa Claus'.")
    if shutdown == 'Santa Claus':
        os.system("shutdown /s /t 1")
    else:
        Speak_Os("security Hotward to terminate system not detected.")

is_running = False
INITIAL_TAP_THRESHOLD = 0.25
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME
def get_rms(block):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack(format, block)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    return math.sqrt(sum_squares/count)



class ClapDetecter(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0
    def stop(self):
        self.stream.close()
    def find_input_device(self):
        device_index = None            
        for i in range(self.pa.get_device_count()):     
            devinfo = self.pa.get_device_info_by_index(i)
            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    device_index = i
                    return device_index
        if device_index == None:
            print( "No preferred input found; using default input device." )
        return device_index
    def open_mic_stream(self):
        device_index = self.find_input_device()
        stream = self.pa.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, input_device_index = device_index, frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream
    def listen(self):  
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError as e:
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return
        amplitude = get_rms(block)       
        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                self.tap_threshold *= 1.1
        else:            
            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return "True-Mic"
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                self.tap_threshold *= 2



def startDetection():
    detect  = ClapDetecter()
    while True:
        hearClap = detect.listen()
        if "True-Mic" == hearClap:
            Speak_Os("Initializing the AI Assistant!")
            break

def exitDetection():
    detect  = ClapDetecter()
    while True:
        hearClap = detect.listen()
        if "True-Mic" == hearClap:
            Speak_Os("Goodbye Sir it was nice helping You!")
            break

def Start_AI():
    while 1:
        global is_running
        if not is_running:
            startDetection()
            sleep(1)
            Speak_Os("Welcome back again sir I am ready to help you!")
            is_running = True
        if is_running:
            exitDetection()
            sleep(1)
            Speak_Os("Terminated the AI Assistant!")
            is_running = False

def TaskExecutionSample():
    global is_running
    while is_running == True :
        query = Listen_English()
        if "hello" in query:
            Speak_Os("Hello Sir! This is your AI Assistant EMILLY!")
            Speak_Os("How can I help you")
        elif "goodbye" in query:
            Speak_Os("Goodbye sir, it was nice to help you!")
        elif "password" in query:
            Speak_Os("Disabled the AI Assistant!")
            is_running = False
        else:
            pass

def Start_AI_Password():
    Speak_Os("Password Detection Activated")
    global is_running
    while is_running == False:
        if not is_running:
            query = Listen_English()
            if "password" in query:
                Speak_Os("Welcome back again sir I am ready to help you!")
                is_running = True         
                TaskExecutionSample()
            else:
                Speak_Os("enter the correct password.")

def Password():
        Speak_Os("please Enter the Password.")
        passwordInput = input("Enter Password:-\n")
        protectionFile = open("password.txt","r")
        pw = protectionFile.read()
        protectionFile.close()
        if (passwordInput==pw):
            Speak_Os("Provied Credentials have matched.")
            Speak_Os("AI Assistant's access has been granted")
        elif (passwordInput!=pw):
            Speak_Os("Provied Credentials do not  match AI Assistant's access is denied.")
            Speak_Os("Please enter the passoword again.")

def LiveCricketScores():
    CricketWebsite = "https://www.cricbuzz.com/"
    page = get(CricketWebsite)
    soup = BeautifulSoup(page.text,"html.parser")
    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text
    try:
        SCORE1 = Speak_Os(f"{team1} : {team1_score}")
    except Exception as e:
        print(e)
        Speak_Os("can't get scores.")
    try:
        SCORE2 = Speak_Os(f"{team2} : {team2_score}")
    except Exception as e:
        print(e)
        Speak_Os("can't get scores.")
    notification.notify(
    title = "LIVE CRICKET SCORE :- ",
    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
    timeout = 15)

def ClickPicture():
    Speak_Os("opening the camera.")
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    Speak_Os("Your picture will get clicked in three,       two,       one.")
    Speak_Os("Say Cheese")
    pyautogui.press("enter")

