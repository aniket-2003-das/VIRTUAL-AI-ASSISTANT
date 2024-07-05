import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def Speak_Os(Text):
    Assistant = pyttsx3.init('sapi5')
    voices = Assistant.getProperty('voices')
    Assistant.setProperty('voice', voices[3].id)
    Text = str(Text)
    lengthcode = len(Text)
    if lengthcode>70:
        Assistant.setProperty('rate',192)
    else:
        Assistant.setProperty('rate',170)
    print("")
    print(f"EMILLY-: {Text}")
    Assistant.say(Text)
    Assistant.runAndWait()
    print("")

# DriverPath1 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\ChromeDriver\\chromedriver.exe"
# s1 = Service(DriverPath1)
# chrome_options1 = Options()
# chrome_options1.add_argument('--log-level=3')
# # chrome_options1.headless = True
# driver1 = webdriver.Chrome(service = s1,options=chrome_options1)
# driver1.maximize_window()
# Website1 = f'https://ttsmp3.com/text-to-speech/indian%20English/'
# driver1.get(Website1)
# ButtonSelection1 = Select(driver1.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection1.select_by_visible_text('Indian English / Aditi')

# def Speak_ttsmp3(Text):
#     print("")
#     print(f" EMILLY : {Text}.")
#     print("")
#     Data = str(Text)
#     xpathtec = '/html/body/div[4]/div[2]/form/textarea'
#     driver1.find_element(by=By.XPsATH, value=xpathtec).send_key(Data)
#     driver1.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
#     driver1.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
#     sleep(2)

# DriverPath2 = "C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\ChromeDriver\\chromedriver.exe"
# s = Service(DriverPath2)
# chrome_options2 = Options()
# chrome_options2.add_argument('--log-level=3')
# driver2 = webdriver.Chrome(service = s,options=chrome_options2)
# driver2.maximize_window()
# Website = 'https://www.naturalreaders.com/online/'
# driver2.get(Website)
# sleep(2)
# driver2.find_element(by=By.XPATH, value='//*[@id="v_4"]').click()
# driver2.find_element(by=By.XPATH, value='/html/body/app-root/app-voice-selection/div/div[3]/button').click()
# sleep(4)
# driver2.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()

# def Speak_NaturalReaders(Text): # for presentation purpose.
#     try:
#         driver2.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
#         sleep(1)
#     except:
#         pass
#     Text = str(Text)
#     xpathtec = '//*[@id="inputDiv"]'
#     driver2.find_element(by=By.XPATH, value=xpathtec).click()
#     driver2.find_element(by=By.XPATH, value=xpathtec).send_keys(Text)
#     driver2.find_element(by=By.XPATH, value='//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]').click()
#     sleep(2)
#     try:
#         driver2.find_element(by=By.XPATH, value='//*[@id="pw-reading-scroll"]/div[1]/button').click()
#         sleep(1)
#     except:
#         pass
#     print("")
#     print(f" EMILLY-: {Text}.")
#     print("") 
