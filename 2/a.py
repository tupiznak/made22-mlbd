from pyhive import hive

if __name__ == '__main__':
    cursor = hive.connect('hive-server').cursor()
    cursor.execute('USE default')
    cursor.execute('SELECT MAX(scrobbles_lastfm) FROM artists')
    result = cursor.fetchone()[0]
    print(result)
