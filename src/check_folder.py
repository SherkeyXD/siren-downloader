from pathlib import Path


def check_folder(name):
    path = Path(name).expanduser()
    if path.exists():
        return True
    else:
        path.mkdir(parents=True, exist_ok=True)
        return False