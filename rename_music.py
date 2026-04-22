import os
INPUT_DIR = r"output\ChaosStation\Sound\stream"

rename_map = {
    # --- World map BGM ---
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
    "WarioWare_ Smooth Moves  - Level Select.brstm": "STRM_BGM_MENU.brstm",

    # --- In-level BGM ---
    # Ground levels
    "Donkey Kong Country_ Tropical Freeze - Grassland Groove (Medley).brstm": "STRM_BGM_CHIJOU.brstm",
    # Athletic / fast-scroll levels
    "Donkey Kong Country 2_ Diddy's Kong Quest - Stickerbrush Symphony.brstm": "athletic_lr.n.32.brstm",
    # Underground / cave levels
    "Super Mario Galaxy - Buoy Base Galaxy (CD Version).brstm": "STRM_BGM_CHIKA.brstm",
    # Ghost house levels
    "Ghostly Galaxy - Super Mario Galaxy Music.brstm": "BGM_OBAKE.32.brstm",
    # Airship levels
    "Super Mario Galaxy - Battlerock Galaxy - Main Track.brstm": "BGM_HIKOUSEN.32.brstm",
    # Tower levels
    "Donkey Kong Country_ Tropical Freeze - Volcano Dome (Boss Battle).brstm": "toride_lr.n.32.brstm",
    # Castle levels
    "Super Mario Galaxy 2 - Bowser's Galaxy Generator.brstm": "BGM_SIRO.32.brstm",
    # Tower boss fight (Kamek)
    "Paper Mario_ Sticker Star - Malevolent Magikoopa, Kamek Battle.brstm": "BGM_TORIDE_BOSS.32.brstm",
    # Castle boss fight (Bowser) — same track, second copy
    "Super Mario Galaxy 2 - Megahammer_castle.brstm": "shiro_boss_lr.n.32.brstm",
    # Forest levels
    "Donkey Kong Country 2 (GBA) - Forest Interlude.brstm": "mori_lr.ry.32.brstm",
    # Lava levels
    "Donkey Kong Country Returns - Furious Fire.brstm": "kazan_lr.n.32.brstm",
    # Sky levels
    "Mario Kart 8 - Cloudtop Cruise.brstm": "STRM_BGM_SANBASHI.brstm",
}

for old_name, new_name in rename_map.items():
    old_path = os.path.join(INPUT_DIR, old_name)
    new_path = os.path.join(INPUT_DIR, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"Not found: {old_name}")
