import json
import os
import psycopg2

conn = psycopg2.connect(
        host = os.environ['DB_HOST'],
        dbname = os.environ['DB_NAME'],
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        port = os.environ['DB_PORT']
        )

def lambda_handler(event, context):
    records = event['Records']
    data = [json.loads(record['body']) for record in records]

    insert_sql = "INSERT INTO log VALUES (%s, %s);"
    
    conn.cursor().executemany(insert_sql, data)
    conn.commit()
    
    return {
        'statusCode': 200,
        'body': json.dumps('SUCCESS')
    }
