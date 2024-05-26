import json
import pytest

from gendiff.scripts.gendiff import generate_diff

file_1 = "tests/fixtures/file1.json"
file_2 = "tests/fixtures/file2.json"
result = "tests/fixtures/result.txt"

@pytest.fixture
def res():
    with open(result) as r:
        return r.read().replace('\n', '')

def test(res):
    assert generate_diff(file_1, file_2).replace('\n', '') == res
    
        