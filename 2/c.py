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
    
    SELECT C.new_tag, D.artist_lastfm FROM artists D
    INNER JOIN (
      SELECT A.new_tag, max(B.scrobbles_lastfm) as top_scrobble
      FROM TOP_TAGS A
      INNER JOIN artists B 
      ON B.tags_lastfm!='' AND instr(lower(B.tags_lastfm), A.new_tag) > 0
      GROUP BY A.new_tag
      ) as C
    ON D.scrobbles_lastfm = C.top_scrobble
    """
    cursor.execute(query)
    result = {row[0]:row[1] for row in cursor.fetchall()}
    print(result)
