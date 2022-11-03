from pyhive import hive

if __name__ == '__main__':
    cursor = hive.connect('hive-server').cursor()
    cursor.execute('USE default')
    query = r"""
    SELECT lower(trim(tag)) as new_tag, count(*) AS cnt FROM artists 
    LATERAL VIEW explode(split(tags_lastfm,'[\;]') ) tmpTable AS tag
    WHERE tag != ''
    GROUP BY lower(trim(tag))
    ORDER BY cnt DESC
    LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()[0]
    print(result)
