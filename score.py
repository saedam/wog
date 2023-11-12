
from utils import SCORES_FILE_NAME

def get_value_from_scores_file(file_path):
    line = ""
    score = 0

    try:
        with open(SCORES_FILE_NAME) as file:
            line = file.readline()

        if line.isnumeric():
            score = int(line)
        else:
            score = 0
    except:
        score = 0

    return score

def save_value_to_scores_file(file_path, score):
    with open(SCORES_FILE_NAME, "w") as file:
        file.write(f"{score}")


def get_score():
    return get_value_from_scores_file(SCORES_FILE_NAME)

def add_score(difficulty):
    score = get_value_from_scores_file(SCORES_FILE_NAME)
    score += difficulty * 3 + 5
    save_value_to_scores_file(SCORES_FILE_NAME, score)

