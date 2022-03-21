import gtts
import os
import logging

"""
Init logging
"""

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|message: [%(message)s]',
    datefmt='%d/%m/%y - %H:%M:%S',
    filename='./logs.txt'
)

logger = logging.getLogger(__name__)

# Variable file data
file_to_import = './data.txt'
# Variable file mp3 to export
file_to_export = './files/text_to_audio.mp3'
# Variable lang
lang = 'es'


def logging_and_print(text):
    print(text)
    logging.info(text)


def read_file():
    with open(file_to_import, 'r') as file:
        logging_and_print(f"Reading {file_to_import} .")
        data_read = file.read()
    return data_read


def create_file():
    with open(file_to_import, 'a') as file:
        logging_and_print(f"File {file_to_import} was created.")


def make_request_synthesis(text: str):
    logging_and_print(f"Making request to text")
    try:
        return gtts.gTTS(text, lang=lang)
    except:
        logging_and_print(f"Error making request to Google")


def save_file(tts):
    tts.save(file_to_export)
    logging_and_print(f"Saved file {file_to_export} .")


if (not os.path.exists(file_to_import)):
    create_file()
else:
    data_read = read_file()
    if (data_read):
        request_synthesis = make_request_synthesis(data_read)
        save_file(request_synthesis)
    else:
        logging_and_print(f"There is not returned data in file {file_to_import}")
