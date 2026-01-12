from collections import Counter
from src.query_parser import extract_where_columns

def analyze_queries(query_file):
    with open(query_file, "r") as f:
        queries = f.readlines()

    all_columns = []

    for q in queries:
        all_columns.extend(extract_where_columns(q))

    return Counter(all_columns)
