from pyhive import hive

if __name__ == '__main__':
    cursor = hive.connect('hive-server').cursor()
    cursor.execute('USE default')
    cursor.execute("""
    SELECT A.artist_lastfm from 
    ( 
      SELECT * FROM artists
      ORDER BY scrobbles_lastfm DESC
      LIMIT 1
    ) as A
    """)
    result = cursor.fetchone()[0]
    print(result)
