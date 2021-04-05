
from pv211_utils.cranfield.entities import CranfieldQueryBase

from utils import simplify_text


class Query(CranfieldQueryBase):

    def __init__(self, query_id: int, body: str):
        super().__init__(query_id, body)
        self.tokens = self.translate_query(body)

    def translate_query(self, body):
        """
        Process the body of query and split it into tokens
        :param body: string with text of the query
        :return: tokens extracted from query
        """
        preprocessed = simplify_text(body)

        tokens = set()
        for token in preprocessed:
            if token not in tokens:
                tokens.add(token)

        return tokens
