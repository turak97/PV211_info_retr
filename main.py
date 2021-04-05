
from Document import Document
from Query import Query
from IRSystem import IRSystem

from pv211_utils.cranfield.loader import load_documents
from pv211_utils.cranfield.loader import load_queries

from pv211_utils.cranfield.loader import load_judgements
from pv211_utils.cranfield.leaderboard import CranfieldLeaderboard
from pv211_utils.cranfield.eval import CranfieldEvaluation

from tqdm.notebook import tqdm

if __name__ == '__main__':
    submit_result = False
    author_name = "Joch, Otakar"

    documents = load_documents(Document)
    queries = load_queries(Query)

    print('Initializing your system ...', end='', flush=True)
    system = IRSystem()
    evaluation = CranfieldEvaluation(system, load_judgements(queries, documents), CranfieldLeaderboard(), author_name)
    print(end='\r', flush=True)
    evaluation.evaluate(tqdm(queries.values(), desc="Querying your system", leave=False), submit_result)

