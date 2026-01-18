from pythonnet import load

load("coreclr")
import clr
import json
from pathlib import Path

def JSON_to_uasset(input_json: dict, path: str):
    # Load the assembly. The dll_path needs to be an absolute reference to libs/UAssetAPI.dll:
    dll_path = Path.cwd() / "libs" / "UAssetAPI.dll"
    clr.AddReference(str(dll_path))
    # We load the methods to read from JSON and save:
    from UAssetAPI import UAsset
    from UAssetAPI import UnrealTypes

    # DeserializeJson expects a string:
    UAsset.DeserializeJson(json.dumps(input_json)).Write(str(path))

def UAsset_to_string(path_to_uasset: str) -> dict:
    # Load the assembly. The dll_path needs to be an absolute reference to libs/UAssetAPI.dll:
    dll_path = Path.cwd() / "libs" / "UAssetAPI.dll"
    clr.AddReference(str(dll_path))
    # We load the methods to read from JSON and save:
    from UAssetAPI import UAsset
    from UAssetAPI import UnrealTypes

    return UAsset(
        str(path_to_uasset), UnrealTypes.EngineVersion.VER_UE4_27
    ).SerializeJson()
