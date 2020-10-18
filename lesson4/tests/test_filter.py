import pytest
from random import randint


@pytest.mark.parametrize('user_id', range(1, 11))
def test_filter_user_id(session, base_url, user_id):
    res_all = session.get(base_url)
    assert res_all.status_code == 200
    res_all_j = res_all.json()
    count_user = sum(i["userId"] == user_id for i in res_all_j)

    res_one = session.get(url=f'{base_url}/?userId={user_id}')
    res_one_j = res_one.json()
    len_res_one = len(res_one_j)
    assert res_one.status_code == 200
    assert len_res_one == count_user
    for r in res_one_j:
        assert r["userId"] == user_id


@pytest.mark.parametrize('item_id', (1, randint(2, 199), 200))
def test_filter_id(session, base_url, item_id):
    res = session.get(url=f'{base_url}/?id={item_id}')
    res_j = res.json()
    assert res.status_code == 200
    assert len(res_j) == 1
    assert res_j[0]["id"] == item_id


@pytest.mark.parametrize('completed', ['true', 'false'])
def test_filter_completed(session, base_url, completed):
    res_all = session.get(base_url)
    assert res_all.status_code == 200
    res_all_j = res_all.json()
    count_compl = sum(i["completed"] == (completed == "true") for i in res_all_j)
    res_one = session.get(url=f'{base_url}/?completed={completed}')
    res_one_j = res_one.json()
    assert res_one.status_code == 200
    assert len(res_one_j) == count_compl


@pytest.mark.parametrize('title', ['test', 'sed et ea eum'])
def test_filter_title(session, base_url, title):
    res_all = session.get(base_url)
    assert res_all.status_code == 200
    res_all_j = res_all.json()
    count_title = sum(i["title"] == title for i in res_all_j)
    res_one = session.get(url=f'{base_url}/?title={title}')
    res_one_j = res_one.json()
    assert res_one.status_code == 200
    assert len(res_one_j) == count_title


@pytest.mark.parametrize('user_id', [1, randint(2, 10), 11])
@pytest.mark.parametrize('completed', ['true', 'false'])
def test_filter_user_id_completed(session, base_url, user_id, completed):
    res_all = session.get(base_url)
    assert res_all.status_code == 200
    res_all_j = res_all.json()
    count_uc = sum(
        i["userId"] == user_id and i["completed"] == (completed == "true")
        for i in res_all_j
    )
    res_one = session.get(url=f'{base_url}/?userId={user_id}&completed={completed}')
    assert res_one.status_code == 200
    res_one_j = res_one.json()
    assert len(res_one_j) == count_uc


@pytest.mark.parametrize('user_id', [1, randint(2, 10), 11])
@pytest.mark.parametrize('item_id', [1, randint(2, 199), 200])
def test_filter_user_id_item_id(session, base_url, user_id, item_id):
    res_all = session.get(base_url)
    assert res_all.status_code == 200
    res_all_j = res_all.json()
    count_uc = sum(
        i["userId"] == user_id and i["id"] == item_id
        for i in res_all_j
    )
    res_one = session.get(url=f'{base_url}/?userId={user_id}&id={item_id}')
    assert res_one.status_code == 200
    res_one_j = res_one.json()
    len_res_one = len(res_one_j)
    assert len_res_one == count_uc
    if len_res_one > 0:
        for r in res_one_j:
            assert r["userId"] == user_id
            assert r["id"] == item_id


@pytest.mark.parametrize('user_id', [-1, 12, 'test', None])
def test_filter_user_id_negative(session, base_url, user_id):
    res_one = session.get(url=f'{base_url}/?userId={user_id}')
    res_one_j = res_one.json()
    assert res_one.status_code == 200
    assert len(res_one_j) == 0


@pytest.mark.parametrize('item_id', [0, 201, None, 'test'])
def test_filter_id_negative(session, base_url, item_id):
    res = session.get(url=f'{base_url}/?id={item_id}')
    res_j = res.json()
    assert res.status_code == 200
    assert len(res_j) == 0


def test_filter_completed_negative(session, base_url):
    res_one = session.get(url=f'{base_url}/?completed=')
    res_one_j = res_one.json()
    assert res_one.status_code == 200
    assert len(res_one_j) == 0


def test_filter_title_negative(session, base_url):
    res_one = session.get(url=f'{base_url}/?title=')
    res_one_j = res_one.json()
    assert res_one.status_code == 200
    assert len(res_one_j) == 0


