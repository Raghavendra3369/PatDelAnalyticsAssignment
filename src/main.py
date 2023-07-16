from fastapi import FastAPI, status
from typing import List

from src import Operations
from src.env import dir_path

app = FastAPI()

keyword_file_dict = Operations.get_keyword_file_dict(dir_path)


@app.get('/search/{keyword}', status_code=status.HTTP_200_OK, response_model=List[str])
def get_files_containing_keyword(keyword: str):
    matched_files = keyword_file_dict.get(keyword, [])
    return matched_files
