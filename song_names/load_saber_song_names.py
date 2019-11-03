# %%
import glob
import numpy as np
import pandas as pd
import json
import os

# %%
maps_path_location = "BeatSaberMaps"
all_map_paths = glob.glob(maps_path_location + "/*")
assert len(
    all_map_paths) > 1, f"There are no songs/maps in the specified location {maps_path_location}"
song_names = []

for path in all_map_paths:
    filepath = path+'/info.dat'
    if os.path.isfile(filepath):
        with open(filepath) as json_file:
            data = json.load(json_file)
            song_names.append(data['_songName'])
# %%
song_names_pd = pd.Series(song_names)
output_filename = "song_names.csv"
song_names_pd.to_csv(output_filename, header=False)
print(f"Wrote {len(song_names_pd)} song titles to {output_filename}")

# %%
