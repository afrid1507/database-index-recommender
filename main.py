from src.workload_analyzer import analyze_queries
from src.index_recommender import recommend_indexes
from src.performance_evaluator import measure_query_time

freq = analyze_queries("data/queries.sql")

print("COLUMN USAGE")
for col, cnt in freq.items():
    print(col, ":", cnt)

indexes = recommend_indexes(freq)

print("\nRECOMMENDED INDEXES")
for idx in indexes:
    print(idx)

print("\nQUERY PERFORMANCE")
q = "SELECT * FROM orders WHERE customer_id = 101;"
print(measure_query_time(q), "seconds")
