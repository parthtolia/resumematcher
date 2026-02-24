import psycopg2
from urllib.parse import quote_plus

password = quote_plus("Kqu.44qRRL@y9!z")
conn = psycopg2.connect(
    "postgresql://postgres.ogrsosqwwybaiukzgmil:postgresql123@aws-1-eu-west-1.pooler.supabase.com:6543/postgres"
)

print("Connected successfully!")

conn.close()