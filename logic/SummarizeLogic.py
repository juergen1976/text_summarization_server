from persistence.TextStorage import TextStorage
from summarize.TextSummarizer import TextSummarizer

class SummarizeLogic:
    def __init__(self):
        self._textStorage = TextStorage()

    def summarizeTextAndStore(self, original_text: str):
        text_summarizer = TextSummarizer()
        # Generate unqiue document id
        document_id = text_summarizer.createKeyFromText(original_text)
        # check if already in database
        loaded_id, loaded_summary = self._textStorage.loadSummary(document_id)
        if (loaded_id):
            return loaded_id, loaded_summary

        # Summarize text and store it with document id
        summary_text = text_summarizer.summarize(original_text)
        self._textStorage.saveEntry(document_id, original_text, summary_text)
        return document_id, summary_text

    def getTextSummarize(self, document_id: str):
        return self._textStorage.loadSummary(document_id)

