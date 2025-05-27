from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapp.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Ato Executa o (SUT - System Under Test)
    - A: Assert  - Garanta que A é A
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Primeiro endpoint com fastAPI'}
    assert response.status_code == HTTPStatus.OK
