import unittest
from summarize.TextSummarizer import TextSummarizer


class TextSummarizeTest(unittest.TestCase):
    """
    Test main components
    """

    def test_document_id_generation(self):
        """
        Test that key generation in unique
        :return: None
        """
        summarizer = TextSummarizer()
        text_to_test = "very long, long, long text"
        key1 = summarizer.createKeyFromText(text_to_test)
        key2 = summarizer.createKeyFromText(text_to_test)
        self.assertEqual(key1, key2)

    def test_document_summary_generation(self):
        """
        Test that text summary is unique for same original text
        :return: None
        """
        summarizer = TextSummarizer()
        text_to_test = "Vader enforced the rule of the New Order as the Emperor's Sith apprentice throughout most of the Imperial Era. In the aftermath of the Battle of Yavin in 0 BBY, he discovered the existence of his son and was determined to turn Luke to the dark side. Luke sought to become a Jedi, like his father before him, and believed that Vader had the potential to turn back to the light side of the Force. Vader was defeated by Luke during the Battle of Endor in 4 ABY, but the young Jedi refused to strike down his father in anger, causing the Emperor to torture Luke with Force lightning. The pain inflicted on his son awakened the part of Vader that was still Anakin, resulting in a redeemed Skywalker killing Sidious at the cost of his own life. Having destroyed the Sith and fulfilled his destiny as the Chosen One, Skywalker made peace with his son and became one with the Force."
        summary1 = summarizer.summarize(text_to_test)
        summary2 = summarizer.summarize(text_to_test)
        self.assertEqual(summary1, summary2)

if __name__ == '__main__':
    unittest.main()
