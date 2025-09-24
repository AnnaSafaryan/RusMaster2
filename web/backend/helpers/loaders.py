import json
import pickle

# TODO: умный лоадер-дампер для всего


def json_load(path):
    return json.load(fp=open(path, encoding="utf-8"))


def json_dump(data, path):
    json.dump(
        obj=data,
        fp=open(path, "w", encoding="utf-8"),
        indent=4,
        ensure_ascii=False,
    )


def pickle_load(path):
    return pickle.load(path)


def pickle_dump(data, path):
    with path.open("wb") as file:
        pickle.dump(obj=data, file=file)
