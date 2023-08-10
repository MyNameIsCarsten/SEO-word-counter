import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
import openpyxl
from exclude import exclude


def get_keywords(url):
    # Make a GET request to the website
    page = requests.get(url)

    # Parsing page content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get the text from the website
    text = ' '.join(map(lambda p: p.text, soup.find_all(['p','h1','h2','h3','h4','h5','h6'])))

    # Split the text into words
    all_words = text.split()

    # Convert words to lowercase
    all_words = [word.lower() for word in all_words]

    # Get rid of "."
    all_words = [word.replace(".", "") for word in all_words]

    # Get rid of ","
    all_words = [word.replace(",", "") for word in all_words]

    # Get rid of "?"
    all_words = [word.replace("?", "") for word in all_words]

    # Get rid of "!"
    all_words = [word.replace("!", "") for word in all_words]

    # Get rid of ":"
    all_words = [word.replace(":", "") for word in all_words]

    # Get rid of " " "
    all_words = [word.replace("\"", "") for word in all_words]

    # Get rid of "("
    all_words = [word.replace("(", "") for word in all_words]

    # Get rid of ")"
    all_words = [word.replace("(", "") for word in all_words]

    # Get rid of "["
    all_words = [word.replace("[", "") for word in all_words]

    # Get rid of "]"
    all_words = [word.replace("]", "") for word in all_words]

    # Get rid of words that are listed in our exclude list
    words = [word for word in all_words if word.lower() not in exclude]

    # Count the frequency of each word
    word_count = Counter(words)

    # Find the percentage of each word
    total_words = len(words)
    for word in word_count:
        word_count[word] = str(round((word_count[word] / total_words) * 100, 2)) + "%"

    # Create a dataframe to store the keywords and their percentages
    df = pd.DataFrame(word_count.items(), columns=['Keyword', 'Percentage'])
    df = df.sort_values(by='Percentage', ascending=False)

    # Save table in excel
    df.to_excel("output.xlsx", index=False)

    return df


# Example usage
url = 'https://en.wikipedia.org/wiki/ELISA'
keywords_df = get_keywords(url)
