
# Author:    Maximilian Noppel
# Date:      April 2021

import unittest

import flask_unittest

from Server import app


class TestFlask(flask_unittest.ClientTestCase):
    app = app
    labels = ["give_away", "public", "owner_only", "instructed", "documented"]

    def setUp(self, client):
        pass

    def tearDown(self, client):
        pass

    def test_invalidPath(self, client):
        status = client.get('/invalidPath').status_code
        assert(status != 200)

    def test_invalidLabel(self, client):
        status = client.get('/invalidLabel').status_code
        assert(status != 200)

    def test_png_NormalUseCase(self, client):
        status = client.get('/give_away/test.png').status_code
        assert(status == 200)

    def test_png_empty(self, client):
        status = client.get('/give_away/.png').status_code
        assert(status == 200)

        status = client.get('/documented/.png').status_code
        assert(status == 200)

    def test_png_CheckAllLabels(self, client):

        for label in self.labels:
            status = client.get(f"/{label}/test.png").status_code
            assert(status == 200)

    def test_png_AllCharacters(self, client):
        for i in range(0, 0xff):
            if i != 0x2f:  # for all characters except '/'
                status = client.get(f"/give_away/%"+'{:0>2x}'.format(i)+"test.png").status_code
                assert(status == 200)
            else:
                status = client.get(f"/give_away/%"+'{:0>2x}'.format(i)+"test.png").status_code
                assert(status == 308)

    def test_jpeg_NormalUseCase(self, client):
        status = client.get('/give_away/test.jpeg').status_code
        assert(status == 200)

    def test_jpeg_empty(self, client):
        status = client.get('/give_away/.jpeg').status_code
        assert(status == 200)

        status = client.get('/documented/.jpeg').status_code
        assert(status == 200)

    def test_jpeg_CheckAllLabels(self, client):
        for label in self.labels:
            status = client.get(f"/{label}/test.jpeg").status_code
            assert(status == 200)

    def test_jpeg_AllCharacters(self, client):
        for i in range(0, 0xff):
            if i != 0x2f:  # for all characters except '/'
                status = client.get(f"/give_away/%"+'{:0>2x}'.format(i)+"test.jpeg").status_code
                assert(status == 200)
            else:
                status = client.get(f"/give_away/%"+'{:0>2x}'.format(i)+"test.jpeg").status_code
                assert(status == 308)

    def test_home(self, client):
        status = client.get('/').status_code
        assert(status == 200)


if __name__ == '__main__':
    unittest.main()
