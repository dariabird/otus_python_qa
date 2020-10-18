def test_update_completed(session, base_url):
    todo_id = 1
    res = session.get(url=f'{base_url}/{todo_id}')
    title = res.json()['title']
    user_id = res.json()['userId']
    completed = not res.json()['completed']
    payload = {'completed': completed}
    res = session.patch(url=f'{base_url}/{todo_id}', json=payload)

    assert res.status_code == 200
    res_json = res.json()
    assert res_json['title'] == title
    assert res_json['userId'] == user_id
    assert res_json['completed'] == completed
    assert res_json['id'] == todo_id


def test_update_title(session, base_url):
    todo_id = 1
    res = session.get(url=f'{base_url}/{todo_id}')
    user_id = res.json()['userId']
    title = res.json()['title'] + "test"
    completed = res.json()['completed']
    payload = {'title': title}
    res = session.patch(url=f'{base_url}/{todo_id}', json=payload)
    assert res.status_code == 200
    res_json = res.json()
    assert res_json['id'] == todo_id
    assert res_json['userId'] == user_id
    assert res_json['title'] == title
    assert res_json['completed'] == completed


def test_update_user_id(session, base_url):
    todo_id = 1
    new_user_id = 2
    res = session.get(url=f'{base_url}/{todo_id}')
    title = res.json()['title']
    completed = res.json()['completed']
    payload = {'userId': new_user_id}
    res = session.patch(url=f'{base_url}/{todo_id}', json=payload)

    assert res.status_code == 200
    res_json = res.json()

    assert res_json['id'] == todo_id
    assert res_json['userId'] == new_user_id
    assert res_json['title'] == title
    assert res_json['completed'] == completed


def test_update_todo_id(session, base_url):
    todo_id = 1
    new_todo_id = 2
    res = session.get(url=f'{base_url}/{todo_id}')
    user_id = res.json()['userId']
    title = res.json()['title']
    completed = res.json()['completed']
    payload = {'id': new_todo_id}
    res = session.patch(url=f'{base_url}/{todo_id}', json=payload)

    assert res.status_code == 200
    res_json = res.json()
    assert res_json['id'] == new_todo_id
    assert res_json['userId'] == user_id
    assert res_json['title'] == title
    assert res_json['completed'] == completed
