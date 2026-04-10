import os
INPUT_DIR = r"output\ChaosStation\Sound\stream"

rename_map = {
    "Super Mario 3D World - Super Bell Hill.brstm": "select_map01_nohara_lr.n.32.brstm",
    "The Legend of Zelda_ Ocarina of Time - Gerudo Valley.brstm": "select_map02_sabaku.ry.32.brstm",
    "Kirby Air Ride - Air Ride - Frozen Hillside.brstm": "select_map03_yuki.ry.32.brstm",
    "Donkey Kong Country (SNES) - Aquatic Ambiance (Remastered by TroyAnthony).brstm": "select_map04_umii.ry.32.brstm",
    "Super Mario Odyssey - Steam Gardens.brstm": "BGM_MAP_W5.32.brstm",
    "Mario Kart 8 - Wii Grumble Volcano.brstm": "select_map06_cliff_lr.n.32.brstm",
    "Super Mario Galaxy - Gusty Garden Galaxy.brstm": "BGM_MAP_W7.32.brstm",
    "Mario & Luigi_ Bowser's Inside Story - In the Final (Restored).brstm": "BGM_MAP_W8.32.brstm",
    "Mario Kart Wii - Rainbow Road.brstm": "select_map09_rainbow_lr.n.32.brstm",
    "Super Mario Galaxy - Overture.brstm": "title_lr.ry.32.brstm",
    "Super Smash Bros. Brawl - Final Destination.brstm": "BGM_LAST_BOSS1_lr.ry.32.brstm",
    "Super Smash Bros. Ultimate - Galeem_Dharkon.brstm": "STRM_BGM_LAST_BOSS2.brstm",
    "WarioWare_ Smooth Moves  - Level Select.brstm": "STRM_BGM_MENU.brstm"
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(INPUT_DIR, old_name)
    new_path = os.path.join(INPUT_DIR, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"Not found: {old_name}")
