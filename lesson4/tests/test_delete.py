import pytest
from .conftest import TODOS_MAX


@pytest.mark.parametrize('todo_id', [1, TODOS_MAX])
def test_delete_positive(session, base_url, todo_id):
    res = session.delete(url=f'{base_url}/{todo_id}')

    assert res.status_code == 200
    assert not res.json()


# Deletion of non-existing todo_id has no effect. So test cases are weird
@pytest.mark.parametrize('todo_id', ['', '?'])
def test_delete_negative(session, base_url, todo_id):
    res = session.delete(url=f'{base_url}/{todo_id}')

    assert res.status_code == 404
    assert not res.json()
