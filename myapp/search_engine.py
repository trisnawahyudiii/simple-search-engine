import re
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")
nltk.download("stopwords")


# Case Folding
# Definisikan fungsi untuk menghilangkan angka, tanda baca, dan whitespace
def remove_numbers_punctuation_whitespace(document):
    document = re.sub(r"\d+", "", document)
    document = re.sub(r"[^\w\s]", "", document)
    document = document.strip()
    document = " ".join(document.split())
    return document


def case_folding(document):
    document = document.lower()
    return remove_numbers_punctuation_whitespace(document)


# Tokenizing
def tokenizing(document):
    return word_tokenize(document)


# Filtering (Stopword Removal) dengan NLTK
def remove_stopwords_nltk(tokens):
    stop_words = set(stopwords.words("indonesian"))
    return [word for word in tokens if word not in stop_words]


# Tahap 4: Stemming dengan Sastrawi
def apply_stemming_sastrawi(tokens):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return [stemmer.stem(word) for word in tokens]


def get_search_result(data, query):
    df = []
    for item in data:
        df.append(item[1])

    documents = pd.DataFrame({"text": df})

    # Melakukan Case Folding pada setiap dokumen
    documents["text"] = documents["text"].apply(case_folding)

    # Melakukan Tokenizing pada setiap dokumen yang telah melalui Case Folding
    # tokenized_documents = [tokenizing(document) for document in case_folded_documents]
    documents["text"] = documents["text"].apply(tokenizing)

    # Melakukan Filtering dengan NLTK pada setiap dokumen yang telah melalui Tokenizing
    # filtered_documents_nltk = [
    #     remove_stopwords_nltk(tokens) for tokens in tokenized_documents
    # ]
    documents["text"] = documents["text"].apply(remove_stopwords_nltk)

    # Melakukan Stemming dengan Sastrawi pada setiap dokumen yang telah melalui Filtering dengan NLTK
    # stemmed_documents_sastrawi = [
    #     apply_stemming_sastrawi(tokens) for tokens in filtered_documents_nltk
    # ]
    documents["text"] = documents["text"].apply(apply_stemming_sastrawi)

    # Menggabungkan tokens yang telah di-stemming menjadi teks kembali
    stemmed_documents_text = [" ".join(tokens) for tokens in documents["text"]]

    # Menginisialisasi objek TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Menghitung TF-IDF dari dokumen
    tfidf_matrix = tfidf_vectorizer.fit_transform(stemmed_documents_text)

    # Preproses query
    query = case_folding(query)
    query_tokens = tokenizing(query)
    query_stemmed = apply_stemming_sastrawi(query_tokens)
    query_tfidf = tfidf_vectorizer.transform([" ".join(query_stemmed)])

    # Hitung cosine similarity antara query dan dokumen
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix)

    # Temukan dokumen dengan similarity tertinggi
    highest_similarity_idx = cosine_similarities.argmax()

    return highest_similarity_idx + 1
