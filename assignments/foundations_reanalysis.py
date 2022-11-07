"""
Reanalysis of the Anthropic paper for "Foundations of Social Data Science" course
This script will
- load the jsonl.gz file
- extract the data
- plot the success rates for the different models
"""
import gzip
import json
import pandas as pd
from pathlib import Path
from typing import List

DATA_DIR = Path("../data")


def read_jsonl_gz(filename: Path) -> List[dict]:
    with gzip.open(filename, "rt", encoding="utf8") as f:
        data = json.load(f)
    return data


def main():
    data_file = DATA_DIR / "red_team_attempts.jsonl.gz"
    data = read_jsonl_gz(data_file)

    df = pd.DataFrame(data)
    # select only the relevant columns
    df = df[["red_team_member_id", "num_params", "model_type", "rating"]]
    # save the data to a csv file
    df.to_csv(DATA_DIR / "red_team_attempts.csv", index=False)

    pass


if __name__ == "__main__":
    main()
