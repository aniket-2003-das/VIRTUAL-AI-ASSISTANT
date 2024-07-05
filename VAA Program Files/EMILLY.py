import sys
import wikipedia
import pyjokes
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaContent
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Tasks_Functions import *
from ui_Frontend import Ui_MainWindow
from Listening_Functions import Listen_English
from Speaking_Functions import Speak_Os
from AI_Chatbots import Chatbot_Open_AI

class Backend(QThread):
    def __init__(self): 
        super(Backend,self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        # while 1:
            query = Listen_English()
            if "hello" in query:
                Speak_Os("Hello ! this is your AI Assistant EMILLY")
                Speak_Os("How can I help you?")
            elif "wake up" in query:
                Speak_Os("I am ready to help you!")
            elif "sleep" in query:
                Speak_Os("ok sir you can say activate to activate hotward and deactivate to terminate me.")
            elif "open website" in query:
                openWebsite()
            elif "light automation" in query:
                Lights_Automation()
            elif "Space news" in query:
                Speak_Os("enter the date for which you want to know news. ")
                Date = str(input("enter the date-:20xx-12-31.\n"))
                SpaceNews(Date)
            elif "image from mars" in query:
                MarsImage()
            elif "space station" in query:
                ISS_Tracker()
            elif "new space objects" in query:
                Speak_Os("ok enter the time duration")
                start_date = str(input("enter the start date-: 20xx-12-31\n"))
                end_date = str(input("enter the end date-: 20xx-12-31\n"))
                Speak_Os("checking the trackers")
                SpaceObjects(start_date, end_date)
            elif "information about solar body" in query:
                Speak_Os("Ok. Enter the name of the body you want to know about.")
                Speak_Os("enter the name of the body:")
                body = input("enter the name of the body:")
                SorlarBodies(body)
            elif "send a mail" in query:
                Speak_Os("enter the EMAIL ID of the recipient")
                to = input("enter the EMAIL ID:")
                Speak_Os("dictate the content of the mail.")
                content = Listen_English()
                sendEmail(to, content)
            elif "use whatsapp" in query:
                whatsApp_Automation()
            elif "open application" in query:
                OpenApps()
            elif "temperature" in query:
                Temperature()
            elif "notepad" in query:
                Notepad()
            elif "computer networks" in query:
                CSE3006_Computer_Networks_BL2022235000368()
            elif "computer language" in query:
                Computational_Linguistics_F11_F12_CL_2021()
            elif "maths class" in query:
                B21_B22_B23_MAT3003_ProbabilityStatisticsAndReliability_DrBHUMIKACHOKSI()
            elif "data structures" in query:
                E21_E22_E23_DS_AA_Winter2023()
            elif "project presentation" in query:
                DSN2099_Project_Exhibition_II()
            elif "internet of things" in query:
                SensorsAndIOT_B11_B12()
            elif "read a book" in query:
                TextReader()
            elif "close application" in query:
                CloseApps()
            elif "shedule" in query:
                TimeTable()
            elif "youtube automation" in query:
                YoutubeAutomation()
            elif "chrome automation" in query:
                ChromeAutomation()
            elif "covid cases" in query:
                Speak_Os("Ok. Enter the country name.")
                Country = input("Enter the country name:")
                CoronaVirus(Country)
            elif "screenshot" in query:
                screenshot()
            elif "windows automation" in query:
                WindowsAutomation()
            elif "internet speed" in query:
                InternetSpeed()
            elif "automate refrigerator" in query:
                Fridge_Automation()
            elif 'wikipedia search' in query: 
                Speak_Os("ok wait i am Searching the internet...")
                query = query.replace("wikipedia search", "")
                Wikipedia_results = wikipedia.summary(query, sentences = 2)
                Speak_Os("Sorry for delay sir ! here's what i found it says.")
                print(Wikipedia_results)
                Speak_Os(Wikipedia_results)
            elif 'play music' in query:
                music_dir = "C:\\Users\\anike\\Music\\Sample Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'what is the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")
                Speak_Os(f" Sir the clock shows {strTime}")
            elif 'set alarm' in query:
                Speak_Os("For what time!")
                time = input(":For what time:")
                Speak_Os(f"A alarm has been saved just now at {time}!")
                while 1:
                    Time_Ac = datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    if now == time:                    
                        music_dir = "C:\\Users\\anike\\Music\\Sample Music"
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[1]))                               
                    elif now>time:
                        break
            elif 'youtube search' in query:
                query = query.replace("youtube search", "")
                ytTitle = 'https://www.youtube.com/results?search_query='+ query
                Speak_Os("ok sir here are the results!")
                webbrowser.open(ytTitle)
            elif 'google search' in query:
                import wikipedia as googleScrap
                Speak_Os("Here are your results.")
                query = query.replace("google search", "")
                pywhatkit.search(query)
                try:
                    search_result = googleScrap.summary(query,1)
                    Speak_Os(search_result)
                except:
                    Speak_Os("here are the results!")
            elif "comedy" in query:
                joke = pyjokes.get_joke()
                Speak_Os(joke)
            elif "repeat" in query:
                Speak_Os("start the naration!")
                naration = Listen_English()
                Speak_Os(f"you said: {naration}")
            elif "location" in query:
                My_Location()
            elif "remember important information" in query:
                Speak_Os("what do you want me to remember")
                impText = Listen_English()
                Speak_Os("ok i will remember!")
                imp_info = open('important-information.txt', 'w')
                imp_info.write(impText)
                imp_info.close
            elif "tell important information" in query:
                imp_info = open('important-information.txt', 'r')
                Speak_Os("yes once you told me that" + imp_info.read())
            elif "translate this line" in query:
                TransLater()
            elif "download youtube video" in query:
                YoutubeVideoDownloader()
            elif "locate a place" in query:
                PlaceLocator()
            elif "manage files" in query:
                HiddenFiles()
            elif "how much charge" in query:
                Battery()
            elif "volume" in query:
                Volume(query)
            elif "news headlines" in query:
                NewsHeadlines()
            elif "calculate" in query:
                query = query.replace("calculate","")
                Calculator(query)
            elif "shutdown the system" in query:
                Terminator()
            elif "change password" in query:
                Speak_Os("What's the new password")
                new_pswd = input("Enter the new password\n")
                new_password = open("password.txt","w")
                new_password.write(new_pswd)
                new_password.close()
                Speak_Os("saved the new password.")
                Speak_Os(f"Your new password is{new_pswd}")
            elif "cricket scores" in query:
                LiveCricketScores()
            elif "click my photo" in query:
                ClickPicture() 
            elif "tell about a solar body" in query:
                Speak_Os("ok tell the name of the object.")
                body = input("enter object-:")
                SorlarBodies(body)
            else:
                reply = Chatbot_Open_AI(query)
                Speak_Os(reply)

startBackend = Backend()

class Frontend(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Ui_guibeast = Ui_MainWindow()     
        self.Ui_guibeast.setupUi(self)
        self.Ui_guibeast.micon.clicked.connect(self.startFunc)
        self.Ui_guibeast.close.clicked.connect(self.close)
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("C:\\Users\\anike\\Music\\Sample Music\\Emilly-ThemeMusic.mp3")))
        self.player.setVolume(50)
        self.player.positionChanged.connect(self.handlePositionChanged)
        self.player.play()
    def handlePositionChanged(self, position):
        if position == self.player.duration():
            self.player.setPosition(0)
            self.player.play()
    def startFunc(self):
        self.Ui_guibeast.face.setMovie(QtGui.QMovie("Gui_Gifs\\face.gif"))
        self.Ui_guibeast.face.movie().start()    
        self.Ui_guibeast.brain.setMovie(QtGui.QMovie("Gui_Gifs\\brain.gif"))
        self.Ui_guibeast.brain.movie().start()
        self.Ui_guibeast.loading.setMovie(QtGui.QMovie("Gui_Gifs\\loading.gif"))
        self.Ui_guibeast.loading.movie().start()
        self.Ui_guibeast.neurons.setMovie(QtGui.QMovie("Gui_Gifs\\neurons.gif"))
        self.Ui_guibeast.neurons.movie().start()
        self.Ui_guibeast.speed.setMovie(QtGui.QMovie("Gui_Gifs\\speed.gif"))
        self.Ui_guibeast.speed.movie().start()
        self.Ui_guibeast.voiceball.setMovie(QtGui.QMovie("Gui_Gifs\\voiceball.gif"))
        self.Ui_guibeast.voiceball.movie().start()
        self.Ui_guibeast.soundwave.setMovie(QtGui.QMovie("Gui_Gifs\\soundwaves.gif"))
        self.Ui_guibeast.soundwave.movie().start()
        startBackend.start()
        
EMILLY = QApplication(sys.argv)
startFrontend = Frontend()
startFrontend.show()
sys.exit(EMILLY.exec_())
