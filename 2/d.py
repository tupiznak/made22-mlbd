from pyhive import hive

if __name__ == '__main__':
    cursor = hive.connect('hive-server').cursor()
    cursor.execute('USE default')
    query = r"""
    SELECT lower(trim(country)), count(*) AS cnt FROM artists A
    LATERAL VIEW explode(split(country_lastfm,'[\;]') ) tmpTable AS country
    WHERE country_lastfm != ''
    GROUP BY lower(trim(country))
    ORDER BY cnt DESC
    LIMIT 10
    """
    cursor.execute(query)
    result = [row[0] for row in cursor.fetchall()]
    print(result)
