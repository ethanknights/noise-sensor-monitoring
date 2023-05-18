# Pipeline order (WIP!)
import sys
sys.path.append('sensor-pipeline')
import importlib
import functions_simulate
importlib.reload(functions_simulate)  # For local debugging
import os
import pandas as pd

# Init environment
out_dir = 'derivatives'
os.makedirs(out_dir, exist_ok=True)

# If we don't have data yet, simulate a parquet dB timeseries (written to ./derivatives):
# df = functions_simulate.simulate_streamed_timeseries_as_df(600)
df = pd.read_parquet(os.path.join(out_dir, 'tS_duration-600_created-20230518_111638' + '.parquet'))


