import os
from gendiff.modules.diff import generate_diff

current_dir = os.path.dirname(os.path.abspath(__file__))
test_data_json_dir = 'fixtures/json'
test_data_yaml_dir = 'fixtures/yaml'
results_dir = 'fixtures/results'


def test_json():
    file1_path = os.path.join(current_dir, f'{test_data_json_dir}', 'simple_file1.json')
    file2_path = os.path.join(current_dir, f'{test_data_json_dir}', 'simple_file2.json')
    result_path = os.path.join(current_dir, f'{results_dir}', 'simple_stylish_result.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path) == result_data


def test_yaml():
    file1_path = os.path.join(current_dir, f'{test_data_yaml_dir}', 'simple_file1.yml')
    file2_path = os.path.join(current_dir, f'{test_data_yaml_dir}', 'simple_file2.yml')
    result_path = os.path.join(current_dir, f'{results_dir}', 'simple_stylish_result.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path) == result_data


def test_nested_json_stylish():
    file1_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file1.json')
    file2_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file2.json')
    result_path = os.path.join(current_dir, f'{results_dir}', 'nested_result_stylish.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path) == result_data
    assert generate_diff(file1_path, file2_path, 'stylish') == result_data


def test_nested_yaml_plain():
    file1_path = os.path.join(current_dir, f'{test_data_yaml_dir}', 'nested_file1.yml')
    file2_path = os.path.join(current_dir, f'{test_data_yaml_dir}', 'nested_file2.yml')
    result_path = os.path.join(current_dir, f'{results_dir}', 'nested_result_plain.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path, 'plain') == result_data


def test_nested_json_plain():
    file1_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file1.json')
    file2_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file2.json')
    result_path = os.path.join(current_dir, f'{results_dir}', 'nested_result_plain.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path, 'plain') == result_data


def test_nested_json_json():
    file1_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file1.json')
    file2_path = os.path.join(current_dir, f'{test_data_json_dir}', 'nested_file2.json')
    result_path = os.path.join(current_dir, f'{results_dir}', 'nested_result_json.txt')
    result_data = open(result_path, 'r').read()

    assert generate_diff(file1_path, file2_path, 'json') == result_data
