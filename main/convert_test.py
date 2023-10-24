# import sys
# sys.path.append('./Summarizing')
# from  Summarizing import main
# from  Summarizing import ConvertSTRToTXT
import sys
import os

sys.path.append('./main/Summarize')
from Summarize import main
# from Summarize import ConvertSTRToTXT
path = os.path.abspath("Summarize")
sys.path.append(path)

# import Summarize.main as main
import Summarize.ConvertSTRToTXT as ConvertSTRToTXT

from Summarize import word_lists

# import main
# import ConvertSTRToTXT

# import os
# current_directory = os.getcwd()
# print(current_directory)
text = """hi this is the first paraghraf for testing apps"""
# print(text)
ConvertSTRToTXT.converting(text)
# def converting(input_txt):
#     with open("text2.txt","w") as file:
#         file.write(input_txt)
# converting(input_txt=text)

# x=main.summarize(filename="C:/Workarea/File_Analyser/main/Summarize/text.txt")
# print(x)

summarize = main.summarize(filename="text.txt")
print(summarize)
