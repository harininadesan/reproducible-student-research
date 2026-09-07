import pandas as pd
from scipy.stats import kruskal


def load_data(path):
    """Load the student dataset."""
    return pd.read_csv(path)


def clean_data(df):
    """Apply the preregistered inclusion and exclusion rules."""
    required_columns = ["studytime", "G3"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    data = df[required_columns].copy()

    # Remove missing exposure/outcome values
    data = data.dropna(subset=["studytime", "G3"])

    # Keep only documented study-time categories
    data = data[data["studytime"].isin([1, 2, 3, 4])]

    # Keep valid final grades
    data = data[data["G3"].between(0, 20)]

    # Remove exact duplicate observations
    data = data.drop_duplicates()

    return data


def run_primary_analysis(df):
    """Run the preregistered Kruskal-Wallis test."""
    groups = [
        group["G3"].values
        for _, group in df.groupby("studytime")
    ]

    if len(groups) < 2:
        raise ValueError(
            "At least two study-time groups are required."
        )

    statistic, p_value = kruskal(*groups)

    return {
        "test": "Kruskal-Wallis",
        "statistic": statistic,
        "p_value": p_value,
        "n": len(df),
    }


def expected_output_contract(result):
    """Return the required output fields."""
    required_fields = [
        "test",
        "statistic",
        "p_value",
        "n",
    ]

    missing = [
        field for field in required_fields
        if field not in result
    ]

    if missing:
        raise AssertionError(
            f"Missing output fields: {missing}"
        )

    return True
