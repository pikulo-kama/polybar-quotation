import json


def save_json(path: str, obj):
    """
    Save JSON object to specified path
    """
    with open(path, 'wt') as f:
        json.dump(obj, f)


def load_json(path):
    with open(path, 'rt') as f:
        data = json.load(f)
    return data


def q_splitter(string: str, line_len: int):
    """
    Splits one large quote in smaller (with specified line length)
    """
    iterations = len(string) // line_len + 1
    parts = [[] for _ in range(iterations)]
    current = 0

    for w in string.split(' '):

        if len(' '.join(parts[current])) > line_len:
            current += 1

        parts[current].append(w)

    for i, w_list in enumerate(parts):
        parts[i] = ' '.join(w_list)

    return parts
