import json
import pytest
import requests
import responses


@responses.activate
def test_simulate_data_cannot_be_found(session, base_url):
    responses.add(
        responses.GET,
        base_url,
        json={"error": "No data"},
        status=404
    )

    response = session.get(base_url)
    assert response.status_code == 404


@responses.activate
def test_unmatched_endpoint_raises_connectionerror(session, base_url):
    with pytest.raises(requests.exceptions.ConnectionError):
        session.get(f'{base_url}/1234')


@responses.activate
def test_responses_can_raise_error_on_demand(session, base_url):
    responses.add(
        responses.GET,
        base_url,
        body=RuntimeError('A runtime error occurred')
    )
    with pytest.raises(RuntimeError) as re:
        session.get(base_url)
        assert str(re.value) == 'A runtime error occurred'
