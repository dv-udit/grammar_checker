from langchain.llms import OpenAI
from langchain.text_splitter import NLTKTextSplitter
from langchain.document_loaders import TextLoader
from nltk.tokenize import blankline_tokenize
from langchain import PromptTemplate
import json
from colorama import Fore, init

import nltk

llm = OpenAI(temperature=0, model_name="gpt-4")



# with open("pages.txt") as f:
with open("NEU-23000041_manuscript.txt") as f:
    big_document = f.read()

paragraphs = blankline_tokenize(big_document)


# print(type(paragraphs))


# print("paragraphs>>>>>>>>>>>>",paragraphs[-1])
# for i in paragraphs:
#     print(i," \n\n--->>>")
    
    
prompt = """You are a professional proofreader and I will give you a {sentence} or paragraph for grammar and spelling correction, along with part of speech and tense annotation including old spelling, corrected spelling, part of speech annotation, tense, the total number of grammar and spelling mistakes in the paragraph
The response should contain changes, corrected_sentence, alternative_suggestions, spelling_errors : give response in the following format : format:{'orignal_sentence' : '' ,'corrected_sentence': '','changes': [{'previous': '', 'changed_to': '', 'explanation': '', 'tense' : '', 'part of speech' : ''},'alternative_suggestions': ['', '', ''],'spelling_errors': [ 'aple'] , total_number of grammar and spelling errors : ''}
give keys and string values in double quotes, do not give any other comment like "Here is the corrected text with JSON structure:"
use apostrophe where necessary with escape characters
"""

# output = ""
output = []
for i in paragraphs:
    result = llm(prompt.replace("{sentence}", i))
    output.append(result)
# print("type(result)>>>>>>>>>",type(result))
# print(result,"\n\n")

print("type(output)>>>>>>>>>",type(output))
# print(output,"\n\n")


for i in output:
    print(i,"\n\n")
    print("------------------------------------------------------")