from flask import Flask, request, jsonify;
from app.tables import Aluno, Disciplina, Turma, HistoricoEscolar, PreRequisito, Model
from app.db import Banco
import os


app = Flask(__name__);

password = os.getenv("REDIS_PASSWORD", "senhaPadrao")

print("pass", password)

redis = Banco(password=password)

ROTAS = {
    'alunos': 'Aluno',
    'disciplinas': 'Disciplina',
    'turmas': 'Turmas',
    'historicos': 'HistoricoEscolar',
    'pre-requisitos': 'PreRequisito'
}

TABELAS = {
    'alunos': Aluno,
    'disciplinas': Disciplina,
    'turmas': Turma,
    'historicos': HistoricoEscolar,
    'pre-requisitos': PreRequisito
}

@app.get('/api/<string:table_name>/')
def get_all(table_name: str):
    table_name = table_name.lower()
    tabela = ROTAS[table_name]
    tabela = list(redis.search_for_key(f"*{tabela}*", getvalues=True))
    # print(tabela)
    # import ipdb; ipdb.set_trace()
    return jsonify(tabela)


@app.route('/api/<string:table_name>/', methods=['POST', 'PUT'])
def set_in_db(table_name):
    table_name = table_name.lower()
    nome_tabela = ROTAS[table_name]
    data = dict(request.values)
    print(data)
    import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        return jsonify("POST")
    
    if request.method == "PUT":
        # Adicionar novo registo
        ultimo = redis.get_last(nome_tabela + "*") + 1
        tabela: Model = TABELAS[table_name](*data.values())
        tabela.fields_values[0] = ultimo

        # nome = '{}:{}'.format(tabela.table_name, ultimo)
        # redis.set_one(tabela)
        print(ultimo)
        print()

        return jsonify("PUT")



    # return jsonify(tabela)


if __name__ == '__main__':
    from time import sleep
    app.run(debug=True)
