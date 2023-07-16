import json
import os
from collections import defaultdict


def get_keyword_file_dict(dir_path):
    keyword_file_dict = defaultdict(list)
    for filename in os.listdir(dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(dir_path, filename)
            with open(file_path) as file:
                data = json.load(file)
                for keyword in data.keys():
                    keyword_file_dict[keyword].append(filename)
    return keyword_file_dict
