# -*- coding: utf-8 -*-
from .languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    clean_list = text.split()
    
    match = {
        'English': 0,
        'Spanish':0,
        'German':0
    }
    

    for lang in LANGUAGES:
        for word in lang['common_words']:
            if word in clean_list:
                match[lang['name']] += 1
                
    max_counter = 0
    language = ""
    for index in match.keys():
        if match[index] > max_counter:
            language = index
            max_counter = match[index]
    return language
