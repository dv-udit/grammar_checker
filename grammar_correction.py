from langchain.llms import OpenAI
from langchain.text_splitter import NLTKTextSplitter
from langchain.document_loaders import TextLoader
from nltk.tokenize import blankline_tokenize
from langchain import PromptTemplate


import nltk


llm = OpenAI(temperature=0, model_name="gpt-4")


# prompt = "You are a professional proofreader and I will give you a sentence which can be specific to a domain, correct the grammar without changing the meaning or context of the statement and return the response in json format .Here alternative_suggestions are suggestion that we can make it more grammatically correct without loosing the context.The response should contain changes, corrected_sentence, alternative_suggestions, spelling_errors : {sentence} give response in the following format : format:{'corrected_sentence': '','changes': [{'previous': '', 'changed_to': '', 'explanation': ''},{'previous': '', 'changed_to': '', 'explanation': ''},{'previous': '', 'changed_to': '', 'explanation': ''}],'alternative_suggestions': ['', '', ''],'spelling_errors: [ 'aple']}"


# text_splitter = NLTKTextSplitter(chunk_size=1000)

with open("doc.txt") as f:
# with open("sample.txt") as f:
    big_document = f.read()


# paragraphs = text_splitter.split_text(big_document)
paragraphs = blankline_tokenize(big_document)

# prompt = 'You are a professional proofreader and I will give you a sentence which can be specific to a domain, correct the grammar without changing the meaning or context of the statement and return the response in json format .The response should contain changes, corrected_sentence, alternative_suggestions, spelling_errors. Here alternative_suggestions are suggestion that we can make it more grammatically correct without loosing the context: {sentence}. give response in the json format '




# prompt = "You are a professional proofreader and I will give you a {sentence} or paragraph for grammar and spelling correction, along with part of speech and tense annotation, also calculate the score based on the following formula

# score = 1 * total number of noun-related errors + 2 * total number of proper noun errors + 5 * total number of verb related errors + 10 * total number of contraction-related errors

# provide the corrected text with JSON structure, including old spelling, corrected spelling, part of speech annotation, tense, the total number of grammar and spelling mistakes in the paragraph, and the calculated score."

prompt = "You are a professional proofreader and I will give you a {sentence} or paragraph for grammar and spelling correction, along with part of speech and tense annotation,provide the corrected text with JSON structure, including old spelling, corrected spelling, part of speech annotation, tense, the total number of grammar and spelling mistakes in the paragraph"

# template = '''You are a professional proofreader and I will give you a {sentence} or paragraph for grammar and spelling correction, along with part of speech and tense annotation ,provide the corrected text with JSON structure, including old spelling, corrected spelling, part of speech annotation, tense, the total number of grammar and spelling mistakes in the paragraph '''

# formula = (1 * noun_errors + 2 * proper_noun_errors + 5 * verb_errors + 10 * contraction_errors)

# prompt = PromptTemplate(
#     input_variables = ['sentence'],
#     template = template
# )

# prompt = 'You are a professional proofreader and I will give you a sentence which can be specific to a domain, correct the grammar without changing the meaning or context of the statement and return the response in json format .The response should contain changes, corrected_sentence, alternative_suggestions, spelling_errors. Here alternative_suggestions are suggestion that we can make it more grammatically correct without loosing the context: {sentence} give response in the json format:'


# sentence = input("Enter the sentence here \n")
# result = llm(prompt.format(sentence="I have a apple."))

for i in paragraphs:
    # print("i>>>>>>>>>>",i)
    # print(i)
    result = llm(prompt.format(sentence=i))

# print(type(result))
print(result)
