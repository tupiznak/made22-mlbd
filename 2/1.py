from pyhive import hive  # or import hive or import trino

if __name__ == '__main__':
    cursor = hive.connect('127.0.0.1').cursor()
    cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
    print(cursor.fetchone())
    print(cursor.fetchall())
