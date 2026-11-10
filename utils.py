from pathlib import Path
import pandas as pd


# Project Configuration
PROJECT_ROOT = Path(file).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

EXPERIMENT_DIR = PROJECT_ROOT / "experiments"


def load_data(filename: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the project's raw data directory.
    """

    file_path = RAW_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}\n"
            f"Please place '{filename}' inside: {RAW_DATA_DIR}"
        )

    df = pd.read_csv(file_path, encoding="latin-1")

    if df.empty:
        raise ValueError("The loaded dataset is empty.")

    return df