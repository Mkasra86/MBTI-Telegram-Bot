# Importing needed libraries
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Bot
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters

# Importing all data from others files
from QA import *
from Q94 import * 
from A94 import *
from TestAnalysis import *
from API import token

# Gettin the bot for some uses /=

bot = Bot(token=token)

# Defining Needed Variables

userId = None

enORfa = ""
testType = ""
eResult = 0
iResult = 0
sResult = 0
nResult = 0
tResult = 0
fResult = 0
jResult = 0
pResult = 0

# Varible for all users data

userData = {}
userStartLog = {}

# ***

# -------------Every function I needed-------------

# Gives the question automatically based on the test log and language
def QlistTypeChoosing(indent, userTesttype , userLang):
    if userLang == "EN":
        if userTesttype == "20":
            return list_q_20[indent]
        elif userTesttype == "94":
            return list_q_94[indent]
        
    elif userLang == "FA":
        if userTesttype == "20":
            return list_qp_20[indent]
        elif userTesttype == "94":
            return list_qp_94[indent]
                
# Gives the first option of question automatically based on the test log and language
def AAlistTypeChoosing(indent, userTesttype , userLang):
    if userLang == "EN":
        if userTesttype == "20":
            return list_a_20a[indent]
        elif userTesttype == "94":
            return list_a_94a[indent]
        
    elif userLang == "FA":
        if userTesttype == "20":
            return list_ap_20a[indent]
        elif userTesttype == "94":
            return list_ap_94a[indent]
        
# Gives the second option of question automatically based on the test log and language
def ABlistTypeChoosing(indent, userTesttype , userLang):
    if userLang == "EN":
        if userTesttype == "20":
            return list_a_20b[indent]
        elif userTesttype == "94":
            return list_a_94b[indent]
        
    elif userLang == "FA":
        if userTesttype == "20":
            return list_ap_20b[indent]
        elif userTesttype == "94":
            return list_ap_94b[indent]
                
# Returns a quit text based on user's language   
def returnText(userLang):
    if userLang == "EN":
        return "Quit 🔙"
    elif userLang == "FA":
        return "انصراف 🔙"
            
# Sets the callback data when hitting the quit/return button based on user's language
def returnCallback(userTesttype, userLang):
    if userLang == "EN":
        if userTesttype == "20":
            return "20q"
        elif userTesttype == "94":
            return "94q"
        
    elif userLang == "FA":
        if userTesttype == "20":
            return "20qp"
        elif userTesttype == "94":
            return "94qp"

# Writes (Returns) the text above the questions in the tests and calculate the
# percentage of completed questions
def testText(userLang):
    testPercentage = str(round((userData[userId][0]["questionNum"] / int(userData[userId][0]["testType"]) * 100) , 1)) + "%"
    if userLang == "EN":
        return f"MBTI {userData[userId][0]["testType"]} questions test \nQuestions number : {str(userData[userId][0]["questionNum"])} ({testPercentage} Done)\n\n"
    elif userLang == "FA":
        return f"تست {userData[userId][0]["testType"]} سواله MBTI \nسوال شماره : {str(userData[userId][0]["questionNum"])} ({testPercentage} انجام شده)\n\n"

# Saves the first options of question based on the test log and test type (20 or 90)    
def AResultSaving(questionNumber, userTesttype, userLang):
    
    global eResult
    global sResult
    global tResult
    global jResult
    
    if userTesttype == "20":
        if 0 < questionNumber < 6:
            userData[userId][0]["eResult"] += 1
        elif 5 < questionNumber < 11:
            userData[userId][0]["sResult"] += 1
        elif 10 < questionNumber < 16:
            userData[userId][0]["tResult"] += 1
        elif 15 < questionNumber:
            userData[userId][0]["jResult"] += 1
        return "a1_callback"
    elif userTesttype == "94":
        if userLang == "EN":
            if 0 < questionNumber < 16:
                userData[userId][0]["eResult"] += 1
            elif 15 < questionNumber < 37:
                userData[userId][0]["sResult"] += 1
            elif 36 < questionNumber < 58:
                userData[userId][0]["tResult"] += 1
            elif 57 < questionNumber:
                userData[userId][0]["jResult"] += 1
            return "a1_callback"
        elif userLang == "FA":  
            if 0 < questionNumber < 32:
                userData[userId][0]["eResult"] += 1
            elif 31 < questionNumber < 59:
                userData[userId][0]["sResult"] += 1
            elif 58 < questionNumber < 78:
                userData[userId][0]["tResult"] += 1
            elif 77 < questionNumber:
                userData[userId][0]["jResult"] += 1
            return "a1_callback"   

# Saves the second options of question based on the test log and test type (20 or 90)
def BResultSaving(questionNumber, userTesttype, userLang):
        
    global iResult
    global nResult
    global fResult
    global pResult
    
    if userTesttype == "20":
        if 0 < questionNumber < 6:
            userData[userId][0]["iResult"] += 1
        elif 5 < questionNumber < 11:
            userData[userId][0]["nResult"] += 1
        elif 10 < questionNumber < 16:
            userData[userId][0]["fResult"] += 1
        elif 15 < questionNumber:
            userData[userId][0]["pResult"] += 1
        return "a2_callback"
    elif userTesttype == "94":
        if userLang == "EN":
            if 0 < questionNumber < 16:
                userData[userId][0]["iResult"] += 1
            elif 15 < questionNumber < 37:
                userData[userId][0]["nResult"] += 1
            elif 36 < questionNumber < 58:
                userData[userId][0]["fResult"] += 1
            elif 57 < questionNumber:
                userData[userId][0]["pResult"] += 1
            return "a2_callback"
        elif userLang == "FA":  
            if 0 < questionNumber < 32:
                userData[userId][0]["iResult"] += 1
            elif 31 < questionNumber < 59:
                userData[userId][0]["nResult"] += 1
            elif 58 < questionNumber < 78:
                userData[userId][0]["fResult"] += 1
            elif 77 < questionNumber:
                userData[userId][0]["pResult"] += 1
            return "a2_callback"
        
# The first question saving is different so these functions save in another way
def firstSavingA(questionNumber):
    if questionNumber == 1:
                AResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
                
def firstSavingB(questionNumber):
    if questionNumber == 1:
                BResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
                
# Returns a report text based on user's language    
def reportMenuText(userLang):
    if userLang == "EN":
        text = "Send report 🛑"
            
        return text
    elif userLang == "FA":
        text = "ثبت گزارش 🛑"
            
        return text
    
# Returns a return text based on user's language   
def returnMainMenuText(userLang):
    
    if userLang == "EN":
        text = "Return to main menu"
        
        return text
    elif userLang == "FA":
        text = "بازگشت به منوی اصلی"
            
        return text
    
# Returns the the user's test type and report description based on the user's language 
def reportText(userTesttype, userLang):
    if userLang == "EN":
        reportText = """
        
Please write down what was the mistake or wrong thing
in the test and say which question if needed.
We very thank you for helping us to make this bot better for you!
We also appreciate to see your suggestions to get better.😇
        
        """
        return [reportText, userTesttype]
        
    elif userLang == "FA":
        reportText = """
        
لطفا اشتباه یا خطایی که داخل آزمون مشاهده کردید رو بنویسید و در صورت نیاز حتما شماره سوال تست رو ذکر کنید. از اینکه به ما کمک میکنید برای بهبود این ربات بسیار متشکریم. خوشحال میشیم اگر پیشنهادی داشتید اون رو به گوشمون برسونید. 😇
        
        """
        return [reportText, userTesttype]
    
# Gettin (calculating) the result of user's test

def result(eResult, iResult, sResult, nResult, tResult, fResult, jResult, pResult):
    testResult = ""
    if eResult > iResult:
        testResult += "E"
    else:
        testResult += "I"
        
    if sResult > nResult:
        testResult += "S"
    else:
        testResult += "N"
        
    if tResult > fResult:
        testResult += "T"
    else:
        testResult += "F"
        
    if jResult > pResult:
        testResult += "J"
    else:
        testResult += "P"
        
    return testResult  

# Returns the description about the user's MBTI type in both English
# and Persian (again based on user's language)
def resultAnalysis(testResult, userLang):
    if userLang == "EN":
        if testResult == "ESTJ":
            testAnalysis = ESTJ
        elif testResult == "ISTJ":
            testAnalysis = ISTJ
        elif testResult == "ENTJ":
            testAnalysis = ENTJ
        elif testResult == "INTJ":
            testAnalysis = INTJ
        elif testResult == "ESFJ":
            testAnalysis = ESFJ
        elif testResult == "ISFJ":
            testAnalysis = ISFJ
        elif testResult == "ENFJ":
            testAnalysis = ENFJ
        elif testResult == "INFJ":
            testAnalysis = INFJ
        elif testResult == "ESTP":
            testAnalysis = ESTP
        elif testResult == "ISTP":
            testAnalysis = ISTP
        elif testResult == "ENTP":
            testAnalysis = ENTP
        elif testResult == "INTP":
            testAnalysis = INTP
        elif testResult == "ESFP":
            testAnalysis = ESFP
        elif testResult == "ISFP":
            testAnalysis = ISFP
        elif testResult == "ENFP":
            testAnalysis = ENFP
        elif testResult == "INFP":
            testAnalysis = INFP
            
        return testAnalysis
    
    elif userLang == "FA":
        if testResult == "ESTJ":
            testAnalysis = ESTJ_p
        elif testResult == "ISTJ":
            testAnalysis = ISTJ_p
        elif testResult == "ENTJ":
            testAnalysis = ENTJ_p
        elif testResult == "INTJ":
            testAnalysis = INTJ_p
        elif testResult == "ESFJ":
            testAnalysis = ESFJ_p
        elif testResult == "ISFJ":
            testAnalysis = ISFJ_p
        elif testResult == "ENFJ":
            testAnalysis = ENFJ_p
        elif testResult == "INFJ":
            testAnalysis = INFJ_p
        elif testResult == "ESTP":
            testAnalysis = ESTP_p
        elif testResult == "ISTP":
            testAnalysis = ISTP_p
        elif testResult == "ENTP":
            testAnalysis = ENTP_p
        elif testResult == "INTP":
            testAnalysis = INTP_p
        elif testResult == "ESFP":
            testAnalysis = ESFP_p
        elif testResult == "ISFP":
            testAnalysis = ISFP_p
        elif testResult == "ENFP":
            testAnalysis = ENFP_p
        elif testResult == "INFP":
            testAnalysis = INFP_p
            
        return testAnalysis
        
# Base of the program starts here 0_0
    
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

UserName = "" # Defining a global UserName variable so that I can use it in the whole app

# Answers the "/start" command sent by the user at any time
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global userId
    global UserName
    global user
    global userData
    global userStartLog
    
    userStartLog[userId] = [
                {
                    "userStart" : 1
                }
            ] 
    
    try:
         # Tries to clear the previous keyboards if there
         # was one (a little bit tricky to understand this /=)
        await update.callback_query.edit_message_reply_markup(None)
    except:
        
        keyboard =[
            [
                InlineKeyboardButton("FA 🇮🇷", callback_data="FA"),
                InlineKeyboardButton("EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="EN"),
            ]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        user = update.message.from_user
        
        # Gets the user's name from Telegram ( from updated message )
        UserName = user['first_name']
        
        # Gets the user's chat_id from Telegram ( from updated message )
        userId = user['id']
        await update.message.reply_text(f"Welcome {UserName}👋🏻 \nPlease choose:", reply_markup=reply_markup)

# Menus and other stuffs

# Every callback will be answered in here
async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    # Making everything needed global so that I can set and use it 
    # again in every part of the app
    global query
    global eResult
    global iResult
    global sResult
    global nResult
    global tResult
    global fResult
    global jResult
    global pResult
    global enORfa
    global testType
    global userId
    global userData
        
    query = update.callback_query
    user = update.callback_query.from_user

    
    userId = user['id']
    
    # When you want to choose your language again it comes here
    await query.answer()
    if query.data == "lan_selection":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data
                    "enORfa" : ""
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : ""
                    ,"questionNum" : None
                }
            ]
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        
        keyboard =[
            [
                InlineKeyboardButton("FA 🇮🇷", callback_data="FA"),
                InlineKeyboardButton("EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿", callback_data="EN"),
            ]
        ]
        
        user = update.callback_query.from_user
        UserName = user['first_name']
        userId = user['id']
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"Ok {UserName}!😊 \nPlease choose:", reply_markup=reply_markup)
        
    # Showing the Persian menu and letting user to choose its test type (20 or 94 questions)
    elif query.data == "FA":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user 
                    # language because it was choosen in here )
                    "enORfa" : "FA"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : ""
                    ,"questionNum" : None
                }
            ]    
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        enORfa = userData[userId][0]["enORfa"]
        keyboardfa = [ 
            [
                InlineKeyboardButton("تست سریع MBTI (20 سوال)", callback_data="20qp")   
            ],
            [
                InlineKeyboardButton("تست کامل پیشنهادی MBTI (94 سوال)", callback_data="94qp")
            ],
            [
                InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
            ],
            [
                InlineKeyboardButton("بازگشت🔙", callback_data="lan_selection")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa = InlineKeyboardMarkup(keyboardfa)
        await query.edit_message_text(f"تستی که میخوای رو انتخاب کن 😇 \n", reply_markup=reply_markup_fa)
        
    # Showing the English menu and letting user to choose its test type (20 or 94 questions)
    elif query.data == "EN":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user 
                    # because it they were already choosen )
                    "enORfa" : "EN"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : ""
                    ,"questionNum" : None
                }
            ]    
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        enORfa = userData[userId][0]["enORfa"]
        keyboarden = [ 
            [
                InlineKeyboardButton("Short MBTI test (20 Questions)", callback_data="20q")   
            ],
            [
                InlineKeyboardButton("Suggested full MBTI test (94 Questions)", callback_data="94q")
            ],
            [
                InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
            ],
            [
                InlineKeyboardButton("Return 🔙", callback_data="lan_selection")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_en = InlineKeyboardMarkup(keyboarden)
        await query.edit_message_text(f"Choose which test you want 😇 \n", reply_markup=reply_markup_en)
    
    # User comes here if choosed 20 Perisan MBTI test
    elif query.data == "20qp":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user language 
                    # and test type because it they were already choosen )
                    "enORfa" : "FA"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : "20"
                    ,"questionNum" : None
                }
            ]
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        keyboard20qp = [ 
            [
                InlineKeyboardButton("شروع!", callback_data="test_start")   
            ],
            [
                InlineKeyboardButton("بازگشت🔙", callback_data="FA")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa20qp = InlineKeyboardMarkup(keyboard20qp)
        await query.edit_message_text(f"شروع کنیم؟! \n", reply_markup=reply_markup_fa20qp)
    # User comes here if choosed 20 English MBTI test
    elif query.data == "20q":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user language 
                    # and test type because it they were already choosen )
                    "enORfa" : "EN"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : "20"
                    ,"questionNum" : None
                }
            ]
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        keyboard20qp = [ 
            [
                InlineKeyboardButton("Start!", callback_data="test_start")   
            ],
            [
                InlineKeyboardButton("Return 🔙", callback_data="EN")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa20qp = InlineKeyboardMarkup(keyboard20qp)
        await query.edit_message_text(f"Should we start?! \n", reply_markup=reply_markup_fa20qp)
    
    # User comes here if choosed 94 Perisan MBTI test
    elif query.data == "94qp":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user language 
                    # and test type because it they were already choosen )
                    "enORfa" : "FA"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : "94"
                    ,"questionNum" : None
                }
            ]
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        keyboard20qp = [ 
            [
                InlineKeyboardButton("شروع!", callback_data="test_start")   
            ],
            [
                InlineKeyboardButton("بازگشت🔙", callback_data="FA")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa20qp = InlineKeyboardMarkup(keyboard20qp)
        await query.edit_message_text(f"شروع کنیم؟! \n", reply_markup=reply_markup_fa20qp)
    
    # User comes here if choosed 94 English MBTI test
    elif query.data == "94q":
        
        userData[userId] = [
                {
                    # Reseting and defining user's data (except user language 
                    # and test type because it they were already choosen )
                    "enORfa" : "EN"
                    ,"testsLog" : None
                    ,"eResult" : None
                    ,"iResult" : None
                    ,"sResult" : None
                    ,"nResult" : None
                    ,"tResult" : None
                    ,"fResult" : None
                    ,"jResult" : None
                    ,"pResult" : None
                    ,"testType" : "94"
                    ,"questionNum" : None
                }
            ]
        userStartLog[userId] = [
                {
                    "userStart" : 0
                }
            ] 
        keyboard20qp = [ 
            [
                InlineKeyboardButton("Start!", callback_data="test_start")   
            ],
            [
                InlineKeyboardButton("Return 🔙", callback_data="EN")
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa20qp = InlineKeyboardMarkup(keyboard20qp)
        await query.edit_message_text(f"Should we start?! \n", reply_markup=reply_markup_fa20qp)
    
        
# !! Program Brain (Asking questions) !!

    # Test start menu in both languages
    elif query.data == "test_start":
        
        # Reseting and defining data
        userStartLog[userId][0]["userStart"] = 0
        userData[userId][0]["testsLog"] = 0
        userData[userId][0]["eResult"] = 0
        userData[userId][0]["iResult"] = 0
        userData[userId][0]["sResult"] = 0
        userData[userId][0]["nResult"] = 0
        userData[userId][0]["tResult"] = 0
        userData[userId][0]["fResult"] = 0
        userData[userId][0]["jResult"] = 0
        userData[userId][0]["pResult"] = 0
        userData[userId][0]["questionNum"] = userData[userId][0]["testsLog"] + 1
        keyboard20qp = [ 
            [
                InlineKeyboardButton(text=AAlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a1_callback")   
            ],
            [
                InlineKeyboardButton(text=ABlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a2_callback")
            ],
            [
                InlineKeyboardButton(text=returnText(userData[userId][0]["enORfa"]), callback_data=returnCallback(userData[userId][0]["testType"], userData[userId][0]["enORfa"]))
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reply_markup_fa20qp = InlineKeyboardMarkup(keyboard20qp)
        await query.edit_message_text(text= testText(userData[userId][0]["enORfa"]) + QlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), reply_markup=reply_markup_fa20qp)
        
        userData[userId][0]["testsLog"] += 1 # Adding 1 so the question number is recognizable and for the next question
        
    elif query.data == "a1_callback":
        
        # Saving answer of FIRST choice
        userStartLog[userId][0]["userStart"] = 0
        
        firstSavingA(userData[userId][0]["questionNum"])
        userData[userId][0]["questionNum"] = userData[userId][0]["testsLog"] + 1 # Adding 1 so the question number is recognizable
        try:
            keyboardTest = [ 
                [
                    InlineKeyboardButton(text=AAlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a4_callback")   
                ],
                [
                    InlineKeyboardButton(text=ABlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a2_callback")
                ],
                [
                    InlineKeyboardButton(text=returnText(userData[userId][0]["enORfa"]), callback_data=returnCallback(userData[userId][0]["testType"], userData[userId][0]["enORfa"]))
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test = InlineKeyboardMarkup(keyboardTest)
            await query.edit_message_text(text= testText(userData[userId][0]["enORfa"]) + QlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), reply_markup=reply_markup_test)
            
            # Saving answers of FIRST choice
            AResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
            
        # If there was no other questions, it comes here for showing the test result         
        except:
            keyboardTestEnd = [
                [
                    InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
                ],
                [
                    InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test_done = InlineKeyboardMarkup(keyboardTestEnd)
            await query.edit_message_text(text= resultAnalysis(result(userData[userId][0]["eResult"], userData[userId][0]["iResult"], userData[userId][0]["sResult"], userData[userId][0]["nResult"], userData[userId][0]["tResult"], userData[userId][0]["fResult"], userData[userId][0]["jResult"], userData[userId][0]["pResult"]), userData[userId][0]["enORfa"]), reply_markup=reply_markup_test_done)
            
        userData[userId][0]["testsLog"] += 1 # Adding 1 so the question number is recognizable and for the next question
        
    elif query.data == "a2_callback":

        userStartLog[userId][0]["userStart"] = 0
        
        # Saving answer of SECOND choice
        firstSavingB(userData[userId][0]["questionNum"])
        userData[userId][0]["questionNum"] = userData[userId][0]["testsLog"] + 1 # Adding 1 so the question number is recognizable
        try:
            keyboardTest = [ 
                [
                    InlineKeyboardButton(text=AAlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a1_callback")   
                ],
                [
                    InlineKeyboardButton(text=ABlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a3_callback")
                ],
                [
                    InlineKeyboardButton(text=returnText(userData[userId][0]["enORfa"]), callback_data=returnCallback(userData[userId][0]["testType"], userData[userId][0]["enORfa"]))
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test = InlineKeyboardMarkup(keyboardTest)
            await query.edit_message_text(text= testText(userData[userId][0]["enORfa"]) + QlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), reply_markup=reply_markup_test)
            
            # Saving answers of second choice
            BResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
            
        # If there was no other questions, it comes here for showing the test result         
        except:
            keyboardTestEnd = [
                [
                    InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
                ],
                [
                    InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test_done = InlineKeyboardMarkup(keyboardTestEnd)
            await query.edit_message_text(text= resultAnalysis(result(userData[userId][0]["eResult"], userData[userId][0]["iResult"], userData[userId][0]["sResult"], userData[userId][0]["nResult"], userData[userId][0]["tResult"], userData[userId][0]["fResult"], userData[userId][0]["jResult"], userData[userId][0]["pResult"]), userData[userId][0]["enORfa"]), reply_markup=reply_markup_test_done)
    
        userData[userId][0]["testsLog"] += 1 # Adding 1 so the question number is recognizable and for the next question
     
    elif query.data == "a3_callback":
        
        userStartLog[userId][0]["userStart"] = 0
        
        userData[userId][0]["questionNum"] = userData[userId][0]["testsLog"] + 1 # Adding 1 so the question number is recognizable
        try:
            keyboardTest = [ 
                [
                    InlineKeyboardButton(text=AAlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a1_callback")   
                ],
                [
                    InlineKeyboardButton(text=ABlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a2_callback")
                ],
                [
                    InlineKeyboardButton(text=returnText(userData[userId][0]["enORfa"]), callback_data=returnCallback(userData[userId][0]["testType"], userData[userId][0]["enORfa"]))
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test = InlineKeyboardMarkup(keyboardTest)
            await query.edit_message_text(text= testText(userData[userId][0]["enORfa"]) + QlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), reply_markup=reply_markup_test)
            
            # Saving answers of second choice
            BResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
                   
        # If there was no other questions, it comes here for showing the test result  
        except:
            keyboardTestEnd = [
                [
                    InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
                ],
                [
                    InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test_done = InlineKeyboardMarkup(keyboardTestEnd)
            await query.edit_message_text(text= resultAnalysis(result(userData[userId][0]["eResult"], userData[userId][0]["iResult"], userData[userId][0]["sResult"], userData[userId][0]["nResult"], userData[userId][0]["tResult"], userData[userId][0]["fResult"], userData[userId][0]["jResult"], userData[userId][0]["pResult"]), userData[userId][0]["enORfa"]), reply_markup=reply_markup_test_done)
 
        userData[userId][0]["testsLog"] += 1 # Adding 1 so the question number is recognizable and for the next question
        
    elif query.data == "a4_callback":
        
        userStartLog[userId][0]["userStart"] = 0
        
        userData[userId][0]["questionNum"] = userData[userId][0]["testsLog"] + 1 # Adding 1 so the question number is recognizable
        try:
            keyboardTest = [ 
                [
                    InlineKeyboardButton(text=AAlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a1_callback")   
                ],
                [
                    InlineKeyboardButton(text=ABlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), callback_data="a2_callback")
                ],
                [
                    InlineKeyboardButton(text=returnText(userData[userId][0]["enORfa"]), callback_data=returnCallback(userData[userId][0]["testType"], userData[userId][0]["enORfa"]))
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test = InlineKeyboardMarkup(keyboardTest)
            await query.edit_message_text(text= testText(userData[userId][0]["enORfa"]) + QlistTypeChoosing(userData[userId][0]["testsLog"], userData[userId][0]["testType"], userData[userId][0]["enORfa"]), reply_markup=reply_markup_test)
                
            # Saving answers of FIRST choice
            AResultSaving(userData[userId][0]["questionNum"], userData[userId][0]["testType"], userData[userId][0]["enORfa"])
        
        # If there was no other questions, it comes here for showing the test result         
        except:
            keyboardTestEnd = [
                [
                    InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
                ],
                [
                    InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                ]
            ]
            
            user = update.callback_query.from_user
            userId = user['id']
            
            reply_markup_test_done = InlineKeyboardMarkup(keyboardTestEnd)
            await query.edit_message_text(text= resultAnalysis(result(userData[userId][0]["eResult"], userData[userId][0]["iResult"], userData[userId][0]["sResult"], userData[userId][0]["nResult"], userData[userId][0]["tResult"], userData[userId][0]["fResult"], userData[userId][0]["jResult"], userData[userId][0]["pResult"]), userData[userId][0]["enORfa"]), reply_markup=reply_markup_test_done)
 
        userData[userId][0]["testsLog"] += 1 # Adding 1 so the question number is recognizable and for the next question
        
    # Send report works from here
    elif query.data == "sendReport":
        
        userStartLog[userId][0]["userStart"] = 0
        
        keyboardReport = [
            [
                InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
            ]
        ]
        
        user = update.callback_query.from_user
        userId = user['id']
        
        reportKeyboard = InlineKeyboardMarkup(keyboardReport)
        await query.edit_message_text(text=reportText(userData[userId][0]["testType"], userData[userId][0]["enORfa"])[0], reply_markup=reportKeyboard)
        # rest of it in (async def report)
        
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: # rest of sendReport from callbacks and useless messages
    
    global userId
    global userData
    
    
    # This is used fro sending report
    if query.data == "sendReport":
        
        # If the user uses a command when send report was choosen, it 
        # comes here to cancel the sending report
        if userStartLog[userId][0]["userStart"] == 1:
            
            keyboardReport = [
                [
                    InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
                ]
            ]
            
            user = update.message.from_user
            userId = user['id']
            
            keyboard = InlineKeyboardMarkup(keyboardReport)
            if userData[userId][0]["enORfa"] == "EN":
                await bot.send_message(chat_id=userId, text="I didn't understand what you said 👀", reply_markup=keyboard)
            elif userData[userId][0]["enORfa"] == "FA":
                await bot.send_message(chat_id=userId, text="متوجه نشدم چی گفتی 👀", reply_markup=keyboard)
            
        # If everything was okay and no command was choosen it sends the message to the chat_id written down
        else:
            await bot.send_message(chat_id=5445616530, text= f"""
                                
User @{update.message.from_user['username']} has send 
a report from the {reportText(userData[userId][0]["testType"], userData[userId][0]["enORfa"])[1]}q test.

The report : 
{update.message.text}
                                
                                """)
            
            keyboarden = [ 
                    [
                        InlineKeyboardButton("Short MBTI test (20 Questions)", callback_data="20q")   
                    ],
                    [
                        InlineKeyboardButton("Suggested full MBTI test (94 Questions)", callback_data="94q")
                    ],
                    [
                        InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                    ],
                    [
                        InlineKeyboardButton("Return 🔙", callback_data="lan_selection")
                    ]
            ]

            user = update.message.from_user
            userId = user['id']

            reply_markup_en = InlineKeyboardMarkup(keyboarden)


            keyboardfa = [ 
                [
                    InlineKeyboardButton("تست سریع MBTI (20 سوال)", callback_data="20qp")   
                ],
                [
                    InlineKeyboardButton("تست کامل پیشنهادی MBTI (94 سوال)", callback_data="94qp")
                ],
                [
                    InlineKeyboardButton(text=reportMenuText(userData[userId][0]["enORfa"]), callback_data="sendReport")
                ],
                [
                    InlineKeyboardButton("بازگشت🔙", callback_data="lan_selection")
                ]
            ]

            user = update.message.from_user
            userId = user['id']

            reply_markup_fa = InlineKeyboardMarkup(keyboardfa)
            
            # After the message was sent to the chat_id, it shows a text and goes back to the main menu
            if userData[userId][0]["enORfa"] == "EN":
                await bot.send_message(chat_id=userId, text= "Your report has been sent to bot admin. 🤖")
                await bot.send_message(chat_id=userId, text= None, reply_markup=reply_markup_en )
            elif userData[userId][0]["enORfa"] == "FA":
                await bot.send_message(chat_id=userId, text="گزارش شما به ادمین ارسال شد. 🤖", reply_markup=reply_markup_fa) 
            
            
            userStartLog[userId][0]["userStart"] = 1 
          
    # This is used for unrecognized messages  
    else:
        keyboardReport = [
            [
                InlineKeyboardButton(text=returnMainMenuText(userData[userId][0]["enORfa"]), callback_data=userData[userId][0]["enORfa"])
            ]
        ]
        
        user = update.message.from_user
        userId = user['id']
        
        keyboard = InlineKeyboardMarkup(keyboardReport)
        
        # This shows the message for unrecognized messages and gives 
        # a button for going to the main menu
        if userData[userId][0]["enORfa"] == "EN":
            await bot.send_message(chat_id=userId, text="I didn't understand what you said 👀", reply_markup=keyboard)
        elif userData[userId][0]["enORfa"] == "FA":
            await bot.send_message(chat_id=userId, text="متوجه نشدم چی گفتی 👀", reply_markup=keyboard)
        
# --------------------------------

# Help command 
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global userData
    global userId
    userStartLog[userId][0]["userStart"] = 1
    
    keyboard = [
                [
                    InlineKeyboardButton(text="Return/بازگشت 🔙", callback_data="lan_selection")
                ]
            ]
    
    user = update.message.from_user
    userId = user['id']
    
    reply_markup_command = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("""

Welcome to the MBTI Quiz Bot! Here's how you can use the bot:

/start – Begin the bot and find out your MBTI personality type.
/about - See what the bot is. 😁👍
/credit – Information about who developed this bot.
/help – See this help message again. 🤐

How it Works:

Answer each question honestly to get the most accurate result.
After completing the quiz, you'll receive a result with your personality type.😊
                                    
""", reply_markup=reply_markup_command)
   
# Credit command    
async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global userData
    global userId
    userStartLog[userId][0]["userStart"] = 1
    
    keyboard = [
                [
                    InlineKeyboardButton(text="Return/بازگشت 🔙", callback_data="lan_selection")
                ]
            ]
    
    user = update.message.from_user
    userId = user['id']
    
    reply_markup_command = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("""

This MBTI quiz bot was created and programmed by Matin Kasra. It uses a carefully designed set of questions inspired by the Myers-Briggs Type Indicator (MBTI) to help you discover your personality type. Whether you're curious about your own traits or simply exploring, this bot is here to make your journey both insightful and fun! 😊

""", reply_markup=reply_markup_command)
    
# About command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global userData
    global userId
    userStartLog[userId][0]["userStart"] = 1
    
    keyboard = [
                [
                    InlineKeyboardButton(text="Return/بازگشت 🔙", callback_data="lan_selection")
                ]
            ]
    
    user = update.message.from_user
    userId = user['id']
    
    reply_markup_command = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("""
                                    
This bot lets you take psychological tests like MBTI and others ( Not 
ready yet ). You can see and know a little bit about your result in the bot. 
This bot is just here to have these kind of psychological tests in 
Telegram. Since this bot is not 100% accurate and might not give you 
the best results we are not responsible for any wrong result or answer 
as you can take more accurate tests in 16personalities.com or other
similar sites.😊                  
    \n
    
با استفاده از این ربات می توانید تستهای روانشناسی
ازجمله MBTI را انجام داده و نتیجه تست خود را 
مشاهده نمایید با توجه به اینکه تستهای آنلاین 100% 
دقیق نیستند احتمال خطا یا بروز اشتباه وجود دارد،
فسیر نتایج بر عهده شماست و در این رابطه از
کارشناسان این رشته بهره گیرید .
این ربات صرفا به منظور بهره برداری ساده تر 
توسط شما  در تلگرام ساخته شده و میتوانید برای
انجام تست های دقیق تر به سایت 16personalities.com 
یا دیگر سایتهای مشابه مراجعه کنید.😊
\n""", reply_markup=reply_markup_command)
    
# -------------------------------

# Leting the app know to read evrything from where 0_0 
def main() -> None:

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("credit", credit))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CallbackQueryHandler(callbacks))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, report))
    

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()