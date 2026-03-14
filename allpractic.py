print("Namaste! Welcome to your chatbot")
print("You can ask me  basic questions ,Type  'bye' to exit the bot")

# chatbot memory creation [ dictionary of responses]

responses = {
    "hello": "Hi, welcome .How can i help you?",
    "how are you":  "I am very fine .Thank you",
    "who are you":  "I am smart AI chatbot",
    "motivate me":  "Keep going . Every bug of your project makes you a better developer",
    "happy": "Great to hear that ",
    "function kya hota hai": "jaker chapter 7 padho"
    }

# Method/Function to get response of chatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I am not able to tell that yet. main jald hi ye sikh loungiii"

# take user input
while True:
     userInput= input("please ask your question:")
     print("bot Response :",reply)
     if "bye" in userInput.lower():
        break
     
     reply = getResponseOfBot(userInput)
     print("Bot Response:", reply)