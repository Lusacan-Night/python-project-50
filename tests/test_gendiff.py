import json
import pytest

from gendiff.scripts.gendiff import generate_diff

file_1 = "tests/fixtures/file1.json"
file_2 = "tests/fixtures/file2.json"
filepath1 = "tests/fixtures/filepath1.yml"
filepath2 = "tests/fixtures/filepath2.yml"
result = "tests/fixtures/result.txt"

@pytest.fixture
def res():
    with open(result) as r:
        return r.read().replace('\n', '')


def test_json(res):
    assert generate_diff(file_1, file_2) == res
    

def test_yml(res):
    assert generate_diff(filepath1, filepath2) == res
