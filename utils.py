from nltk.stem import WordNetLemmatizer
from stop_words import LIST_OF_STOP_WORDS
import nltk
nltk.download('wordnet')


def remove_crumbs(text: str):
    text = text.replace("'", "")
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace("-", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("\\", " ")
    text = text.replace("/", " ")
    text = text.replace("=", " ")
    return text


def remove_stop_words(split_text):
    res = []
    for word in split_text:
        if word not in LIST_OF_STOP_WORDS:
            res.append(word)
    return res


def stemming(split_text):
    i = 0
    while i < len(split_text):
        word = split_text[i]
        if len(word) > 4 and word[-4:] == "sses":
            word = word[:-4] + "ss"
        elif len(word) > 3 and word[-3:] == "ies":
            word = word[:-3] + "i"
        elif len(word) > 3 and word[-1:] == "s":
            word = word[:-1]

        split_text[i] = word
        i += 1
    return split_text


def lemmatize(split_text):
    lm = WordNetLemmatizer()

    i = 0
    while i < len(split_text):
        word = split_text[i]
        word = lm.lemmatize(word)
        split_text[i] = word
        i += 1

    return split_text


def simplify_text(text: str):
    text = remove_crumbs(text)
    split_text = text.split()
    split_text = remove_stop_words(split_text)
    split_text = lemmatize(split_text)
    split_text = stemming(split_text)
    return split_text
