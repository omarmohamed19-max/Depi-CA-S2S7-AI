from pre import drop_cols, get_data_info
from config import cols_drop, num_col, cat_cols
import pandas as pd

drop_cols(df, cols_drop)
get_data_info(df)