import pymorphy2
from translate import Translator
import csv

def readFile(fileName = "input.txt"):
    result = ""
    file = open(fileName, mode='r', encoding='UTF-8')
    for line in file:
        result += line.replace('\n', '')
    return result
def clearWords(words):
    result = words.replace(' ', '')
    result = result.replace('!', '')
    result = result.replace('.', '')
    result = result.replace('?', '')
    result = result.replace(';', '')
    result = result.replace(':', '')
    result = result.replace('-', '')
    result = result.replace('_', '')
    return result

def normaliseWords(words):
    result = []
    morph = pymorphy2.MorphAnalyzer(lang="ru")
    for word in words:
        result.append(morph.parse(word)[0].normal_form)
    return result
def wordCount(words):
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
def wordDictSort(words):
    return dict(sorted(words.items(), key=lambda item: -item[1]))
def getTranslate(words):
    result = []
    translator = Translator(from_lang='ru', to_lang='en', provider='mymemory')
    for word in words:
        result.append([word,translator.translate(word),words[word]])
    return result
def writeFile(words):
    with open('output.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter='|',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['слово|перевод|количество'])
        for element in words:
            writer.writerow(element)

writeFile(getTranslate(wordDictSort(wordCount(normaliseWords(clearWords(readFile()))))))