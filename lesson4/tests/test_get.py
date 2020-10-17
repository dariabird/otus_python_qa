import pytest
from .conftest import TODOS_MAX


@pytest.mark.parametrize('todo_id', [1, TODOS_MAX])
def test_get_positive(session, base_url, todo_id):
    res = session.get(url=f'{base_url}/{todo_id}')

    assert res.status_code == 200
    assert res.json()['id'] == todo_id


@pytest.mark.parametrize('todo_id', [-1, 0, TODOS_MAX + 1])
def test_get_negative(session, base_url, todo_id):
    res = session.get(url=f'{base_url}/{todo_id}')

    assert res.status_code == 404
    assert not res.json()
