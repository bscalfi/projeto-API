import psycopg2 as pg
from dotenv import load_dotenv
import os 

load_dotenv()

def conector():
    try:
        conexao = pg.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        cursor = conexao.cursor()
        print("Deu certoooo, eu amo back-end ")
        return conexao, cursor
    except Exception as erro:
        print(f"Error de conexao: {erro}")
        return None , None
    
conector()