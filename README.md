This is a simple Python script that substitutes tags in DNA files in Deep Rock Galactic. The DNA files contain the tags that the game will use when generating new rooms. By substituting the tags, we can create missions that use exclusively our custom rooms, see https://github.com/vonacht/drg-room-editor/.

The script uses uv to manage the dependencies. The tags are inside a configuration file in config/config.json:

```json
#config/config.json
{
  "DNA": {
    "Mining": [
      "DNA_2_02.uasset",
      "DNA_2_03.uasset",
      "DNA_2_04.uasset",
      "DNA_2_05.uasset"
   ]
  },
  "Tags": {
    "Mining": {
      "Rooms.Linear.Small": "Rooms.Linear.CustomTest",
      "Rooms.Linear.Medium": "Rooms.Linear.CustomMedium",
      "Rooms.Linear.Big": "Rooms.Linear.CustomBig",
      "Rooms.Linear.MiniLevel": "Rooms.Linear.CustomBig"
    }
}
```

The list in `Mining` in the `DNA` tells the script which assets to patch for that mission type. You can check the names for each [here](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vSrIEAbg8iWAKqYcxuMYua-lhWncY8UWThzlHun5L2CQ9oNeZt9AzvHHO7xRRDmHY51jN16MnnDerua/pubhtml). If you want to keep a certain mission without modifying just remove it from the list.

The map in `Tags` contains the old vanilla tag and the new tags for each. 

After editing the config, you can run the script with:

`uv run main.py`

The patched DNA files will be placed in the assets/ directory. A different config file can be provided with option -c:

`uv run main.py -c myconfigfile.json`

and a different output path for the patched UAssets can be specified with option -o:

`uv run main.py -o ~/modding/DNA_files/`


