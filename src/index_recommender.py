def recommend_indexes(column_frequency):
    indexes = []

    for column, count in column_frequency.items():
        if count >= 2:
            indexes.append(
                f"CREATE INDEX idx_{column} ON orders({column});"
            )

    return indexes
