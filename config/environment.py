import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/stylefinds')
secret = os.getenv('SECRET', 'shh, it\'s a secret')
