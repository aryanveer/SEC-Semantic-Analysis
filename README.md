# README #

**Objective**

Objective of this assignment is to extract some sections from SEC / EDGAR financial reports and perform text analysis to compute variables those are explained below. Link to SEC / EDGAR financial reports are given in excel spreadsheet “cik_list.xlsx”. 

Add https://www.sec.gov/Archives/ to every cells of column F (cik_list.xlsx) to access link to the financial report. 
Example: Row 2, column F contains edgar/data/3662/0000950170-98-000413.txt
Add https://www.sec.gov/Archives/ to form financial report link i.e. 
https://www.sec.gov/Archives/edgar/data/3662/0000950170-98-000413.txt


**Sentiment Analysis**

Sentimental analysis is the process of determining whether a piece of writing is positive, negative or neutral. The below Algorithm is designed for use on Financial Texts. It consists of steps:

**USE Python 3**
Run the following:

```
pip install -r requirements.txt
(i) python scrap.py  # to download the files
(ii) main.py # for sentiment analysis
```

Downloaded data will be in data/raw_data.
