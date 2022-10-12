"""
Rubric: 
Functioning: 
- Can use get (for row 1pt, for col 1pt, for cell 1pt)
- Can use set (for cell 1pt)
- Can exit (1pt)
- Can loadcsv (1pt, note we will use a different csv to test)
- Can list row length (1pt), column names (1pt)
- Additional action 1. Should be using the DataFrame (2pts)
- Additional action 2. (either on DF or elsewise, 2pts)
- Does have easter egg (1pt)
- Does have intro and/or help page (1pt)
Robust:
- Handles bad input gracefully (2pts)
- Methods have at least a single comment explaining purpose (1pt)
Elegant:
- Has actions separated usefully into methods. (1pt)
- Has other refactoring (subjective, 2pts)
Creative: 
- Be creative. This might involve a useful help message, some interesting feature, or a refactoring that uses novel components. (5pts)
"""
import pandas as pd
from pathlib import Path
from typing import Callable, Dict, Optional


def loadcsv(filestr: str) -> Optional[pd.DataFrame]:
    """Loads a csv file into the DataFrame."""
    filepath = Path(filestr)
    if not filepath.exists():
        print("Sorry, I couldn't find that file.")
        return
    if not filepath.suffix == ".csv":
        print("Sorry, I can only load .csv files.")
        return
    print(f"Loading {filepath.name}...")
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower()
    return df


def check_df(
    df: Optional[pd.DataFrame],
    rownum: Optional[int] = None,
    colname: Optional[str] = None,
) -> bool:
    """Prints the length of a dataframe"""
    if df is None:
        print("Sorry, you need to load a file first.")
        return False
    elif rownum is not None and rownum not in df.index:
        print("Sorry, I couldn't find that row.")
        return False
    elif colname is not None and colname.strip() not in df.columns:
        print(
            "Sorry, I couldn't find that column. Type 'list columns' to see a list of columns."
        )
        return False
    return True


def get_help(command_dict: Dict[str, Callable]) -> None:
    """Prints a help message for using the Pandas Explorer."""
    print("### Pandas Explorer Help ###")
    for command, func in command_dict.items():
        print(f"{command}: {func.__doc__}")


def set_cell(df: Optional[pd.DataFrame], rownum: int, colname: str, value: str) -> None:
    """Sets a value in a dataframe"""
    df_ok = check_df(df, rownum=rownum, colname=colname)
    if not df_ok:
        return
    df.loc[rownum, colname] = value
    print("Value set.")


def get_column(df: pd.DataFrame, colname: str) -> None:
    """Prints information about a column from a dataframe"""
    df_ok = check_df(df, colname=colname)
    if not df_ok:
        return
    print(f"Column {colname} has {len(df[colname].unique())} unique values.")
    print("The first 10 values are:")
    print(df[colname].head(10))


def exit_file():
    """Exits the program."""
    print("Goodbye!")
    exit()


def list_columns(df: pd.DataFrame) -> None:
    """Prints the columns in a dataframe."""
    df_ok = check_df(df)
    if not df_ok:
        return
    print("The columns in this file are:")
    print(df.columns.tolist())


def get_cell(df: pd.DataFrame, rownum: int, colname: str) -> None:
    """Prints information about a cell from a dataframe"""
    df_ok = check_df(df, rownum=rownum, colname=colname)
    if not df_ok:
        return
    print(
        f"The value at row {rownum} and column {colname} is {df.loc[rownum, colname]}."
    )


def rock_paper_scissors():
    game_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    print("You want to fight me? Fine.")
    choice = input("Rock, paper, or scissors? ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("You can't even play the game right. I win.")
        return
    print(f"You chose {choice}. I choose {game_dict[choice]}!")
    print("I win!")


def get_row(df: pd.DataFrame, rownum: int) -> None:
    """Prints information about a row from a dataframe"""
    df_ok = check_df(df, rownum=rownum)
    if not df_ok:
        return
    print(f"The values at row {rownum} are:")
    print(df.loc[rownum])


def list_rows(df: Optional[pd.DataFrame]) -> None:
    """Prints the number of rows in a dataframe."""
    if df is None:
        print("Sorry, you need to load a file first.")
        return
    print(f"This file has {len(df)} rows.")

def list_incomplete_rows(df: pd.DataFrame) -> None:
    """Prints the number of rows in a dataframe."""
    df_ok = check_df(df)
    if not df_ok:
        return
    n_incomplete = df.isnull().sum(axis=1).sum()
    print(f"This file has {n_incomplete} incomplete rows. ({n_incomplete/len(df)*100:.2f}%)")

def get_random_row(df: pd.DataFrame) -> None:
    """Prints a random row from a dataframe"""
    df_ok = check_df(df)
    if not df_ok:
        return
    print("Here's a random row:")
    print(df.sample(1))

AVAILABLE_COMMANDS = {
    "get col <column name>": get_column,
    "get cell <row number> <column name>": get_cell,
    "set cell <row number> <column name> <value>": set_cell,
    "list rows": list_rows,
    "get row <row number>": get_row,
    "random row": get_random_row,
    "incomplete rows": list_incomplete_rows,
    "exit": exit_file,
    "loadcsv": loadcsv,
    "list columns": list_columns,
    "help": get_help,
}
implemented_commands = {k: v for k, v in AVAILABLE_COMMANDS.items() if v is not None}


def main():
    print("### Welcome to the Pandas Explorer! ###")
    print("- Type 'help' for a list of commands.")
    print("- Type 'exit' to quit.")
    df = None
    while True:
        print("What would you like to do now?")
        command = input(">>> ").lower()
        match command.split():
            case ["help"]:
                get_help(command_dict=implemented_commands)
            case ["exit"]:
                exit_file()
            case ["loadcsv", filepath]:
                df = loadcsv(filepath)
            case ["get", "row", rownum]:
                get_row(df, int(rownum))
            case ["get", "col", colname]:
                get_column(df, colname)
            case ["get", "cell", rownum, colname]:
                get_cell(df, int(rownum), colname)
            case ["set", "cell", rownum, colname, value]:
                set_cell(df, int(rownum), colname, value)
            case ["list", "columns"]:
                list_columns(df)
            case ["list", "rows"]:
                list_rows(df)
            case ["fight", "me"]:
                rock_paper_scissors()
            case ["incomplete", "rows"]:
                list_incomplete_rows(df)
            case ["random", "row"]:
                get_random_row(df)
            case _:
                print(
                    "Sorry, I didn't understand that command. Type 'help' for a list of commands."
                )


if __name__ == "__main__":
    main()
