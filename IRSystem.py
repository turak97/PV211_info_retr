
from typing import Iterable
from pv211_utils.cranfield.irsystem import CranfieldIRSystemBase
from pv211_utils.cranfield.loader import load_documents

import math

from Query import Query
from Document import Document


class IRSystem(CranfieldIRSystemBase):

    def __init__(self):
        self.documents = load_documents(Document)
        self.doc_total_N = len(self.documents)
        self.document_frequency = self.make_document_frequency(self.documents)
        self.idf = self.make_idf(self.document_frequency)

    def make_idf(self, document_frequency):
        """
        Inverse document frequency (idf) tells us, how the term is relevant in the whole collection of documents
        :param document_frequency: Dict with total number of occurrences in all documents
        :return: dict with all terms and its' idf
        """
        idf = {}
        for word, occurrences in document_frequency.items():
            idf[word] = math.log(self.doc_total_N / occurrences, 1.5)
        return idf

    def make_document_frequency(self, documents):
        """
        Document frequency tells us, how many occurences of term there is in the whole collection of documents
        :param documents: List of all documents in collection
        :return: dict with all terms and its' number of occurrences
        """
        document_frequency = {}
        for id, document in documents.items():
            for word in document.term_frequency:
                if word not in document_frequency:
                    document_frequency[word] = 1
                else:
                    document_frequency[word] += 1
        return document_frequency

    def search(self, query: Query) -> Iterable[Document]:
        """
        Process the query, compute the ranks and sort the documents based on its' ranks
        :param query: a query to be processed
        :return: list of all documents sorted by relevance
        """
        score_of_all = []

        for id, document in self.documents.items():
            score_of_this = 0

            for query_token in query.tokens:
                if query_token in document.term_frequency:
                    # score is boosted. 1/2 is fixed, the other 1/2 is added based on how token is relevant
                    score_of_this += 1/2 + 1/2 * (document.term_frequency[query_token] * self.idf[query_token])
                elif query_token in self.idf:
                    # score is penalized based on token relevance
                    # 3 is Bulgarian constant (= it works just fine with it, but dunno exactly why)
                    score_of_this -= 3 * self.idf[query_token]
            score_of_all.append((document, score_of_this))

        score_of_all = sorted(score_of_all, key=lambda x: x[1], reverse=True)

        result = [i[0] for i in score_of_all]
        return result
