import re
from collections import Counter


def count_words(sentence):
    matched_words = re.findall(r"(?!\')[a-z\d\']+(?<!\')", sentence.lower())
    return Counter(matched_words)
