import sqlite3 as sl

class TextStorage:
    def __init__(self):
        conn = sl.connect('summary.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS TEXT_SUMMARY
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             DOCUMENT_ID,
             ORIGINAL_TEXT  TEXT NOT NULL,
             SUMMARY_TEXT   TEXT  NOT NULL
             );''')

        conn.close()

    def saveEntry(self, document_id, original_text, summary_text):
        """
        Save new text summary information
        :param document_id: unique document_id
        :param original_text: the original text
        :param summary_text: the text summary
        :return: None
        """
        conn = sl.connect('summary.db')
        conn.execute("INSERT INTO TEXT_SUMMARY (DOCUMENT_ID, ORIGINAL_TEXT, SUMMARY_TEXT) VALUES (?, ?, ?)",
                     (document_id,original_text, summary_text));
        conn.commit()
        conn.close()

    def loadSummary(selfself, document_id):
        """
        Load the summary
        :param document_id: The unique id from the original text
        :return: tuple of document_id and summary
        """
        conn = sl.connect('summary.db')
        cursor = conn.execute("SELECT DOCUMENT_ID, SUMMARY_TEXT from TEXT_SUMMARY WHERE DOCUMENT_ID=:doc_id", { "doc_id" : document_id })
        row = cursor.fetchone()
        if (row):
            return row[0], row[1]
        return None, None
