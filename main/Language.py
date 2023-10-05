from translate import Translator


def translate_text(input_text, lang: str):
    try:
        translator = Translator(to_lang=lang)
        translated = translator.translate(input_text)
        return translated
    except Exception as e:
        if str(e) == "generator raised StopIteration":
            return "input word is not a correct word"
        else:
            return e
