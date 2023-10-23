# import sys
# sys.path.append('./Summarizing')
# from  Summarizing import main
# from  Summarizing import ConvertSTRToTXT
import main
import ConvertSTRToTXT

text="While each module serves a function and contributes to the overall algorithm, they are also designed to work independently to serve their own particular function by themselves. For example, “extractor.py” is used by the Summarizer to extract sentences and words from text, but it can also be used independently to see exactly what it extracts. This is useful for debugging as it allows one to test each individual component separately."
# ConvertSTRToTXT.converting(input_txt=text)
# def converting(input_txt):
#     with open("text.txt","w") as file:
#         file.write(input_txt)
# converting(input_txt=text)

x=main.summarize(filename="C:/Workarea/File_Analyser/main/Summarize/test/test2.txt",num_of_sentences=2)
print(x)
