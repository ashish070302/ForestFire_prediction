import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class FlaskTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.status_code,200)

    def test_classification_prediction(self):
        data = {
            'Temperature': 25.0,
            'Ws': 10,
            'FFMC': 80.0,
            'DMC': 150.0,
            'ISI': 10.0
        }
        response = self.client.post('/predictC', data=data)
        self.assertEqual(response.status_code, 200)

    def test_regression_prediction(self):
        data = {
            'Temperature': 25.0,
            'Ws': 10,
            'FFMC': 80.0,
            'DMC': 150.0,
            'ISI': 10.0
        }
        response = self.client.post('/predictR', data=data)
        self.assertEqual(response.status_code, 200)
    

if __name__ == "_main_":
    unittest.main()