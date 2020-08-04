"""### 1.2 Making sense out of the mess
You're currently working on a project that requires to analyze some webpages in order to create a better indexation.
As a Proof of Concept (PoC), ___you proposed that creating a some visualization could be a nice and simple way to show how easy it is to identify important tags___. So, the basic steps should be:
- Access to the extract of every page.
- Clean the data and keep only the informative words (remove stop words).
- Count the occurrences of each word and use it as an input for a visualization.
- Generate a figure merging data from all pages.
"""

# Solve this problem here

import requests, re
import matplotlib.pyplot as plt
from wordcloud import WordCloud 

def cleaning_data():
    request_url = """https://en.wikipedia.org/w/api.php?action=query&\
    format=json&prop=extracts&titles=Stack%20Overflow%7CArch%20Linux%7cSuper%20Mario\
    &utf8=1&exintro=1&exsectionformat=plain"""

    response = requests.get(url=request_url)
    json_response = response.json()
    pages = json_response["query"]["pages"]

    word_list = []

    for key in pages:
        extract = pages[key]["extract"]
        no_html = clean('<.*?>', extract, '')
        no_signs = clean('[^\d\w\s]', no_html, ' ')
        text = no_signs.lower()
        word_list.append(text)

    words = " ".join(word_list)


    plot_data(words)


def clean(regexp, text, sustitute):
    cleaner = re.compile(regexp)
    cleantext = re.sub(cleaner, sustitute, text)
    return cleantext


def plot_data(words):
    wordcloud = WordCloud(max_font_size=30, max_words=len(words), background_color='white')
    
    plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.imshow(wordcloud.generate(words), interpolation="bilinear")
    
    plt.show()



cleaning_data()
