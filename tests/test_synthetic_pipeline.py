from pathlib import Path

from src.analysis import (
    load_data,
    clean_data,
    run_primary_analysis,
    expected_output_contract,
)


def test_synthetic_pipeline():
    data_path = Path(
        "tests/fixtures/synthetic_student_data.csv"
    )

    df = load_data(data_path)
    cleaned = clean_data(df)

    result = run_primary_analysis(cleaned)

    # Check that the expected output contract is satisfied
    assert expected_output_contract(result)

    # Check basic output requirements
    assert result["test"] == "Kruskal-Wallis"
    assert result["n"] > 0
    assert result["statistic"] >= 0
    assert 0 <= result["p_value"] <= 1
