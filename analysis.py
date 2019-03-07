from nltk.corpus import cmudict
import pandas as pd

huge_dict = cmudict.dict()
def syllables_count(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in huge_dict[word.lower()]]

def score_analysis(words,sent):
   
    huge_dict = cmudict.dict()
    master_dictionary = pd.read_excel("LoughranMcDonald_MasterDictionary_2014.xlsx")
    uncertainty_table = pd.read_excel("uncertainty_dictionary.xlsx")
    constraining_table = pd.read_excel("constraining_dictionary.xlsx")
    uncertainty_list = uncertainty_table.Word.values.tolist()
    constraining_list = constraining_table.Word.values.tolist()
    length_words = len(words)
    length_sent = len(sent)
    neg=0
    pos=0
    neu=0
    pos_words_list = []
    for good_para_word in words:
        b = master_dictionary.Word == good_para_word
        negative = master_dictionary.Negative[b]   
        positive = master_dictionary.Positive[b]
        if negative.all() == True:
            neg += 1

        elif positive.all() == True:
            pos += 1
            pos_words_list.append(good_para_word)

        else:
                neu += 1
    pol = (pos-neg)/((pos+neg)+0.000001)
    
    average_sentence_length = len(words)/len(sent)
    
    positive_word_proportion = pos/length_words
    
    negative_word_proportion = neg/length_words
    
    lowercase_cleaned_words = [x.lower() for x in words]
    
    syl = []
    word_in_d = 0
    complex_word_count = 0
    for xword in lowercase_cleaned_words:
        if xword in huge_dict:
            word_in_d += 1
            syl = syllables_count(xword)
            if syl[0] > 2:
                complex_word_count += 1
                
    percentage_of_complex_words = complex_word_count/length_words     
    
    fog_index = 0.4 * (percentage_of_complex_words + average_sentence_length)
    
    uncertainty_score = 0
    constraining_score = 0
    
    for word in words:
        if word in uncertainty_list:
            uncertainty_score += 1
        
    for word in words:    
        if word in constraining_list:
            constraining_score += 1
    
    uncertainty_word_proportion = uncertainty_score/length_words
    constraining_word_proportion = constraining_score/length_words

    scoreslist = [pos, neg, pol, average_sentence_length, percentage_of_complex_words, fog_index, complex_word_count, length_words, uncertainty_score, constraining_score, positive_word_proportion, negative_word_proportion,uncertainty_word_proportion,constraining_word_proportion]
    return scoreslist
