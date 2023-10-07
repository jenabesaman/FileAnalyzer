import googletrans

translator = googletrans.Translator()


def translation(input_text, src, dest):
    try:
        translated = translator.translate(input_text, src=src, dest=dest)
        return translated
    except Exception as e:
        return e

# translation("آدم",src="ruccc",dest="en")
#
# x=translation("آدم",src="ruccc",dest="en")
# # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print(x.text)


# translation = translator.translate("آدم",  dest="en")
# print(translation.text)
