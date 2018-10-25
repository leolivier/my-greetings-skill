from mycroft import MycroftSkill, intent_file_handler


class MyGreetings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('greetings.my.intent')
    def handle_greetings_my(self, message):
        self.speak_dialog('greetings.my')


def create_skill():
    return MyGreetings()

