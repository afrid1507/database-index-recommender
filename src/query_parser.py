def extract_where_columns(query):
    columns = []

    query = query.upper()

    if "WHERE" in query:
        where_part = query.split("WHERE")[1]
        conditions = where_part.split("AND")

        for cond in conditions:
            column = cond.split("=")[0].strip().lower()
            columns.append(column)

    return columns
