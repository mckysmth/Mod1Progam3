from conference import Conference
from speaker import Speaker

def addSpeaker():
    name = input("\n\n\nName: ")
    position = input("Position: ")
    session = input("Session: ")
    speaker = Speaker(name, position, session)
    userInput = None
    while userInput != "":
        userInput = input("\nAdd Note [Enter '' to quit]:\n> ")
        
        if userInput != "":
            speaker.addNote(userInput)
        print()
        
    
    speaker.setTopic(input("Topic:\n> "))
    print()
    print()
    return speaker

def main():
    conference = Conference()

    # userInput = None

    
    while True:
        userInput = input("1. Save \n2. Load \n3. Add speaker \n4. Quit \n> ")
        print()
        if userInput == "1":
            conference.save()

        elif userInput == "2":
            conference.load()

        elif userInput == "3":
            conference.addSpeaker(addSpeaker())
            

        elif userInput == "4":
            break

    
    

if __name__ == "__main__":
    main()