import pandas as pd

from python_pandas_translation import pandas_row

def main():
    sample_df = pd.DataFrame(
            {
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [30, 25, 35]
            }
        )

    print(pandas_row.get_rows(sample_df, start=0, end=1))


if __name__ == '__main__':
    main()
