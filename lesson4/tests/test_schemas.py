import json
from jsonschema import validate, RefResolver
import os


def assert_valid_schema(data, schema_file):
    schema_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schemas')
    resolver = RefResolver('file://' + schema_dir + '/', None)
    fp = os.path.join(schema_dir, schema_file)
    print(fp)
    with open(fp) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema, resolver=resolver)


def test_get_todo(session, base_url):
    res = session.get(url=f'{base_url}/1')
    assert_valid_schema(res.json(), 'todo_schema.json')


def test_get_todos(session, base_url):
    res = session.get(url=f'{base_url}')
    assert_valid_schema(res.json(), 'todos_schema.json')
