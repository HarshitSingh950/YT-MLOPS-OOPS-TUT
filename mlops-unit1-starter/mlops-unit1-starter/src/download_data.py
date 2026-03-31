from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "iris.csv"


def main() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    urlretrieve(DATA_URL, DATA_PATH)
    print(f"Dataset downloaded to: {DATA_PATH}")


if __name__ == "__main__":
    main()
