# Product Review Analysis
Scraping of publicly available reviews and analysis its sentiment and keywords

## Step 1- Scraping of public reviews
Scraping flipkart reviews scrapes reviews from the website flipkart using selenium and beautiful soup libraries

## Step 2- Processing data to make it useful
Text data needs some processing steps before we can analyse and work on it, pre-processing reviews needs to be run

## Step 3- Sentiment analysis
Use sent_analysis to analyse the sentiment of the different reviews and gives it a positive or negative score according to the sentiment. Post analysis divide into different files and save it separately. Publicly RoBERTa model used for analysis

## Step 4- Keyword analysis
Analyse the review texts by using the keywords and gathering the most used keywords in the reviews. Tfid vectorizer used for this

## Steo 5- Word Cloud
With the bunch of keywords/original reviews use the word cloud library in python to create a word cloud as a means of visualisation for the textual review data
