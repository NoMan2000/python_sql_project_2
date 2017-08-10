from modules import connection, formatter


def get_top_authors():
    conn = connection.get_connection()
    conn.execute('''
        SELECT
        COUNT(authors.id) AS totalViews,
        authors.name
        FROM log, authors, articles
        WHERE log.path != '/' AND
        articles.slug =
        SUBSTR(log.path, LENGTH('/article/') + 1)
        AND articles.author = authors.id
        GROUP BY
        authors.name,
        authors.id
        ORDER BY totalViews DESC
    ''')

    return conn


def print_top_authors():
    print("Top authors:")
    formatter.repeat_separator()
    for item in get_top_authors():
        print("The total views for the author '" + str(item[1]) +
              "' are " + formatter.format_num(item[0]) + '.')
    formatter.repeat_separator()
