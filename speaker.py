import json

class Speaker:
    def __init__(self, name, position, session):
        self.name = name
        self.position = position
        self.session = session
        self.topic = ""
        self.notes = []

    def addNote(self, note):
        self.notes.append(note)

    def setTopic(self, topic):
        self.topic = topic

    def toJSON(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)#, sort_keys=True, indent=4)
