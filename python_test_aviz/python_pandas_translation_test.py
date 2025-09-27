import logging

import pandas as pd
from custom_python_logger import build_logger, get_logger
from python_pandas_translation import pandas_row

logger = get_logger(__name__)


def main() -> None:
    sample_df = pd.DataFrame(
        {
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [30, 25, 35]
        }
    )

    logger.info(pandas_row.get_rows(sample_df, start=0, end=1))


if __name__ == '__main__':
    _ = build_logger(
        project_name='Logger Project Test',
        log_level=logging.DEBUG,
        # extra={'user': 'test_user'}
    )

    main()
