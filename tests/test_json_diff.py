from gendiff.modules.diff import generate_diff, get_ast;
import os

# def test_json():
#     print(os.getcwd())
#     file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file1.json')
#     file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file2.json')
#     result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'results', 'result.txt')
#     result_data = open(result_path, 'r').read()

#     assert generate_diff(file1_path, file2_path) == result_data

# def test_yaml():
#     file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'yaml', 'file1.yml')
#     file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'yaml', 'file2.yml')
#     result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'results', 'result.txt')
#     result_data = open(result_path, 'r').read()

#     assert generate_diff(file1_path, file2_path) == result_data

def test_big_json():
    print(os.getcwd())
    file1_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file11.json')
    file2_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'json', 'file21.json')
    result_path = os.path.join(os.getcwd(), 'tests', 'fixtures', 'results', 'result1.txt')
    result_data = open(result_path, 'r').read()

    # print(generate_diff(file1_path, file2_path))
    print('heres', generate_diff(file1_path, file2_path))
    print(f"tee\nddd")

    assert generate_diff(file1_path, file2_path) == result_data

