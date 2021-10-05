from unittest import TestCase
from app.app import app
from flask import url_for


class TestApp(TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app_client = app.test_client()
        self.app_context = app.app_context()
        self.base_url = "http://localhost:5000/api"

    def test_get(self):
        url = self.base_url + "/alunos/"
        r = self.app_client.get(url)

        self.assertEqual(r.status_code, 200)
    
    def test_put_new_aluno(self):
        url = self.base_url + "/alunos/"
        aluno = {
            '_id': '6', 'curso': 'Engenharia Mecânica',
            'nome': 'Edgar Galván', 'numeroAluno': '106', 'tipoAluno': '1'}
        self.app_client.put(url, data=aluno)
        import ipdb; ipdb.set_trace()