# import unittest
# from flask import Flask
# from flask_testing import TestCase
# from app import app

# class FlaskTest(TestCase):

#     def create_app(self):
#         app.config['TESTING'] = True
#         return app

#     def test_index(self):
#         tester = app.test_client(self)
#         response = tester.get("/fo")
#         self.assertEqual(response.status_code,200)

#     def test_classification_prediction(self):
#         data = {
#             'Temperature': 25.0,
#             'Ws': 10,
#             'FFMC': 80.0,
#             'DMC': 150.0,
#             'ISI': 10.0
#         }
#         response = self.client.post('/predictC', data=data)
#         self.assertEqual(response.status_code, 200)

#     def test_regression_prediction(self):
#         data = {
#             'Temperature': 25.0,
#             'Ws': 10,
#             'FFMC': 80.0,
#             'DMC': 150.0,
#             'ISI': 10.0
#         }
#         response = self.client.post('/predictR', data=data)
#         self.assertEqual(response.status_code, 200)
    

# if __name__ == "_main_":
#     unittest.main()

import unittest
import subprocess

class TestApplication(unittest.TestCase):

    def test_unit_failure(self):
        # Simulate a unit test failure
        self.assertEqual(1 + 1, 3)

    def test_docker_image_build_failure(self):
        # Simulate a Docker image build failure
        # This could involve running a subprocess that intentionally fails
        # For example, trying to build a Dockerfile that doesn't exist
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.run(['docker', 'build', '-t', 'test_image', '-f', 'nonexistent_Dockerfile', '.'])

    def test_build_process_failure(self):
        # Simulate a build process failure
        # This could involve running a subprocess that intentionally fails
        # For example, trying to execute a build script that exits with a non-zero status
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.run(['./build_script.sh'])

if __name__ == '_main_':
    unittest.main()