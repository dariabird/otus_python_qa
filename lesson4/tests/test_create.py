from .conftest import TODOS_MAX
import pytest


@pytest.mark.parametrize('completed', [True, False])
def test_create_completed(session, base_url, completed):
    title = 'foo'
    user_id = 1
    payload = {'title': title, 'completed': completed, 'userId': user_id}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['id'] == TODOS_MAX + 1
    assert j['userId'] == user_id
    assert j['title'] == title
    assert j['completed'] == completed


@pytest.mark.parametrize('user_id', [1, 5, 10])
def test_create_user_id(session, base_url, user_id):
    title = 'foo'
    completed = False
    payload = {'title': title, 'completed': completed, 'userId': user_id}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['id'] == TODOS_MAX + 1
    assert j['userId'] == user_id
    assert j['title'] == title
    assert j['completed'] == completed


@pytest.mark.parametrize('title', ['', 'abc', 'привет', '@#$%^&*()_+:\",.}{><?'])
def test_create_title(session, base_url, title):
    completed = False
    user_id = 10
    payload = {'title': title, 'completed': False, 'userId': user_id}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['id'] == TODOS_MAX + 1
    assert j['userId'] == user_id
    assert j['title'] == title
    assert j['completed'] == completed


@pytest.mark.parametrize('title', ['', 'abc', 'привет', '@#$%^&*()_+:\",.}{><?'])
@pytest.mark.parametrize('completed', [True, False])
@pytest.mark.parametrize('user_id', [1, 5, 10])
def test_create_combination(session, base_url, title, user_id, completed):
    payload = {'title': title, 'completed': completed, 'userId': user_id}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 201
    j = res.json()
    assert j['id'] == TODOS_MAX + 1
    assert j['userId'] == user_id
    assert j['title'] == title
    assert j['completed'] == completed


# Something wrong with API. It accepts almost everything as a valid request.
def test_create_negative(session, base_url):
    payload = {'title': 123.e456, 'completed': False, 'userId': 1}
    res = session.post(url=base_url, json=payload)

    assert res.status_code == 500
