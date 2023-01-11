from gendiff.modules.diff import generate_diff;
import os
import json

def test_json():
    print(os.getcwd())
    file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file1.json')
    file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file2.json')
    result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'results', 'result.txt')
    result_data = open(result_path, 'r').read()
    print('result_data', result_data)

    # print('result_data', result_data)
    # print('generate_diff', type(generate_diff(file1_path, file2_path)))

    assert generate_diff(file1_path, file2_path) == result_data

def test_yaml():
    file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'yaml', 'file1.yml')
    file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'yaml', 'file2.yml')
    result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'results', 'result.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path) == result_data

