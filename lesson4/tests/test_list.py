from .conftest import TODOS_MAX


def test_listing_all_resources(session, base_url):
    res = session.get(url=f'{base_url}')
    assert res.status_code == 200
    assert len(res.json()) == TODOS_MAX
