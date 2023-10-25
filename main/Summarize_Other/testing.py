# import sys
# sys.path.append('./Summarizing')
# from  Summarizing import main
# from  Summarizing import ConvertSTRToTXT
import main
import ConvertSTRToTXT
import sys
sys.path.append('./Summarize')

text="""hi this is the first paraghraf for testing apps"""
input=input("input")
input2="'"+input+"'"

print(text)
ConvertSTRToTXT.converting(input2)
# def converting(input_txt):
#     with open("text2.txt","w") as file:
#         file.write(input_txt)
# converting(input_txt=text)

# x=main.summarize(filename="C:/Workarea/File_Analyser/main/Summarize/text.txt")
# print(x)

summarize = main.summarize(filename="text.txt")
print(summarize)
