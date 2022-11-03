from pyhive import hive

if __name__ == '__main__':
    cursor = hive.connect('hive-server',
                          configuration={
                              'hive.strict.checks.cartesian.product': 'false',
                              'hive.mapred.mode': 'notstrict'
                          }).cursor()
    cursor.execute('USE default')
    query = r"""
    WITH TOP_TAGS AS (
      SELECT lower(trim(tag)) as new_tag, count(*) AS cnt FROM artists A
      LATERAL VIEW explode(split(tags_lastfm,'[\;]') ) tmpTable AS tag
      WHERE tag != ''
      GROUP BY lower(trim(tag))
      ORDER BY cnt DESC
      LIMIT 10
    )
    
    SELECT A.artist_lastfm, count(*) AS cnt FROM artists A
    CROSS JOIN TOP_TAGS B ON A.tags_lastfm!='' AND instr(lower(A.tags_lastfm), B.new_tag) > 0
    GROUP BY A.artist_lastfm
    ORDER BY cnt DESC
    LIMIT 10
    """
    cursor.execute(query)
    result = [row[0] for row in cursor.fetchall()]
    print(result)
