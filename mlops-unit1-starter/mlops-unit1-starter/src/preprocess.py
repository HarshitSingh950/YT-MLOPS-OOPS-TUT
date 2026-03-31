from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "iris.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    print("--- Dataset Statistics ---")
    print(df.describe())

    print("\n--- Feature Correlation Matrix ---")
    print(df.drop("species", axis=1).corr())


if __name__ == "__main__":
    main()
