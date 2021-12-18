from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import hashlib

class TextSummarizer:
    def __init__(self):
        nltk.download('punkt')
    def summarize(self, original_text):
        """
        Summarize any text
        :param original_text: Original text to summarize
        :return: Text summary
        """
        num_sentences_in_summary = 2
        parser = PlaintextParser.from_string(original_text, Tokenizer("english"))

        # Possible Summarization techniques
        # "TextRankSummarizer", "LexRankSummarizer", "LuhnSummarizer" "LsaSummarizer"
        summarizer = TextRankSummarizer()
        sentences = summarizer(parser.document, num_sentences_in_summary)
        result =  ""
        for sentence in summarizer(parser.document, num_sentences_in_summary):
            result = result + sentence._text
        return result

    def createKeyFromText(self, text):
        """
        Create a uniqe key from an abitary string
        :param text: any string
        :return: key as hex digest
        """
        return hashlib.md5(text.encode('utf-8')).hexdigest()
