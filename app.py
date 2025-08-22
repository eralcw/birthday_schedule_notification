import streamlit as st
from datetime import datetime
import os
import mysql.connector
import mysql.connector.errorcode as Error
from dotenv import load_dotenv
import requests

load_dotenv('.env')

def get_connection():
    conn = None
    try:
        db_config = {
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'host': 'localhost',
        'database': 'birthdates'
            }
        return mysql.connector.connect(**db_config)
         
    except Error as err:
        print(f"Error: '{err}'")
    
        return conn
    
def get_bot():
    TOKEN = os.getenv('TOKEN')
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    resp = requests.get(url).json() 
    
    if resp == {'ok': True, 'result': []}:
        return {'message': 'Nenhum bot encontrado'}
    return resp['ok']
    
def post_msg(name):
    TOKEN = os.getenv('TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    url_post= f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"Hoje é aniversário de {name}"}

    res = requests.post(url_post, json=payload)

    print(res)


def get_today():
  conn = get_connection()
  today = datetime.now()
  cursor = conn.cursor()
  cursor.execute("SELECT name, date_birth FROM birth")
  resultado = cursor.fetchall()
  data = []
  for name, date_birth in resultado:
    if date_birth.month == today.month and date_birth.day == today.day:
      data.append({
        "name": name
      })
  return data

def execute_today():
    today = get_today()
    if len(today) == 0:
        print("Estou aqui")
        return None
    print(today)
    for i in today:
        post_msg(i["name"])

col1, col2 = st.columns(2)

with col1:
    st.title("Olá!")
    birthdates = st.text_input("Digite nome:")
    if st.button("Enviar"):
        print(execute_today())


with col2:
    if st.button('Enviar nome'):
        st.write(f"{nome}")

