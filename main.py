import string 
import re 
import nltk
from nltk.corpus import stopwords 

input_str = ""
with open("C:\\Users\\lenovo\\Documents\\Test Assignment 20211030\\URL_ID_150.txt", "r", encoding = "utf8") as f: 
    for line in f.read():
        input_str = input_str + line 
# print(input_str) 

# stop_words_0 = set(stopwords.words('english')) 
stop_words_1 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_Auditor.txt")) 
# stop_words_2 = set(stopwords.words("C:\\Users\\lenovo\Downloads\\StopWords\\StopWords_Currencies.txt")) 
stop_words_3 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_DatesandNumbers.txt")) 
stop_words_4 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_Generic.txt")) 
stop_words_5 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_GenericLong.txt")) 
stop_words_6 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_Geographic.txt")) 
stop_words_7 = set(stopwords.words("C:\\Users\\lenovo\\Downloads\\StopWords\\StopWords_Names.txt")) 

from nltk.tokenize import word_tokenize 
token = word_tokenize(input_str) 

result_0 = [i for i in token if not i in stop_words_1] 
# print(result_0) 

result_1 = [i for i in result_0 if not i in stop_words_3] 
# print(result_1) 

result_2 = [i for i in result_1 if not i in stop_words_4] 
# print(result_2) 

result_3 = [i for i in result_2 if not i in stop_words_5] 
# print(result_3) 

result_4 = [i for i in result_3 if not i in stop_words_6] 
# print(result_4) 

result_5 = [i for i in result_4 if not i in stop_words_7] 
# print(result_5) 

table = str.maketrans("","", string.punctuation) 
stripped = [w.translate(table) for w in result_5] 
# print(stripped) 

file = "C:\\Users\\lenovo\Downloads\\StopWords\\StopWords_Currencies.txt"

with open (file, "r") as fr:
    Currencies = fr.read()
    # print(Currencies)

stop_words_final = [i for i in stripped if not i in Currencies] 
# print(stop_words_final) 

# assembled = " ".join(stop_words_final)
# print(assembled) 

text_file = "C:\\Users\\lenovo\\Downloads\\MasterDictionary\\positive-words.txt" 

with open (text_file, "r") as fk:
    positive = fk.read()
    # print(positive) 

positive_result = set([i for i in stop_words_final if i in positive]) 
# print(positive_result) 

filename = "C:\\Users\\lenovo\\Downloads\\MasterDictionary\\negative-words.txt"

with open (filename, "r") as fn:
    negative = fn.read() 
    # print(negative) 

negative_result = set([i for i in stop_words_final if i in negative])  
# print(negative_result) 

# POSITIVE SCORE 
positive_score = len(positive_result) 
print(positive_score) 

# NEGATIVE SCORE 
negative_score = -(len(negative_result))*-1 
print(negative_score) 

# POLARITY SCORE
Polarity_Score = (positive_score - negative_score)/ ((positive_score + negative_score) + 0.000001) 
print(Polarity_Score) 

# SUBJECTIVITY SCORE
Subjectivity_Score = (positive_score + negative_score)/ ((len(stop_words_final)) + 0.000001) 
print(Subjectivity_Score) 

p = open("C:\\Users\\lenovo\\Documents\\Test Assignment 20211030\\URL_ID_150.txt", mode = 'r', encoding = "utf8") 

number_of_words = 0
number_of_chars = 0
number_of_lines = 0 

for line in p: 
    number_of_lines += 1 
    line = line.strip("\n")
    number_of_chars += len(line) 
    list1 = line.split()
    number_of_words += len(list1) 
p.close() 

# print("number of lines:", number_of_lines) 
# print("number of words:", number_of_words) 
# print("number of characters:", number_of_chars)  

# AVERAGE SENTENCE LENGTH
Average_Sentence_Length = number_of_words / number_of_lines
print(Average_Sentence_Length) 

# AVERAGE NUMBER OF WORDS PER SENTENCE 
Average_Number_of_Words_Per_Sentence = number_of_words / number_of_lines 
print(Average_Number_of_Words_Per_Sentence) 

# WORD COUNT 
word_count = len(stop_words_final)
print(word_count) 

# SYLLABLE PER WORD 
def syllable_per_word():
    document = open("C:\\Users\\lenovo\\Documents\\Test Assignment 20211030\\URL_ID_150.txt", mode = 'r', encoding = "utf8")  
    content = document.read() 
    syllables = list("AEIOUaeiou")
    count = 0
    for syllable in content:
        if syllable in syllables:
            count += 1 

    return count 

print("Total syllables in file are:", syllable_per_word())  

# PERSONAL PRONOUNS 
text = "C:\\Users\\lenovo\\Documents\\Test Assignment 20211030\\URL_ID_150.txt" 
pattern = '["I", "we", "my", "ours", "us"] +' 
Personal_pronouns = re.findall(pattern, text) 
# print(Personal_pronouns) 
print(len(Personal_pronouns)) 

# AVERAGE WORD LENGTH
Average_word_length = number_of_chars / number_of_words 
print(Average_word_length)  





















