from modules import connection
from modules import formatter


def get_errors_per_day():
    conn = connection.get_connection()
    conn.execute('''
    WITH t AS
        (SELECT DATE(log.time) AS failureDate,
        ROUND((SUM(CASE WHEN
            SUBSTRING(log.status, 0, 4)::INTEGER >= 400
            THEN 1
            ELSE 0
            END
        )  * 100.0)::DECIMAL /
        (COUNT(log.status)), 1) AS totalFailures
        FROM log GROUP BY DATE(log.time)
        )
    SELECT CONCAT(t.totalFailures, '%') AS failure,
    TO_CHAR(t.failureDate, 'Month DD, YYYY') AS date
    FROM t
    GROUP BY t.totalFailures, t.failureDate
    HAVING t.totalFailures > 1
    ''')

    return conn


def print_errors_per_day():
    print("Errors per day:")
    formatter.repeat_separator()
    for item in get_errors_per_day():
        print(
            "The days that have more than 1% errors per day are '" + str(item[1]) +
            "' with a total percent of errors of '" + str(item[0]) + "'")
    formatter.repeat_separator()
