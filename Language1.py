# Import the necessary library
from googletrans import Translator
from translate import Translator

# Create a Translator object


def translate_text(input_text,lang:str):
    translator = Translator(to_lang=lang)
    translated= translator.translate(input_text)

    return translated

# Test the function
# print(translate_text("Hello World"))