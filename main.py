import pandas as pd
from settings import *
import csv
import itertools
import os
import re
import unicodedata
from collections import namedtuple
from glob import glob
import requests
from bs4 import BeautifulSoup
import nltk
import string
from string import punctuation
import numpy as np
import os
import csv
import pandas as pd
from urllib.request import urlretrieve
import errno
import urllib.request
import nltk.tokenize
import re
from stopwords import *
from analysis import score_analysis
import openpyxl

def get_mda(file):

    text = text_normalization(file)
    
    mda1, end = extracting_mda_section(text)
   
    if mda1 and len(mda1.encode('utf-8')) < 1000:
        mda1, _ = extracting_mda_section(text, start=end)

    if mda1:
        return mda1
    else:
        print("extract mda failed ")

def get_qqdmr(file):

    text = text_normalization(file)

    qqdmr1, end = extracting_qqdmr_section(text)
   
    if qqdmr1 and len(qqdmr1.encode('utf-8')) < 1000:
        qqdmr1, _ = extracting_mda_section(text, start=end)

    if qqdmr1:
        return qqdmr1
    else:
        print("extract qqdmr failed ")
        
def get_rf(file):

    text = text_normalization(file)

    rf1, end = extracting_rf_section(text)
    
    if rf1 and len(mda1.encode('utf-8')) < 1000:
        rf1, _ = extracting_mda_section(text, start=end)

    if rf1:
        return rf1
    else:
        print("extract rf failed ")

        
def text_normalization(text):
    
    text = unicodedata.normalize("NFKD", text) 
    text = '\n'.join(
        text.splitlines())  
    text = text.upper()  
    
    text = re.sub(r'[ ]+\n', '\n', text)
    text = re.sub(r'\n[ ]+', '\n', text)
    text = re.sub(r'\n+', '\n', text)

    text = text.replace('\n.\n', '.\n') 

    text = text.replace('\nI\nTEM', '\nITEM')
    text = text.replace('\nITEM\n', '\nITEM ')
    text = text.replace('\nITEM  ', '\nITEM ')

    text = text.replace(':\n', '.\n')
    text = text.replace('$\n', '$')
    text = text.replace('\n%', '%')

    text = text.replace('\n', '\n\n') 

    return text


def extracting_mda_section(text, start=0):
    
    debug = False
    mda = ""
    end = 0

    item7_begins = ['\nITEM 7.', '\nITEM 7 –', '\nITEM 7:', '\nITEM 7 ', '\nITEM 7\n',
                   '\nITEM 2.', '\nITEM 2 –', '\nITEM 2:', '\nITEM 2 ', '\nITEM 2\n']
    item7_ends = ['\nITEM 7A', 'PART II', 'PART  II','\nITEM 8']
    if start != 0:
        item7_ends.append('\nITEM 8') 
    item8_begins = ['\nITEM 8.','\nITEM 8']
    """
        Parsing code section
    """
    text = text[start:]

    for item7 in item7_begins:
        begin = text.find(item7)
        if debug:
            print(item7, begin)
        if begin != -1:
            break

    if begin != -1:  
        for item7A in item7_ends:
            end = text.find(item7A, begin + 1)
            if debug:
                print(item7A, end)
            if end != -1:
                break

        if end == -1:  
            for item8 in item8_begins:
                end = text.find(item8, begin + 1)
                if debug:
                    print(item8, end)
                if end != -1:
                    break

        if end > begin:
            mda = text[begin:end].strip()
        else:
            end = 0

    return mda, end

def extracting_qqdmr_section(text, start=0):
    
    debug = False
    mda = ""
    end = 0

    item7_begins = ['\nITEM 7A.', '\nITEM 7A –', '\nITEM 7A:', '\nITEM 7A ', '\nITEM 7A\n',]
    item7_ends = ['\nITEM 8', 'PART III', 'PART  III']
    if start != 0:
        item7_ends.append('\nITEM 9') 
    item8_begins = ['\nITEM 8.','\nITEM 8','\nITEM 9.','\nITEM 9']

    text = text[start:]

  
    for item7 in item7_begins:
        begin = text.find(item7)
        if debug:
            print(item7, begin)
        if begin != -1:
            break

    if begin != -1: 
        for item7A in item7_ends:
            end = text.find(item7A, begin + 1)
            if debug:
                print(item7A, end)
            if end != -1:
                break

        if end == -1:  # ITEM 7A does not exist
            for item8 in item8_begins:
                end = text.find(item8, begin + 1)
                if debug:
                    print(item8, end)
                if end != -1:
                    break

        if end > begin:
            mda = text[begin:end].strip()
        else:
            end = 0

    return mda, end



def extracting_rf_section(text, start=0):
    
    debug = False
    mda = ""
    end = 0

    item7_begins = ['\nITEM 1A.', '\nITEM 1A –', '\nITEM 1A:', '\nITEM 1A ', '\nITEM 1A\n']
    item7_ends = ['\nITEM 1B', 'PART II', 'PART  II']
    if start != 0:
        item7_ends.append('\nITEM 2') 
    item8_begins = ['\nITEM 2.','\nITEM 2','\nITEM 3.','\nITEM 3']

    text = text[start:]

    for item7 in item7_begins:
        begin = text.find(item7)
        if debug:
            print(item7, begin)
        if begin != -1:
            break

    if begin != -1:  
        for item7A in item7_ends:
            end = text.find(item7A, begin + 1)
            if debug:
                print(item7A, end)
            if end != -1:
                break

        if end == -1: 
            for item8 in item8_begins:
                end = text.find(item8, begin + 1)
                if debug:
                    print(item8, end)
                if end != -1:
                    break

        if end > begin:
            mda = text[begin:end].strip()
        else:
            end = 0

    return mda, end

def text_cleaning(dirty_text):
    output = re.sub(r'\d+', '', dirty_text) 
    para = nltk.word_tokenize(output)
    sent = nltk.sent_tokenize(output)
    
    good_para = [words for words in para
             if words not in combined_stopwords_list]

    dash = "-"
    slash = "/"
    to_delete = []
    for w in good_para:
        if dash in w:
            x=w.split("-")
            to_delete.append(w)
            good_para.append(x[0])
            good_para.append(x[1])

        elif slash in w:
            x=w.split("/")
            to_delete.append(w)
            good_para.append(x[0])
            if x[1]:
                good_para.append(x[1])

    good_para = [words for words in good_para
                 if words not in to_delete]
    
    return good_para,sent

def get_file_path(a):
    field = cik_list['SECFNAME'][a]
    path_list = [RAW_DATA_PATH] + field.split("/")
    return os.path.join(*path_list)

def read_file(path):
    temp = open(path)
    file_text = temp.read()
    return file_text

def main():
    global cik_list
    excel_file_path = os.path.join(DATA_DIR, IMPORT_FILE_NAME)
    cik_list = pd.read_excel(excel_file_path)
    output_file_path = os.path.join(BASE_DIR, OUTPUT_FILE)
    output = pd.read_excel(output_file_path)
    output['CIK'] = cik_list['CIK']
    output['CONAME'] = cik_list['CONAME']
    output['FYRMO'] = cik_list['FYRMO']
    output['FDATE'] = cik_list['FDATE']
    output['FORM'] = cik_list['FORM']
    output['SECFNAME'] = cik_list['SECFNAME']
   
    
    for i in range(0,len(cik_list)):
        path_for_file = get_file_path(i)
        print("Getting path for file")
        
        file_text = read_file(path_for_file)
        print("Reading text from {}".format(cik_list['SECFNAME'][i]))
        
        extracted_mda = get_mda(file_text)
        extracted_qqdmr = get_qqdmr(file_text)
        extracted_rf = get_rf(file_text)
        
        global cleaned_words_mda, sentences_mda, cleaned_words_qqdmr, sentences_qqdmr, cleaned_words_rf, sentences_rf
        
        if extracted_mda:
            cleaned_words_mda, sentences_mda = text_cleaning(extracted_mda)
            mda_scores = score_analysis(cleaned_words_mda, sentences_mda)
            #print(mda_scores)
            for j in range(0,len(mda_scores)):
                output.iloc[i,j+6]=mda_scores[j]
            
        if extracted_qqdmr:
            cleaned_words_qqdmr, sentences_qqdmr = text_cleaning(extracted_qqdmr)
            qqdmr_scores = score_analysis(cleaned_words_qqdmr, sentences_qqdmr)
            for j in range(0,len(qqdmr_scores)):
                output.iloc[i,j+20]=qqdmr_scores[j]
            
        if extracted_rf:
            cleaned_words_rf, sentences_rf = text_cleaning(extracted_rf)
            rf_scores = score_analysis(cleaned_words_rf, sentences_rf)
            for j in range(0,len(rf_scores)):
                output.iloc[i,j+34]=rf_scores[j]
    writer = pd.ExcelWriter('finaloutput.xlsx')
    output.to_excel(writer,'Sheet1')
    writer.save()
if __name__ == "__main__":
    main()
