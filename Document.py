
from pv211_utils.cranfield.entities import CranfieldDocumentBase

from utils import simplify_text


class Document(CranfieldDocumentBase):

    def __init__(self, document_id: str, authors: str, bibliography: str, title: str, body: str):
        super().__init__(document_id, authors, bibliography, title, body)
        self.term_frequency = self.make_term_frequency(body)

    def make_term_frequency(self, body):
        """
        Process the body of document, split it into tokens and make an dict with all terms in the document and
        its' number of occurrences
        :param body: string with the text of the document
        :return: dict with all terms and it's occurrences in the document
        """
        preprocessed = simplify_text(body)

        index = {}
        for token in preprocessed:
            if token not in index:
                index[token] = 1
            else:
                index[token] += 1

        return index
