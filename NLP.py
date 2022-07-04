from stemming.porter2 import stem
import re

key_list = ['social media', 'facebook', 'twitter', 'instagram', 'linkedin', \
    'data scraping', 'scraping data', 'data analyst', 'NLP', 'ML', 'DL', 'natural language processing', \
    'machine learning', 'deep learning' ]
# social media|facebook|twitter|instagram|linkedin|data scrap|scraping data|data analyst


def filter(text):
    return re.findall('|'.join([stem(word) for word in key_list]), text, flags=re.IGNORECASE)

def content_stem(text):
    return ' '.join([stem(word) for word in text.replace('\n', ' ').split(' ')])

###test###
# raw_text = 'Return to the home page\nPrintable Format\n data scrapring Job Description\n Research Assistant - (2100005G)\nDescription\n The Centre is working on FinTech projects for industrial collaborations and looking for a Research Assistant who would be expected to work on research projects related to cryptocurrencies, trading strategies, data analytics and machine learning. The interim outputs would be used to produce demos of the research outcome, together with the documentation.\n \nApplicants should (i) have a Bachelor’s degree in engineering, or with a quantitative major; (ii) be strong in programming (please state all the programming languages you possessed in the online application) and preferably knowledge in Python or Matlab; and (iii) be good at quantitative subjects. Background in artificial intelligence will be advantageous.\n  Appointment will initially be made on contract basis for one year, renewable subject to mutual agreement.\n Job: Research Posts\nOrganization: Centre for Financial Engineering\nUnposting Date: Ongoing\n   '
# print(filter(raw_text))