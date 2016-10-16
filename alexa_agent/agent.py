from alexa_client import AlexaClient
from simple_tts import tts
import os
import subprocess
import shlex


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
AUDIO_DIR = BASE_DIR + '/audio'


class AlexaAgent(object):
    def __init__(self):
        self.audio_dir = AUDIO_DIR        
    
    def wakeup(self):
        self.play_mp3("{}/wakeup.mp3".format(self.audio_dir))

    def say(self, input):
        """Alexa will say the text.
        
        @param: input: Text you want Alexa to say.
        @type: input: str or list of str
        """
        if isinstance(input, list):
            self.send_to_alexa(
                text="Simon says, {}".format(input[0]),
                addl_text_list=["Simon says, {}".format(t) for t in input[1:]]
            )
        else:
            self.send_to_alexa(text=input)

    def ask(self, input):
        """Ask Alexa to do something(s).
        
        @param: input: Text command you want to send to Alexa.
        @type: input: str or list of str
        """
        if isinstance(input, list):
            self.send_to_alexa(
                text=input[0],
                addl_text_list=input[1:]
            )
        else:
            self.send_to_alexa(text=input)
    
    def send_to_alexa(self, text, addl_text_list=[]):
        """Send text to Alexa. If addl_text_list is provided, all the text
        commands will be sent concurrently and responses played back in order.

        @param: text: Text command to send to Alexa.
        @type: text: str

        @param: addl_text_list: List of additional text commands to send.
        @type: addl_text_list: list
        """
        alexa = AlexaClient()
        text_list = [text] + addl_text_list
        input_list = [tts(t) for t in text_list]
        output_list = alexa.ask_multiple(input_list)
        if len(output_list) > 1:
            self.play_mp3(output_list[0], output_list[1:])
        else:
            self.play_mp3(output_list[0])
        alexa.clean()

    def play_mp3(self, filename, addl_filenames=[], pause=True):
        """Plays MP3 file(s).
        
        @param: filename: The file path of the MP3 file to play.
        @type: filename: str
        
        @param: addl_filenames: List of paths to additional MP3 files to play.
        @type: addl_filenames: list

        @param: pause: Whether to insert a 1 second pause between files.
        @type: pause: bool
        """
        cmd_args = ["mpg123", "-q"]
        input_list = [filename] + addl_filenames

        for f in input_list:
            cmd_args.append(f)
            if pause:
                cmd_args.append('{}/1sec.mp3'.format(self.audio_dir))

        # Join the args into a string and use shlex to parse it for subprocess
        cmd_str = " ".join(cmd_args)
        cmd = shlex.split(cmd_str)

        # Popen and communicate() to make sure all the audio finishes playing
        p = subprocess.Popen(cmd)
        p.communicate()
