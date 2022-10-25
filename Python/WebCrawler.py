from json import loads
from urllib3 import PoolManager
import pymysql


def conversor(valor):
    return float(valor[0:4].replace(",", '.'))

with PoolManager() as pool:
    for i in range(1, 2001):

        conexao = pymysql.connect(db='OHM', user='aluno', passwd='sptech')
        cursor = conexao.cursor()
        

        response = pool.request('GET', 'http://localhost:9000/data.json')
        data = loads(response.data.decode('utf-8'))
        temp_value = data['Children'][0]['Children'][0]['Children'][1]['Children'][0]['Value']
        print(conversor(temp_value))
        

        cursor.execute("INSERT INTO temperatura (id, valor) VALUES (null, %s)", conversor(temp_value))
        conexao.commit()
        conexao.close()