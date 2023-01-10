from gendiff.modules.diff import generate_diff;
import os
import json

def test_1():
    print(os.getcwd())
    file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file1.json')
    file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file2.json')
    result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'result.json')
    result_data = json.load(open(result_path, 'r'))

    # print('result_data', result_data)
    # print('generate_diff', type(generate_diff(file1_path, file2_path)))

    assert generate_diff(file1_path, file2_path) == json.dumps(result_data)

