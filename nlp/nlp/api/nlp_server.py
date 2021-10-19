import nlp
from flask import request
import requests


@nlp.app.route('/', methods=["GET"])
def base():
    return "Welcome to the NLP server!"


@nlp.app.route('/voice/', methods=["GET"])
def parse_voice():
    path = request.args.get('path')
    # 1. speech 2 text
    text = _speech_to_text(path)
    # 2. parse command & email_id
    command = _parse_command(text)
    email_id = -1
    args = {}
    # 3. send command to backend
    _send_command(command, email_id, args)
    return text

# @nlp.app.route('/send/', methods=["GET"])


def _send_command(command, email_id, args):
    email_dict = _get_email(email_id) # for other functionalities
    command_dict = {
        "id": email_id,
        "command": command,
        "args": args
    }
    requests.get(
        f"http://localhost:{nlp.app.config['BACKEND_SERVER_PORT']}/api/command/", json=command_dict)
    return command_dict


def _get_email(email_id):
    return requests.get(f"http://localhost:{nlp.app.config['BACKEND_SERVER_PORT']}/api/email/").json()


def _speech_to_text(path, verbose=False):
    '''
    path:       the path to the speech file
    returns:    text version of speech content
    '''
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            if verbose:
                print('Converting audio transcripts into text ...')
                print(text)
        except:
            print('Sorry.. run again...')
    return text

def _parse_command(text, keywords):
    '''
    text:       the text to be parsed for commands
    keywords:   either a set of string, or a path to keywords_file
    returns:    query dict containing counts of each keyword
    '''

    # get keywords first
    if isinstance(keywords, set):
        keywords = keywords
    else:
        try:
            keywords_file = open("keywords.txt", 'r+')
            keywords = set(line.rstrip() for line in keywords_file.readlines())
        except FileNotFoundError
            print("Keywords file not found")

    def preprocess(word : str) -> str:
        return word.lower() # FIXME: 
    
    query = dict()
    for word in text.split(' '):
        word = preprocess(word)
        if word in keywords:
            query[word] = query.get(word, 0) + 1

    return query

def _text_to_audio(text : str, save_file : str, language="en", slow=False):
    audio_obj = gTTS(text=text, lang=language, slow=slow)
    ext = os.path.splitext(save_file)[-1]
    if ext.lower() == ".mp3":
        audio_obj.save(save_file)
    elif ext.lower() == ".wav":
        audio_obj.save("/tmp/tmp.mp3")
        sound = AudioSegment.from_mp3("/tmp/tmp.mp3")
        sound.export(save_file, format="wav")
    else:
        print("Unsupported format, available formats are mp3 and wav", file=sys.stderr)
        raise NotImplementedError