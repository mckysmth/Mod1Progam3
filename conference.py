from speaker import Speaker
import json


class Conference:
    def __init__(self):
        self.speakers =[]

    def addSpeaker(self,speaker):
        self.speakers.append(speaker)

    def save(self):
        exportList = []

        for speaker in self.speakers:
            exportList.append(speaker.toJSON())

        with open('data.json', 'w') as filehandle:
            for listitem in exportList:
                filehandle.write('%s\n' % listitem)


    def load(self):
        with open('data.json', 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentPlace = line[:-1]
                self.speakers.append(eval(currentPlace))
        



    
