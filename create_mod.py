"""
Chaos Station v1 — Custom Level Pack for NSMBW
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.level_builder import LevelBuilder, AreaBuilder
from tools.sprite_db import *
from tools.course_parser import Entrance, Background, Bounding, Zone


def create_level_1_1():
    """Level 1-1: Welcome to Chaos — Harder grassy gauntlet."""
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_GRASS)
    a.set_time(350)
    a.set_background(258)  # World 1 grass/sky

    # Zone (pixels): same height as original, wide level
    ZX, ZY = 512, 256
    ZW, ZH = 7200, 385
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_OVERWORLD, visibility=16)

    # Entrances
    # Entrance 0 = level start. Entrance 1 = midway respawn point (past midway flag at TX+109)
    a.add_entrance(0, x=ZX + 48, y=ZY + 320, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2000, y=576, etype=ENTRANCE_NORMAL, zone_id=0)

    TX = 32   # tile X offset (matches zone start)
    GY = 38   # ground Y in tiles

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Welcoming start (safe zone, then easy jumps) ───
    a.add_ground(TX, GY, width=15, height=4)

    # First gap (3 tiles) — gentle intro
    a.add_ground(TX + 18, GY, width=10, height=4)

    # ? blocks above the second platform
    a.add_question_block(TX + 20, GY - 4)              # Coin
    a.add_question_block(TX + 22, GY - 4, contents=1)  # Mushroom/Fire Flower
    a.add_question_block(TX + 24, GY - 4)              # Coin

    # ─── Section 2: Staircase and elevated section ───
    a.add_staircase(TX + 30, GY, steps=5, direction=1)
    a.add_ground(TX + 35, GY - 5, width=8, height=2)
    a.add_ground(TX + 35, GY - 3, width=8, height=7)

    # Drop to lower area with running jump required
    a.add_ground(TX + 46, GY, width=5, height=4)
    # Wide gap (5 tiles) — need running jump
    a.add_ground(TX + 54, GY, width=20, height=4)

    # ─── Section 3: Pipe gauntlet ───
    a.add_ground(TX + 76, GY, width=30, height=4)
    a.add_pipe(TX + 80, GY - 3, height=3)
    a.add_pipe(TX + 86, GY - 5, height=5)
    a.add_pipe(TX + 92, GY - 2, height=2)
    a.add_pipe(TX + 97, GY - 4, height=4)
    # ? blocks between pipes
    a.add_question_block(TX + 83, GY - 4)
    a.add_question_block(TX + 89, GY - 6)
    a.add_question_block(TX + 95, GY - 5)  # Removed extra powerup

    # ─── Section 5: Midway & rising challenge ───
    a.add_ground(TX + 108, GY, width=12, height=4)

    # Tricky platforming: alternating heights
    a.add_ground(TX + 123, GY - 2, width=4, height=2)
    a.add_ground(TX + 130, GY - 4, width=3, height=2)
    a.add_ground(TX + 136, GY - 2, width=4, height=2)
    a.add_ground(TX + 143, GY, width=4, height=4)

    # ? block in hard-to-reach spot
    a.add_question_block(TX + 131, GY - 7)

    # ─── Section 6: Double staircase with enemies ───
    a.add_ground(TX + 149, GY, width=25, height=4)
    a.add_staircase(TX + 155, GY, steps=4, direction=1)
    # Valley
    a.add_ground(TX + 160, GY - 4, width=3, height=1)
    # Down staircase
    a.add_ground(TX + 164, GY - 3, width=1, height=1)
    a.add_ground(TX + 165, GY - 2, width=1, height=1)
    a.add_ground(TX + 166, GY - 1, width=1, height=1)
    a.add_ground(TX + 167, GY, width=7, height=4)

    # ─── Section 7: Final rush ───
    a.add_ground(TX + 177, GY, width=8, height=4)
    # Wide gap with brick bridge (breakable!)
    a.add_gap_bridge(TX + 187, GY - 1, width=5)
    a.add_ground(TX + 194, GY, width=15, height=4)

    # ─── Section 8: Goal area ───
    a.add_ground(TX + 212, GY, width=25, height=4)
    a.add_staircase(TX + 225, GY, steps=8, direction=1)
    a.add_ground(TX + 233, GY - 8, width=25, height=2)
    a.add_ground(TX + 233, GY - 6, width=25, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Safe start — enemies after safe zone
    a.add_sprite(GOOMBA, x=(TX + 10) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 13) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 21) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Elevated enemies
    a.add_sprite(GOOMBA, x=(TX + 37) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 40) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 49) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 3: Hill enemies
    a.add_sprite(KOOPA, x=(TX + 56) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 61) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 65) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 71) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: Pipe enemies
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 80) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 86) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 97) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 102) * 16, y=(GY - 1) * 16, zone_id=0)

    # Midway flag — all-zero spritedata: game tracks the nearest entrance 1
    # (spritedata byte 1 = 0x01 was causing issues — reset to default)
    a.add_sprite(MIDWAY_FLAG, x=(TX + 109) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Section 5: Harder post-midway
    a.add_sprite(KOOPA, x=(TX + 114) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 124) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 128) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 137) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 139) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 6: Staircase enemies
    a.add_sprite(GOOMBA, x=(TX + 152) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 162) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 170) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 7: Dense final rush
    a.add_sprite(GOOMBA, x=(TX + 180) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 183) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 190) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 196) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 202) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 206) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 215) * 16, y=(GY - 1) * 16, zone_id=0)

    # Star coins (3 total, properly numbered)
    a.add_star_coin(TX + 38, GY - 9, coin_num=0)   # Above elevated section
    a.add_star_coin(TX + 89, GY - 8, coin_num=1)   # Between pipes - hard to reach
    a.add_star_coin(TX + 188, GY - 3, coin_num=2)  # On brick bridge over gap

    # Red coin ring
    a.add_red_coin_ring(TX + 90, GY - 3)

    # Coin lines to guide players and reward exploration
    a.add_coin_line(TX + 15, GY - 3, count=3)      # First gap hint
    a.add_coin_line(TX + 45, GY - 3, count=4)      # Running jump gap
    a.add_coin_line(TX + 85, GY - 3, count=5)      # Pipe gauntlet reward
    a.add_coin_line(TX + 150, GY - 3, count=4)     # After midway
    a.add_coin_line(TX + 190, GY - 2, count=3)     # Near bridge

    # Goal
    a.add_sprite(GOAL_POLE, x=(TX + 238) * 16, y=(GY - 10) * 16, zone_id=0)

    # ════════════════ DECORATIONS ════════════════
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 3, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 55, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 110, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 195, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.FLOWER_A, TX + 12, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_B, TX + 60, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_A, TX + 150, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_C, TX + 214, GY - 1, 1, 1)

    level.save('output/ChaosStation/Stage/01-01.arc')


def create_level_1_2():
    """Level 1-2: Underground Rumble — Pipe into underground cave."""
    level = LevelBuilder()

    # ═══════════ AREA 1: Short overworld intro with pipe down ═══════════
    a1 = level.add_area(1)
    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_GRASS)
    a1.set_time(400)
    a1.set_background(258)  # Grass/sky for overworld intro

    # Zone for overworld section
    a1.add_zone(0, 256, 1600, 385, zone_id=0, music=MUSIC_OVERWORLD, visibility=16)

    TX1, GY1 = 0, 38

    # Entrances
    a1.add_entrance(0, x=48, y=(GY1 - 2) * 16, etype=ENTRANCE_NORMAL, zone_id=0)

    # Short overworld: ground, enemies, then pipe down
    a1.add_ground(TX1, GY1, width=15, height=4)
    a1.add_ground(TX1 + 18, GY1, width=20, height=4)
    a1.add_pipe(TX1 + 30, GY1 - 4, height=4)
    a1.add_ground(TX1 + 40, GY1, width=10, height=4)

    # Pipe entrance: goes DOWN to area 2
    a1.add_entrance(2, x=(TX1 + 31) * 16, y=(GY1 - 4) * 16,
                    etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=3)

    # Some enemies in overworld
    a1.add_sprite(GOOMBA, x=(TX1 + 8) * 16, y=(GY1 - 1) * 16, zone_id=0)
    a1.add_sprite(GOOMBA, x=(TX1 + 12) * 16, y=(GY1 - 1) * 16, zone_id=0)
    a1.add_sprite(KOOPA, x=(TX1 + 22) * 16, y=(GY1 - 1) * 16, zone_id=0)

    # Decorations
    a1.add_object(0, 0, StandardObjs.BG_BUSH, TX1 + 3, GY1 - 2, 3, 2)

    # ═══════════ AREA 2: Underground cave ═══════════
    a2 = level.add_area(2)
    a2.set_tileset(0, TILESET_UNDERGROUND)
    a2.set_tileset(1, TILESET_CAVE)
    a2.set_background(770)  # Underground/cave background
    a2.set_time(400)

    ZX2, ZY2 = 0, 0
    ZW2, ZH2 = 6400, 384
    a2.add_zone(ZX2, ZY2, ZW2, ZH2, zone_id=0, music=MUSIC_UNDERGROUND)

    TX2, GY2 = 0, 22

    # Entrance from pipe (arrive from area 1)
    a2.add_entrance(3, x=48, y=(GY2 - 2) * 16,
                    etype=ENTRANCE_PIPE_LEFT, zone_id=0,
                    dest_area=1, dest_entrance=2)
    # Midway (entrance 1)
    a2.add_entrance(1, x=2560, y=400,
                    etype=ENTRANCE_NORMAL, zone_id=0)

    # ─── Ceiling ───
    a2.add_ground(TX2, 0, width=400, height=4)

    # ─── Section 1: Arrival corridor ───
    a2.add_ground(TX2, GY2, width=25, height=4)
    a2.add_question_block(TX2 + 8, GY2 - 4)
    a2.add_question_block(TX2 + 10, GY2 - 4, contents=7)  # Yoshi!
    a2.add_question_block(TX2 + 12, GY2 - 4)

    # ─── Section 2: Step-down corridor ───
    a2.add_ground(TX2 + 27, GY2 + 1, width=15, height=3)
    a2.add_ground(TX2 + 44, GY2 + 2, width=15, height=2)
    # Low ceiling creates cramped spaces
    a2.add_ground(TX2 + 44, GY2 - 4, width=15, height=3)

    # ─── Section 3: Pit hopping ───
    a2.add_ground(TX2 + 61, GY2, width=6, height=4)
    # Small platforms over pit
    a2.add_ground(TX2 + 70, GY2 - 1, width=3, height=2)
    a2.add_ground(TX2 + 76, GY2 - 2, width=3, height=2)
    a2.add_ground(TX2 + 82, GY2, width=8, height=4)

    # ─── Section 4: Pipe maze ───
    a2.add_ground(TX2 + 92, GY2, width=40, height=4)
    a2.add_pipe(TX2 + 96, GY2 - 3, height=3)
    a2.add_pipe(TX2 + 102, GY2 - 6, height=6)
    a2.add_pipe(TX2 + 108, GY2 - 2, height=2)
    a2.add_pipe(TX2 + 113, GY2 - 5, height=5)
    a2.add_pipe(TX2 + 119, GY2 - 3, height=3)
    # Elevated walkway between tall pipes
    a2.add_platform(TX2 + 104, GY2 - 7, width=4)
    a2.add_platform(TX2 + 115, GY2 - 6, width=3)

    # ? blocks above    # High platforms
    a2.add_question_block(TX2 + 100, GY2 - 4)
    a2.add_question_block(TX2 + 106, GY2 - 8)
    a2.add_question_block(TX2 + 116, GY2 - 7)

    # ─── Section 5: After midway — tighter corridors ───
    a2.add_ground(TX2 + 134, GY2, width=15, height=4)
    # Low ceiling squeeze
    a2.add_ground(TX2 + 134, GY2 - 4, width=15, height=2)

    # ─── Section 6: Elevated run with gaps ───
    a2.add_ground(TX2 + 151, GY2 - 2, width=8, height=2)
    a2.add_ground(TX2 + 151, GY2, width=8, height=4)
    # Gap
    a2.add_ground(TX2 + 162, GY2, width=5, height=4)
    # Gap
    a2.add_ground(TX2 + 170, GY2 - 3, width=5, height=3)
    a2.add_ground(TX2 + 170, GY2, width=5, height=4)
    # Landing
    a2.add_ground(TX2 + 178, GY2, width=10, height=4)

    # ─── Section 7: Double-height challenge ───
    a2.add_ground(TX2 + 190, GY2, width=30, height=4)
    # Secret upper path with red coins
    a2.add_ground(TX2 + 195, GY2 - 8, width=6, height=2)
    a2.add_ground(TX2 + 204, GY2 - 8, width=6, height=2)
    # Lower ceiling obstacles
    a2.add_ground(TX2 + 198, GY2 - 4, width=4, height=2)
    a2.add_ground(TX2 + 208, GY2 - 4, width=4, height=2)

    # ─── Section 8: Exit corridor and stairs ───
    a2.add_ground(TX2 + 222, GY2, width=25, height=4)
    a2.add_staircase(TX2 + 236, GY2, steps=6, direction=1)
    a2.add_ground(TX2 + 242, GY2 - 6, width=25, height=2)
    a2.add_ground(TX2 + 242, GY2 - 4, width=25, height=8)

    # ═══ SPRITES ═══

    # Section 1: Cave arrival
    a2.add_sprite(GOOMBA, x=(TX2 + 10) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 16) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(KOOPA, x=(TX2 + 22) * 16, y=(GY2 - 1) * 16, zone_id=0)

    # Section 2: Step corridor
    a2.add_sprite(SPINY, x=(TX2 + 32) * 16, y=GY2 * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 36) * 16, y=GY2 * 16, zone_id=0)
    a2.add_sprite(BUZZY_BEETLE, x=(TX2 + 48) * 16, y=(GY2 + 1) * 16, zone_id=0)
    a2.add_sprite(BUZZY_BEETLE, x=(TX2 + 52) * 16, y=(GY2 + 1) * 16, zone_id=0)

    # Section 3: Pit area
    a2.add_sprite(KOOPA_PARATROOPA, x=(TX2 + 67) * 16, y=(GY2 - 3) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 71) * 16, y=(GY2 - 2) * 16, zone_id=0)
    a2.add_sprite(SPINY, x=(TX2 + 84) * 16, y=(GY2 - 1) * 16, zone_id=0)

    # Section 4: Pipe enemies
    a2.add_sprite(PIPE_PIRANHA_UP, x=(TX2 + 96) * 16, y=(GY2 - 4) * 16, zone_id=0)
    a2.add_sprite(PIPE_PIRANHA_UP, x=(TX2 + 102) * 16, y=(GY2 - 7) * 16, zone_id=0)
    a2.add_sprite(PIPE_PIRANHA_UP, x=(TX2 + 113) * 16, y=(GY2 - 6) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 110) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(KOOPA, x=(TX2 + 125) * 16, y=(GY2 - 1) * 16, zone_id=0)

    # Midway
    a2.add_sprite(MIDWAY_FLAG, x=(TX2 + 135) * 16, y=(GY2 - 1) * 16, zone_id=0,
                  spritedata=b'\x00\x01\x00\x00\x00\x00')

    # Section 5-6: Post-midway harder
    a2.add_sprite(SPINY, x=(TX2 + 140) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(BUZZY_BEETLE, x=(TX2 + 145) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 154) * 16, y=(GY2 - 3) * 16, zone_id=0)
    a2.add_sprite(KOOPA, x=(TX2 + 164) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(SPINY, x=(TX2 + 172) * 16, y=(GY2 - 4) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 175) * 16, y=(GY2 - 4) * 16, zone_id=0)

    # Section 7: Dense enemies
    a2.add_sprite(KOOPA, x=(TX2 + 193) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(SPINY, x=(TX2 + 198) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(GOOMBA, x=(TX2 + 205) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(BUZZY_BEETLE, x=(TX2 + 210) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(SPINY, x=(TX2 + 215) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(PARAGOOMBA, x=(TX2 + 218) * 16, y=(GY2 - 4) * 16, zone_id=0)

    # Section 8: Exit enemies
    a2.add_sprite(GOOMBA, x=(TX2 + 226) * 16, y=(GY2 - 1) * 16, zone_id=0)
    a2.add_sprite(KOOPA, x=(TX2 + 233) * 16, y=(GY2 - 1) * 16, zone_id=0)

    # Star coins (in area 2 — underground)
    a2.add_star_coin(TX2 + 73, GY2 - 3, coin_num=0)    # On pit platform - tricky
    a2.add_star_coin(TX2 + 106, GY2 - 9, coin_num=1)   # Above tall pipe - elevated walkway
    a2.add_star_coin(TX2 + 200, GY2 - 9, coin_num=2)   # Upper path in double-height section

    # Red coin ring in the cave
    a2.add_red_coin_ring(TX2 + 120, GY2 - 3, pattern='wave')

    # Coin lines throughout the cave
    a2.add_coin_line(TX2 + 55, GY2 - 2, count=5)       # Cave start
    a2.add_coin_line(TX2 + 90, GY2 - 2, count=4)       # Mid-cave
    a2.add_coin_line(TX2 + 160, GY2 - 2, count=5)      # Before double section
    a2.add_coin_line(TX2 + 230, GY2 - 2, count=4)      # Before exit

    # Goal
    a2.add_sprite(GOAL_POLE, x=(TX2 + 252) * 16, y=(GY2 - 10) * 16, zone_id=0)

    level.save('output/ChaosStation/Stage/01-02.arc')


def create_level_1_3():
    """Level 1-3: Sky High Chaos — Athletic precision platforming."""
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_GRASS)
    a.set_time(300)  # Tight time
    a.set_background(258)  # Grass/sky background (athletic)

    ZX, ZY = 0, 0
    ZW, ZH = 7200, 384
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, visibility=16)

    TX = 0
    GY = 20  # High for sky level — falling = death

    # Entrance 0 = level start. Entrance 1 = midway respawn (just past midway flag)
    a.add_entrance(0, x=48, y=(GY - 2) * 16, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2352, y=464, etype=ENTRANCE_NORMAL, zone_id=0)

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Intro — safe start, then widening gaps ───
    a.add_ground(TX, GY, width=10, height=3)
    a.add_platform(TX + 13, GY - 1, width=5)
    a.add_ground(TX + 20, GY, width=8, height=3)
    a.add_platform(TX + 30, GY - 2, width=4)
    a.add_platform(TX + 36, GY - 1, width=3)
    a.add_ground(TX + 41, GY, width=6, height=3)

    # ? blocks on starting platforms
    a.add_question_block(TX + 14, GY - 5)
    a.add_question_block(TX + 23, GY - 4)  # Removed extra powerup

    # ─── Section 2: Ascending tower ───
    a.add_platform(TX + 49, GY - 2, width=4)
    a.add_platform(TX + 55, GY - 4, width=3)
    a.add_platform(TX + 61, GY - 6, width=3)
    a.add_ground(TX + 66, GY - 6, width=8, height=2)
    a.add_ground(TX + 66, GY - 4, width=8, height=7)

    # ─── Section 3: Descending zigzag ───
    a.add_platform(TX + 77, GY - 5, width=3)
    a.add_platform(TX + 82, GY - 3, width=3)
    a.add_platform(TX + 87, GY - 5, width=3)
    a.add_ground(TX + 92, GY - 3, width=5, height=2)
    a.add_ground(TX + 92, GY - 1, width=5, height=4)

    # ? blocks in zigzag area
    a.add_question_block(TX + 78, GY - 8)
    a.add_question_block(TX + 88, GY - 8)

    # ─── Section 4: Long gap gauntlet ───
    a.add_platform(TX + 100, GY - 2, width=3)
    a.add_platform(TX + 106, GY - 3, width=2)
    a.add_platform(TX + 111, GY - 2, width=2)
    a.add_platform(TX + 116, GY - 4, width=3)
    a.add_ground(TX + 122, GY - 2, width=6, height=2)
    a.add_ground(TX + 122, GY, width=6, height=3)

    # ─── Section 5: After midway — tiny platforms ───
    a.add_ground(TX + 130, GY, width=10, height=3)

    a.add_platform(TX + 143, GY - 1, width=2)
    a.add_platform(TX + 148, GY - 3, width=2)
    a.add_platform(TX + 153, GY - 1, width=2)
    a.add_platform(TX + 158, GY - 4, width=2)
    a.add_ground(TX + 163, GY - 2, width=5, height=2)
    a.add_ground(TX + 163, GY, width=5, height=3)

    # ? block at hard spot
    a.add_question_block(TX + 149, GY - 6)

    # ─── Section 6: Island hopping (SECRET PIPE hidden here!) ───
    a.add_ground(TX + 170, GY, width=4, height=3)
    a.add_ground(TX + 177, GY - 2, width=5, height=2)
    a.add_ground(TX + 177, GY, width=5, height=3)
    a.add_ground(TX + 185, GY - 4, width=4, height=2)
    a.add_ground(TX + 185, GY - 2, width=4, height=5)
    # Secret pipe on this island — hard to reach!
    a.add_pipe(TX + 186, GY - 6, height=2)
    a.add_ground(TX + 192, GY, width=5, height=3)

    # ─── Section 7: Rapid-fire final stretch ───
    a.add_platform(TX + 200, GY - 1, width=2)
    a.add_platform(TX + 204, GY - 2, width=2)
    a.add_platform(TX + 208, GY - 1, width=2)
    a.add_platform(TX + 212, GY - 3, width=2)
    a.add_ground(TX + 217, GY, width=6, height=3)

    # ─── Section 8: Goal area ───
    a.add_ground(TX + 225, GY, width=15, height=3)
    a.add_staircase(TX + 230, GY, steps=8, direction=1)
    a.add_ground(TX + 238, GY - 8, width=25, height=2)
    a.add_ground(TX + 238, GY - 6, width=25, height=9)

    # ════════════════ SPRITES ════════════════

    # Section 1: Light enemies
    a.add_sprite(GOOMBA, x=(TX + 14) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 23) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 33) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 43) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Tower enemies
    a.add_sprite(KOOPA, x=(TX + 50) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 58) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 68) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 72) * 16, y=(GY - 7) * 16, zone_id=0)

    # Section 3: Zigzag
    a.add_sprite(PARAGOOMBA, x=(TX + 80) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 89) * 16, y=(GY - 8) * 16, zone_id=0)

    # Section 4: Gap enemies
    a.add_sprite(PARAGOOMBA, x=(TX + 104) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 113) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 119) * 16, y=(GY - 7) * 16, zone_id=0)

    # Midway
    a.add_sprite(MIDWAY_FLAG, x=(TX + 131) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x01\x00\x00\x00\x00')

    # Section 5: Post-midway — spines on tiny platforms!
    a.add_sprite(SPINY, x=(TX + 135) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 144) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 150) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 154) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 160) * 16, y=(GY - 7) * 16, zone_id=0)

    # Section 6: Island enemies
    a.add_sprite(KOOPA, x=(TX + 171) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 179) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 187) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 194) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 7: Rapid-fire enemies
    a.add_sprite(PARAGOOMBA, x=(TX + 202) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 206) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 210) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 219) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 227) * 16, y=(GY - 1) * 16, zone_id=0)

    # Star coins (properly numbered)
    a.add_star_coin(TX + 55, GY + 2, coin_num=0)    # Below ascending tower - risky drop
    a.add_star_coin(TX + 117, GY - 7, coin_num=1)   # Above gap gauntlet - precision jump
    a.add_star_coin(TX + 186, GY - 7, coin_num=2)   # On secret pipe island

    # Red coin ring
    a.add_red_coin_ring(TX + 82, GY - 5, pattern='line')

    # Coin lines across sky gaps
    a.add_coin_line(TX + 15, GY - 3, count=4)       # Start area
    a.add_coin_line(TX + 53, GY - 5, count=3)       # Between towers
    a.add_coin_line(TX + 100, GY - 5, count=5)      # Mid-level gap
    a.add_coin_line(TX + 143, GY - 3, count=3)      # Before tiny platforms
    a.add_coin_line(TX + 200, GY - 3, count=4)      # Final stretch

    # Secret pipe entrance — goes DOWN into secret area
    a.add_entrance(2, x=(TX + 187) * 16, y=(GY - 6) * 16,
                   etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                   dest_area=2, dest_entrance=3)

    # Goal (normal exit)
    a.add_sprite(GOAL_POLE, x=(TX + 243) * 16, y=(GY - 10) * 16, zone_id=0)

    # ═══════════ AREA 2: Secret exit room ═══════════
    a2 = level.add_area(2)
    a2.set_tileset(0, TILESET_UNDERGROUND)
    a2.set_tileset(1, TILESET_CAVE)
    a2.set_background(770)
    a2.set_time(100)

    a2.add_zone(0, 0, 800, 384, zone_id=0, music=MUSIC_UNDERGROUND)

    # Entrance from pipe
    a2.add_entrance(3, x=48, y=288,
                    etype=ENTRANCE_PIPE_LEFT, zone_id=0,
                    dest_area=1, dest_entrance=2)

    # Small secret room with coins and the secret goal
    SX, SY = 0, 20  # Secret room coords
    a2.add_ground(SX, SY, width=40, height=4)   # Floor
    a2.add_ground(SX, 0, width=40, height=4)     # Ceiling

    # Coin line leading to the secret flag
    a2.add_coin_line(SX + 8, SY - 2, count=8)

    # SECRET goal — stairs and RED flagpole (byte 2 = 0x10)
    a2.add_staircase(SX + 28, SY, steps=5, direction=1)
    a2.add_ground(SX + 33, SY - 5, width=15, height=2)
    a2.add_ground(SX + 33, SY - 3, width=15, height=7)
    a2.add_secret_goal(SX + 38, SY - 8)

    level.save('output/ChaosStation/Stage/01-03.arc')


def create_level_1_4():
    """Level 1-4: Sunken Abyss — Aquatic gauntlet with deadly underwater foes.

    A treacherous level where Mario must navigate over and through water,
    dodging Cheep Cheeps, Bloopers, and Urchins. Features narrow platforming
    sections above water with aquatic enemies leaping from below.
    """
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, 'Pa1_kaigan')  # Ocean/beach tileset for water level
    a.set_time(400)
    a.set_background(4098,  # Ocean underwater background
                     x_scroll_a=0, y_scroll_a=0,
                     x_scroll_b=0, y_scroll_b=0,
                     zoom_a=1, zoom_b=2)

    # Zone setup — cam_mode=0 = normal scrolling camera.
    # Sprite 138 (WATER_FILL) already handles swim physics; cam_mode=4 was
    # locking the view to a fixed square, so we use normal scrolling here.
    ZX, ZY = 512, 128
    ZW, ZH = 8400, 512
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_UNDERWATER, cam_mode=0)

    # Entrances — etype=0 (normal) works in an all-water zone
    a.add_entrance(0, x=ZX + 48, y=ZY + 240, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2016, y=544, etype=ENTRANCE_NORMAL, zone_id=0)

    # ─── WATER FILL — Sprite 138 fills the entire zone with swim physics ───
    # byte 0 = 0x01 -> flat top (no surface wave, fills zone completely)
    # Position at top of zone, w/h covering the full area
    water_sd = b'\x01\x00\x00\x00\x00\x00'
    a.add_sprite(WATER_FILL, x=ZX, y=ZY, zone_id=0, spritedata=water_sd)

    TX = 32   # tile X offset
    GY = 30   # ocean floor Y (in tiles) — swimable space above
    WY = 8    # high-water ceiling Y (in tiles from start of zone)

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Safe shore start ───
    a.add_ground(TX, GY, width=18, height=6)

    # Intro ? blocks
    a.add_question_block(TX + 6, GY - 4)               # Coin
    a.add_question_block(TX + 8, GY - 4, contents=1)   # Mushroom/Fire Flower
    a.add_question_block(TX + 10, GY - 4)              # Coin

    # ─── TITLE SCREEN BRANDING — visible in opening camera during title screen ───
    # The title demo replay uses this level's 01-04.arc, so the camera pans through
    # the area starting at TX,GY. We place giant pixel-art letters high in the sky
    # using ? blocks and coins so "CS MOD" is readable on the title screen.
    # Letters are at Y = GY-8..GY-14 (above water, well in camera view).
    # X starts at TX+1 (just after the left edge of the visible start area).

    BX = TX + 1   # letter block start X
    LY = GY - 10  # letter top row Y

    def qb(tx, ty):  # helper: add question block
        a.add_question_block(BX + tx, LY + ty)

    def cn(tx, ty):  # helper: add coin
        a.add_sprite(COIN, x=(BX + tx) * 16, y=(LY + ty) * 16, zone_id=0)

    # ── Letter C ──
    #  ###
    # #
    # #
    #  ###
    qb(1,0); qb(2,0); qb(3,0)
    qb(0,1)
    qb(0,2)
    qb(0,3)
    qb(1,4); qb(2,4); qb(3,4)

    # ── Letter S ──  (offset 5 right)
    #  ###
    # #
    #  ##
    #    #
    # ###
    qb(5,0); qb(6,0); qb(7,0)
    qb(5,1)
    qb(5,2); qb(6,2); qb(7,2)
    qb(7,3)
    qb(5,4); qb(6,4); qb(7,4)

    # Coin separator  (dot between CS and MOD)
    cn(9, 2)
    cn(9, 3)

    # ── Letter M ──  (offset 10 right)
    # # #
    # ###
    # # #
    # # #
    qb(10,0); qb(12,0)
    qb(10,1); qb(11,1); qb(12,1)
    qb(10,2); qb(12,2)
    qb(10,3); qb(12,3)
    qb(10,4); qb(12,4)

    # ── Letter O ──  (offset 14)
    #  ##
    # #  #
    # #  #
    # #  #
    #  ##
    qb(14,0); qb(15,0); qb(16,0)   # top
    qb(14,1); qb(16,1)
    qb(14,2); qb(16,2)
    qb(14,3); qb(16,3)
    qb(14,4); qb(15,4); qb(16,4)   # bottom

    # ── Letter D ──  (offset 18)
    # ##
    # #  #
    # #  #
    # #  #
    # ##
    qb(18,0); qb(19,0)
    qb(18,1); qb(20,1)
    qb(18,2); qb(20,2)
    qb(18,3); qb(20,3)
    qb(18,4); qb(19,4)


    # ─── Section 2: First water crossing — narrow platforms ───
    # Small islands over "water" (deep gaps where aquatic enemies swim)
    a.add_ground(TX + 22, GY, width=4, height=3)    # Tiny island
    a.add_ground(TX + 30, GY, width=3, height=3)    # Even tinier
    a.add_ground(TX + 37, GY, width=5, height=3)    # Medium island
    a.add_ground(TX + 46, GY, width=4, height=3)    # Tiny island

    # Elevated platforms to jump between
    a.add_platform(TX + 26, GY - 3, width=3)
    a.add_platform(TX + 34, GY - 5, width=3)
    a.add_platform(TX + 42, GY - 3, width=3)

    # Coin trail guiding through the crossing
    a.add_coin_line(TX + 19, GY - 3, count=3)
    a.add_coin_line(TX + 27, GY - 4, count=3)
    a.add_coin_line(TX + 35, GY - 6, count=2)
    a.add_coin_line(TX + 43, GY - 4, count=3)

    # ─── Section 3: Pipe cavern with enemies ───
    a.add_ground(TX + 53, GY, width=25, height=6)
    a.add_pipe(TX + 57, GY - 3, height=3)
    a.add_pipe(TX + 63, GY - 5, height=5)
    a.add_pipe(TX + 69, GY - 4, height=4)
    a.add_pipe(TX + 74, GY - 3, height=3)

    # ? blocks in pipe section
    a.add_question_block(TX + 60, GY - 4)
    a.add_question_block(TX + 66, GY - 6)
    a.add_question_block(TX + 72, GY - 5)  # Powerup

    # ─── Section 4: Deep water gap — longest crossing ───
    a.add_ground(TX + 82, GY, width=3, height=3)    # Start island
    a.add_platform(TX + 88, GY - 2, width=2)        # Floating platform
    a.add_ground(TX + 93, GY - 1, width=2, height=2) # Raised rock
    a.add_platform(TX + 98, GY - 4, width=2)        # High floating
    a.add_ground(TX + 103, GY, width=3, height=3)   # Landing island

    # ─── Section 5: Midway checkpoint area ───
    a.add_ground(TX + 109, GY, width=15, height=6)

    # Ascending platforms for vertical exploration
    a.add_platform(TX + 112, GY - 4, width=3)
    a.add_platform(TX + 116, GY - 7, width=3)
    a.add_platform(TX + 120, GY - 4, width=3)

    # ? blocks hidden up high
    a.add_question_block(TX + 117, GY - 9, contents=1)  # Fixed to normal powerup
    a.add_question_block(TX + 113, GY - 6)

    # ─── Section 6: Treacherous island chain ───
    a.add_ground(TX + 128, GY, width=4, height=3)
    a.add_ground(TX + 136, GY, width=3, height=3)
    a.add_ground(TX + 142, GY - 1, width=5, height=4)
    a.add_ground(TX + 150, GY, width=3, height=3)
    a.add_ground(TX + 157, GY, width=4, height=3)

    # Elevated route option (harder but has star coin)
    a.add_platform(TX + 131, GY - 5, width=2)
    a.add_platform(TX + 138, GY - 6, width=2)
    a.add_platform(TX + 146, GY - 5, width=2)
    a.add_platform(TX + 154, GY - 5, width=2)

    # Coins on high route
    a.add_coin_line(TX + 132, GY - 6, count=2)
    a.add_coin_line(TX + 139, GY - 7, count=2)
    a.add_coin_line(TX + 147, GY - 6, count=2)

    # ─── Section 7: Final gauntlet — dense enemies ───
    a.add_ground(TX + 164, GY, width=5, height=3)
    a.add_ground(TX + 173, GY, width=4, height=3)
    a.add_ground(TX + 181, GY, width=3, height=3)
    a.add_platform(TX + 168, GY - 3, width=3)
    a.add_platform(TX + 177, GY - 4, width=3)

    # ? block with 1up in hard spot
    a.add_question_block(TX + 178, GY - 7, contents=3)

    # ─── Section 8: Goal area ───
    a.add_ground(TX + 187, GY, width=25, height=6)
    a.add_staircase(TX + 200, GY, steps=8, direction=1)
    a.add_ground(TX + 208, GY - 8, width=25, height=2)
    a.add_ground(TX + 208, GY - 6, width=25, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Safe start — just a few goombas
    a.add_sprite(GOOMBA, x=(TX + 11) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 14) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Water crossing — aquatic enemies in gaps
    a.add_sprite(CHEEP_CHEEP, x=(TX + 20) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 25) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 28) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 33) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 40) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 44) * 16, y=(GY - 2) * 16, zone_id=0)

    # Section 3: Pipe enemies
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 57) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 63) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 69) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 61) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 72) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: Deep water crossing enemies
    a.add_sprite(CHEEP_CHEEP, x=(TX + 85) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 90) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 95) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 100) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 97) * 16, y=(GY + 1) * 16, zone_id=0)

    # Midway flag — all-zero spritedata (default, game uses nearest entrance 1)
    a.add_sprite(MIDWAY_FLAG, x=(TX + 110) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Section 5: Post-midway — harder enemies
    a.add_sprite(SPINY, x=(TX + 115) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 118) * 16, y=(GY - 6) * 16, zone_id=0)

    # Section 6: Island chain — dense aquatic threats
    a.add_sprite(CHEEP_CHEEP, x=(TX + 130) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 134) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 139) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 145) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 148) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 153) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 158) * 16, y=(GY - 2) * 16, zone_id=0)

    # Section 7: Final gauntlet
    a.add_sprite(CHEEP_CHEEP, x=(TX + 166) * 16, y=(GY + 2) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 170) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 175) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 180) * 16, y=(GY + 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 174) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 179) * 16, y=(GY - 5) * 16, zone_id=0)

    # Goal area — a few guards
    a.add_sprite(KOOPA, x=(TX + 192) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 195) * 16, y=(GY - 1) * 16, zone_id=0)

    # Star coins
    a.add_star_coin(TX + 35, GY - 8, coin_num=0)    # High above deep crossing
    a.add_star_coin(TX + 139, GY - 8, coin_num=1)   # On elevated route in island chain
    a.add_star_coin(TX + 178, GY - 9, coin_num=2)   # Near the 1up in final section

    # Red coin ring over the deep crossing
    a.add_red_coin_ring(TX + 87, GY - 3, pattern='drop')

    # Coin trails for guidance
    a.add_coin_line(TX + 82, GY - 1, count=3)
    a.add_coin_line(TX + 103, GY - 1, count=3)
    a.add_coin_line(TX + 164, GY - 1, count=3)
    a.add_coin_line(TX + 187, GY - 2, count=4)

    # Goal
    a.add_sprite(GOAL_POLE, x=(TX + 213) * 16, y=(GY - 10) * 16, zone_id=0)

    # Decorations
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 3, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 55, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 110, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 190, GY - 2, 3, 2)

    level.save('output/ChaosStation/Stage/01-04.arc')


def create_level_1_5():
    """Level 1-5: Skyline Sprint — Athletic precision platforming.

    A high-altitude sprint across floating platforms, moving lifts, and
    cloud walkways. Features Bullet Bill launchers, Paragoomba swarms, and
    treacherous gaps. The level is designed for speed and precision, with
    generous but fleeting platforms and constant aerial threats.
    """
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_GRASS)
    a.set_time(350)
    a.set_background(17666, bg2b=20994,  # Athletic sky — two cloud layers
                     x_scroll_a=2, y_scroll_a=2,
                     x_scroll_b=1, y_scroll_b=1,
                     zoom_a=1, zoom_b=2)

    # Zone — tall to allow vertical exploration
    ZX, ZY = 512, 128
    ZW, ZH = 8800, 512
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, visibility=16)

    # Entrance 0 = level start. Entrance 1 = midway respawn (past midway flag at TX+121)
    a.add_entrance(0, x=ZX + 48, y=ZY + 440, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2192, y=432, etype=ENTRANCE_NORMAL, zone_id=0)

    TX = 32   # tile X offset
    GY = 38   # base ground Y
    SY = 30   # sky platform Y (high up)

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Starting area — safe launch pad ───
    a.add_ground(TX, GY, width=12, height=4)

    # Intro ? blocks
    a.add_question_block(TX + 4, GY - 4)               # Coin
    a.add_question_block(TX + 6, GY - 4)   # Mushroom/Fire Flower

    # ─── Section 2: Cloud hop — multiple small platforms ───
    # Cloud platforms (using standard cloud terrain)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 16, GY - 2, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 22, GY - 4, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 28, GY - 2, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 34, GY - 5, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 40, GY - 3, 3, 1)

    # Coin guides between clouds
    a.add_coin_line(TX + 13, GY - 3, count=3)
    a.add_coin_line(TX + 19, GY - 3, count=3)
    a.add_coin_line(TX + 25, GY - 5, count=3)
    a.add_coin_line(TX + 31, GY - 3, count=3)
    a.add_coin_line(TX + 37, GY - 6, count=3)

    # ─── Section 3: Solid platform rest + Bullet Bill zone ───
    a.add_ground(TX + 46, GY, width=15, height=4)

    # Bullet Bill launchers flanking the safe zone
    a.add_pipe(TX + 50, GY - 3, height=3)   # acts as a launcher visually
    a.add_pipe(TX + 56, GY - 4, height=4)

    # ? blocks with powerup
    a.add_question_block(TX + 53, GY - 4)
    a.add_question_block(TX + 55, GY - 6)  # Powerup

    # ─── Section 4: Staircase to the sky ───
    a.add_staircase(TX + 64, GY, steps=6, direction=1)
    a.add_ground(TX + 70, GY - 6, width=5, height=2)
    a.add_ground(TX + 70, GY - 4, width=5, height=8)

    # Upper platforms — optional higher route
    a.add_platform(TX + 72, GY - 10, width=3)
    a.add_platform(TX + 78, GY - 12, width=3)
    a.add_platform(TX + 84, GY - 10, width=3)

    # Coin trail on high route
    a.add_coin_line(TX + 75, GY - 11, count=3)
    a.add_coin_line(TX + 81, GY - 13, count=3)

    # ─── Section 5: Gap gauntlet — precision jumping ───
    # Alternating platforms at different heights
    a.add_ground(TX + 78, GY, width=5, height=4)
    a.add_ground(TX + 87, GY - 2, width=4, height=6)
    a.add_ground(TX + 95, GY, width=5, height=4)
    a.add_ground(TX + 104, GY - 3, width=4, height=7)
    a.add_ground(TX + 112, GY, width=5, height=4)

    # Cloud bridges between gaps (easier route)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 83, GY - 1, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 92, GY - 1, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 100, GY - 2, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 109, GY - 1, 3, 1)

    # ─── Section 6: Midway checkpoint ───
    a.add_ground(TX + 120, GY, width=12, height=4)

    # ? blocks cluster — reward for making it here
    a.add_question_block(TX + 124, GY - 4)
    a.add_question_block(TX + 126, GY - 4, contents=7)  # Yoshi!
    a.add_question_block(TX + 128, GY - 4)

    # ─── Section 7: Sky high challenge — mixed platforms ───
    # Ground islands with big gaps
    a.add_ground(TX + 136, GY, width=4, height=4)
    a.add_ground(TX + 146, GY - 2, width=5, height=6)
    a.add_ground(TX + 157, GY, width=4, height=4)

    # Cloud platforms zigzagging between
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 140, GY - 3, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 143, GY - 6, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 152, GY - 4, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 155, GY - 1, 3, 1)

    # Coin guides
    a.add_coin_line(TX + 140, GY - 4, count=3)
    a.add_coin_line(TX + 152, GY - 5, count=3)

    # ─── Section 8: Bullet Bill alley ───
    a.add_ground(TX + 164, GY, width=6, height=4)
    a.add_ground(TX + 176, GY, width=5, height=4)
    a.add_ground(TX + 187, GY, width=4, height=4)

    # Pipes acting as visual launchers in the gaps
    a.add_pipe(TX + 171, GY - 3, height=3)
    a.add_pipe(TX + 183, GY - 4, height=4)

    # Floating ? block with star
    a.add_question_block(TX + 174, GY - 6, contents=1)  # Powerup!

    # Cloud platforms for navigation
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 170, GY - 1, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 181, GY - 2, 3, 1)
    a.add_object(1, 0, StandardObjs.CLOUD_PLATFORM, TX + 191, GY - 1, 3, 1)

    # ─── Section 9: Rising staircase finale ───
    a.add_ground(TX + 194, GY, width=20, height=4)
    a.add_staircase(TX + 200, GY, steps=5, direction=1)
    a.add_ground(TX + 205, GY - 5, width=4, height=2)
    a.add_ground(TX + 205, GY - 3, width=4, height=7)

    # Descending platforms to goal
    a.add_ground(TX + 212, GY - 3, width=3, height=1)
    a.add_ground(TX + 218, GY - 1, width=3, height=1)
    a.add_question_block(TX + 215, GY - 6)  # Last powerup

    # ─── Section 10: Goal area ───
    a.add_ground(TX + 224, GY, width=25, height=4)
    a.add_staircase(TX + 237, GY, steps=8, direction=1)
    a.add_ground(TX + 245, GY - 8, width=25, height=2)
    a.add_ground(TX + 245, GY - 6, width=25, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Easy start
    a.add_sprite(GOOMBA, x=(TX + 7) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 9) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Cloud hop — aerial threats
    a.add_sprite(PARAGOOMBA, x=(TX + 18) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 24) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 31) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 38) * 16, y=(GY - 7) * 16, zone_id=0)

    # Section 3: Bullet Bill zone
    a.add_sprite(KOOPA, x=(TX + 48) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 52) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 50) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 56) * 16, y=(GY - 5) * 16, zone_id=0)
    # Bullet Bills from launchers
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 59) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 4: Staircase area
    a.add_sprite(KOOPA, x=(TX + 72) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 76) * 16, y=(GY - 9) * 16, zone_id=0)

    # Section 5: Gap gauntlet enemies
    a.add_sprite(GOOMBA, x=(TX + 80) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 89) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 97) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 100) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 106) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 114) * 16, y=(GY - 1) * 16, zone_id=0)

    # Midway flag — all-zero spritedata (default, game uses nearest entrance 1)
    a.add_sprite(MIDWAY_FLAG, x=(TX + 121) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Section 6: After midway — ramping up
    a.add_sprite(SPINY, x=(TX + 125) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 130) * 16, y=(GY - 4) * 16, zone_id=0)

    # Section 7: Sky challenge — dense aerial enemies
    a.add_sprite(PARAGOOMBA, x=(TX + 138) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 142) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 148) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 150) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 155) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 159) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 8: Bullet Bill alley — intense!
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 168) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 172) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 185) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 177) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 179) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 189) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 9: Final push
    a.add_sprite(GOOMBA, x=(TX + 196) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 198) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 207) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 220) * 16, y=(GY - 4) * 16, zone_id=0)

    # Final guard before goal
    a.add_sprite(HAMMER_BRO, x=(TX + 230) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 235) * 16, y=(GY - 1) * 16, zone_id=0)

    # Star coins
    a.add_star_coin(TX + 36, GY - 8, coin_num=0)    # High cloud in section 2
    a.add_star_coin(TX + 80, GY - 14, coin_num=1)   # On optional high route above stairs
    a.add_star_coin(TX + 174, GY - 8, coin_num=2)   # Near bullet bill alley

    # Red coin ring mid-level
    a.add_red_coin_ring(TX + 100, GY - 3, pattern='line')

    # Goal
    a.add_sprite(GOAL_POLE, x=(TX + 250) * 16, y=(GY - 10) * 16, zone_id=0)

    # Decorations
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 3, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 47, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 120, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 195, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.FLOWER_A, TX + 8, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_B, TX + 50, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_C, TX + 122, GY - 1, 1, 1)
    a.add_object(0, 0, StandardObjs.FLOWER_A, TX + 226, GY - 1, 1, 1)

    level.save('output/ChaosStation/Stage/01-05.arc')

def create_level_1_6():
    """Level 1-6: Phantom Passage — Ghost house bonus level (from scratch).

    A spooky, maze-like ghost house with Boos, Dry Bones, and Swoop bats.
    Accessed via secret exit in 1-3. Features tricky platforming with
    invisible blocks, moving platforms, and haunting atmosphere.
    """
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_GRASS)
    a.set_time(350)
    a.set_background(770)  # Ghost house / cave dark background

    # Zone — slightly taller for vertical ghost house exploration
    ZX, ZY = 512, 128
    ZW, ZH = 7600, 480
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_GHOST_HOUSE, visibility=16)

    # Entrance 0 = level start. Entrance 1 = midway respawn (after ghost house mid section)
    a.add_entrance(0, x=ZX + 48, y=ZY + 416, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2288, y=432, etype=ENTRANCE_NORMAL, zone_id=0)

    TX = 32   # tile X offset
    GY = 38   # ground Y

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Eerie entrance hall ───
    a.add_ground(TX, GY, width=16, height=6)

    # Questions blocks — first encounters
    a.add_question_block(TX + 5, GY - 4)               # Coin
    a.add_question_block(TX + 8, GY - 4)   # Mushroom
    a.add_question_block(TX + 11, GY - 4)              # Coin

    # ─── Section 2: Floating platforms with gaps ───
    a.add_ground(TX + 20, GY, width=5, height=4)
    a.add_platform(TX + 28, GY - 3, width=4)
    a.add_ground(TX + 35, GY, width=4, height=4)
    a.add_platform(TX + 42, GY - 5, width=3)
    a.add_ground(TX + 48, GY, width=5, height=4)

    # Brick bridges (breakable!)
    a.add_gap_bridge(TX + 25, GY - 1, width=3)
    a.add_gap_bridge(TX + 39, GY - 2, width=3)
    a.add_gap_bridge(TX + 45, GY - 3, width=3)

    # Coin guides through the floating section
    a.add_coin_line(TX + 17, GY - 3, count=3)
    a.add_coin_line(TX + 29, GY - 4, count=3)
    a.add_coin_line(TX + 43, GY - 6, count=3)

    # ─── Section 3: Pipe and block corridor ───
    a.add_ground(TX + 56, GY, width=30, height=6)
    a.add_pipe(TX + 60, GY - 4, height=4)
    a.add_pipe(TX + 67, GY - 3, height=3)
    a.add_pipe(TX + 73, GY - 5, height=5)
    a.add_pipe(TX + 79, GY - 3, height=3)

    # ? blocks between pipes
    a.add_question_block(TX + 63, GY - 5)
    a.add_question_block(TX + 70, GY - 4)  # Powerup
    a.add_question_block(TX + 76, GY - 6)

    # ─── Section 4: Vertical challenge ───
    a.add_ground(TX + 89, GY, width=6, height=4)

    # Staircase going up
    a.add_staircase(TX + 95, GY, steps=5, direction=1)
    a.add_ground(TX + 100, GY - 5, width=6, height=2)
    a.add_ground(TX + 100, GY - 3, width=6, height=7)

    # Upper platforms route
    a.add_platform(TX + 108, GY - 3, width=3)
    a.add_platform(TX + 114, GY - 6, width=3)
    a.add_platform(TX + 120, GY - 3, width=3)

    # Coins on upper route
    a.add_coin_line(TX + 109, GY - 4, count=3)
    a.add_coin_line(TX + 115, GY - 7, count=3)

    # ─── Section 5: Midway vault ───
    a.add_ground(TX + 126, GY, width=14, height=6)

    # Reward cluster
    a.add_question_block(TX + 130, GY - 4)
    a.add_question_block(TX + 132, GY - 4)  # Powerup
    a.add_question_block(TX + 134, GY - 4)

    # ─── Section 6: The haunted gauntlet ───
    # Narrow platforms over deep voids
    a.add_ground(TX + 144, GY, width=3, height=3)
    a.add_platform(TX + 150, GY - 2, width=2)
    a.add_ground(TX + 155, GY, width=3, height=3)
    a.add_platform(TX + 161, GY - 4, width=2)
    a.add_ground(TX + 166, GY - 1, width=4, height=4)
    a.add_platform(TX + 173, GY - 2, width=2)
    a.add_ground(TX + 178, GY, width=3, height=3)

    # ? block with star in hard section
    a.add_question_block(TX + 167, GY - 6, contents=2)  # Star!

    # ─── Section 7: Final spooky corridor ───
    a.add_ground(TX + 184, GY, width=20, height=6)

    # Brick bridge over one last trap
    a.add_gap_bridge(TX + 200, GY - 1, width=4)
    a.add_ground(TX + 207, GY, width=5, height=4)

    # ─── Section 8: Goal area ───
    a.add_ground(TX + 215, GY, width=25, height=4)
    a.add_staircase(TX + 228, GY, steps=8, direction=1)
    a.add_ground(TX + 236, GY - 8, width=25, height=2)
    a.add_ground(TX + 236, GY - 6, width=25, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Welcoming Boos
    a.add_sprite(BOO, x=(TX + 10) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 14) * 16, y=(GY - 2) * 16, zone_id=0)

    # Section 2: Floating section — aerial threats
    a.add_sprite(SWOOP, x=(TX + 23) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 30) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 37) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 44) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 49) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 3: Pipe corridor — ghost piranhas
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 60) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 73) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 65) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 71) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 77) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 82) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: Climbing section
    a.add_sprite(BOO, x=(TX + 91) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 102) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 110) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 116) * 16, y=(GY - 8) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 122) * 16, y=(GY - 4) * 16, zone_id=0)

    # Midway flag — all-zero spritedata (default, game uses nearest entrance 1)
    a.add_sprite(MIDWAY_FLAG, x=(TX + 127) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Section 5: Post-midway warmup
    a.add_sprite(DRY_BONES, x=(TX + 133) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 137) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 6: Haunted gauntlet — DENSE and dangerous
    a.add_sprite(BOO, x=(TX + 146) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 152) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 157) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 156) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 163) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 168) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 175) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 179) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 7: Final corridor
    a.add_sprite(DRY_BONES, x=(TX + 188) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 193) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 197) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 203) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 209) * 16, y=(GY - 2) * 16, zone_id=0)

    # Goal area guards
    a.add_sprite(DRY_BONES, x=(TX + 220) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BOO, x=(TX + 225) * 16, y=(GY - 3) * 16, zone_id=0)

    # Star coins
    a.add_star_coin(TX + 43, GY - 8, coin_num=0)    # High above floating section
    a.add_star_coin(TX + 115, GY - 9, coin_num=1)   # On upper route in vertical section
    a.add_star_coin(TX + 201, GY - 3, coin_num=2)   # On brick bridge near end

    # Red coin ring in the haunted gauntlet
    a.add_red_coin_ring(TX + 155, GY - 3, pattern='circle')

    # Coin trails
    a.add_coin_line(TX + 89, GY - 1, count=4)
    a.add_coin_line(TX + 144, GY - 1, count=3)
    a.add_coin_line(TX + 184, GY - 2, count=5)

    # Goal
    a.add_sprite(GOAL_POLE, x=(TX + 241) * 16, y=(GY - 10) * 16, zone_id=0)

    # Decorations (ghostly bushes)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 3, GY - 2, 3, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 57, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 126, GY - 2, 4, 2)
    a.add_object(0, 0, StandardObjs.BG_BUSH, TX + 215, GY - 2, 3, 2)

    level.save('output/ChaosStation/Stage/01-06.arc')


def create_level_2_1():
    """Level 2-1: Sandstorm Blitz — A scorching desert sprint.

    Wide-open desert with rolling dunes, sand plateaus at different heights,
    Lakitu harassment from above, Pokeys blocking the path, and Bullet Bills
    crossing the gaps. A hidden pipe leads to a brief underground cache.
    Fast horizontal level designed for skilled players who know when to duck
    and when to run.
    """
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_DESERT)
    a.set_time(350)
    a.set_background(BG_DESERT)  # Sandy desert sky

    ZX, ZY = 256, 256
    ZW, ZH = 12000, 352   # Intentionally massively widened
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_DESERT, cam_mode=6, visibility=16)

    TX = 16   # tile start X
    GY = 34   # ground Y in tiles (y=544px). Zone bottom=608px — ground inside zone ✅

    # Entrance y=512 (absolute) = 32px above ground (544). Mario falls onto sand naturally.
    # Matches original 2-1 entrance at y=512.
    a.add_entrance(0, x=ZX + 48,   y=512, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=1696, y=528, etype=ENTRANCE_NORMAL, zone_id=0)

    # ════════════════ TERRAIN ════════════════

    # ─── Section 1: Desert intro — rolling dunes, safe start ───
    a.add_ground(TX, GY, width=14, height=5)

    # Dune hills in the background (decorative layer 0)
    a.add_hill(TX + 4, GY, half_width=4, height=2)
    a.add_hill(TX + 10, GY, half_width=3, height=2)

    # ? blocks on the dune crest
    # REMOVED MUSHROOM: 
    a.add_question_block(TX + 3, GY - 3)
    a.add_question_block(TX + 5, GY - 3)  # Powerup
    # REMOVED MUSHROOM: 
    a.add_question_block(TX + 7, GY - 3)

    # ─── Section 2: First sand plateaus — different heights ───
    # Low plateau
    a.add_ground(TX + 17, GY, width=6, height=5)
    # High plateau
    a.add_ground(TX + 26, GY - 4, width=5, height=5)
    # Mid plateau
    a.add_ground(TX + 34, GY - 2, width=7, height=5)

    # Coin trails along the tops
    a.add_coin_line(TX + 14, GY - 1, count=3)    # gap coins
    a.add_coin_line(TX + 27, GY - 5, count=3)    # high plateau reward
    a.add_coin_line(TX + 35, GY - 3, count=4)

    # ─── Section 3: Pipe leading to underground cache ───
    a.add_ground(TX + 44, GY, width=18, height=5)
    # The secret pipe — Mario can enter to grab coins underground
    a.add_pipe(TX + 48, GY - 3, height=3)   # entry pipe (down)
    a.add_pipe(TX + 54, GY - 2, height=2)   # second pipe (visual)
    a.add_pipe(TX + 59, GY - 4, height=4)   # tall pipe with piranha

    a.add_question_block(TX + 51, GY - 4)
    a.add_question_block(TX + 56, GY - 5, contents=2)  # Star! High up

    # ─── Section 4: Wide sand plain — Lakitu's territory ───
    # Long flat stretch perfect for Lakitu harassment
    a.add_ground(TX + 65, GY, width=30, height=5)
    a.add_hill(TX + 72, GY, half_width=5, height=3)   # decorative dune

    # ? blocks to give player cover options
    # REMOVED MUSHROOM: 
    a.add_question_block(TX + 68, GY - 4)
    a.add_question_block(TX + 76, GY - 4)  # Powerup mid-blitz
    # REMOVED MUSHROOM: 
    a.add_question_block(TX + 85, GY - 4)

    # Midway flag planted in the sand
    a.add_sprite(MIDWAY_FLAG, x=(TX + 90) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ─── Section 5: After midway — mixed heights + Bullet Bills ───
    a.add_ground(TX + 98, GY, width=5, height=5)
    a.add_ground(TX + 106, GY - 3, width=6, height=5)
    a.add_ground(TX + 116, GY, width=4, height=5)
    a.add_ground(TX + 124, GY - 5, width=5, height=5)
    a.add_ground(TX + 133, GY, width=5, height=5)

    # Coin guides across the gaps
    a.add_coin_line(TX + 103, GY - 1, count=3)
    a.add_coin_line(TX + 112, GY - 3, count=3)
    a.add_coin_line(TX + 120, GY - 4, count=3)
    a.add_coin_line(TX + 129, GY, count=3)

    # ─── Section 6: Pokey canyon — tight passages ───
    a.add_ground(TX + 141, GY, width=20, height=5)
    a.add_hill(TX + 148, GY, half_width=4, height=2)

    # Staircase up to elevated crossing
    a.add_staircase(TX + 163, GY, steps=4, direction=1)
    a.add_ground(TX + 167, GY - 4, width=8, height=5)
    a.add_ground(TX + 178, GY, width=5, height=5)

    # ─── Section 7: Final dash — sand walls and Bullet Bill gauntlet ───
    a.add_ground(TX + 186, GY, width=6, height=5)
    a.add_ground(TX + 196, GY - 3, width=4, height=5)
    a.add_ground(TX + 204, GY, width=4, height=5)
    a.add_ground(TX + 212, GY - 2, width=6, height=5)

    # Coin reward for surviving
    a.add_coin_line(TX + 183, GY - 1, count=3)
    a.add_coin_line(TX + 193, GY - 2, count=3)
    a.add_coin_line(TX + 200, GY - 1, count=3)

    # ─── Section 8: The Oasis Miramar ───
    a.add_ground(TX + 221, GY, width=15, height=5)
    
    # A huge gap requiring precision jumps across falling pillars
    a.add_ground(TX + 242, GY + 1, width=3, height=6)
    a.add_ground(TX + 250, GY + 1, width=3, height=6)
    a.add_ground(TX + 258, GY + 1, width=3, height=6)
    a.add_ground(TX + 266, GY, width=15, height=5)
    
    # ─── Section 9: Lakitu's Last Stand ───
    a.add_ground(TX + 285, GY, width=5, height=5)
    a.add_ground(TX + 293, GY - 3, width=5, height=5)
    a.add_ground(TX + 301, GY - 6, width=5, height=5)
    a.add_ground(TX + 309, GY - 3, width=5, height=5)
    a.add_ground(TX + 317, GY, width=25, height=5)
    
    # ─── Section 10: Goal area ───
    a.add_staircase(TX + 330, GY, steps=8, direction=1)
    a.add_ground(TX + 338, GY - 8, width=20, height=2)
    a.add_ground(TX + 338, GY - 6, width=20, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Gentle intro — just a Goomba on the dune
    a.add_sprite(GOOMBA, x=(TX + 8) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 11) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 12) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Pokeys on plateaus — can't kill, must go around!
    a.add_sprite(POKEY, x=(TX + 18) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(POKEY, x=(TX + 27) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(POKEY, x=(TX + 36) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 3: Pipe section enemies
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 59) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 62) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 55) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: Lakitu raining Spinies over the long flat! The real threat.
    # One Lakitu at the start, another mid-section — player can't stop moving!
    a.add_sprite(LAKITU, x=(TX + 70) * 16, y=(GY - 8) * 16, zone_id=0)
    a.add_sprite(LAKITU, x=(TX + 82) * 16, y=(GY - 8) * 16, zone_id=0)
    # Ground Spinies from earlier throws
    a.add_sprite(SPINY, x=(TX + 69) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 74) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 80) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 87) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 5: Post-midway — Bullet Bill launchers dominate the gaps
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 103) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 123) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 108) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 117) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(POKEY, x=(TX + 125) * 16, y=(GY - 6) * 16, zone_id=0)

    # Section 6: Pokey canyon — maximum Pokey density!
    a.add_sprite(POKEY, x=(TX + 142) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(POKEY, x=(TX + 146) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(POKEY, x=(TX + 152) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 157) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 168) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 170) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 175) * 16, y=(GY - 5) * 16, zone_id=0)

    # Section 7: Final Bullet Bill gauntlet
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 193) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 206) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 215) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 199) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 210) * 16, y=(GY - 5) * 16, zone_id=0)

    # Goal guards
    a.add_sprite(HAMMER_BRO, x=(TX + 228) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 232) * 16, y=(GY - 1) * 16, zone_id=0)

    # Star coins
    a.add_star_coin(TX + 28, GY - 9, coin_num=0)   # High above 2nd plateau (risky jump)
    a.add_star_coin(TX + 86, GY - 6, coin_num=1)   # Floating over the Lakitu section!
    a.add_star_coin(TX + 168, GY - 10, coin_num=2) # On the raised staircase top

    # Red coin ring over the Pokey canyon
    a.add_red_coin_ring(TX + 157, GY - 4, pattern='drop')

    # Coin lines to guide players
    a.add_coin_line(TX + 15, GY - 1, count=2)
    a.add_coin_line(TX + 22, GY - 1, count=4)
    a.add_coin_line(TX + 64, GY - 1, count=4)

    # New Enemies for the extension
    a.add_sprite(LAKITU, x=(TX + 290) * 16, y=(GY - 10) * 16, zone_id=0) # Another Lakitu
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 280) * 16, y=(GY - 5) * 16, zone_id=0)

    # Goal pole moved further down
    a.add_sprite(GOAL_POLE, x=(TX + 346) * 16, y=(GY - 10) * 16, zone_id=0)
    level.save('output/ChaosStation/Stage/02-01.arc')


def create_level_2_2():
    """Level 2-2: Pyramid Descent — From desert sands into a dark pyramid.

    Area 1: Short outdoor approach — tricky terrain with Hammer Bros and
            rising sand pillars. A pipe at the end drops Mario inside.
    Area 2: The Pyramid interior — three floors of tightening corridors.
            Fire Bars, Rocky Wrenches, and the ever-present dread of
            falling into the lower chamber. Exits via a hidden pipe.

    The two-area structure creates a satisfying 'outside-then-inside' feel.
    """
    level = LevelBuilder()

    # ═══════════ AREA 1: Desert Approach ═══════════
    a1 = level.add_area(1)

    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_DESERT)
    a1.set_time(300)
    a1.set_background(BG_DESERT)

    ZX1, ZY1 = 256, 256
    ZW1, ZH1 = 4800, 352   # bottom=608; ground at GY1*16=544 inside zone ✅
    a1.add_zone(ZX1, ZY1, ZW1, ZH1, zone_id=0, music=MUSIC_DESERT, cam_mode=6, visibility=16)

    TX1 = 16
    GY1 = 34   # ground at y=544; zone bottom=608 — ground visible ✅

    # Entrance 0 = level start. Entrance 1 = pipe out of pyramid
    # y=512 = 32px above ground (544), Mario falls naturally onto sand
    a1.add_entrance(0, x=ZX1 + 48,   y=512, etype=ENTRANCE_NORMAL, zone_id=0)
    a1.add_entrance(1, x=ZX1 + 4528, y=512, etype=ENTRANCE_NORMAL, zone_id=0)

    # Pipe entrances: entrance 2 = pipe-down entry into pyramid
    #                entrance 3 = emerge from pipe on the other side
    # Pipe object is at TX1 + 83, GY1 - 8. Middle of pipe is +16px from left edge.
    a1.add_entrance(2, x=(TX1 + 83) * 16 + 16, y=(GY1 - 8) * 16,
                    etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=0)
    # Emerge pipe (unused but kept for safety)
    a1.add_entrance(3, x=(TX1 + 83) * 16 + 16, y=(GY1 - 8) * 16,
                    etype=ENTRANCE_PIPE_UP, zone_id=0,
                    dest_area=2, dest_entrance=1)

    # ── Terrain ──

    # Starting platform
    a1.add_ground(TX1, GY1, width=10, height=5)
    # REMOVED MUSHROOM: 
    a1.add_question_block(TX1 + 3, GY1 - 3)
    a1.add_question_block(TX1 + 5, GY1 - 4)  # Powerup
    a1.add_coin_line(TX1 + 1, GY1 - 1, count=3)

    # Sand pillar row — rising and descending heights
    a1.add_ground(TX1 + 13, GY1 - 1, width=4, height=6)
    a1.add_ground(TX1 + 20, GY1 - 3, width=4, height=8)
    a1.add_ground(TX1 + 27, GY1 - 5, width=4, height=10)
    a1.add_ground(TX1 + 34, GY1 - 3, width=4, height=8)
    a1.add_ground(TX1 + 41, GY1 - 1, width=4, height=6)

    # Coin bridges across pillar tops
    a1.add_coin_line(TX1 + 10, GY1 - 1, count=3)
    a1.add_coin_line(TX1 + 14, GY1 - 2, count=3)
    a1.add_coin_line(TX1 + 21, GY1 - 4, count=3)
    a1.add_coin_line(TX1 + 28, GY1 - 6, count=3)

    # ? block at peak
    a1.add_question_block(TX1 + 29, GY1 - 8, contents=1)

    # Long flat section — where Hammer Bros set up shop
    a1.add_ground(TX1 + 48, GY1, width=20, height=5)
    a1.add_pipe(TX1 + 52, GY1 - 3, height=3)   # pipe (visual)
    a1.add_pipe(TX1 + 58, GY1 - 4, height=4)   # taller pipe
    # REMOVED MUSHROOM: 
    a1.add_question_block(TX1 + 55, GY1 - 5)
    a1.add_question_block(TX1 + 62, GY1 - 6, contents=1)

    # Staircase up to pyramid entrance
    a1.add_staircase(TX1 + 70, GY1, steps=5, direction=1)
    # Pyramid wall — tall enough to look like a pyramid, but pipe is accessible
    a1.add_ground(TX1 + 75, GY1 - 8, width=20, height=13)
    # The entry pipe — leads to area 2
    a1.add_pipe(TX1 + 83, GY1 - 8, height=3)   # Pyramid entry pipe (DOWN into area 2)

    # Star coin visible at top of sand pillar zigzag (need precise jumping)
    a1.add_star_coin(TX1 + 28, GY1 - 9, coin_num=0)

    # ── Sprites ──
    a1.add_sprite(GOOMBA, x=(TX1 + 6) * 16, y=(GY1 - 1) * 16, zone_id=0)
    a1.add_sprite(KOOPA, x=(TX1 + 8) * 16, y=(GY1 - 1) * 16, zone_id=0)

    # Pokeys on the pillar tops
    a1.add_sprite(POKEY, x=(TX1 + 14) * 16, y=(GY1 - 2) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX1 + 21) * 16, y=(GY1 - 4) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX1 + 35) * 16, y=(GY1 - 4) * 16, zone_id=0)

    # Hammer Bros guarding the flat section before the pyramid!
    a1.add_sprite(HAMMER_BRO, x=(TX1 + 53) * 16, y=(GY1 - 1) * 16, zone_id=0)
    a1.add_sprite(HAMMER_BRO, x=(TX1 + 60) * 16, y=(GY1 - 1) * 16, zone_id=0)
    a1.add_sprite(BULLET_BILL_LAUNCHER, x=(TX1 + 66) * 16, y=(GY1 - 3) * 16, zone_id=0)
    a1.add_sprite(SPINY, x=(TX1 + 68) * 16, y=(GY1 - 1) * 16, zone_id=0)

    # Pipe piranha in the entry pipe
    a1.add_sprite(PIPE_PIRANHA_UP, x=(TX1 + 52) * 16, y=(GY1 - 4) * 16, zone_id=0)

    # ═══════════ AREA 2: Pyramid Interior ═══════════
    a2 = level.add_area(2)

    a2.set_tileset(0, TILESET_UNDERGROUND)    # Pa0_jyotyu_chika
    a2.set_tileset(1, TILESET_CAVE)           # Pa1_chika — inner pyramid walls
    a2.set_time(280)  # Pressure timer!
    a2.set_background(BG_UNDERGROUND)  # Dark cave background inside

    # Interior zone — tighter, vertical camera movement
    # Position to the right so pipe connects from area 1 logically
    ZX2, ZY2 = 512, 96
    ZW2, ZH2 = 6400, 600
    a2.add_zone(ZX2, ZY2, ZW2, ZH2, zone_id=0, music=MUSIC_UNDERGROUND, visibility=16)

    TX2 = 32
    # Three floor heights inside the pyramid
    F1 = 16    # Top floor Y (in tiles from zone top)
    F2 = 27    # Middle floor Y
    F3 = 40    # Bottom floor Y (deepest chamber)

    # Entrance 0 = enter from pipe (area 1)
    a2.add_entrance(0, x=ZX2 + 80, y=(F1 - 3) * 16,
                    etype=ENTRANCE_PIPE_DOWN, zone_id=0)

    # Entrances 4 & 5: Floor 1 -> Floor 2 pipe
    a2.add_entrance(4, x=(TX2 + 55) * 16 + 16, y=(F1 - 3) * 16,
                    etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=5)
    # Spawn on the left side of Floor 2 (falling from ceiling)
    a2.add_entrance(5, x=(TX2 + 4) * 16, y=(F2 - 6) * 16,
                    etype=ENTRANCE_NORMAL, zone_id=0)

    # Entrances 6 & 7: Floor 2 -> Floor 3 pipe
    a2.add_entrance(6, x=(TX2 + 72) * 16 + 16, y=(F2 - 3) * 16,
                    etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=7)
    # Spawn on the left side of Floor 3 (falling from ceiling)
    a2.add_entrance(7, x=(TX2 + 4) * 16, y=(F3 - 6) * 16,
                    etype=ENTRANCE_NORMAL, zone_id=0)

    # Midway respawn in the middle chamber
    a2.add_entrance(3, x=(TX2 + 32) * 16, y=(F2 - 3) * 16,
                    etype=ENTRANCE_NORMAL, zone_id=0)

    # ── FLOOR 1: Entry chamber — narrow with Fire Bars ──
    # Solid ceiling and floor
    a2.add_ground(TX2, F1, width=60, height=3)   # Floor 1 ground
    a2.add_ground(TX2, F1 - 7, width=60, height=3)  # Ceiling
    # Blocking wall to prevent jumping past the pipe
    a2.add_ground(TX2 + 58, F1 - 7, width=2, height=10)

    # Platforms on floor 1
    a2.add_platform(TX2 + 10, F1 - 3, width=5)
    a2.add_platform(TX2 + 18, F1 - 5, width=4)
    a2.add_platform(TX2 + 26, F1 - 3, width=5)
    a2.add_platform(TX2 + 36, F1 - 5, width=4)
    a2.add_platform(TX2 + 44, F1 - 3, width=5)

    # Coin lines on floor 1 platforms
    a2.add_coin_line(TX2 + 11, F1 - 4, count=3)
    a2.add_coin_line(TX2 + 19, F1 - 6, count=3)
    a2.add_coin_line(TX2 + 27, F1 - 4, count=3)

    # Pipe down to floor 2 at end of floor 1
    a2.add_pipe(TX2 + 55, F1 - 3, height=3)    # Down pipe

    # ? blocks
    # REMOVED MUSHROOM: 
    a2.add_question_block(TX2 + 15, F1 - 4)
    a2.add_question_block(TX2 + 32, F1 - 6, contents=1)  # Powerup
    # REMOVED MUSHROOM: 
    a2.add_question_block(TX2 + 48, F1 - 4)

    # ── FLOOR 2: Middle chamber — Rocky Wrenches + Thwomps ──
    a2.add_ground(TX2, F2, width=76, height=3)
    a2.add_ground(TX2, F2 - 8, width=76, height=2)  # Ceiling
    # Blocking wall to prevent jumping past the pipe
    a2.add_ground(TX2 + 75, F2 - 8, width=2, height=11)

    # Platforms
    a2.add_platform(TX2 + 8, F2 - 3, width=4)
    a2.add_platform(TX2 + 16, F2 - 5, width=4)
    a2.add_platform(TX2 + 26, F2 - 3, width=4)
    a2.add_platform(TX2 + 36, F2 - 5, width=5)
    a2.add_platform(TX2 + 48, F2 - 3, width=4)
    a2.add_platform(TX2 + 58, F2 - 5, width=4)

    # Coin lines
    a2.add_coin_line(TX2 + 9, F2 - 4, count=3)
    a2.add_coin_line(TX2 + 27, F2 - 4, count=3)
    a2.add_coin_line(TX2 + 49, F2 - 4, count=3)

    # Midway flag
    a2.add_sprite(MIDWAY_FLAG, x=(TX2 + 65) * 16, y=(F2 - 1) * 16, zone_id=0,
                  spritedata=b'\x00\x00\x00\x01\x00\x00')

    # More ? blocks on floor 2
    a2.add_question_block(TX2 + 20, F2 - 6, contents=1)
    a2.add_question_block(TX2 + 40, F2 - 6, contents=2)  # Star!

    # Pipe down to floor 3
    a2.add_pipe(TX2 + 72, F2 - 3, height=3)

    # ── FLOOR 3: Deep chamber — Dry Bones, Fire Bars, and the exit ──
    a2.add_ground(TX2, F3, width=100, height=4)
    a2.add_ground(TX2, F3 - 9, width=100, height=2)  # Ceiling

    # Tight platforms — smaller, more spread out
    a2.add_platform(TX2 + 9, F3 - 3, width=3)
    a2.add_platform(TX2 + 16, F3 - 5, width=3)
    a2.add_platform(TX2 + 24, F3 - 3, width=3)
    a2.add_platform(TX2 + 33, F3 - 6, width=3)
    a2.add_platform(TX2 + 42, F3 - 4, width=3)
    a2.add_platform(TX2 + 52, F3 - 3, width=3)
    a2.add_platform(TX2 + 62, F3 - 5, width=3)
    a2.add_platform(TX2 + 72, F3 - 3, width=3)

    # Coin breadcrumbs
    a2.add_coin_line(TX2 + 10, F3 - 4, count=2)
    a2.add_coin_line(TX2 + 17, F3 - 6, count=2)
    a2.add_coin_line(TX2 + 25, F3 - 4, count=2)

    # Goal pole inside the pyramid — secret exit feel!
    a2.add_ground(TX2 + 88, F3, width=25, height=4)  # Final platform (extended for castle run)
    a2.add_sprite(GOAL_POLE, x=(TX2 + 93) * 16, y=(F3 - 1) * 16, zone_id=0)

    # Star coins inside pyramid
    a2.add_star_coin(TX2 + 37, F2 - 8, coin_num=1)  # Floating near floor 2 ceiling
    a2.add_star_coin(TX2 + 35, F3 - 8, coin_num=2)  # Floating near floor 3 ceiling

    # Red coin ring inside pyramid (floor 2)
    a2.add_red_coin_ring(TX2 + 44, F2 - 3, pattern='drop')

    # ── SPRITES — Floor 1 (entry) ──
    # Fire Bars blocking the path — enemies guarding platforms
    a2.add_sprite(FIRE_BAR, x=(TX2 + 12) * 16, y=(F1 - 2) * 16, zone_id=0)
    a2.add_sprite(FIRE_BAR, x=(TX2 + 30) * 16, y=(F1 - 2) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 20) * 16, y=(F1 - 1) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 40) * 16, y=(F1 - 1) * 16, zone_id=0)
    a2.add_sprite(BOO, x=(TX2 + 45) * 16, y=(F1 - 4) * 16, zone_id=0)

    # ── SPRITES — Floor 2 (middle — Rocky Wrenches!) ──
    a2.add_sprite(ROCKY_WRENCH, x=(TX2 + 12) * 16, y=(F2 - 5) * 16, zone_id=0)
    a2.add_sprite(ROCKY_WRENCH, x=(TX2 + 28) * 16, y=(F2 - 3) * 16, zone_id=0)
    a2.add_sprite(ROCKY_WRENCH, x=(TX2 + 44) * 16, y=(F2 - 5) * 16, zone_id=0)
    a2.add_sprite(ROCKY_WRENCH, x=(TX2 + 58) * 16, y=(F2 - 3) * 16, zone_id=0)
    a2.add_sprite(THWOMP, x=(TX2 + 22) * 16, y=(F2 - 7) * 16, zone_id=0)
    a2.add_sprite(THWOMP, x=(TX2 + 52) * 16, y=(F2 - 7) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 34) * 16, y=(F2 - 1) * 16, zone_id=0)

    # ── SPRITES — Floor 3 (deepest — the final push) ──
    a2.add_sprite(FIRE_BAR, x=(TX2 + 10) * 16, y=(F3 - 2) * 16, zone_id=0)
    a2.add_sprite(FIRE_BAR, x=(TX2 + 26) * 16, y=(F3 - 2) * 16, zone_id=0)
    a2.add_sprite(FIRE_BAR, x=(TX2 + 45) * 16, y=(F3 - 2) * 16, zone_id=0)
    a2.add_sprite(FIRE_BAR, x=(TX2 + 65) * 16, y=(F3 - 2) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 14) * 16, y=(F3 - 1) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 32) * 16, y=(F3 - 1) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 55) * 16, y=(F3 - 1) * 16, zone_id=0)
    a2.add_sprite(DRY_BONES, x=(TX2 + 75) * 16, y=(F3 - 1) * 16, zone_id=0)
    # Hammer Bro guarding the exit pipe!
    a2.add_sprite(HAMMER_BRO, x=(TX2 + 80) * 16, y=(F3 - 1) * 16, zone_id=0)
    a2.add_sprite(BOO, x=(TX2 + 60) * 16, y=(F3 - 5) * 16, zone_id=0)
    a2.add_sprite(BOO, x=(TX2 + 70) * 16, y=(F3 - 4) * 16, zone_id=0)

    level.save('output/ChaosStation/Stage/02-02.arc')


def create_level_castle():
    """Castle (01-24): Clone-and-modify Larry Koopa's castle.

    Keeps the original castle shape, terrain, and boss room (areas 2+3) intact.
    Area 1 gets harder enemies: Thwomps->Big Thwomps, Dry Bones->Giant Dry Bones,
    extra fire hazards, and reduced time limit.
    """
    import copy
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin, Sprite,
        parse_layer_data, serialize_layer_data
    )

    # Load original castle
    with open('extracted files/Stage/01-24.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ MODIFY AREA 1 (Castle Traversal) ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))

    # Reduce time for extra pressure
    area1.settings.time_limit = 300

    # Rework enemies while keeping non-enemy sprites
    new_sprites = []
    for s in area1.sprites:
        # Keep infrastructure sprites unchanged
        # 32=star coin, 144=red coin, 147=coin, 156=red ring, 179=??,
        # 188=midway, 221=invisible block, 253=controller, 274=controller,
        # 278=controller, 310=controller, 358=controller,
        # 436=controller, 465=controller, 477=controller, 139=controller
        if s.stype in [32, 139, 144, 147, 156, 179, 188, 221, 253, 274,
                       278, 310, 358, 436, 465, 477]:
            new_sprites.append(s)
            continue

        # Thwomps (47) -> Big Thwomps (48) — more imposing!
        if s.stype == 47:
            new_s = copy.deepcopy(s)
            new_s.stype = 48  # BIG_THWOMP
            new_sprites.append(new_s)
            continue

        # Big Thwomps stay as-is (already scary)
        if s.stype == 48:
            new_sprites.append(s)
            continue

        # Dry Bones (118) -> Giant Dry Bones (119) — tougher
        if s.stype == 118:
            new_s = copy.deepcopy(s)
            new_s.stype = 119  # GIANT_DRY_BONES
            new_sprites.append(new_s)
            continue

        # Rocky Wrenches (149) -> keep but add extra
        if s.stype == 149:
            new_sprites.append(s)
            # Add an extra one offset by 64 pixels to the right
            extra = copy.deepcopy(s)
            extra.x = s.x + 64
            new_sprites.append(extra)
            continue

        # Everything else: keep as-is
        new_sprites.append(s)

    # Add extra hazards
    # Fire Bars in the mid-section of the castle
    new_sprites.append(Sprite(stype=FIRE_BAR, x=3200, y=480,
                              spritedata=b'\x00\x00\x00\x00\x00\x00',
                              zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=FIRE_BAR, x=5600, y=480,
                              spritedata=b'\x00\x00\x00\x00\x00\x00',
                              zone_id=0, extra_byte=0))

    # Spinies near the end for extra pressure
    new_sprites.append(Sprite(stype=SPINY, x=7000, y=512,
                              spritedata=b'\x00\x00\x00\x00\x00\x00',
                              zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=SPINY, x=7200, y=512,
                              spritedata=b'\x00\x00\x00\x00\x00\x00',
                              zone_id=0, extra_byte=0))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))

    # Serialize modified area 1
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ MODIFY AREA 2 (Boss Room) ═══════════
    # Larry Koopa arena: zone 0 is at (1568,1408) size 1456x224
    # Boss floor is at y=1600 (verified from original data)
    # Zone x range: 1568 -> 3024. Zone y range: 1408 -> 1632.
    # Existing boss sprites: Larry(192) at (2560,1408), shutter(407) at
    # (2560,1600), controller(436) at (2768,1616)
    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))

    # Keep all original sprites (boss mechanics)
    boss_sprites = list(area2.sprites)

    # Add Podoboos (lava bubbles) — rise from the arena floor on both sides
    # X must be within 1568–3024, Y near 1600 (floor of the arena)
    boss_sprites.append(Sprite(stype=PODOBOO, x=1800, y=1600,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=PODOBOO, x=2150, y=1600,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=PODOBOO, x=2850, y=1600,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))

    # Add Dry Bones patrolling the arena floor — they revive when stomped!
    boss_sprites.append(Sprite(stype=DRY_BONES, x=1750, y=1568,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=DRY_BONES, x=2900, y=1568,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))

    # Fire Bar spinning in the center of the arena (between player & Larry)
    boss_sprites.append(Sprite(stype=FIRE_BAR, x=2050, y=1440,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))

    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))

    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # Area 3 (connecting room) — keep untouched

    # Save
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/01-24.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/01-24.arc ({len(data)} bytes)')




def create_level_tower():
    """Tower (01-22): Major overhaul — new enemy gauntlet, modified boss room."""
    import copy
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin, Sprite, LayerObject,
        parse_layer_data, serialize_layer_data
    )

    with open('extracted files/Stage/01-22.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1: Tower Climb ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.settings.time_limit = 250  # Tight! Gotta move fast

    # Keep ONLY essential non-enemy sprites, strip everything else
    essential_types = {
        32,   # Star coins
        96,   # Spine Coaster cars (brown rideable platforms)
        144,  # Red coins
        156,  # Red coin ring
        176,  # Roulette block
        188,  # Midway flag
        207,  # ? block
        253,  # Moving platform controllers
        255,  # Moving platform 2
        277,  # Controller
        310,  # Area controller
        345,  # Wire net mesh (structural)
        346,  # Wire net mesh 2 (structural)
        356,  # Brown segment/crushing platforms — the main traversal mechanic!
        436,  # System controller
        477,  # System controller 2
    }

    new_sprites = []
    for s in area1.sprites:
        if s.stype in essential_types:
            new_sprites.append(s)

    SD = b'\x00\x00\x00\x00\x00\x00'

    def add(stype, x, y):
        new_sprites.append(Sprite(stype=stype, x=x, y=y,
            spritedata=SD, zone_id=0, extra_byte=0))

    # ╔══════════════════════════════════════════════════╗
    # ║  BOTTOM (y=3808->3000): Welcome to the chaos     ║
    # ╚══════════════════════════════════════════════════╝
    # Dry Bones pairs on every platform
    for y in range(3760, 3000, -120):
        pass
# Spinies lurking between Dry Bones
    for y in range(3700, 3000, -200):
        add(SPINY, 500, y)
    # ParaGoombas swooping from above
    for y in range(3750, 3100, -250):
        add(PARAGOOMBA, 450, y)
        add(PARAGOOMBA, 550, y)
    # Bob-omb surprise near the start
    add(BOB_OMB, 500, 3600)
    add(BOB_OMB, 400, 3400)
    # Hammer Bro at bottom section exit
    add(HAMMER_BRO, 500, 3050)

    # ╔══════════════════════════════════════════════════╗
    # ║  MIDDLE (y=3000->2000): Pure madness              ║
    # ╚══════════════════════════════════════════════════╝
    # Spinies EVERYWHERE
    for y in range(2950, 2000, -100):
        add(SPINY, 380 + (y % 200), y)
    # Dry Bones reinforcements
    for y in range(2900, 2000, -150):
        pass
# Bob-omb clusters — 3 in a row!
    add(BOB_OMB, 420, 2700); add(BOB_OMB, 480, 2700); add(BOB_OMB, 540, 2700)
    add(BOB_OMB, 400, 2300); add(BOB_OMB, 460, 2300); add(BOB_OMB, 520, 2300)
    # ParaGoombas swarming
    for y in range(2800, 2000, -200):
        add(PARAGOOMBA, 400, y)
        add(PARAGOOMBA, 520, y)
        add(PARAGOOMBA, 600, y)
    # Hammer Bro mid-tower
    add(HAMMER_BRO, 480, 2500)

    # ╔══════════════════════════════════════════════════╗
    # ║  UPPER (y=2000->1200): Absolute insanity          ║
    # ╚══════════════════════════════════════════════════╝
    # Hammer Bro + Spinies combo
    add(HAMMER_BRO, 500, 1900)
    for y in range(1850, 1200, -100):
        add(SPINY, 400 + (y % 160), y)
    # Dry Bones guarding every ledge
    for y in range(1800, 1200, -120):
        pass
# Bob-omb rain
    add(BOB_OMB, 500, 1600); add(BOB_OMB, 400, 1500)
    add(BOB_OMB, 600, 1400); add(BOB_OMB, 500, 1300)
    # Extra ParaGoombas — constant aerial threat
    for y in range(1750, 1200, -150):
        add(PARAGOOMBA, 450, y)
        add(PARAGOOMBA, 550, y)

    # ╔══════════════════════════════════════════════════╗
    # ║  TOP (y=1200->896): Boss gate gauntlet            ║
    # ╚══════════════════════════════════════════════════╝
    # TWO Hammer Bros guarding the boss pipe!
    add(HAMMER_BRO, 420, 1100)
    add(HAMMER_BRO, 580, 1050)
    # Spinies for good measure
    add(SPINY, 450, 1000); add(SPINY, 550, 1000)
    add(SPINY, 500, 950)
    # Bob-omb farewell party
    add(BOB_OMB, 400, 980); add(BOB_OMB, 500, 960); add(BOB_OMB, 600, 940)

    # Coins scattered through the climb
    for y in range(3700, 900, -200):
        add(COIN, 450, y)
        add(COIN, 550, y)

    # Red coin ring mid-climb with 8 matching coins
    ring_sd = b'\x00\x22\x00\x00\x00\x00'  # group_id=0x22 in byte 1
    coin_sd = b'\x00\x22\x00\x00\x00\x00'
    new_sprites.append(Sprite(stype=RED_COIN_RING, x=500, y=2600,
        spritedata=ring_sd, zone_id=0, extra_byte=0))
    coin_offsets = [
        (32, 0), (32, -16), (16, -32), (-16, -32),
        (-32, -16), (-32, 0), (-16, 32), (16, 32),
    ]
    for dx, dy in coin_offsets:
        new_sprites.append(Sprite(stype=RED_COIN, x=500+dx, y=2600+dy,
            spritedata=coin_sd, zone_id=0, extra_byte=0))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Modified Boss Room ═══════════
    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))

    # Keep boss sprites (Larry + controllers) exactly as-is
    # But modify the terrain to add small side platforms for dodge opportunities
    l1_boss = parse_layer_data(arc.get_file('course/course2_bgdatL1.bin'))

    # Add two small elevated platforms on the sides of the arena
    l1_boss.append(LayerObject(tileset=1, obj_type=0, x=22, y=32, w=4, h=1))
    l1_boss.append(LayerObject(tileset=1, obj_type=0, x=38, y=32, w=4, h=1))
    # Small center platform higher up
    l1_boss.append(LayerObject(tileset=1, obj_type=0, x=30, y=28, w=4, h=1))

    arc.set_file('course/course2_bgdatL1.bin', serialize_layer_data(l1_boss))

    # Save
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/01-22.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/01-22.arc ({len(data)} bytes)')


def create_level_2_castle():
    """Castle (02-24): Roy's Three-Way Maze. Overhauled traversal and boss room."""
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/02-24.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1: Traversal ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.settings.time_limit = 400

    essential_types = {
        31, 32, 33, 41, 65, 91, 139, 147, 278, 310, 358, 465, 477 # Checkpoints, platforms, blocks, doors
    }

    new_sprites = []
    for s in area1.sprites:
        if s.stype in essential_types:
            new_sprites.append(s)

    # Convert Dry Bones (118) to Giant Dry Bones (119) and Thwomps (46) to Big Thwomps (48)
    for s in area1.sprites:
        if s.stype == 118:
            new_s = copy.deepcopy(s)
            new_s.stype = 119
            new_sprites.append(new_s)
        elif s.stype == 46:
            new_s = copy.deepcopy(s)
            new_s.stype = 48
            new_sprites.append(new_s)

    SD = b'\x00\x00\x00\x00\x00\x00'
    def add(stype, x, y, spritedata=SD):
        new_sprites.append(Sprite(stype=stype, x=x, y=y, spritedata=spritedata, zone_id=0, extra_byte=0))

    # Add Sand Geysers throughout the level. 0x03 is tall, 0x01 is short
    gsr_tall = b'\x00\x00\x00\x00\x00\x03'
    gsr_med = b'\x00\x00\x00\x00\x00\x02'

    # Injecting geysers across the long straightaways (X bounds 1500 to 6000)
    for x in range(1600, 6000, 500):
        # Place Geyser at ground level (Y ~ 480)
        add(140, x, 512, spritedata=gsr_tall)
        add(140, x + 100, 512, spritedata=gsr_med)

    # Add some Pokeys into the castle corridors to disrupt horizontal movement
    for x in range(2000, 6000, 650):
        add(POKEY, x, 512)

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Boss Room ═══════════
    # Boss Zone 1: x=3488-4032, y=1360-1632 (the actual boss arena)
    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)

    # Two Dry Bones on the arena floor — they revive during the fight,
    # adding an extra nuisance without making it impossible.
    boss_sprites.append(Sprite(stype=DRY_BONES, x=3600, y=1584, spritedata=b'\x00\x00\x00\x00\x00\x00', zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=DRY_BONES, x=3900, y=1584, spritedata=b'\x00\x00\x00\x00\x00\x00', zone_id=0, extra_byte=0))

    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # Save modified archive
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/02-24.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/02-24.arc ({len(data)} bytes)')


def create_level_cannon():
    """Cannon (01-36): Modify the real world 1 cannon room with a chaotic gauntlet.
    Also copy/modify enemy courses (01-33/34/35)."""
    import copy
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    os.makedirs('output/ChaosStation/Stage', exist_ok=True)

    # ═══════════ REAL CANNON: 01-36 ═══════════
    # This is the cannon room — wide 1792x512 area with cannon barrels (387)
    # and launcher sprites (248/249). Player runs through to reach the cannon.
    with open('extracted files/Stage/01-36.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    area = parse_course_bin(arc.get_file('course/course1.bin'))
    area.settings.time_limit = 200  # Pressured but fair

    # Keep ALL existing sprites (cannons, launchers, controllers, items)
    # but ADD enemies to create a gauntlet challenge!
    SD = b'\x00\x00\x00\x00\x00\x00'

    # Original entrance at x=464, cannon barrels spread from x=400 to x=1616
    # Ground level around y=736, zone top at y=256

    # Enemies guarding the path to the cannon!
    # Early section (x=500-800): Easy enemies
    area.sprites.append(Sprite(stype=GOOMBA, x=560, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=GOOMBA, x=640, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=SPINY, x=700, y=720, spritedata=SD, zone_id=0, extra_byte=0))

    # Mid section (x=800-1100): Getting harder
    area.sprites.append(Sprite(stype=DRY_BONES, x=800, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=SPINY, x=880, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=HAMMER_BRO, x=960, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=BOB_OMB, x=1040, y=720, spritedata=SD, zone_id=0, extra_byte=0))

    # ParaGoombas swooping overhead
    area.sprites.append(Sprite(stype=PARAGOOMBA, x=600, y=600, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=PARAGOOMBA, x=850, y=580, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=PARAGOOMBA, x=1100, y=600, spritedata=SD, zone_id=0, extra_byte=0))

    # Late section (x=1100-1500): Intense
    area.sprites.append(Sprite(stype=SPINY, x=1150, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=DRY_BONES, x=1250, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=BOB_OMB, x=1350, y=720, spritedata=SD, zone_id=0, extra_byte=0))
    area.sprites.append(Sprite(stype=HAMMER_BRO, x=1450, y=720, spritedata=SD, zone_id=0, extra_byte=0))

    # Coins to guide the way
    for cx in range(520, 1500, 120):
        area.sprites.append(Sprite(stype=COIN, x=cx, y=680, spritedata=SD, zone_id=0, extra_byte=0))

    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))

    data = arc.pack()
    with open('output/ChaosStation/Stage/01-36.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/01-36.arc ({len(data)} bytes)')

    # ═══════════ ENEMY COURSES: 01-33/34/35 ═══════════
    # These are the toad rescue / enemy ambush levels.
    # W1 vanilla has Goombas (20) in -33, Parabombs (198) in -34, sprite 199 in -35.
    # Cycle through tougher enemies and add extra companions for a real challenge.
    enemy_cycle = [SPINY, HAMMER_BRO, DRY_BONES, PARAGOOMBA, 
                   BOB_OMB, SPINY, HAMMER_BRO, DRY_BONES]
    # Enemy types that should be replaced (the actual threats)
    replaceable = {20, 198, 199}  # Goomba, Parabomb, sprite 199
    
    for fname in ['01-33', '01-34', '01-35']:
        src = f'extracted files/Stage/{fname}.arc'
        if not os.path.exists(src):
            continue
        with open(src, 'rb') as f:
            arc2 = U8Archive.load(f.read())
        area2 = parse_course_bin(arc2.get_file('course/course1.bin'))
        area2.settings.time_limit = 60  # Tighter!

        new_sprites = []
        enemy_idx = 0
        for s in area2.sprites:
            if s.stype in replaceable:
                ns = copy.deepcopy(s)
                ns.stype = enemy_cycle[enemy_idx % len(enemy_cycle)]
                ns.spritedata = SD
                new_sprites.append(ns)
                # Add a Goomba companion nearby
                extra = copy.deepcopy(s)
                extra.x += 32
                extra.stype = GOOMBA
                extra.spritedata = SD
                new_sprites.append(extra)
                enemy_idx += 1
            else:
                new_sprites.append(s)

        area2.sprites = new_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in new_sprites))
        arc2.set_file('course/course1.bin', serialize_course_bin(area2))
        data2 = arc2.pack()
        with open(f'output/ChaosStation/Stage/{fname}.arc', 'wb') as f:
            f.write(data2)
        print(f'Saved: output/ChaosStation/Stage/{fname}.arc ({len(data2)} bytes)')


def create_mushroom_houses():
    """Mushroom Houses (01-26 to 01-29, 02-26 to 02-28, 03-26 to 03-28): Modified item configurations and structure."""
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin, LayerObject,
        parse_layer_data, serialize_layer_data
    )

    os.makedirs('output/ChaosStation/Stage', exist_ok=True)

    configs = {
        '01-26': b'\x00\x00\x08\x00\x00\xe0',
        '01-27': b'\x00\x00\x0c\x00\x00\xe0',
        '01-28': b'\x00\x00\x04\x00\x00\xe0',
        '01-29': b'\x00\x00\x10\x00\x00\xe0',
        '02-26': b'\x00\x00\x08\x00\x00\xe0',
        '02-27': b'\x00\x00\x0c\x00\x00\xe0',
        '02-28': b'\x00\x00\x10\x00\x00\xe0',
        '03-26': b'\x00\x00\x10\x00\x00\xe0',
        '03-27': b'\x00\x00\x08\x00\x00\xe0',
        '03-28': b'\x00\x00\x0c\x00\x00\xe0',
    }

    for fname, item_sd in configs.items():
        src = f'extracted files/Stage/{fname}.arc'
        dst = f'output/ChaosStation/Stage/{fname}.arc'
        if not os.path.exists(src):
            continue

        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())

        area = parse_course_bin(arc.get_file('course/course1.bin'))

        # Modify item rewards
        for s in area.sprites:
            if s.stype == 179:
                s.spritedata = item_sd

        arc.set_file('course/course1.bin', serialize_course_bin(area))

        # Completely redesign the interior architecture of the power-up room
        # Green/Yellow houses use course2.bin for the powerup room.
        # Red houses (like W3's 03-26, 03-27, 03-28) use course1.bin for the powerup room.
        # Completely redesign the interior architecture of the power-up room
        # Green/Yellow houses use course2.bin for the powerup room.
        # Red houses (like W3's 03-26, 03-27, 03-28) use course1.bin for the powerup room.
        # Since Toad Houses lack a collision layer by default, we will CREATE a bgdatL0.bin
        # and inject it into the archive so our custom terrain has physics and visuals!
        try:
            has_area2 = 'course/course2.bin' in arc.list_files()
            target_area_fname = 'course/course2.bin' if has_area2 else 'course/course1.bin'
            target_layer_fname = 'course/course2_bgdatL0.bin' if has_area2 else 'course/course1_bgdatL0.bin'
            
            world_prefix = fname[:2]  # '01', '02', or '03'
            
            # The X coordinate offset varies. In course2.bin it starts around blocks 21. 
            # In course1.bin (for red houses) it starts around block 84.
            ox = 21 if has_area2 else 84
            
            l0 = []
            
            if world_prefix == '01':
                # W1: "Checkerboard Platforms" (Single Bricks)
                # Left platforms
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+3, y=31, w=1, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+5, y=31, w=1, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+7, y=31, w=1, h=1))
                # Right platforms
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+40, y=31, w=1, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+42, y=31, w=1, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+44, y=31, w=1, h=1))
                
                # High middle platforms
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+16, y=25, w=3, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+30, y=25, w=3, h=1))
                    
            elif world_prefix == '02':
                # W2: "The Ancient Ruins" (Brick pillars)
                # Left pillar
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+6, y=26, w=2, h=12))
                # Right pillar
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+42, y=26, w=2, h=12))
                # Crossbeams
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+8, y=26, w=2, h=1))
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+40, y=26, w=2, h=1))
                    
            elif world_prefix == '03':
                # W3: "Crystal Bridges" (Brick bridges)
                # Left bridge
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+1, y=31, w=12, h=1))
                # Right bridge
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+33, y=31, w=12, h=1))
                # Lower safety net
                l0.append(LayerObject(tileset=0, obj_type=31, x=ox+19, y=35, w=11, h=1))

            # Inject the newly created collision layer into the archive
            arc.set_file(target_layer_fname, serialize_layer_data(l0))
            
        except Exception as e:
            print(f"Error processing terrain for {fname}: {e}")

        data = arc.pack()
        with open(dst, 'wb') as f:
            f.write(data)
        print(f'Saved: {dst} ({len(data)} bytes)')


def create_riivolution_xml():
    """Create Riivolution XML for the mod."""
    xml = """<?xml version="1" encoding="utf-8"?>
<wiidisc version="1">
    <id game="SMN" />
    <options>
        <section name="Chaos Station v2">
            <option id="levels" name="Custom Levels" default="1">
                <choice name="Enabled">
                    <patch id="chaoslevels" />
                </choice>
            </option>
        </section>
    </options>
    <patch id="chaoslevels">
        <folder external="/ChaosStation/Stage" disc="/Stage" />
        <folder external="/ChaosStation/Object" disc="/Object" />
        <folder external="/ChaosStation/Layout" disc="/Layout" />
        <folder external="/ChaosStation/US/Layout" disc="/US/Layout" />
        <folder external="/ChaosStation/US/EngUS/staffroll" disc="/US/EngUS/staffroll" />
        <folder external="/ChaosStation/EU/Layout" disc="/EU/Layout" />
        <folder external="/ChaosStation/Sound/stream" disc="/Sound/stream" />
        <file external="/ChaosStation/Sound/wii_mj2d_sound.brsar" disc="/Sound/wii_mj2d_sound.brsar" />
    </patch>
</wiidisc>
"""
    os.makedirs('output/riivolution', exist_ok=True)
    with open('output/riivolution/nsmbw_mod.xml', 'w') as f:
        f.write(xml)
    print('Saved: output/riivolution/nsmbw_mod.xml')


def _is_skin_tone(r, g, b):
    """Detect if a pixel is a skin tone (peachy/beige)."""
    import colorsys
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    if s < 0.25 and 0.15 < v < 0.95:
        if 0.0 < h < 0.15 or h > 0.9:
            return True
    if r > 180 and g > 140 and b > 100 and r > g > b:
        if (r - b) > 50 and (g - b) > 20:
            return True
    if 100 < r < 220 and 80 < g < 180 and 60 < b < 140:
        if r > g and g > b and (r - b) > 30:
            return True
    return False


def _is_eye_or_white(r, g, b):
    """Detect white/gray (eyes, buttons, etc)."""
    if r > 200 and g > 200 and b > 200:
        return True
    if r < 60 and g < 60 and b < 60:
        return True
    return False


def _shift_pixel_smart(r, g, b, target_hue_range, new_hue, sat_mult, val_mult):
    """Smart pixel shift with hue-based masking and skin tone preservation."""
    import colorsys
    if r > 230 and g > 230 and b > 230 or r < 30 and g < 30 and b < 30:
        return r, g, b
    if _is_skin_tone(r, g, b):
        return r, g, b
    if _is_eye_or_white(r, g, b):
        return r, g, b
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    if s < 0.15:
        return r, g, b
    h_min, h_max = target_hue_range
    if h_min <= h_max:
        if not (h_min <= h <= h_max):
            return r, g, b
    else:
        if not (h >= h_min or h <= h_max):
            return r, g, b
    hue_offset = h - sum(target_hue_range) / 2
    new_h = (new_hue + hue_offset * 0.2) % 1.0
    new_s = min(1.0, s * sat_mult)
    new_v = min(1.0, v * val_mult)
    nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
    return int(nr * 255), int(ng * 255), int(nb * 255)


def _toad_shifter(r, g, b):
    """Toad color shifter: Blue->Purple, Yellow->Orange."""
    import colorsys
    if r > 230 and g > 230 and b > 230 or r < 30 and g < 30 and b < 30:
        return r, g, b
    if _is_skin_tone(r, g, b):
        return r, g, b
    if _is_eye_or_white(r, g, b):
        return r, g, b
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    if s < 0.15:
        return r, g, b
    if 0.55 <= h <= 0.72:
        return _shift_pixel_smart(r, g, b, (0.55, 0.72), 0.78, 1.1, 0.8)
    if 0.08 <= h <= 0.18:
        return _shift_pixel_smart(r, g, b, (0.08, 0.18), 0.03, 1.2, 0.9)
    if h >= 0.92 or h <= 0.06:
        return _shift_pixel_smart(r, g, b, (0.92, 0.06), 0.98, 0.8, 0.7)
    return r, g, b


def build_all_textures():
    """Build all Chaos Station texture modifications."""
    import colorsys
    from tpl_converter import png_to_tpl_match_size
    from tools.u8archive import U8Archive

    print("\n[Texture Mods] Building all texture modifications...")

    print("  [a] Title screen logo...")
    try:
        from create_logo import create_chaos_station_logo
        create_chaos_station_logo('title_logo.png')
        with open(r'extracted files/US/Layout/openingTitle/openingTitle.arc', 'rb') as f:
            arc = U8Archive.load(f.read())
        orig_tpl = arc.get_file('arc/timg/wiiMario_Title_logo_local_00.tpl')
        png_to_tpl_match_size('title_logo.png', '_logo_new.tpl', len(orig_tpl))
        with open('_logo_new.tpl', 'rb') as f:
            new_tpl = f.read()
        arc.set_file('arc/timg/wiiMario_Title_logo_local_00.tpl', new_tpl)
        dst = 'output/ChaosStation/Layout/openingTitle/openingTitle.arc'
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(arc.pack())
        try: os.remove('_logo_new.tpl')
        except: pass
        print("    Title logo injected")
    except Exception as e:
        print(f"    Title logo failed: {e}")

    print("  [b] Character & item 3D models...")
    try:
        from color_shift_v2 import process_character
        process_character('extracted files/Object/Mario.arc',
                          'output/ChaosStation/Object/Mario.arc',
                          lambda r, g, b: _shift_pixel_smart(r, g, b, (0.92, 0.06), 0.75, 0.5, 0.45),
                          'Mario (Red -> Dark Purple)')
        process_character('extracted files/Object/Luigi.arc',
                          'output/ChaosStation/Object/Luigi.arc',
                          lambda r, g, b: _shift_pixel_smart(r, g, b, (0.20, 0.45), 0.52, 1.1, 0.7),
                          'Luigi (Green -> Teal)')
        process_character('extracted files/Object/Kinopio.arc',
                          'output/ChaosStation/Object/Kinopio.arc',
                          _toad_shifter,
                          'Toads (Blue->Purple, Yellow->Orange)')
        # Dark Peach - like Paper Mario TTYD (pink dress -> dark/black)
        process_character('extracted files/Object/peach.arc',
                          'output/ChaosStation/Object/peach.arc',
                          lambda r, g, b: _shift_pixel_smart(r, g, b, (0.88, 0.02), 0.0, 0.2, 0.25),
                          'Peach (Pink -> Dark Peach)')
        def coin_shifter(r, g, b):
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            if s < 0.1: return r, g, b
            if 0.08 <= h <= 0.18:
                return [int(c*255) for c in colorsys.hsv_to_rgb((h+0.40)%1.0, s*0.9, v*0.9)]
            return r, g, b
        for name in ['star_coin', 'coin', 'obj_coin', 'red_ring']:
            src = f'extracted files/Object/{name}.arc'
            dst = f'output/ChaosStation/Object/{name}.arc'
            if os.path.exists(src):
                process_character(src, dst, coin_shifter, f'{name} gold->teal')
        print("    All 3D models shifted")
    except Exception as e:
        print(f"    3D models failed: {e}")

    print("  [c] HUD character icons...")
    try:
        from shift_icons import ICON_ARCHIVES, ICON_SHIFTS
        from shift_icons import shift_icon_rgb5a3
        for src_path, dst_path in ICON_ARCHIVES:
            if not os.path.exists(src_path):
                continue
            with open(src_path, 'rb') as f:
                arc = U8Archive.load(f.read())
            for tpl, hue_range, new_hue, sat_m, val_m, label in ICON_SHIFTS:
                if tpl in arc.list_files():
                    orig = arc.get_file(tpl)
                    shifted = shift_icon_rgb5a3(orig, hue_range, new_hue, sat_m, val_m)
                    arc.set_file(tpl, shifted)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            with open(dst_path, 'wb') as f:
                f.write(arc.pack())
    except Exception as e:
        print(f"    HUD icons failed: {e}")

    print("  [d] Item textures...")
    try:
        from build_textures import TEXTURE_SHIFTS, shift_rgb5a3_tile, shift_icon_rgb5a3
        for arc_name, shifts in TEXTURE_SHIFTS.items():
            src_path = f'extracted files/Layout/{arc_name}/{arc_name}.arc'
            dst_path = f'output/ChaosStation/Layout/{arc_name}/{arc_name}.arc'
            if not os.path.exists(src_path):
                continue
            with open(src_path, 'rb') as f:
                arc = U8Archive.load(f.read())
            for shift_args in shifts:
                tpl = shift_args[0]
                if tpl not in arc.list_files():
                    continue
                orig = arc.get_file(tpl)
                if shift_args[1] == 'icon':
                    _, _, target_range, new_h, sat, val, lbl = shift_args
                    shifted = shift_icon_rgb5a3(orig, target_range, new_h, sat, val)
                else:
                    _, hue, sat, val, lbl = shift_args
                    shifted = shift_rgb5a3_tile(orig, hue, sat, val)
                arc.set_file(tpl, shifted)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            with open(dst_path, 'wb') as f:
                f.write(arc.pack())
    except Exception as e:
        print(f"    Item textures failed: {e}")

    print("  All textures built!")


def create_title_screen_branding():
    """Patch opening.bnr to show 'Chaos Station Mod' in the Wii menu channel banner.

    The NSMBW opening.bnr uses the BNR1 format:
      Offset 0x0000: "BNR1" magic
      Offset 0x0020: 6 repeating IMD5-compressed image blocks (not relevant here)
      The text section begins at the first occurrence after the image data.

    For BNR1 (single region), the string block starts at 0x1820:
      +0x00  (32 bytes): Game short title in Shift-JIS / Latin-1
      +0x20  (32 bytes): Developer short name in Shift-JIS / Latin-1
      +0x40  (64 bytes): Game long title
      +0x80  (64 bytes): Developer long name
      +0xC0  (128 bytes): Game description / comment

    We overwrite these with our mod's identity, keeping null termination.
    """
    src = 'extracted files/opening.bnr'
    dst = 'output/ChaosStation/opening.bnr'

    with open(src, 'rb') as f:
        data = bytearray(f.read())

    # BNR1 magic may be at offset 0x40 (after IMET header), not necessarily at start
    bnr_offset = data.find(b'BNR1')
    if bnr_offset == -1:
        bnr_offset = data.find(b'BNR2')
    if bnr_offset == -1:
        print(f'  [!] opening.bnr: no BNR1/BNR2 magic found — skipping title patch')
        return

    TEXT_OFFSET = bnr_offset + 0x1820  # Standard BNR1 text block start (relative to magic)

    def write_ascii(buf, offset, text, max_len):
        """Write null-terminated ASCII string into buf at offset, max_len bytes."""
        encoded = text.encode('ascii', errors='replace')[:max_len - 1]
        buf[offset:offset + max_len] = b'\x00' * max_len  # zero-fill first
        buf[offset:offset + len(encoded)] = encoded

    short_title = "Chaos Station"       # 32 bytes
    short_dev   = "Custom Mod"          # 32 bytes
    long_title  = "New Super Mario Bros. Wii — Chaos Station Mod"  # 64 bytes
    long_dev    = "A Fan-Made Modification"                         # 64 bytes
    description = "A challenging World 1 overhaul mod featuring custom levels, " \
                  "harder enemies, ocean depths and ghost house chaos!"          # 128 bytes

    write_ascii(data, TEXT_OFFSET + 0x00, short_title, 32)
    write_ascii(data, TEXT_OFFSET + 0x20, short_dev,   32)
    write_ascii(data, TEXT_OFFSET + 0x40, long_title,  64)
    write_ascii(data, TEXT_OFFSET + 0x80, long_dev,    64)
    write_ascii(data, TEXT_OFFSET + 0xC0, description, 128)

    os.makedirs('output/ChaosStation', exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)
    print(f'Saved: {dst} (BNR title patched to "Chaos Station Mod")')


def create_level_2_3():
    """
    Level 2-3: "Oasis Heights"

    A high-altitude athletic desert level focused on narrow pillars,
    tricky gaps, and managing Pokeys and Bullet Bills.
    """
    level = LevelBuilder()
    a1 = level.add_area(1)

    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_DESERT)
    a1.set_time(350)
    a1.set_background(BG_DESERT)

    ZX, ZY = 256, 256
    ZW, ZH = 7200, 352
    a1.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, cam_mode=0, visibility=16)

    TX = 16
    GY = 34

    # Player start
    a1.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)

    # Midway respawn
    a1.add_entrance(1, x=1568, y=544, etype=ENTRANCE_NORMAL, zone_id=0)

    # ── TERRAIN ──
    # Start platform
    a1.add_ground(TX, GY, width=12, height=5)
    a1.add_question_block(TX + 5, GY - 4, contents=1)  # Mushroom

    # Gap jumping section 1
    a1.add_ground(TX + 15, GY, width=3, height=5)
    a1.add_ground(TX + 21, GY - 2, width=3, height=7)
    a1.add_ground(TX + 27, GY - 4, width=3, height=9)
    a1.add_ground(TX + 33, GY - 6, width=2, height=11)

    a1.add_coin_line(TX + 18, GY - 2, count=3)
    a1.add_coin_line(TX + 24, GY - 4, count=3)
    a1.add_coin_line(TX + 30, GY - 6, count=3)

    # Small safe zone
    a1.add_ground(TX + 38, GY - 2, width=15, height=7)
    a1.add_question_block(TX + 42, GY - 6, contents=5) # Propeller block
    a1.add_question_block(TX + 46, GY - 6)
    a1.add_star_coin(TX + 44, GY - 9, coin_num=0)

    # Pillar section 2 - moving up and down
    a1.add_ground(TX + 56, GY, width=4, height=5)
    a1.add_ground(TX + 63, GY - 3, width=2, height=8)
    a1.add_ground(TX + 68, GY, width=4, height=5)
    a1.add_ground(TX + 75, GY - 4, width=2, height=9)
    a1.add_ground(TX + 80, GY, width=10, height=5)

    # Midway flag
    a1.add_sprite(MIDWAY_FLAG, x=(TX + 82) * 16, y=(GY - 3) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Star coin 2 requires propeller or a good jump (height lowered to be reachable in wind)
    a1.add_star_coin(TX + 76, GY - 8, coin_num=1)

    # The Pokeys of Doom
    a1.add_ground(TX + 93, GY, width=25, height=5)
    # Staggered small platforms above
    a1.add_platform(TX + 96, GY - 4, width=3)
    a1.add_platform(TX + 102, GY - 6, width=3)
    a1.add_platform(TX + 108, GY - 4, width=3)

    a1.add_star_coin(TX + 103, GY - 2, coin_num=2) # Under the middle platform, risky Pokey jump

    # Final gap sequence
    a1.add_ground(TX + 121, GY - 2, width=4, height=7)
    a1.add_ground(TX + 128, GY - 4, width=2, height=9)
    a1.add_ground(TX + 133, GY - 6, width=2, height=11)
    a1.add_ground(TX + 138, GY - 8, width=2, height=13)

    # Goal area
    a1.add_ground(TX + 143, GY, width=30, height=5)
    a1.add_staircase(TX + 150, GY, steps=8, direction=1)
    a1.add_sprite(GOAL_POLE, x=(TX + 162) * 16, y=(GY - 10) * 16, zone_id=0)

    # ── SPRITES ──
    # Environment effect: Sandstorm (wind) visuals (Nybble 12 = 1 => Sandstorm)
    a1.add_sprite(SANDSTORM, x=ZX + 16, y=ZY + 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x01')
    # Physics for wind (Sprite 90)
    # Nybble 5 (Time ON) = F, Nybble 6 (Time OFF) = 0 => Byte 2 = 0xF0
    # Nybble 7 (Blows Left) = 1 => Byte 3 = 0x10
    # Nybble 12 (Force) = 1 (Low) => Byte 5 = 0x01
    a1.add_sprite(90, x=ZX + 16, y=ZY + 16, zone_id=0, spritedata=b'\x00\x00\xF0\x10\x00\x01')

    a1.add_sprite(POKEY, x=(TX + 15) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 27) * 16, y=(GY - 5) * 16, zone_id=0)

    a1.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 40) * 16, y=(GY - 5) * 16, zone_id=0)
    a1.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 50) * 16, y=(GY - 4) * 16, zone_id=0)

    a1.add_sprite(POKEY, x=(TX + 57) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 69) * 16, y=(GY - 1) * 16, zone_id=0)

    # The gauntlet Pokeys
    a1.add_sprite(POKEY, x=(TX + 98) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 104) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 110) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 116) * 16, y=(GY - 1) * 16, zone_id=0)

    a1.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 122) * 16, y=(GY - 5) * 16, zone_id=0)
    level.save("output/ChaosStation/Stage/02-03.arc")


def create_level_2_4():
    """
    Level 2-4: "Desert Gales"

    Heavy focus on lateral wind currents, bottomless pits, Lakitus, and Sand Geysers.
    Forces the player to manage momentum while avoiding Spinies.
    """
    level = LevelBuilder()
    a1 = level.add_area(1)

    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_DESERT)
    a1.set_time(400)
    a1.set_background(BG_DESERT)

    ZX, ZY = 256, 256
    ZW, ZH = 11000, 352
    a1.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, cam_mode=0, visibility=16)

    TX = 16
    GY = 34

    # Player start
    a1.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)

    # Midway respawn
    a1.add_entrance(1, x=1296, y=464, etype=ENTRANCE_NORMAL, zone_id=0)

    # ── TERRAIN ──
    # Start platform
    a1.add_ground(TX, GY, width=15, height=5)
    a1.add_question_block(TX + 5, GY - 4, contents=5)  # Propeller suit is a trap/blessing in wind

    # Jump 1 - introduction to bottomless pits in wind
    a1.add_ground(TX + 20, GY - 2, width=8, height=7)
    a1.add_coin_line(TX + 17, GY - 2, count=3)

    a1.add_ground(TX + 32, GY, width=6, height=5)
    a1.add_star_coin(TX + 34, GY - 3, coin_num=0)

    # Geyser section
    a1.add_ground(TX + 42, GY, width=10, height=5)
    
    # We place a physical block, but the geyser sprite will be under it
    a1.add_ground(TX + 45, GY, width=2, height=1) 
    a1.add_question_block(TX + 46, GY - 5, contents=1) # Mushroom above the geyser
    
    # Gap with floating platform
    a1.add_platform(TX + 56, GY - 4, width=4)
    a1.add_ground(TX + 64, GY - 2, width=8, height=7)
    
    # Midway flag
    a1.add_sprite(MIDWAY_FLAG, x=(TX + 65) * 16, y=(GY - 5) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Lakitu assault zone - very sparse platforms
    a1.add_ground(TX + 78, GY, width=5, height=5)
    a1.add_platform(TX + 88, GY - 4, width=3)
    a1.add_platform(TX + 96, GY - 6, width=3)
    
    a1.add_star_coin(TX + 97, GY - 2, coin_num=1) # Tricky low Star Coin under Lakitu fire

    a1.add_ground(TX + 104, GY - 2, width=6, height=7)
    a1.add_ground(TX + 115, GY, width=5, height=5)
    
    # Triple geyser setup
    a1.add_ground(TX + 125, GY, width=20, height=5)
    a1.add_ground(TX + 150, GY, width=8, height=5)

    a1.add_star_coin(TX + 135, GY - 10, coin_num=2)

    # ─── Extension: The Windy Chasm ───
    a1.add_ground(TX + 162, GY, width=15, height=5)
    
    # Series of floating islands
    a1.add_platform(TX + 180, GY - 3, width=3)
    a1.add_platform(TX + 188, GY - 6, width=3)
    a1.add_platform(TX + 196, GY - 9, width=4)
    a1.add_platform(TX + 206, GY - 6, width=3)
    a1.add_platform(TX + 214, GY - 3, width=3)
    
    a1.add_ground(TX + 222, GY, width=15, height=5)
    
    # ─── Final Extension: Geyser Dash ───
    a1.add_ground(TX + 242, GY, width=2, height=1) 
    a1.add_ground(TX + 248, GY, width=2, height=1) 
    a1.add_ground(TX + 254, GY, width=2, height=1) 
    
    # New Goal area
    a1.add_ground(TX + 262, GY, width=30, height=5)
    a1.add_staircase(TX + 269, GY, steps=8, direction=1)
    a1.add_sprite(GOAL_POLE, x=(TX + 282) * 16, y=(GY - 10) * 16, zone_id=0)

    # ── SPRITES ──
    # Environment effect: Sandstorm (wind) visuals
    a1.add_sprite(SANDSTORM, x=ZX + 16, y=ZY + 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x01')
    
    # Physics for wind (Sprite 90) - Blowing RIGHT this time to push the player TOO FAST
    # Nybble 5 (Time ON) = F, Nybble 6 (Time OFF) = F => Byte 2 = 0xFF (pulsing wind)
    # Nybble 7 (Blows Left) = 0 => Byte 3 = 0x00
    # Nybble 12 (Force) = 3 (High) => Byte 5 = 0x03
    a1.add_sprite(90, x=ZX + 16, y=ZY + 16, zone_id=0, spritedata=b'\x00\x00\xFF\x00\x00\x03')

    # Pokeys
    a1.add_sprite(POKEY, x=(TX + 22) * 16, y=(GY - 3) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 68) * 16, y=(GY - 3) * 16, zone_id=0)
    
    # Sand Geysers (Sprite 140). Nybble 12 sets size/height.
    # We will use 0x03 for a tall geyser
    a1.add_sprite(140, x=(TX + 46) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')
    a1.add_sprite(140, x=(TX + 130) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')
    a1.add_sprite(140, x=(TX + 135) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')
    a1.add_sprite(140, x=(TX + 140) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')

    # Extended geysers
    a1.add_sprite(140, x=(TX + 243) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')
    a1.add_sprite(140, x=(TX + 249) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')
    a1.add_sprite(140, x=(TX + 255) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x00\x00\x03')

    # Lakitu (Sprite 54). Spawns and starts throwing spinies.
    a1.add_sprite(54, x=(TX + 82) * 16, y=(GY - 10) * 16, zone_id=0)
    
    level.save("output/ChaosStation/Stage/02-04.arc")





def create_level_2_5():
    """
    Level 2-5: "Sunbaked Ruins"
    A harsh mixed-terrain level focusing on Hammer/Boomerang/Fire Bros.
    Heavy use of vertical Pa1_nohara block structures simulating pyramids.
    """
    import os
    level = LevelBuilder()
    
    a1 = level.add_area(1)
    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_DESERT)
    a1.set_time(400)
    a1.set_background(BG_DESERT)
    
    ZX, ZY = 256, 256
    ZW, ZH = 10000, 384
    a1.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, cam_mode=0, visibility=16)
    
    TX = 16
    GY = 35
    
    # ── ENTRANCES ──
    a1.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)
    a1.add_entrance(1, x=ZX + 4800, y=368, etype=ENTRANCE_NORMAL, zone_id=0)
    
    # ── TERRAIN & ENEMIES ──
    # Starting platform
    a1.add_ground(TX, GY, width=20, height=5)
    
    # Pyramid structure 1
    a1.add_staircase(TX + 22, GY, steps=5, direction=1)   # up
    a1.add_staircase(TX + 27, GY - 5, steps=5, direction=-1) # down
    a1.add_ground(TX + 27, GY - 5, width=5, height=10) # core block
    
    # Fire Bro on top of pyramid
    a1.add_sprite(FIRE_BRO, x=(TX + 30) * 16, y=(GY - 7) * 16, zone_id=0)
    
    # Valley
    a1.add_ground(TX + 34, GY, width=12, height=5)
    a1.add_sprite(POKEY, x=(TX + 40) * 16, y=(GY - 3) * 16, zone_id=0)
    
    # Second, taller pyramid with gaps
    a1.add_ground(TX + 48, GY, width=5, height=5)
    a1.add_ground(TX + 55, GY - 4, width=5, height=9)
    a1.add_ground(TX + 62, GY - 8, width=5, height=13)
    a1.add_ground(TX + 69, GY - 4, width=5, height=9)
    
    a1.add_sprite(HAMMER_BRO, x=(TX + 57) * 16, y=(GY - 6) * 16, zone_id=0)
    a1.add_sprite(BOOMERANG_BRO, x=(TX + 64) * 16, y=(GY - 10) * 16, zone_id=0)
    a1.add_sprite(HAMMER_BRO, x=(TX + 71) * 16, y=(GY - 6) * 16, zone_id=0)
    
    # Star coin under the tall arch
    a1.add_star_coin(TX + 64, GY - 2, coin_num=0)
    
    # Valley 2
    a1.add_ground(TX + 76, GY, width=20, height=5)
    a1.add_sprite(POKEY, x=(TX + 82) * 16, y=(GY - 3) * 16, zone_id=0)
    a1.add_sprite(POKEY, x=(TX + 88) * 16, y=(GY - 3) * 16, zone_id=0)
    
    # Midway at TX + 100
    a1.add_ground(TX + 98, GY, width=15, height=5)
    a1.add_sprite(MIDWAY_FLAG, x=ZX + 4800, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x01\x00\x00')
    
    # Massive gaps with floating square ruins
    a1.add_platform(TX + 115, GY - 3, width=4)
    a1.add_sprite(FIRE_BRO, x=(TX + 116) * 16, y=(GY - 5) * 16, zone_id=0)
    a1.add_platform(TX + 125, GY - 6, width=4)
    a1.add_sprite(HAMMER_BRO, x=(TX + 126) * 16, y=(GY - 8) * 16, zone_id=0)
    a1.add_platform(TX + 135, GY - 2, width=4)
    a1.add_sprite(BOOMERANG_BRO, x=(TX + 137) * 16, y=(GY - 4) * 16, zone_id=0)
    
    a1.add_star_coin(TX + 126, GY - 2, coin_num=1)
    
    # Final stretch
    a1.add_ground(TX + 145, GY, width=25, height=5)
    a1.add_sprite(FIRE_BRO, x=(TX + 155) * 16, y=(GY - 2) * 16, zone_id=0)
    a1.add_sprite(FIRE_BRO, x=(TX + 160) * 16, y=(GY - 2) * 16, zone_id=0)
    
    a1.add_star_coin(TX + 165, GY - 10, coin_num=2)
    
    # Goal
    a1.add_ground(TX + 172, GY, width=25, height=5)
    a1.add_staircase(TX + 175, GY, steps=8, direction=1)
    a1.add_sprite(GOAL_POLE, x=(TX + 185) * 16, y=(GY - 10) * 16, zone_id=0)
    
    level.save("output/ChaosStation/Stage/02-05.arc")


def create_level_2_6():
    """
    Level 2-6: "Bramball Dunes"
    A precise platforming gauntlet featuring Bramballs (Sprite 230).
    Features a secret exit leading to a red goal pole.
    """
    import os
    level = LevelBuilder()
    
    # ═══════════ AREA 1: Bramball Gauntlet ═══════════
    a1 = level.add_area(1)
    a1.set_tileset(0, TILESET_STANDARD)
    a1.set_tileset(1, TILESET_DESERT)
    a1.set_time(400)
    a1.set_background(BG_DESERT)
    
    ZX, ZY = 256, 256
    ZW, ZH = 20000, 384
    a1.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_ATHLETIC, cam_mode=0, visibility=16)
    
    TX = 16
    GY = 35
    BRAMBALL = 230
    
    a1.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)
    a1.add_entrance(1, x=ZX + 3600, y=496, etype=ENTRANCE_NORMAL, zone_id=0)
    
    # Start platform
    a1.add_ground(TX, GY, width=15, height=5)
    a1.add_question_block(TX + 5, GY - 4, contents=5)  # Propeller Suit!
    
    # Gaps with Bramballs walking on short pillar segments
    a1.add_ground(TX + 20, GY - 2, width=8, height=7)
    a1.add_sprite(BRAMBALL, x=(TX + 24) * 16, y=(GY - 3) * 16, zone_id=0)
    
    a1.add_ground(TX + 32, GY - 4, width=6, height=9)
    a1.add_sprite(BRAMBALL, x=(TX + 35) * 16, y=(GY - 5) * 16, zone_id=0)
    
    a1.add_ground(TX + 42, GY - 6, width=6, height=11)
    a1.add_sprite(BRAMBALL, x=(TX + 45) * 16, y=(GY - 7) * 16, zone_id=0)
    a1.add_star_coin(TX + 45, GY - 14, coin_num=0)
    
    # ── Section 2: Midway & Falling Sand Pillars ──
    a1.add_ground(TX + 52, GY - 2, width=12, height=7)
    a1.add_staircase(TX + 64, GY - 2, steps=4, direction=-1)
    
    # Midway Checkpoint
    a1.add_ground(TX + 72, GY, width=15, height=5)
    a1.add_sprite(MIDWAY_FLAG, x=(TX + 80) * 16, y=(GY - 1) * 16, zone_id=0, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a1.add_entrance(1, x=(TX + 80) * 16, y=(GY - 4) * 16, etype=ENTRANCE_NORMAL, zone_id=0)
    a1.add_question_block(TX + 75, GY - 4, contents=5)  # Propeller Suit for checkpoint return
    
    # Long gap with moving platforms / Bramball bridge
    a1.add_ground(TX + 95, GY - 3, width=5, height=8)
    a1.add_sprite(BRAMBALL, x=(TX + 97) * 16, y=(GY - 4) * 16, zone_id=0)
    
    a1.add_ground(TX + 105, GY - 6, width=4, height=11)
    a1.add_sprite(BRAMBALL, x=(TX + 107) * 16, y=(GY - 7) * 16, zone_id=0)
    
    a1.add_ground(TX + 115, GY - 3, width=5, height=8)
    a1.add_sprite(BRAMBALL, x=(TX + 117) * 16, y=(GY - 4) * 16, zone_id=0)
    
    # ── Section 3: Fire Bros & Paragoombas ──
    a1.add_ground(TX + 128, GY, width=20, height=5)
    a1.add_sprite(FIRE_BRO, x=(TX + 138) * 16, y=(GY - 1) * 16, zone_id=0)
    a1.add_sprite(PARAGOOMBA, x=(TX + 145) * 16, y=(GY - 6) * 16, zone_id=0)
    a1.add_star_coin(TX + 140, GY - 5, coin_num=1)
    
    # Stepping stones over quicksand (implied by gap)
    a1.add_ground(TX + 155, GY - 2, width=3, height=7)
    a1.add_ground(TX + 162, GY - 4, width=3, height=9)
    a1.add_ground(TX + 169, GY - 6, width=3, height=11)
    a1.add_sprite(FIRE_BRO, x=(TX + 170) * 16, y=(GY - 7) * 16, zone_id=0)
    
    # ── Section 4: The Great Bramball Chasm ──
    a1.add_ground(TX + 180, GY, width=15, height=5)
    a1.add_sprite(PARAGOOMBA, x=(TX + 185) * 16, y=(GY - 3) * 16, zone_id=0)
    
    # Huge gap, must bounce on Bramballs
    a1.add_ground(TX + 205, GY - 4, width=4, height=9)
    a1.add_sprite(BRAMBALL, x=(TX + 207) * 16, y=(GY - 5) * 16, zone_id=0)
    
    a1.add_ground(TX + 218, GY - 6, width=4, height=11)
    a1.add_sprite(BRAMBALL, x=(TX + 220) * 16, y=(GY - 7) * 16, zone_id=0)
    
    a1.add_ground(TX + 231, GY - 8, width=4, height=13)
    a1.add_sprite(BRAMBALL, x=(TX + 233) * 16, y=(GY - 9) * 16, zone_id=0)
    
    a1.add_star_coin(TX + 233, GY - 14, coin_num=2)
    
    # Safe zone
    a1.add_ground(TX + 245, GY, width=25, height=5)
    a1.add_sprite(FIRE_BRO, x=(TX + 258) * 16, y=(GY - 1) * 16, zone_id=0)
    
    # ── SECRET EXIT ROUTE: The High Bounce ──
    # Player must bounce off a Paragoomba to reach a high cliff
    a1.add_ground(TX + 275, GY, width=20, height=5)
    a1.add_sprite(PARAGOOMBA, x=(TX + 285) * 16, y=(GY - 4) * 16, zone_id=0)
    
    # High Cliff (Unreachable by normal jump)
    a1.add_ground(TX + 293, GY - 12, width=15, height=17)
    
    # Physical pipe for visual reference
    a1.add_pipe(TX + 300, GY - 14, height=2)
    
    # Secret down pipe on top of the cliff
    a1.add_entrance(2, x=(TX + 300) * 16, y=(GY - 14) * 16,
                   etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                   dest_area=2, dest_entrance=3)
                   
    # ── NORMAL EXIT ROUTE ──
    # The normal route continues below the cliff
    a1.add_ground(TX + 305, GY, width=20, height=5)
    a1.add_sprite(BRAMBALL, x=(TX + 312) * 16, y=(GY - 1) * 16, zone_id=0)
    
    a1.add_ground(TX + 330, GY, width=30, height=5)
    a1.add_staircase(TX + 335, GY, steps=8, direction=1)
    a1.add_sprite(GOAL_POLE, x=(TX + 350) * 16, y=(GY - 10) * 16, zone_id=0)
    
    
    # ═══════════ AREA 2: Secret Exit Room ═══════════
    a2 = level.add_area(2)
    a2.set_tileset(0, TILESET_UNDERGROUND)
    a2.set_tileset(1, TILESET_CAVE)
    a2.set_background(770)
    a2.set_time(100)
    
    a2.add_zone(0, 0, 1200, 384, zone_id=0, music=MUSIC_UNDERGROUND)

    # Arrival pipe
    a2.add_entrance(3, x=48, y=288,
                    etype=ENTRANCE_PIPE_LEFT, zone_id=0,
                    dest_area=1, dest_entrance=2)

    # Floor and Ceiling
    a2.add_ground(0, 20, width=65, height=4)
    a2.add_ground(0, 0, width=65, height=4)

    # A few desert coins and Pokeys for flavor in the secret room
    a2.add_sprite(POKEY, x=300, y=256, zone_id=0)
    a2.add_coin_line(15, 18, count=5)

    # Secret Goal Pole (red flag)
    # Ground extends 20 tiles past the pole (x=46 → ground ends at x=68) for the
    # victory walk-off animation to complete cleanly.
    a2.add_staircase(35, 20, steps=6, direction=1)
    a2.add_ground(41, 14, width=28, height=2)
    a2.add_ground(41, 16, width=28, height=4)
    a2.add_secret_goal(46, 11)
    
    level.save("output/ChaosStation/Stage/02-06.arc")


def create_level_2_tower():
    """Tower (02-22): Sandstorm Spire — Desert tower climb with Pokeys and long Fire Bars."""
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin, Sprite, LayerObject,
        parse_layer_data, serialize_layer_data
    )

    with open('extracted files/Stage/02-22.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1: Tower Climb ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.settings.time_limit = 350
    
    essential_types = {
        32,   # Star coins
        53,   # Quicksand
        118,  # Dry Bones (tower enemies)
        147,  # Coins
        188,  # Midway
        259,  # Warp Pipes (CRITICAL for level progression!)
        376,  # Moving Sand Pillars
        392,  # Area controller
        436,  # System controller
        477,  # System controller 2
        407   # Boss door shutter
    }

    new_sprites = []
    for s in area1.sprites:
        if s.stype in essential_types:
            new_sprites.append(s)

    SD = b'\x00\x00\x00\x00\x00\x00'
    def add(stype, x, y, spritedata=SD):
        new_sprites.append(Sprite(stype=stype, x=x, y=y,
            spritedata=spritedata, zone_id=0, extra_byte=0))

    # Long Fire Bar configurations (Nybble 12 controls length)
    fb_long_cw = b'\x00\x00\x00\x00\x10\x08'  # Clockwise, Single, Length 10
    fb_long_ccw = b'\x00\x00\x00\x00\x00\x08' # CCW, Single, Length 10
    fb_double_cw = b'\x00\x00\x00\x00\x11\x18' # Clockwise, Fast, Double, Length 10

    # ╔══════════════════════════════════════════════════╗
    # ║  ENEMIES AND FIREBARS (Y=3400 to 1800)           ║
    # ╚══════════════════════════════════════════════════╝
    for y in range(3200, 1800, -250):
        # Extremely long Firebars in the center crossing
        add(FIRE_BAR, 624, y, spritedata=fb_double_cw)
        
        # Piranha Plants guarding the wall sides (using sprite ID 73)
        add(73, 400, y + 50)  
        add(73, 850, y + 50)  

    # ParaGoombas swarming the moving sand
    for y in range(3300, 1800, -200):
        add(PARAGOOMBA, 550, y)
        add(PARAGOOMBA, 700, y)

    # Spinies dropping down
    for y in range(3100, 1800, -350):
        add(SPINY, 480, y)
        add(SPINY, 760, y)

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Boss Room ═══════════
    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))

    boss_sprites = list(area2.sprites)

    # Add two Fire Bars spinning in the boss room
    # Boss zone: x=288-736, y=424-648.  Boss sprites are at x≈336-608, y≈432-608.
    # Length 6 fits the small chamber; longer bars would clip through walls.
    fb_boss_sd1 = b'\x00\x00\x00\x00\x10\x06' # Clockwise, Length 6
    fb_boss_sd2 = b'\x00\x00\x00\x00\x00\x06' # CCW, Length 6
    
    # Left side of boss room + right side — both inside the zone
    boss_sprites.append(Sprite(stype=FIRE_BAR, x=400, y=520, spritedata=fb_boss_sd1, zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=FIRE_BAR, x=640, y=520, spritedata=fb_boss_sd2, zone_id=0, extra_byte=0))

    # Dry Bones on the arena floor — revives during the fight!
    boss_sprites.append(Sprite(stype=DRY_BONES, x=448, y=576, spritedata=b'\x00\x00\x00\x00\x00\x00', zone_id=0, extra_byte=0))

    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/02-22.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/02-22.arc ({len(data)} bytes)')


def create_ambush_2():
    """Modifies the W2 Enemy Ambush stages (02-33/34/35.arc) — Desert Elite Patrol.
    
    The real ambush files are XX-33, XX-34, XX-35 (3 variants per world).
    W2 vanilla has Spinies (26) as enemies.
    We replace them with a tougher mix and add extra enemies.
    Preserves: Toad rescue sprites (185), controllers (203, 454).
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    SD = b'\x00\x00\x00\x00\x00\x00'
    
    # Cycle of replacement enemies for Spinies (26)
    # Using only 2 distinct heavy enemies to prevent Out Of Memory (OOM) crashes
    enemy_cycle = [FIRE_BRO, BOOMERANG_BRO]
    
    for suffix in ['33', '34', '35']:
        fname = f'02-{suffix}.arc'
        src = f'extracted files/Stage/{fname}'
        dst = f'output/ChaosStation/Stage/{fname}'
        
        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())
        
        area = parse_course_bin(arc.get_file('course/course1.bin'))
        new_sprites = []
        enemy_idx = 0
        
        for s in area.sprites:
            if s.stype == 26:  # Spiny -> cycle through desert elites
                ns = copy.deepcopy(s)
                ns.stype = enemy_cycle[enemy_idx % len(enemy_cycle)]
                ns.spritedata = SD
                new_sprites.append(ns)
                enemy_idx += 1
            else:
                new_sprites.append(s)
        
        area.sprites = new_sprites
        area.loaded_sprites = sorted(set(s.stype for s in new_sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area))
        
        data = arc.pack()
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(data)
        print(f'Saved: {dst} ({len(data)} bytes)')


def create_level_2_cannon():
    """Cannon (02-36): Desert Dash — add a sandy gauntlet before the warp cannon.
    Keeps all vanilla cannon/launcher sprites, adds desert enemies to pressure the player.
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    with open('extracted files/Stage/02-36.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    area = parse_course_bin(arc.get_file('course/course1.bin'))
    area.settings.time_limit = 200

    SD = b'\x00\x00\x00\x00\x00\x00'
    Z = area.zones[0].zone_id  # use correct zone id
    # Ground is around y=720, zone spans y=256-768, entrance at x=464

    def add(stype, x, y):
        area.sprites.append(Sprite(stype=stype, x=x, y=y, spritedata=SD, zone_id=Z, extra_byte=0))

    # Early section: easy desert intro
    add(db.GOOMBA,      560, 720)
    add(db.GOOMBA,      640, 720)
    add(db.SPINY,       720, 720)

    # Mid section: heat rises
    add(db.POKEY,       820, 720)
    add(db.HAMMER_BRO,  960, 720)
    add(db.SPINY,      1040, 720)
    add(db.BOB_OMB,    1120, 720)

    # ParaGoombas swooping from above
    add(db.PARAGOOMBA,  620, 590)
    add(db.PARAGOOMBA,  880, 570)
    add(db.PARAGOOMBA, 1140, 590)

    # Late section: intense push to the cannon
    add(db.POKEY,      1200, 720)
    add(db.FIRE_BRO,   1300, 720)
    add(db.BOB_OMB,    1400, 720)
    add(db.HAMMER_BRO, 1480, 720)

    # Coins to guide the path
    for cx in range(520, 1500, 120):
        add(db.COIN, cx, 672)

    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))

    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    data = arc.pack()
    with open('output/ChaosStation/Stage/02-36.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/02-36.arc ({len(data)} bytes)')


def create_level_3_1():
    """Level 3-1: Penguin Parkway — Slippery ice slopes and Cooligan swarms.

    A dynamic ice level with varied terrain: gentle snow slopes for sliding,
    frozen plateaus with crevasses, an underground cave holding the Penguin Suit,
    and a treacherous summit climb. Cooligans slide down slopes at the player,
    icicles drop from overhangs, and the ice physics make every jump a gamble.

    Layout:
      Section 1  — Snowy Meadow (gentle intro, ? blocks, Goombas)
      Section 2  — Frozen Lake Crossing (flat ice, thin platforms over pit)
      Section 3  — Cooligan Slide (downhill slope with Cooligans)
      Section 4  — Icicle Gauntlet (narrow path under hanging icicles)
      Section 5  — Pipe to Underground (Penguin Suit in cave — Area 2)
      MIDWAY FLAG
      Section 6  — Ice Pillar Canyon (tall pillars, precise jumps)
      Section 7  — Frozen Cliffs (vertical staircase sections)
      Section 8  — Blizzard Blitz (enemies + Bullet Bills)
      Section 9  — Summit Approach (final staircase + goal)
    """
    level = LevelBuilder()

    # ═══════════════════════════════════════════════════════
    #                    AREA 1: Main Level
    # ═══════════════════════════════════════════════════════
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_SNOW)
    a.set_time(400)
    a.set_background(BG_SNOW)

    # Zone: wide horizontal scrolling
    ZX, ZY = 256, 256
    ZW, ZH = 13000, 368
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_SNOW, cam_mode=0, visibility=16)

    TX = 16    # tile start X
    GY = 34    # ground Y in tiles (y=544px)

    # Entrances
    a.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)      # Start
    a.add_entrance(1, x=1856, y=528, etype=ENTRANCE_NORMAL, zone_id=0)          # Checkpoint
    a.add_entrance(10, x=(TX + 68) * 16, y=(GY - 3) * 16,                      # Return from cave
                   etype=ENTRANCE_PIPE_UP, zone_id=0, dest_area=0, dest_entrance=0)

    # ╔══════════════════════════════════════════════════════╗
    # ║          SECTION 1: Snowy Meadow (Intro)             ║
    # ╚══════════════════════════════════════════════════════╝
    # Long gentle ground — the player's first taste of ice
    a.add_ground(TX, GY, width=18, height=5)

    # Decorative snow hills
    a.add_hill(TX + 5, GY, half_width=3, height=2)
    a.add_hill(TX + 12, GY, half_width=4, height=3)

    # ? block — single powerup at start
    a.add_question_block(TX + 6, GY - 3, contents=1)   # Mushroom/Fire

    # Coin trail on the hilltop
    a.add_coin_line(TX + 10, GY - 1, count=6)

    # ╔══════════════════════════════════════════════════════╗
    # ║      SECTION 2: Frozen Lake Crossing                 ║
    # ╚══════════════════════════════════════════════════════╝
    # Gap -> thin floating ice platforms over a bottomless pit
    a.add_platform(TX + 20, GY - 1, width=3)
    a.add_platform(TX + 25, GY - 2, width=3)
    a.add_platform(TX + 30, GY, width=4)

    # Safe landing on far side
    a.add_ground(TX + 36, GY, width=12, height=5)

    # Coins guiding the jumps
    a.add_coin_line(TX + 21, GY - 3, count=2)
    a.add_coin_line(TX + 26, GY - 4, count=2)
    a.add_coin_line(TX + 32, GY - 2, count=2)

    # ╔══════════════════════════════════════════════════════╗
    # ║       SECTION 3: Cooligan Slide Run                  ║
    # ╚══════════════════════════════════════════════════════╝
    # Downhill slope — Cooligans slide toward the player
    a.add_ground(TX + 50, GY - 4, width=5, height=5)
    a.add_staircase(TX + 55, GY - 4, steps=5, direction=1)   # slope going down-right
    a.add_ground(TX + 60, GY, width=15, height=5)

    # Coin trail along the slope
    a.add_coin_line(TX + 55, GY - 5, count=5)

    # Coins at bottom of the slope (removed excess ? block)
    a.add_coin_line(TX + 62, GY - 3, count=3)

    # ╔══════════════════════════════════════════════════════╗
    # ║       SECTION 4: Icicle Gauntlet                     ║
    # ╚══════════════════════════════════════════════════════╝
    # Narrow path with icicles hanging from overhang above
    a.add_ground(TX + 78, GY, width=20, height=5)

    # Overhang ceiling (creates a "cave-like" passage)
    a.add_ground(TX + 80, GY - 8, width=16, height=2)

    # Coin trail below the ceiling
    a.add_coin_line(TX + 82, GY - 2, count=10)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 5: Pipe to Underground Cave              ║
    # ╚══════════════════════════════════════════════════════╝
    # Pipe at the end of the icicle gauntlet leads to Area 2 (Penguin Suit cave)
    a.add_ground(TX + 100, GY, width=10, height=5)
    a.add_pipe(TX + 103, GY - 3, height=3)   # Entry pipe (goes down to Area 2)

    # Entrance for pipe (player enters at entrance 5, arrives in Area 2 entrance 0)
    a.add_entrance(5, x=(TX + 103) * 16, y=(GY - 3) * 16,
                   etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                   dest_area=2, dest_entrance=0)

    # Brick blocks for alternative path (go over the pipe)
    a.add_brick_block(TX + 106, GY - 4)
    a.add_brick_block(TX + 107, GY - 4)
    a.add_brick_block(TX + 108, GY - 4)

    # ═════════════ MIDWAY FLAG ═════════════
    a.add_ground(TX + 113, GY, width=8, height=5)
    a.add_sprite(MIDWAY_FLAG, x=(TX + 116) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 6: Ice Pillar Canyon                     ║
    # ╚══════════════════════════════════════════════════════╝
    # Tall narrow pillars requiring precise jumps (ice makes it slippery!)
    a.add_ground(TX + 124, GY, width=3, height=8)
    a.add_ground(TX + 130, GY - 3, width=3, height=8)
    a.add_ground(TX + 136, GY - 1, width=3, height=8)
    a.add_ground(TX + 142, GY - 5, width=3, height=8)
    a.add_ground(TX + 148, GY - 2, width=3, height=8)

    # Coins between pillars
    a.add_coin_line(TX + 127, GY - 2, count=2)
    a.add_coin_line(TX + 133, GY - 5, count=2)
    a.add_coin_line(TX + 139, GY - 4, count=2)
    a.add_coin_line(TX + 145, GY - 7, count=2)

    # ? block on one pillar (reduced from 2)
    a.add_question_block(TX + 143, GY - 9, contents=1)  # Powerup

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 7: Frozen Cliffs                         ║
    # ╚══════════════════════════════════════════════════════╝
    # Ascending staircase terrain with enemies on each level
    a.add_ground(TX + 155, GY, width=8, height=5)
    a.add_staircase(TX + 163, GY, steps=6, direction=1)  # ascending right
    a.add_ground(TX + 169, GY - 6, width=10, height=5)

    # ? block with star for brave players
    a.add_question_block(TX + 173, GY - 10, contents=3)  # Star!

    # Coin trail on the upper path
    a.add_coin_line(TX + 170, GY - 7, count=6)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 8: Blizzard Blitz                        ║
    # ╚══════════════════════════════════════════════════════╝
    # Mixed platforms with heavy enemy presence — the final challenge
    a.add_ground(TX + 182, GY, width=6, height=5)
    a.add_ground(TX + 192, GY - 3, width=5, height=5)
    a.add_ground(TX + 201, GY, width=5, height=5)
    a.add_ground(TX + 210, GY - 4, width=5, height=5)
    a.add_ground(TX + 219, GY + 1, width=3, height=6)    # narrow stepping stone
    a.add_ground(TX + 226, GY - 2, width=5, height=5)

    # Coins marking the path
    a.add_coin_line(TX + 188, GY - 1, count=3)
    a.add_coin_line(TX + 197, GY - 3, count=3)
    a.add_coin_line(TX + 206, GY - 1, count=3)
    a.add_coin_line(TX + 215, GY - 4, count=3)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 9: Summit Approach + Goal                ║
    # ╚══════════════════════════════════════════════════════╝
    a.add_ground(TX + 234, GY, width=20, height=5)

    # Grand staircase to the summit
    a.add_staircase(TX + 248, GY, steps=8, direction=1)
    a.add_ground(TX + 256, GY - 8, width=20, height=2)
    a.add_ground(TX + 256, GY - 6, width=20, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Gentle intro — Goombas on the snowy meadow
    a.add_sprite(GOOMBA, x=(TX + 7) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 10) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 14) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Paragoomba over the frozen lake gap
    a.add_sprite(PARAGOOMBA, x=(TX + 22) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 28) * 16, y=(GY - 5) * 16, zone_id=0)

    # Dry Bones patrol on the landing
    a.add_sprite(DRY_BONES, x=(TX + 38) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 44) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 3: COOLIGANS sliding down the slope! The signature ice enemy.
    a.add_sprite(COOLIGAN, x=(TX + 51) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 53) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 55) * 16, y=(GY - 5) * 16, zone_id=0)
    # Goombas at the bottom of the slope
    a.add_sprite(GOOMBA, x=(TX + 62) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 67) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: Icicles dropping from the ceiling!
    for i in range(6):
        a.add_sprite(ICICLE, x=(TX + 82 + i * 2) * 16, y=(GY - 7) * 16, zone_id=0)

    # Dry Bones under the icicles (dodging both at once!)
    a.add_sprite(DRY_BONES, x=(TX + 85) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 91) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 5: Pipe area — Piranha Plant guarding the pipe
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 103) * 16, y=(GY - 4) * 16, zone_id=0)

    # Section 6: Ice pillar enemies
    a.add_sprite(SPINY, x=(TX + 125) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 131) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 137) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 149) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 7: Frozen cliffs enemies
    a.add_sprite(KOOPA, x=(TX + 157) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 162) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 171) * 16, y=(GY - 7) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 175) * 16, y=(GY - 7) * 16, zone_id=0)

    # Section 8: Blizzard blitz — heavy enemy density
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 189) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 193) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 195) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(BULLET_BILL_LAUNCHER, x=(TX + 207) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 202) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 212) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 222) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 228) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 9: Goal guards
    a.add_sprite(HAMMER_BRO, x=(TX + 240) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 244) * 16, y=(GY - 1) * 16, zone_id=0)

    # ════════════════ STAR COINS ════════════════
    # Star Coin 1: Hidden above the frozen lake, risky jump from platform 2
    a.add_star_coin(TX + 27, GY - 7, coin_num=0)

    # Star Coin 2: Under the icicle ceiling — dodge icicles to grab it
    a.add_star_coin(TX + 90, GY - 3, coin_num=1)

    # Star Coin 3: In the ice pillar canyon, high up between pillars
    a.add_star_coin(TX + 141, GY - 10, coin_num=2)

    # ════════════════ RED COIN RING ════════════════
    a.add_red_coin_ring(TX + 160, GY - 4, pattern='arc')

    # ════════════════ GOAL ════════════════
    a.add_sprite(GOAL_POLE, x=(TX + 264) * 16, y=(GY - 10) * 16, zone_id=0)

    # ═══════════════════════════════════════════════════════
    #                AREA 2: Underground Penguin Cave
    # ═══════════════════════════════════════════════════════
    cave = level.add_area(2)

    cave.set_tileset(0, TILESET_STANDARD)
    cave.set_tileset(1, TILESET_CAVE)
    cave.set_time(400)
    cave.set_background(BG_UNDERGROUND)

    # Small cave zone
    CX, CY = 256, 256
    CW, CH = 2000, 300
    cave.add_zone(CX, CY, CW, CH, zone_id=0, music=MUSIC_UNDERGROUND, cam_mode=0)

    CTX, CGY = 16, 32  # cave tile coords

    # Entrance from pipe (arrive from Area 1)
    cave.add_entrance(0, x=(CTX + 2) * 16, y=(CGY - 2) * 16,
                      etype=ENTRANCE_PIPE_UP, zone_id=0)

    # Exit pipe (returns to Area 1)
    cave.add_entrance(1, x=(CTX + 30) * 16, y=(CGY - 3) * 16,
                      etype=ENTRANCE_PIPE_UP, zone_id=0,
                      dest_area=1, dest_entrance=10)

    # Cave floor
    cave.add_ground(CTX, CGY, width=35, height=5)

    # Ceiling
    cave.add_ground(CTX, CGY - 8, width=35, height=2)

    # Entry pipe
    cave.add_pipe(CTX + 1, CGY - 3, height=3)

    # Penguin Suit ? block — the prize! (removed excess coin/ice blocks)
    cave.add_question_block(CTX + 10, CGY - 4, contents=6)  # Penguin Suit!

    # Coins filling the cave
    cave.add_coin_line(CTX + 6, CGY - 2, count=8)
    cave.add_coin_line(CTX + 18, CGY - 2, count=8)

    # Exit pipe
    cave.add_pipe(CTX + 29, CGY - 3, height=3)

    # A few enemies guarding the treasure
    cave.add_sprite(DRY_BONES, x=(CTX + 8) * 16, y=(CGY - 1) * 16, zone_id=0)
    cave.add_sprite(DRY_BONES, x=(CTX + 20) * 16, y=(CGY - 1) * 16, zone_id=0)

    # ═══════════════════════════════════════════════════════
    level.save('output/ChaosStation/Stage/03-01.arc')


def create_level_3_2():
    """Level 3-2: Frostbite Chasm — Precision jumps over frozen abysses.

    A treacherous level built around deep chasms and narrow ice platforms.
    Icicles rain from overhangs, Ice Bros hurl freezing projectiles from
    elevated perches, and the slippery ground punishes every mistimed jump.
    A hidden pipe leads to a frozen cavern with an Ice Flower and a star coin.

    Layout:
      Section 1  — Icy Outcrop (safe start, ? blocks on snow)
      Section 2  — First Chasm (thin platforms over void)
      Section 3  — Icicle Corridor (long flat with ceiling hazards)
      Section 4  — Ice Bro Towers (elevated enemies on pillars)
      Section 5  — Hidden Pipe + Midway flag
      Section 6  — Frozen Ruins (broken platforms, Buzzy Beetles)
      Section 7  — Suspended Bridge (brick bridge over void + Swoopers)
      Section 8  — Summit Sprint (final gauntlet to goal)
    """
    level = LevelBuilder()

    # ═══════════════════════════════════════════════════════
    #                   AREA 1: Main Level
    # ═══════════════════════════════════════════════════════
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_SNOW)
    a.set_time(380)
    a.set_background(BG_SNOW)

    ZX, ZY = 256, 256
    ZW, ZH = 12500, 368
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_SNOW, cam_mode=0, visibility=16)

    TX = 16    # tile start X
    GY = 34    # ground Y in tiles

    # Entrances
    a.add_entrance(0, x=ZX + 48, y=512, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=1856, y=528, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(10, x=(TX + 100) * 16, y=(GY - 3) * 16,
                   etype=ENTRANCE_PIPE_UP, zone_id=0, dest_area=0, dest_entrance=0)

    # ╔══════════════════════════════════════════════════════╗
    # ║       SECTION 1: Icy Outcrop (Intro)                 ║
    # ╚══════════════════════════════════════════════════════╝
    a.add_ground(TX, GY, width=16, height=5)
    a.add_hill(TX + 6, GY, half_width=4, height=2)

    # ? block — single powerup at start
    a.add_question_block(TX + 5, GY - 3, contents=1)   # Mushroom

    a.add_coin_line(TX + 9, GY - 1, count=5)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 2: First Chasm Crossing                  ║
    # ╚══════════════════════════════════════════════════════╝
    # Narrow ice platforms floating over the abyss
    a.add_platform(TX + 19, GY - 1, width=2)
    a.add_platform(TX + 23, GY - 3, width=2)
    a.add_platform(TX + 27, GY - 1, width=3)
    a.add_platform(TX + 32, GY - 4, width=2)
    a.add_platform(TX + 36, GY - 2, width=2)

    # Landing
    a.add_ground(TX + 40, GY, width=10, height=5)

    # Coin guides
    a.add_coin_line(TX + 20, GY - 3, count=2)
    a.add_coin_line(TX + 28, GY - 3, count=3)
    a.add_coin_line(TX + 33, GY - 6, count=2)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 3: Icicle Corridor                       ║
    # ╚══════════════════════════════════════════════════════╝
    # Long flat ground with icicle-laden ceiling overhead
    a.add_ground(TX + 53, GY, width=25, height=5)

    # Ceiling overhang creating a claustrophobic corridor
    a.add_ground(TX + 55, GY - 9, width=21, height=2)

    # Single ? block with Ice Flower
    a.add_question_block(TX + 65, GY - 4, contents=8)  # Ice Flower

    a.add_coin_line(TX + 56, GY - 2, count=15)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 4: Ice Bro Towers                        ║
    # ╚══════════════════════════════════════════════════════╝
    # Tall pillars with Ice Bros perched on top throwing ice balls
    a.add_ground(TX + 81, GY, width=4, height=5)
    a.add_ground(TX + 88, GY - 5, width=3, height=10)   # Tall pillar
    a.add_ground(TX + 94, GY, width=6, height=5)
    a.add_ground(TX + 103, GY - 6, width=3, height=10)  # Tall pillar
    a.add_ground(TX + 109, GY, width=5, height=5)

    # Coins between the pillars
    a.add_coin_line(TX + 85, GY - 2, count=2)
    a.add_coin_line(TX + 91, GY - 2, count=2)
    a.add_coin_line(TX + 100, GY - 2, count=2)
    a.add_coin_line(TX + 106, GY - 3, count=2)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 5: Hidden Pipe + Midway Flag             ║
    # ╚══════════════════════════════════════════════════════╝
    a.add_ground(TX + 117, GY, width=14, height=5)
    a.add_pipe(TX + 119, GY - 3, height=3)   # Secret pipe to Area 2

    a.add_entrance(5, x=(TX + 119) * 16, y=(GY - 3) * 16,
                   etype=ENTRANCE_PIPE_DOWN, zone_id=0,
                   dest_area=2, dest_entrance=0)

    # Midway flag
    a.add_sprite(MIDWAY_FLAG, x=(TX + 126) * 16, y=(GY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 6: Frozen Ruins (Broken Platforms)       ║
    # ╚══════════════════════════════════════════════════════╝
    # Shattered ice platforms at varying heights — no safety net
    a.add_ground(TX + 134, GY - 2, width=4, height=5)
    a.add_ground(TX + 140, GY, width=3, height=5)
    a.add_ground(TX + 146, GY - 4, width=3, height=5)
    a.add_ground(TX + 152, GY - 1, width=4, height=5)
    a.add_ground(TX + 159, GY - 3, width=3, height=5)
    a.add_ground(TX + 165, GY, width=5, height=5)

    # ? block at a risky height
    a.add_question_block(TX + 141, GY - 4, contents=1)  # Powerup

    a.add_coin_line(TX + 143, GY - 2, count=2)
    a.add_coin_line(TX + 155, GY - 3, count=3)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 7: Frozen Crossing                       ║
    # ╚══════════════════════════════════════════════════════╝
    # Floating ice platforms across the void — Swoopers attack from below
    a.add_ground(TX + 173, GY, width=4, height=5)
    a.add_platform(TX + 179, GY - 1, width=4)       # Platform 1
    a.add_platform(TX + 185, GY - 2, width=4)       # Platform 2
    a.add_platform(TX + 191, GY - 1, width=4)       # Platform 3
    a.add_ground(TX + 197, GY, width=5, height=5)

    # Coins along the platform path
    a.add_coin_line(TX + 179, GY - 3, count=3)
    a.add_coin_line(TX + 185, GY - 4, count=3)
    a.add_coin_line(TX + 191, GY - 3, count=3)

    # ? block with powerup mid-crossing
    a.add_question_block(TX + 186, GY - 5, contents=1)  # Mushroom

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 8: Summit Sprint + Goal                  ║
    # ╚══════════════════════════════════════════════════════╝
    # Final dash — ascending platforms plus last enemy gauntlet
    a.add_ground(TX + 205, GY, width=6, height=5)
    a.add_ground(TX + 214, GY - 3, width=5, height=5)
    a.add_ground(TX + 222, GY - 5, width=5, height=5)
    a.add_ground(TX + 230, GY, width=15, height=5)

    # Grand staircase to goal
    a.add_staircase(TX + 240, GY, steps=8, direction=1)
    a.add_ground(TX + 248, GY - 8, width=20, height=2)
    a.add_ground(TX + 248, GY - 6, width=20, height=10)

    # ════════════════ SPRITES ════════════════

    # Section 1: Gentle start
    a.add_sprite(GOOMBA, x=(TX + 8) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 12) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 2: Paragoomba harassment over the chasm
    a.add_sprite(PARAGOOMBA, x=(TX + 21) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 30) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(PARAGOOMBA, x=(TX + 35) * 16, y=(GY - 6) * 16, zone_id=0)

    # Section 2 landing enemies
    a.add_sprite(DRY_BONES, x=(TX + 42) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 47) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 3: Icicles across the corridor ceiling
    for i in range(8):
        a.add_sprite(ICICLE, x=(TX + 56 + i * 2) * 16, y=(GY - 8) * 16, zone_id=0)

    # Dry Bones patrolling under the icicles
    a.add_sprite(DRY_BONES, x=(TX + 60) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 68) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 74) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 4: ICE BROS on the tall pillars! They throw ice balls down at you.
    a.add_sprite(ICE_BRO, x=(TX + 89) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(ICE_BRO, x=(TX + 104) * 16, y=(GY - 7) * 16, zone_id=0)
    # Ground enemies between pillars
    a.add_sprite(SPINY, x=(TX + 83) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BUZZY_BEETLE, x=(TX + 96) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(BUZZY_BEETLE, x=(TX + 98) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 111) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 5: Pipe area guard
    a.add_sprite(PIPE_PIRANHA_UP, x=(TX + 119) * 16, y=(GY - 4) * 16, zone_id=0)

    # Section 6: Frozen ruins — enemies on the broken platforms
    a.add_sprite(COOLIGAN, x=(TX + 135) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 147) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(SPINY, x=(TX + 153) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(ICE_BRO, x=(TX + 160) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 167) * 16, y=(GY - 1) * 16, zone_id=0)

    # Section 7: Swoopers hanging from above — swoop down on the player
    a.add_sprite(SWOOP, x=(TX + 180) * 16, y=(GY - 8) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 185) * 16, y=(GY - 8) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 190) * 16, y=(GY - 8) * 16, zone_id=0)
    a.add_sprite(SWOOP, x=(TX + 195) * 16, y=(GY - 8) * 16, zone_id=0)

    # Section 8: Final gauntlet
    a.add_sprite(COOLIGAN, x=(TX + 207) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(COOLIGAN, x=(TX + 209) * 16, y=(GY - 1) * 16, zone_id=0)
    a.add_sprite(ICE_BRO, x=(TX + 216) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(DRY_BONES, x=(TX + 224) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(HAMMER_BRO, x=(TX + 234) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 238) * 16, y=(GY - 1) * 16, zone_id=0)

    # ════════════════ STAR COINS ════════════════
    # Star Coin 1: Floating high above the first chasm — risky jump from platform 3
    a.add_star_coin(TX + 29, GY - 8, coin_num=0)

    # Star Coin 2: In the frozen cave (Area 2) — requires finding the hidden pipe
    # (placed in Area 2 below)

    # Star Coin 3: Above the suspended bridge, visible but breakable floor!
    a.add_star_coin(TX + 186, GY - 6, coin_num=2)

    # ════════════════ RED COIN RING ════════════════
    a.add_red_coin_ring(TX + 136, GY - 6, pattern='arc')

    # ════════════════ GOAL ════════════════
    a.add_sprite(GOAL_POLE, x=(TX + 256) * 16, y=(GY - 10) * 16, zone_id=0)

    # ═══════════════════════════════════════════════════════
    #            AREA 2: Frozen Cavern (Secret)
    # ═══════════════════════════════════════════════════════
    cave = level.add_area(2)

    cave.set_tileset(0, TILESET_STANDARD)
    cave.set_tileset(1, TILESET_CAVE)
    cave.set_time(380)
    cave.set_background(BG_UNDERGROUND)

    CX, CY = 256, 256
    CW, CH = 2000, 300
    cave.add_zone(CX, CY, CW, CH, zone_id=0, music=MUSIC_UNDERGROUND, cam_mode=0)

    CTX, CGY = 16, 32

    cave.add_entrance(0, x=(CTX + 2) * 16, y=(CGY - 2) * 16,
                      etype=ENTRANCE_PIPE_UP, zone_id=0)
    cave.add_entrance(1, x=(CTX + 28) * 16, y=(CGY - 3) * 16,
                      etype=ENTRANCE_PIPE_UP, zone_id=0,
                      dest_area=1, dest_entrance=10)

    cave.add_ground(CTX, CGY, width=32, height=5)
    cave.add_ground(CTX, CGY - 8, width=32, height=2)

    cave.add_pipe(CTX + 1, CGY - 3, height=3)
    cave.add_pipe(CTX + 27, CGY - 3, height=3)

    # Ice Flower + Star Coin 2 — the reward for finding the pipe!
    cave.add_question_block(CTX + 10, CGY - 4, contents=8)  # Ice Flower

    cave.add_star_coin(CTX + 18, CGY - 3, coin_num=1)   # Star Coin 2!

    cave.add_coin_line(CTX + 6, CGY - 2, count=8)
    cave.add_coin_line(CTX + 18, CGY - 2, count=6)

    # Cave guardians
    cave.add_sprite(DRY_BONES, x=(CTX + 9) * 16, y=(CGY - 1) * 16, zone_id=0)
    cave.add_sprite(BUZZY_BEETLE, x=(CTX + 22) * 16, y=(CGY - 1) * 16, zone_id=0)

    level.save('output/ChaosStation/Stage/03-02.arc')


def create_level_3_3():
    """Level 3-3: Sub-Zero Swim — Frozen underwater grotto.

    A fully aquatic level set in an icy underwater cavern. Mario swims
    through frozen coral corridors, dodging Urchins, Fishbones, and
    Bloopers. Ice pillars create tight passages and the ocean floor
    rises and falls unpredictably. Scattered islands above water offer
    brief air pockets with coin rewards and powerups.

    Layout:
      Section 1  — Frozen Shore (dry start, enter water via slope)
      Section 2  — Shallow Swim (gentle intro to water, Cheep Cheeps)
      Section 3  — Urchin Maze (tight corridors with Urchins)
      Section 4  — Ice Island Rest Stop (above-water ? blocks)
      MIDWAY FLAG
      Section 5  — Deep Trench (deeper water, Fishbone ambush)
      Section 6  — Blooper Territory (open water, Blooper Nannies)
      Section 7  — Frozen Coral Garden (pillars + Porcupuffer)
      Section 8  — Shore Ascent (exit water, sprint to goal)
    """
    level = LevelBuilder()
    a = level.add_area(1)

    a.set_tileset(0, TILESET_STANDARD)
    a.set_tileset(1, TILESET_OCEAN)
    a.set_time(400)
    a.set_background(BG_UNDERWATER,
                     x_scroll_a=0, y_scroll_a=0,
                     x_scroll_b=0, y_scroll_b=0,
                     zoom_a=1, zoom_b=2)

    # Wider, taller zone for swimming space
    ZX, ZY = 256, 128
    ZW, ZH = 10000, 512
    a.add_zone(ZX, ZY, ZW, ZH, zone_id=0, music=MUSIC_UNDERWATER, cam_mode=0)

    # Water fill — covers most of the zone (leave top few tiles dry for islands)
    water_sd = b'\x01\x00\x00\x00\x00\x00'  # flat-top water fill
    a.add_sprite(WATER_FILL, x=ZX, y=ZY + 80, zone_id=0, spritedata=water_sd)

    TX = 16   # tile X start
    GY = 32   # ocean floor Y (tiles)
    WY = 13   # water surface Y (tiles) — above this is dry

    # Entrances
    a.add_entrance(0, x=ZX + 48, y=(WY - 2) * 16, etype=ENTRANCE_NORMAL, zone_id=0)
    a.add_entrance(1, x=2400, y=(WY - 1) * 16, etype=ENTRANCE_NORMAL, zone_id=0)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 1: Frozen Shore (Dry Start)              ║
    # ╚══════════════════════════════════════════════════════╝
    # Ground above water line — safe starting area
    a.add_ground(TX, WY, width=14, height=GY - WY + 5)

    # ? block on shore — single powerup
    a.add_question_block(TX + 5, WY - 3, contents=1)  # Mushroom

    a.add_coin_line(TX + 8, WY - 1, count=5)

    # Slope into water (staircase down)
    a.add_staircase(TX + 14, WY, steps=4, direction=1)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 2: Shallow Swim                          ║
    # ╚══════════════════════════════════════════════════════╝
    # Gentle underwater section — low obstacles
    a.add_ground(TX + 20, GY, width=30, height=5)

    # Small coral pillars (ice blocks underwater)
    a.add_ground(TX + 25, GY - 4, width=2, height=4)
    a.add_ground(TX + 32, GY - 6, width=2, height=6)
    a.add_ground(TX + 38, GY - 3, width=2, height=3)
    a.add_ground(TX + 44, GY - 5, width=2, height=5)

    # Coins guiding through the coral
    a.add_coin_line(TX + 22, GY - 2, count=4)
    a.add_coin_line(TX + 28, GY - 3, count=3)
    a.add_coin_line(TX + 35, GY - 2, count=3)
    a.add_coin_line(TX + 41, GY - 3, count=3)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 3: Urchin Maze                           ║
    # ╚══════════════════════════════════════════════════════╝
    # Tight corridors with Urchins blocking the path
    a.add_ground(TX + 53, GY, width=25, height=5)

    # Corridor walls (floor rises, ceiling descends — tight passage)
    a.add_ground(TX + 55, GY - 10, width=20, height=3)  # Ceiling
    a.add_ground(TX + 58, GY - 3, width=3, height=3)    # Floor pillar 1
    a.add_ground(TX + 65, GY - 3, width=3, height=3)    # Floor pillar 2
    a.add_ground(TX + 72, GY - 3, width=3, height=3)    # Floor pillar 3

    a.add_coin_line(TX + 56, GY - 5, count=4)
    a.add_coin_line(TX + 62, GY - 5, count=4)
    a.add_coin_line(TX + 69, GY - 5, count=4)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 4: Ice Island Rest Stop                  ║
    # ╚══════════════════════════════════════════════════════╝
    # Dry island above water — catch your breath!
    a.add_ground(TX + 81, WY, width=12, height=GY - WY + 5)

    a.add_question_block(TX + 84, WY - 3, contents=8)  # Ice Flower!

    a.add_coin_line(TX + 83, WY - 1, count=8)

    # Midway flag on the island
    a.add_sprite(MIDWAY_FLAG, x=(TX + 89) * 16, y=(WY - 1) * 16, zone_id=0,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 5: Deep Trench                           ║
    # ╚══════════════════════════════════════════════════════╝
    # The ocean floor drops away — deeper water with Fishbone ambush
    a.add_ground(TX + 96, GY + 2, width=30, height=5)  # Deeper floor

    # Rocky outcroppings
    a.add_ground(TX + 100, GY - 2, width=3, height=4)
    a.add_ground(TX + 108, GY - 4, width=2, height=6)
    a.add_ground(TX + 115, GY - 2, width=3, height=4)
    a.add_ground(TX + 120, GY - 5, width=2, height=7)

    a.add_coin_line(TX + 103, GY - 1, count=4)
    a.add_coin_line(TX + 111, GY - 1, count=3)
    a.add_coin_line(TX + 118, GY - 1, count=2)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 6: Blooper Territory                     ║
    # ╚══════════════════════════════════════════════════════╝
    # Wide open water — Bloopers patrol freely
    a.add_ground(TX + 129, GY, width=25, height=5)

    # Few obstacles — wide open for Blooper dodging
    a.add_ground(TX + 138, GY - 6, width=2, height=6)
    a.add_ground(TX + 148, GY - 4, width=2, height=4)

    a.add_coin_line(TX + 131, GY - 3, count=6)
    a.add_coin_line(TX + 141, GY - 3, count=5)

    # ? block with star — risky grab in Blooper territory
    a.add_question_block(TX + 145, GY - 8, contents=3)  # Star!

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 7: Frozen Coral Garden                   ║
    # ╚══════════════════════════════════════════════════════╝
    # Dense pillars — the final underwater challenge
    a.add_ground(TX + 157, GY, width=30, height=5)

    # Dense coral forest
    a.add_ground(TX + 160, GY - 8, width=2, height=8)
    a.add_ground(TX + 164, GY - 5, width=2, height=5)
    a.add_ground(TX + 168, GY - 9, width=2, height=9)
    a.add_ground(TX + 172, GY - 4, width=2, height=4)
    a.add_ground(TX + 176, GY - 7, width=2, height=7)
    a.add_ground(TX + 180, GY - 5, width=2, height=5)

    a.add_coin_line(TX + 162, GY - 3, count=2)
    a.add_coin_line(TX + 166, GY - 3, count=2)
    a.add_coin_line(TX + 170, GY - 3, count=2)
    a.add_coin_line(TX + 174, GY - 3, count=2)
    a.add_coin_line(TX + 178, GY - 3, count=2)

    # ╔══════════════════════════════════════════════════════╗
    # ║     SECTION 8: Shore Ascent + Goal                   ║
    # ╚══════════════════════════════════════════════════════╝
    # Rising ground exits the water — sprint to the flagpole on dry land
    a.add_staircase(TX + 190, GY, steps=6, direction=-1)  # ascending left-up
    a.add_ground(TX + 190, WY, width=20, height=GY - WY + 5)

    # Goal area staircase
    a.add_staircase(TX + 204, WY, steps=8, direction=1)
    a.add_ground(TX + 212, WY - 8, width=15, height=2)
    a.add_ground(TX + 212, WY - 6, width=15, height=GY - WY + 10)

    a.add_coin_line(TX + 192, WY - 1, count=8)

    # ════════════════ SPRITES ════════════════

    # Section 1: Shore enemies
    a.add_sprite(GOOMBA, x=(TX + 8) * 16, y=(WY - 1) * 16, zone_id=0)
    a.add_sprite(KOOPA, x=(TX + 11) * 16, y=(WY - 1) * 16, zone_id=0)

    # Section 2: Cheep Cheeps in the shallows
    a.add_sprite(CHEEP_CHEEP, x=(TX + 23) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 30) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 37) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 45) * 16, y=(GY - 4) * 16, zone_id=0)

    # Section 3: URCHINS blocking the maze corridors!
    a.add_sprite(URCHIN, x=(TX + 60) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 67) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 74) * 16, y=(GY - 5) * 16, zone_id=0)
    # Fishbone darting through the maze
    a.add_sprite(FISHBONE, x=(TX + 63) * 16, y=(GY - 4) * 16, zone_id=0)

    # Section 4: Island is safe (no enemies)

    # Section 5: FISHBONES hunting in the deep trench
    a.add_sprite(FISHBONE, x=(TX + 102) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(FISHBONE, x=(TX + 110) * 16, y=(GY - 2) * 16, zone_id=0)
    a.add_sprite(FISHBONE, x=(TX + 117) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 105) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(CHEEP_CHEEP, x=(TX + 122) * 16, y=(GY - 5) * 16, zone_id=0)

    # Section 6: BLOOPERS in open water
    a.add_sprite(BLOOPER, x=(TX + 133) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 140) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(BLOOPER_NANNY, x=(TX + 146) * 16, y=(GY - 6) * 16, zone_id=0)
    a.add_sprite(BLOOPER, x=(TX + 151) * 16, y=(GY - 3) * 16, zone_id=0)

    # Section 7: Final underwater gauntlet — Urchins in the coral
    a.add_sprite(URCHIN, x=(TX + 162) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 170) * 16, y=(GY - 5) * 16, zone_id=0)
    a.add_sprite(URCHIN, x=(TX + 178) * 16, y=(GY - 4) * 16, zone_id=0)
    a.add_sprite(FISHBONE, x=(TX + 166) * 16, y=(GY - 3) * 16, zone_id=0)
    a.add_sprite(FISHBONE, x=(TX + 174) * 16, y=(GY - 3) * 16, zone_id=0)
    # Porcupuffer roaming the garden
    a.add_sprite(PORCU_PUFFER, x=(TX + 182) * 16, y=(GY - 6) * 16, zone_id=0)

    # Section 8: Shore guards
    a.add_sprite(DRY_BONES, x=(TX + 195) * 16, y=(WY - 1) * 16, zone_id=0)
    a.add_sprite(GOOMBA, x=(TX + 200) * 16, y=(WY - 1) * 16, zone_id=0)

    # ════════════════ STAR COINS ════════════════
    # Star Coin 1: Hidden behind the 2nd coral pillar in shallow swim
    a.add_star_coin(TX + 33, GY - 2, coin_num=0)

    # Star Coin 2: Deep in the trench — between rocky outcroppings
    a.add_star_coin(TX + 112, GY + 1, coin_num=1)

    # Star Coin 3: High up in the coral garden — swim up between pillars
    a.add_star_coin(TX + 171, GY - 8, coin_num=2)

    # ════════════════ RED COIN RING ════════════════
    a.add_red_coin_ring(TX + 135, GY - 7, pattern='circle')

    # ════════════════ GOAL ════════════════
    a.add_sprite(GOAL_POLE, x=(TX + 220) * 16, y=(WY - 10) * 16, zone_id=0)

    level.save('output/ChaosStation/Stage/03-03.arc')


def create_level_3_ghost_house():
    """3-Ghost House: The Frozen Mansion of Woe.

    A creative icy ghost house remix. The mansion was flash-frozen ages ago —
    Boos now float through crystalline corridors, and ice blocks seal ancient
    secrets. Glow Blocks are the only light in the darkest wings. A secret
    hidden door leads to a cannon disguised behind a wall of ice.

    Creative twists vs vanilla ghost house:
      • ICE_BLOCKs used as destructible 'fake walls' hiding passages
      • GLOW_BLOCK sections make Boos nearly invisible until they lunge
      • BROOZER punches through ice walls to open shortcuts
      • ICE_SNAKE_BLOCK platforms wind through the frozen attic
      • BIG_BOO patrols the attic — the biggest threat
      • Three BOO circles ambush in the dark hallway  
      • Secret exit: hidden door reached by breaking ice wall with Broozer

    Areas:
      Area 1 — Grand Frozen Hall (main horizontal level)
      Area 2 — The Frozen Attic (vertical climb to normal exit)  
      Area 3 — Secret Cannon Lobby (secret exit -> World 6)
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin,
        Sprite, LayerObject, parse_layer_data, serialize_layer_data
    )

    TILESET_GHOST  = "Pa1_obake"
    TILESET_CAVE   = "Pa1_chika"  # We must use a real terrain tileset for floors
    MUSIC_GHOST    = 5
    BG_GHOST       = 1        # Dark/grey ghost house BG
    BG_GHOST_DARK  = 3        # Even darker BG for glow sections

    # Keep vanilla arc as base for proper ghost house header/settings
    with open('extracted files/Stage/03-21.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ════════════════════════════════════════════════════
    #   AREA 1 — Grand Frozen Hall
    # ════════════════════════════════════════════════════
    # A long horizontal ghost house with themed sections:
    #  §1 Icy Foyer     — safe start, a few Boos  
    #  §2 Dark Wing     — Glow Blocks only, Boo circles in the dark
    #  §3 Ice Wall Maze — ICE_BLOCKs sealing paths, Broozer breaks through
    #  §4 The Parlour   — Big Boo ambush, Star Coin above
    #  §5 Pipe up to Attic (Area 2, normal exit)
    #     + hidden ice-block door to Cannon Lobby (Area 3)

    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.sprites.clear()
    area1.layer1.clear()
    area1.layer0.clear()
    area1.layer2.clear()
    area1.entrances.clear()
    area1.zones.clear()
    area1.boundings.clear()
    area1.settings.time_limit = 400

    from tools.course_parser import (Entrance, Zone, Bounding, AreaSettings,
                                     Background, Tileset)
    from tools.sprite_db import (
        BOO, BIG_BOO, BROOZER, SWOOP, DRY_BONES,
        GLOW_BLOCK, ICE_BLOCK, ICICLE, COIN, STAR_COIN,
        GOAL_POLE, MIDWAY_FLAG,
        TILESET_STANDARD, CaveObjs, StandardObjs
    )

    def obj1(ot, x, y, width=1, h=1):
        area1.layer1.append(LayerObject(tileset=1, obj_type=ot, x=x, y=y, w=width, h=h))

    def obj0_a1(ot, x, y, w=1, h=1):
        area1.layer0.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    def obj0_layer1_a1(ot, x, y, w=1, h=1):
        area1.layer1.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    def obj2_a1(ot, x, y, w=1, h=1):
        area1.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))

    def spr(stype, x, y, data=b'\x00'*6):
        area1.sprites.append(Sprite(stype=stype, x=x, y=y,
                                    spritedata=data, zone_id=0, extra_byte=0))

    # Tileset: use Underground in slot 2 for real terrain
    area1.tileset = Tileset(slot0=TILESET_STANDARD, slot1=TILESET_GHOST,
                            slot2=TILESET_CAVE, slot3='')

    # Zone — large horizontal room
    ZX, ZY = 256, 256
    ZW, ZH = 9000, 368
    area1.zones.append(Zone(x=ZX, y=ZY, w=ZW, h=ZH, zone_id=0,
                            music=MUSIC_GHOST, cam_mode=0, cam_zoom=0,
                            visibility=36))
    area1.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0,
                                    bound_id=0, mp_cam_zoom=15,
                                    upper3=0, lower3=0))

    TX = 16
    GY = 35  # Ground Y (tiles) — lowered by 2
    CY = 20  # Ceiling Y (tiles) — lowered by 2

    # Entrances — standard GROUND_FILL has normal thickness, spawn 2 tiles above
    area1.entrances.append(Entrance(
        x=(TX+2)*16, y=(GY-2)*16, entrance_id=0, dest_area=0, dest_entrance=0,
        etype=ENTRANCE_NORMAL, zone_id=0, layer=0, path=0,
        unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    # From attic coming back
    area1.entrances.append(Entrance(
        x=(TX+80)*16, y=(GY-2)*16, entrance_id=1, dest_area=0, dest_entrance=0,
        etype=ENTRANCE_NORMAL, zone_id=0, layer=0, path=0,
        unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    # ── ENTRANCES ──
    # Main Exit Door (Entrance 2) -> Leads to Area 2 (course2.bin) Attic
    # Door Sprite is at GY-3. Entrance DOOR must be +2 tiles below the sprite (GY-1)
    area1.entrances.append(Entrance(
        x=(TX+112)*16, y=(GY-1)*16, entrance_id=2, dest_area=2, dest_entrance=0,
        etype=ENTRANCE_DOOR, zone_id=0, layer=0, path=0,
        unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # Secret Pipe Down (Entrance 3) -> Hidden inside the floor gap at TX+66
    # Leads to Area 3 (course3.bin) Cannon Lobby.
    area1.entrances.append(Entrance(
        x=(TX+66)*16, y=GY*16, entrance_id=3, dest_area=3, dest_entrance=0,
        etype=ENTRANCE_PIPE_DOWN, zone_id=0, layer=0, path=0,
        unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # ── TERRAIN ──
    # IMPORTANT: Pa1_obake (tileset 1) objects do NOT render as terrain!
    # And Pa0_jyotyu (tileset 0) object 58 is actually a COIN string!
    # We must use tileset 2 (Pa1_chika = Underground) which has real terrain.
    CG_TOP = CaveObjs.GROUND_TOP
    CG_FIL = CaveObjs.GROUND_FILL
    CG_LWL = CaveObjs.LEFT_WALL
    CG_RWL = CaveObjs.RIGHT_WALL
    CG_CIL = CaveObjs.CEILING

    # Floor — structured sections with bottomless gaps between them
    def add_floor_segment(sx, w):
        obj2_a1(CG_TOP, TX + sx, GY, w, 1)
        obj2_a1(CG_FIL, TX + sx, GY+1, w, 6) # deep fill
        obj2_a1(CG_CIL, TX + sx, CY, w, 2)
        
    add_floor_segment(0,  25) # Icy Foyer (0-25)
    # Gap 25-28
    add_floor_segment(28, 27) # Dark Wing (28-55)
    # Gap 55-58

    # Ice Maze (58-82)
    # We leave a 2-tile gap at TX+66 for the Secret Pipe
    add_floor_segment(58, 8)  # 58-66
    # Gap 66-68 (Pipe)
    add_floor_segment(68, 14) # 68-82

    # Gap 82-85
    add_floor_segment(85, 37) # Parlour + Exit (85-122)

    # Left wall
    obj2_a1(CG_LWL, TX, CY+2, 1, GY-CY-2)

    # §1 Icy Foyer (TX to TX+25) — no ? blocks, just atmosphere

    # §2 Dark Wing (TX+28 to TX+55) — glow block lights
    spr(GLOW_BLOCK, (TX+30)*16, (GY-4)*16)
    spr(GLOW_BLOCK, (TX+38)*16, (GY-4)*16)
    spr(GLOW_BLOCK, (TX+46)*16, (GY-4)*16)

    # §3 Ice Wall Maze (TX+58 to TX+82)
    # Split the raised platform into two pillars to expose the pipe gap between them!
    obj2_a1(CG_TOP, TX+64, GY-4, 2, 1) # Left Pillar
    obj2_a1(CG_FIL, TX+64, GY-3, 2, 3)
    
    obj2_a1(CG_TOP, TX+68, GY-4, 2, 1) # Right Pillar
    obj2_a1(CG_FIL, TX+68, GY-3, 2, 3)
    
    # Place physical Secret Exit Pipe DOWN perfectly flush within the floor gap!
    obj0_layer1_a1(StandardObjs.PIPE_ENTRY, TX+66, GY, 2, 2)
    obj0_layer1_a1(StandardObjs.PIPE_BODY,  TX+66, GY+2, 2, 5)

    # §4 The Parlour (TX+85 to TX+103) — midway + Big Boo ambush

    # §5 Exit Area (TX+106 to TX+122)
    # The normal exit door stands at the far right.

    # Right wall
    obj2_a1(CG_RWL, TX+121, CY+2, 1, GY-CY-2)

    # ── SPRITES ──

    # §1 Foyer: gentle intro Boos
    spr(BOO, (TX+8)*16,  (GY-2)*16)
    spr(BOO, (TX+12)*16, (GY-4)*16)
    spr(BOO, (TX+18)*16, (GY-2)*16)
    spr(DRY_BONES, (TX+22)*16, (GY-1)*16)

    # §2 Dark Wing: BOO CIRCLES
    boo_circle = b'\x00\x00\x00\x00\x00\x03'
    spr(BOO, (TX+32)*16, (GY-5)*16, boo_circle)
    spr(BOO, (TX+40)*16, (GY-5)*16, boo_circle)
    spr(BOO, (TX+48)*16, (GY-5)*16, boo_circle)
    spr(SWOOP, (TX+35)*16, (CY+2)*16)
    spr(SWOOP, (TX+43)*16, (CY+2)*16)
    spr(SWOOP, (TX+51)*16, (CY+2)*16)

    # §3 Ice Wall Maze
    spr(ICE_BLOCK, (TX+60)*16, (GY-1)*16)
    spr(ICE_BLOCK, (TX+61)*16, (GY-1)*16)
    spr(ICE_BLOCK, (TX+63)*16, (GY-5)*16)
    spr(ICE_BLOCK, (TX+69)*16, (GY-5)*16)
    spr(ICE_BLOCK, (TX+70)*16, (GY-5)*16)
    # The Broozer that the player must bait into breaking the barrels covering the secret pipe
    spr(BROOZER, (TX+59)*16, (GY-1)*16)
    
    # Hide the Secret Pipe entrance using ICE_BLOCKs that the Broozer can punch!
    # They form a bridge flush with the adjacent ice pillars (GY-5).
    spr(ICE_BLOCK, (TX+66)*16, (GY-5)*16)
    spr(ICE_BLOCK, (TX+67)*16, (GY-5)*16)

    spr(BOO,     (TX+72)*16, (GY-3)*16)
    spr(BOO,     (TX+76)*16, (GY-6)*16)

    # §4 Parlour: BIG BOO + Midway Flag + Star Coin
    spr(MIDWAY_FLAG, (TX+88)*16, (GY-1)*16,
        b'\x00\x00\x00\x01\x00\x00')
    spr(BIG_BOO, (TX+92)*16, (GY-5)*16)
    spr(BOO, (TX+95)*16, (GY-3)*16)
    spr(BOO, (TX+95)*16, (GY-7)*16)
    area1.sprites.append(Sprite(stype=STAR_COIN, x=(TX+92)*16, y=(GY-9)*16,
                                spritedata=b'\x00\x00\x00\x00\x00\x00',
                                zone_id=0, extra_byte=0))

    # §5 Exit: The big door to the Attic.
    # Sprite 276 (Ghost Door). The bottom of this 3-tile tall door sits flush at GY!
    spr(276, (TX+112)*16, (GY-3)*16, b'\x00\x00\x00\x00\x00\x00')

    spr(BOO, (TX+110)*16, (GY-3)*16)
    spr(BOO, (TX+114)*16, (GY-5)*16)
    spr(SWOOP, (TX+108)*16, (CY+1)*16)

    area1.loaded_sprites = sorted(set(s.stype for s in area1.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))
    arc.set_file('course/course1_bgdatL0.bin', serialize_layer_data(area1.layer0))
    arc.set_file('course/course1_bgdatL1.bin', serialize_layer_data(area1.layer1))
    arc.set_file('course/course1_bgdatL2.bin', serialize_layer_data(area1.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 2 — The Frozen Attic (Main Exit)
    # ════════════════════════════════════════════════════
    # A vertical ghost house room accessed via DOOR from Area 1.
    # Big Boos patrol between ice columns. Star Coin 2 at the top.
    # Normal exit: Big door at the very top leading outside.

    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    area2.sprites.clear()
    area2.layer1.clear()
    area2.layer0.clear()
    area2.entrances.clear()
    area2.zones.clear()
    area2.boundings.clear()
    area2.settings.time_limit = 400
    area2.tileset = Tileset(slot0=TILESET_STANDARD, slot1=TILESET_GHOST,
                            slot2=TILESET_CAVE, slot3='')

    # Tall vertical zone
    AX, AY = 256, 0  # Changed AY to 0 so the camera can pan up
    AW, AH = 700, 2200
    area2.zones.append(Zone(x=AX, y=AY, w=AW, h=AH, zone_id=0,
                            music=MUSIC_GHOST, cam_mode=3, cam_zoom=0, # cam_mode 3 = vertical
                            visibility=36))
    area2.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0,
                                    bound_id=0, mp_cam_zoom=15,
                                    upper3=0, lower3=0))

    def obj1_a2(ot, x, y, width=1, h=1):
        area2.layer1.append(LayerObject(tileset=1, obj_type=ot, x=x, y=y, w=width, h=h))

    def obj0_layer1_a2(ot, x, y, w=1, h=1):
        area2.layer1.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    def spr2(stype, x, y, data=b'\x00'*6):
        area2.sprites.append(Sprite(stype=stype, x=x, y=y,
                                    spritedata=data, zone_id=0, extra_byte=0))

    ATX = 16
    ABOT = 126  # Bottom tile Y (must be < 128 to stay in AH=1800 pixel bounds)
    ATOP = 10   # Top tile Y

    # Entrance from Main Door (Mario emerges from Door 0)
    # Door Sprite is at ABOT-3. Entrance DOOR must be +2 tiles below (ABOT-1). 
    area2.entrances.append(Entrance(
        x=(ATX+10)*16, y=(ABOT-1)*16, entrance_id=0,
        dest_area=1, dest_entrance=2, etype=ENTRANCE_DOOR, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    # Exit at top — Door leading OUTSIDE to Area 4
    # Floor is ATOP+6. Entrance DOOR must be +2 tiles below the sprite (Floor - 1 tile = ATOP+5).
    area2.entrances.append(Entrance(
        x=(ATX+4)*16, y=(ATOP+5)*16, entrance_id=1,
        dest_area=4, dest_entrance=0, etype=ENTRANCE_DOOR, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # Bottom floor + walls (using underground tileset)
    def obj2_a2(ot, x, y, w=1, h=1):
        area2.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))
    
    obj2_a2(CG_TOP, ATX,    ABOT,   22, 1)    # floor top
    obj2_a2(CG_FIL, ATX,    ABOT+1, 22, 3)    # floor fill
    obj2_a2(CG_LWL, ATX,    ATOP+2, 1,  ABOT-ATOP-2)  # left wall
    obj2_a2(CG_RWL, ATX+21, ATOP+2, 1,  ABOT-ATOP-2)  # right wall
    obj2_a2(CG_CIL, ATX,    ATOP,   22, 2)    # ceiling

    # Arrival Door Sprite
    spr2(276, (ATX+10)*16, (ABOT-1)*16, b'\x00\x00\x00\x00\x00\x00')

    # Ice columns — narrow pillars forcing weaving path upward
    obj2_a2(CG_FIL, ATX+5,  ABOT-8,  3, 8)
    obj2_a2(CG_FIL, ATX+14, ABOT-14, 3, 14)
    obj2_a2(CG_FIL, ATX+5,  ABOT-22, 3, 6)
    obj2_a2(CG_FIL, ATX+14, ABOT-32, 3, 8)
    obj2_a2(CG_FIL, ATX+5,  ABOT-42, 3, 8)
    obj2_a2(CG_FIL, ATX+14, ABOT-52, 3, 8)

    obj2_a2(CG_TOP, ATX+8,  (ABOT-5), 3, 1)
    obj2_a2(CG_FIL, ATX+8,  (ABOT-4), 3, 2)
    obj2_a2(CG_TOP, ATX+10, (ABOT-18), 3, 1)
    obj2_a2(CG_FIL, ATX+10, (ABOT-17), 3, 2)
    obj2_a2(CG_TOP, ATX+8,  (ABOT-30), 3, 1)
    obj2_a2(CG_FIL, ATX+8,  (ABOT-29), 3, 2)
    obj2_a2(CG_TOP, ATX+11, (ABOT-36), 3, 1) # new
    obj2_a2(CG_FIL, ATX+11, (ABOT-35), 3, 2)
    obj2_a2(CG_TOP, ATX+7,  (ABOT-43), 3, 1) 
    obj2_a2(CG_FIL, ATX+7,  (ABOT-42), 3, 2)
    
    # Extra platforms connecting the massive gap to the top!
    obj2_a2(CG_TOP, ATX+12, (ABOT-49), 3, 1) 
    obj2_a2(CG_FIL, ATX+12, (ABOT-48), 3, 2)
    obj2_a2(CG_TOP, ATX+6,  (ABOT-55), 3, 1) 
    obj2_a2(CG_FIL, ATX+6,  (ABOT-54), 3, 2)
    obj2_a2(CG_TOP, ATX+12, (ABOT-61), 3, 1) 
    obj2_a2(CG_FIL, ATX+12, (ABOT-60), 3, 2)
    obj2_a2(CG_TOP, ATX+8,  (ABOT-67), 3, 1) 
    obj2_a2(CG_FIL, ATX+8,  (ABOT-66), 3, 2)
    obj2_a2(CG_TOP, ATX+13, (ABOT-73), 3, 1) 
    obj2_a2(CG_FIL, ATX+13, (ABOT-72), 3, 2)
    obj2_a2(CG_TOP, ATX+6,  (ABOT-78), 3, 1) 
    obj2_a2(CG_FIL, ATX+6,  (ABOT-77), 3, 2)
    obj2_a2(CG_TOP, ATX+11, (ABOT-84), 3, 1) 
    obj2_a2(CG_FIL, ATX+11, (ABOT-83), 3, 2)
    obj2_a2(CG_TOP, ATX+7,  (ABOT-90), 3, 1) 
    obj2_a2(CG_FIL, ATX+7,  (ABOT-89), 3, 2)

    # Final platforms near the very top so the player can reach the door
    obj2_a2(CG_TOP, ATX+8,  (ATOP+15), 3, 1)
    obj2_a2(CG_FIL, ATX+8,  (ATOP+16), 3, 2)
    obj2_a2(CG_TOP, ATX+4,  (ATOP+6),  4, 1)  # Floor is perfectly at ATOP+6
    obj2_a2(CG_FIL, ATX+4,  (ATOP+7),  4, 2)

    # Exit Door Sprite - Must be EXACTLY Floor - 3 tiles (ATOP+6 - 3 = ATOP+3)
    spr2(276, (ATX+4)*16, (ATOP+3)*16, b'\x00\x00\x00\x00\x00\x00')

    # BOOs and BIG_BOO floating between the columns
    spr2(BOO,     (ATX+9)*16,  (ABOT-10)*16)
    spr2(BOO,     (ATX+11)*16, (ABOT-20)*16)
    spr2(BIG_BOO, (ATX+9)*16,  (ABOT-35)*16)
    spr2(SWOOP,   (ATX+12)*16, (ABOT-25)*16)
    spr2(SWOOP,   (ATX+7)*16,  (ABOT-45)*16)
    spr2(BOO,     (ATX+10)*16, (ABOT-50)*16)

    # Star Coin 2 — floating high up near the top, between columns
    area2.sprites.append(Sprite(stype=STAR_COIN, x=(ATX+10)*16, y=(ABOT-58)*16,
                                spritedata=b'\x00\x00\x00\x01\x00\x00',
                                zone_id=0, extra_byte=0))

    # Icicles hanging from the ceiling
    spr2(ICICLE, (ATX+8)*16,  (ATOP+2)*16)
    spr2(ICICLE, (ATX+12)*16, (ATOP+2)*16)
    spr2(ICICLE, (ATX+16)*16, (ATOP+2)*16)

    # Remove internal Goal Pole since they don't render in Ghost House interiors
    area2.loaded_sprites = sorted(set(s.stype for s in area2.sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))
    arc.set_file('course/course2_bgdatL0.bin', serialize_layer_data(area2.layer0))
    arc.set_file('course/course2_bgdatL1.bin', serialize_layer_data(area2.layer1))
    arc.set_file('course/course2_bgdatL2.bin', serialize_layer_data(area2.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 3 — Secret Cannon Lobby (Secret Exit)
    # ════════════════════════════════════════════════════
    # The player discovers a hidden pipe under ICE_BLOCKs in Area 1.
    # This small room has one last Big Boo, a Star Coin 3, and the
    # Secret Goal Pole Pipe that unlocks World 3-Cannon -> World 6!

    area3 = parse_course_bin(arc.get_file('course/course3.bin'))
    area3.sprites.clear()
    area3.layer1.clear()
    area3.layer0.clear()
    area3.entrances.clear()
    area3.zones.clear()
    area3.boundings.clear()
    area3.settings.time_limit = 100
    area3.tileset = Tileset(slot0=TILESET_STANDARD, slot1=TILESET_GHOST,
                            slot2=TILESET_CAVE, slot3='')

    BX, BY_start = 256, 256
    BW, BH = 1200, 368
    area3.zones.append(Zone(x=BX, y=BY_start, w=BW, h=BH, zone_id=0,
                            music=MUSIC_GHOST, cam_mode=0, cam_zoom=0,
                            visibility=36))
    area3.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0,
                                    bound_id=0, mp_cam_zoom=15,
                                    upper3=0, lower3=0))

    def obj1_a3(ot, x, y, width=1, h=1):
        area3.layer1.append(LayerObject(tileset=1, obj_type=ot, x=x, y=y, w=width, h=h))

    def obj0_layer1_a3(ot, x, y, w=1, h=1):
        area3.layer1.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    def spr3(stype, x, y, data=b'\x00'*6):
        area3.sprites.append(Sprite(stype=stype, x=x, y=y,
                                    spritedata=data, zone_id=0, extra_byte=0))

    CTX = 16
    CGY = 33

    # Arrival from Area 1 (Secret Pipe DOWN) drops him from the ceiling
    # To drop from the ceiling, the entrance type must be ENTRANCE_PIPE_UP!
    area3.entrances.append(Entrance(
        x=(CTX+2)*16, y=(CGY-5)*16, entrance_id=0,
        dest_area=1, dest_entrance=3, etype=ENTRANCE_PIPE_UP, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # Arrival Drop Pipe matching coordinates
    obj0_layer1_a3(StandardObjs.PIPE_BODY,  CTX+1, CGY-15, 2, 8)
    obj0_layer1_a3(StandardObjs.PIPE_ENTRY, CTX+1, CGY-7, 2, 2) # Entry upside down logic

    # Exit pipe in Area 3 -> Area 4 Secret Goal (Entrance 1)
    # Changed to standard vertical pipe!
    # Pipe Entry is at CGY-3. Entrance Y must be EXACTLY equal to Pipe Entry Y (CGY-3) for Mario to enter it!
    area3.entrances.append(Entrance(
        x=(CTX+50)*16, y=(CGY-3)*16, entrance_id=1,
        dest_area=4, dest_entrance=1, etype=ENTRANCE_PIPE_DOWN, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # Physical vertical pipe located safely on the floor
    obj0_layer1_a3(StandardObjs.PIPE_ENTRY, CTX+50, CGY-3, 2, 2)
    obj0_layer1_a3(StandardObjs.PIPE_BODY, CTX+50, CGY-1, 2, 2)

    # Floor and ceiling (using underground tileset)
    def obj2_a3(ot, x, y, w=1, h=1):
        area3.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))
    
    # Redesigned segmented floor with pits and ice pillars!
    obj2_a3(CG_TOP, CTX,    CGY,    15, 1)    # Entry floor 
    obj2_a3(CG_FIL, CTX,    CGY+1,  15, 4)
    
    obj2_a3(CG_TOP, CTX+20, CGY-3,  8, 1)     # Center raised pillar
    obj2_a3(CG_FIL, CTX+20, CGY-2,  8, 7)
    
    obj2_a3(CG_TOP, CTX+35, CGY,    25, 1)    # Exit floor
    obj2_a3(CG_FIL, CTX+35, CGY+1,  25, 4)

    obj2_a3(CG_CIL, CTX,    CGY-15, 60, 2)    # ceiling
    obj2_a3(CG_LWL, CTX,    CGY-13, 1,  13)   # left wall
    obj2_a3(CG_RWL, CTX+59, CGY-13, 1,  13)   # right wall

    # Atmosphere: Glow blocks, Boos, and Ice blocks over gaps!
    spr3(ICE_BLOCK,  (CTX+17)*16, (CGY-1)*16)
    spr3(ICE_BLOCK,  (CTX+31)*16, (CGY-1)*16)
    spr3(ICE_BLOCK,  (CTX+33)*16, (CGY-1)*16)
    
    spr3(GLOW_BLOCK, (CTX+10)*16, (CGY-3)*16)
    spr3(GLOW_BLOCK, (CTX+23)*16, (CGY-7)*16)
    spr3(GLOW_BLOCK, (CTX+40)*16, (CGY-3)*16)
    
    spr3(BOO,        (CTX+15)*16, (CGY-5)*16)
    spr3(BOO,        (CTX+28)*16, (CGY-8)*16)
    spr3(BIG_BOO,    (CTX+35)*16, (CGY-7)*16)
    spr3(SWOOP,      (CTX+20)*16, (CGY-13)*16)
    spr3(SWOOP,      (CTX+40)*16, (CGY-13)*16)

    # Star Coin 3 — floating directly over the central ice pillar!
    area3.sprites.append(Sprite(stype=STAR_COIN, x=(CTX+24)*16, y=(CGY-9)*16,
                                spritedata=b'\x00\x00\x00\x02\x00\x00',
                                zone_id=0, extra_byte=0))

    area3.loaded_sprites = sorted(set(s.stype for s in area3.sprites))
    arc.set_file('course/course3.bin', serialize_course_bin(area3))
    arc.set_file('course/course3_bgdatL0.bin', serialize_layer_data(area3.layer0))
    arc.set_file('course/course3_bgdatL1.bin', serialize_layer_data(area3.layer1))
    arc.set_file('course/course3_bgdatL2.bin', serialize_layer_data(area3.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 4 — Outdoor Courtyard (Goal Poles)
    # ════════════════════════════════════════════════════
    # Both Goal Poles go in Area 4, but spaced very far apart so they don't share a screen.
    area4 = parse_course_bin(arc.get_file('course/course4.bin'))
    area4.sprites.clear()
    area4.entrances.clear()
    # DO NOT CLEAR ZONES OR BOUNDINGS. WE NEED BOTH VANILLA ZONES!
    # Zone 0: Y=256 bounds the Normal Exit
    # Zone 1: Y=1024 bounds the Secret Exit
    
    # -- NORMAL EXIT ZONE --
    DX_NORM = 25
    DGY_NORM = 31
    
    # Arrival from Area 2 (Normal Exit)
    # Door Sprite is at DGY_NORM-3 (Y=28). Entrance DOOR must be +2 tiles below (DGY_NORM-1 -> Y=30).
    area4.entrances.append(Entrance(
        x=(DX_NORM)*16, y=(DGY_NORM-1)*16, entrance_id=0,
        dest_area=2, dest_entrance=1, etype=ENTRANCE_DOOR, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
        
    # Visual Ghost Door for Mario to walk out of!
    area4.sprites.append(Sprite(stype=276, x=(DX_NORM)*16, y=(DGY_NORM-3)*16,
                                spritedata=b'\x00\x00\x00\x00\x00\x00', zone_id=0, extra_byte=0))
    
    # Normal Goal Pole - Aligned precisely with Vanilla Stairs!
    area4.sprites.append(Sprite(stype=GOAL_POLE,
                                x=62*16, y=30*16,
                                spritedata=b'\x00'*6, zone_id=0, extra_byte=0))

    def obj0_layer1_a4(ot, x, y, w=1, h=1):
        area4.layer1.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    # -- SECRET EXIT ZONE --
    DX_SEC = 25
    DGY_SEC = 79
    
    # Arrival from Area 3 (Secret Exit Pipe) 
    # Mario emerges moving OUT of a door towards the flag pole! This is identical to the Normal Exit.
    # Door Sprite is at DGY_SEC-3 (Y=76). Entrance DOOR must be +2 tiles below (DGY_SEC-1 -> Y=78).
    area4.entrances.append(Entrance(
        x=(DX_SEC)*16, y=(DGY_SEC-1)*16, entrance_id=1,
        dest_area=3, dest_entrance=1, etype=ENTRANCE_DOOR, zone_id=1,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
                                
    # Visual Ghost Door for Mario to walk out of!
    area4.sprites.append(Sprite(stype=276, x=(DX_SEC)*16, y=(DGY_SEC-3)*16,
                                spritedata=b'\x00\x00\x00\x00\x00\x00', zone_id=1, extra_byte=0))

    # Secret Goal Pole (red flag) - Aligned precisely with Vanilla Secret Stairs!
    area4.sprites.append(Sprite(stype=GOAL_POLE,
                                x=62*16, y=78*16,
                                spritedata=b'\x00\x00\x10\x00\x00\x00',
                                zone_id=1, extra_byte=0)) # Secret Pole must be mapped to Zone 1
    
    # Block off the left side of the Secret Flag area with a massive invisible wall 
    # to prevent the player from accidentally flying back to the Normal exit mapping somehow
    area4.layer1.append(LayerObject(tileset=2, obj_type=CaveObjs.COLUMN, x=10, y=DGY_SEC-25, w=5, h=30))
    
    area4.loaded_sprites = sorted(set(s.stype for s in area4.sprites))
    arc.set_file('course/course4.bin', serialize_course_bin(area4))

    # Save
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-21.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-21.arc ({len(data)} bytes)')


def create_level_3_cannon():
    """Level 3-Cannon: Frostbite Heights — High-altitude icy gauntlet to World 6.

    A snow-swept vertical climb across slippery ice pillars and drifting platforms.
    Lakitus harass from above while Cooligans slide across the icy runways.
    Reach the Warp Cannon at the summit to blast off to World 6!

    Layout:
      §1 Starting Snowbank      — safe landing, gentle intro
      §2 Ice Pillar Crossing     — precision jumps across tall ice columns
      §3 Cooligan Runway         — long icy runway with sliding Cooligans
      §4 Frozen Towers           — tall narrow pillars with Lakitu overhead
      §5 Summit & Warp Cannon    — final climb to the cannon
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin,
        Sprite, LayerObject, parse_layer_data, serialize_layer_data,
        Entrance, Zone, Bounding, Tileset
    )
    from tools.sprite_db import (
        COIN, STAR_COIN, LAKITU, COOLIGAN, ICE_BRO, ICICLE,
        DRY_BONES, KOOPA, SPINY, GOOMBA,
        TILESET_STANDARD, TILESET_SNOW, GrassObjs, StandardObjs,
        ENTRANCE_NORMAL, MUSIC_SNOW, BG_SNOW
    )

    with open('extracted files/Stage/03-36.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    area = parse_course_bin(arc.get_file('course/course1.bin'))
    area.sprites.clear()
    area.layer1.clear()
    area.layer0.clear()
    area.entrances.clear()
    area.zones.clear()
    area.boundings.clear()

    # Tileset: Standard + Snow
    area.tileset = Tileset(slot0=TILESET_STANDARD, slot1=TILESET_SNOW,
                           slot2='', slot3='')
    area.settings.time_limit = 200

    # Zone — sized to match vanilla cannon level proportions
    ZX, ZY = 256, 256
    ZW, ZH = 1792, 512
    area.zones.append(Zone(x=ZX, y=ZY, w=ZW, h=ZH, zone_id=0,
                           music=MUSIC_SNOW, cam_mode=0, cam_zoom=0,
                           visibility=0))
    area.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0,
                                   bound_id=0, mp_cam_zoom=15,
                                   upper3=0, lower3=0))

    # Helpers
    SD = b'\x00\x00\x00\x00\x00\x00'
    TX = 16    # tile X offset
    GY = 45    # ground Y (tiles) — near bottom

    def snow(ot, x, y, w=1, h=1):
        """Add a snow tileset (slot 1) terrain object."""
        area.layer1.append(LayerObject(tileset=1, obj_type=ot, x=x, y=y, w=w, h=h))

    def std(ot, x, y, w=1, h=1):
        """Add a standard tileset (slot 0) terrain object."""
        area.layer1.append(LayerObject(tileset=0, obj_type=ot, x=x, y=y, w=w, h=h))

    def spr(stype, x, y, data=SD):
        area.sprites.append(Sprite(stype=stype, x=x, y=y,
                                   spritedata=data, zone_id=0, extra_byte=0))

    SG_TOP = GrassObjs.GROUND_TOP      # Snow ground uses same IDs as Grass
    SG_FIL = GrassObjs.GROUND_FILL

    # ── Entrance ──
    area.entrances.append(Entrance(
        x=(TX+2)*16, y=(GY-2)*16, entrance_id=0,
        dest_area=0, dest_entrance=0, etype=ENTRANCE_NORMAL, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    # ════════════════════════════════════════════════════
    #   §1 — Starting Snowbank (TX to TX+12)
    # ════════════════════════════════════════════════════
    snow(SG_TOP, TX, GY, 12, 1)
    snow(SG_FIL, TX, GY+1, 12, 6)

    spr(COIN, (TX+4)*16, (GY-2)*16)
    spr(COIN, (TX+6)*16, (GY-2)*16)
    spr(COIN, (TX+8)*16, (GY-2)*16)
    spr(GOOMBA, (TX+10)*16, (GY-1)*16)

    # Snow particles + area controller
    spr(374, ZX, ZY, SD)
    spr(310, (TX+2)*16, GY*16)

    # ════════════════════════════════════════════════════
    #   §2 — Ice Pillar Crossing (TX+15 to TX+35)
    # ════════════════════════════════════════════════════
    snow(SG_TOP, TX+15, GY-2, 3, 1)    # Pillar 1
    snow(SG_FIL, TX+15, GY-1, 3, 8)

    snow(SG_TOP, TX+21, GY-5, 3, 1)    # Pillar 2
    snow(SG_FIL, TX+21, GY-4, 3, 11)

    snow(SG_TOP, TX+27, GY-3, 3, 1)    # Pillar 3
    snow(SG_FIL, TX+27, GY-2, 3, 9)

    snow(SG_TOP, TX+33, GY-6, 3, 1)    # Pillar 4
    snow(SG_FIL, TX+33, GY-5, 3, 12)

    spr(COIN, (TX+18)*16, (GY-4)*16)
    spr(COIN, (TX+24)*16, (GY-7)*16)
    spr(COIN, (TX+30)*16, (GY-5)*16)
    spr(DRY_BONES, (TX+21)*16, (GY-6)*16)

    # ★ Star Coin 1 — hidden low between pillars
    area.sprites.append(Sprite(stype=STAR_COIN, x=(TX+25)*16, y=(GY-1)*16,
                               spritedata=b'\x00\x00\x00\x00\x00\x00',
                               zone_id=0, extra_byte=0))

    # ════════════════════════════════════════════════════
    #   §3 — Cooligan Runway (TX+38 to TX+62)
    # ════════════════════════════════════════════════════
    snow(SG_TOP, TX+38, GY, 24, 1)
    snow(SG_FIL, TX+38, GY+1, 24, 6)

    # Small raised platform mid-runway
    snow(SG_TOP, TX+48, GY-4, 4, 1)
    snow(SG_FIL, TX+48, GY-3, 4, 3)

    # Pipe obstacle
    std(StandardObjs.PIPE_ENTRY, TX+43, GY-3, 2, 2)
    std(StandardObjs.PIPE_BODY,  TX+43, GY-1, 2, 1)

    # Cooligans sliding in!
    spr(COOLIGAN, (TX+58)*16, (GY-1)*16)
    spr(COOLIGAN, (TX+55)*16, (GY-1)*16)

    # Ice Bro on the raised platform
    spr(ICE_BRO, (TX+49)*16, (GY-5)*16)

    # Coins along the runway
    for i in range(40, 60, 3):
        spr(COIN, (TX+i)*16, (GY-2)*16)

    # ★ Star Coin 2 — above the raised platform
    area.sprites.append(Sprite(stype=STAR_COIN, x=(TX+50)*16, y=(GY-8)*16,
                               spritedata=b'\x00\x00\x00\x01\x00\x00',
                               zone_id=0, extra_byte=0))

    # ════════════════════════════════════════════════════
    #   §4 — Frozen Towers + Lakitu (TX+65 to TX+82)
    # ════════════════════════════════════════════════════
    snow(SG_TOP, TX+65, GY-2, 3, 1)    # Tower 1
    snow(SG_FIL, TX+65, GY-1, 3, 8)

    snow(SG_TOP, TX+70, GY-5, 3, 1)    # Tower 2
    snow(SG_FIL, TX+70, GY-4, 3, 11)

    snow(SG_TOP, TX+75, GY-3, 3, 1)    # Tower 3
    snow(SG_FIL, TX+75, GY-2, 3, 9)

    snow(SG_TOP, TX+80, GY, 5, 1)      # Landing platform
    snow(SG_FIL, TX+80, GY+1, 5, 6)

    # Lakitu above the towers!
    spr(LAKITU, (TX+70)*16, (GY-14)*16)
    spr(DRY_BONES, (TX+76)*16, (GY-4)*16)

    spr(COIN, (TX+68)*16, (GY-4)*16)
    spr(COIN, (TX+73)*16, (GY-7)*16)
    spr(COIN, (TX+78)*16, (GY-5)*16)

    # ════════════════════════════════════════════════════
    #   §5 — Summit & Warp Cannon (TX+87 to TX+105)
    # ════════════════════════════════════════════════════
    snow(SG_TOP, TX+87, GY, 18, 1)
    snow(SG_FIL, TX+87, GY+1, 18, 6)

    # Raised cannon platform
    snow(SG_TOP, TX+93, GY-5, 8, 1)
    snow(SG_FIL, TX+93, GY-4, 8, 4)

    # Staircase up to cannon
    snow(SG_TOP, TX+89, GY-1, 2, 1)
    snow(SG_FIL, TX+89, GY,   2, 1)
    snow(SG_TOP, TX+91, GY-3, 2, 1)
    snow(SG_FIL, TX+91, GY-2, 2, 2)

    # ★ Star Coin 3 — above the gap before the summit
    area.sprites.append(Sprite(stype=STAR_COIN, x=(TX+85)*16, y=(GY-8)*16,
                               spritedata=b'\x00\x00\x00\x02\x00\x00',
                               zone_id=0, extra_byte=0))

    # Final enemies
    spr(DRY_BONES, (TX+88)*16, (GY-1)*16)
    spr(ICE_BRO,   (TX+95)*16, (GY-6)*16)

    # ══════ THE WARP CANNON ══════
    # Sprite 434 = Warp Cannon. Byte 5 = 1 -> World 6.
    spr(434, (TX+97)*16, (GY-8)*16, b'\x00\x00\x00\x00\x00\x01')

    # Icicle decorations
    spr(ICICLE, (TX+93)*16, (GY-5)*16)
    spr(ICICLE, (TX+100)*16, (GY-5)*16)

    # Coins around the cannon
    spr(COIN, (TX+96)*16, (GY-7)*16)
    spr(COIN, (TX+98)*16, (GY-7)*16)

    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))

    # Save
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-36.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-36.arc ({len(data)} bytes)')


def create_level_3_4():
    """Level 3-4: Switchblock Spire — edit-on-base approach.

    Load vanilla 03-04.arc, strip basic enemies, add ice-themed replacements.
    Area 3 left vanilla so the Goal Pole is guaranteed intact.
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    with open('extracted files/Stage/03-04.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    SD = b'\x00\x00\x00\x00\x00\x00'

    # Strip vanilla enemies to make room for ice replacements.
    STRIP_TYPES = {
        db.GOOMBA,              # 20
        db.KOOPA,               # 57
        db.KOOPA_PARATROOPA,    # 58
        db.FIRE_BRO,            # 80
    }

    # ═══════════ AREA 1: Main Level ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.sprites = [s for s in area1.sprites if s.stype not in STRIP_TYPES]
    # Area 1's zone_id is 2 — all added sprites must match or the game breaks
    Z1 = area1.zones[0].zone_id  # = 2

    def add1(stype, x, y):
        area1.sprites.append(Sprite(stype=stype, x=x, y=y, spritedata=SD, zone_id=Z1, extra_byte=0))

    # Early section
    add1(db.COOLIGAN,  1000, 480)
    add1(db.COOLIGAN,  1200, 480)
    add1(db.DRY_BONES,  800, 480)
    add1(db.DRY_BONES, 1400, 480)
    # Mid section
    add1(db.ICE_BRO,   2200, 400)
    add1(db.ICE_BRO,   3000, 384)
    add1(db.DRY_BONES, 2500, 480)
    add1(db.DRY_BONES, 2800, 480)
    # Icicles along the ceiling
    for x_off in range(1600, 4000, 300):
        add1(db.ICICLE, x_off, 200)
    # Post-midway
    add1(db.COOLIGAN,  4400, 480)
    add1(db.COOLIGAN,  4600, 480)
    add1(db.ICE_BRO,   4800, 384)
    add1(db.COOLIGAN,  5000, 480)
    add1(db.DRY_BONES, 5200, 480)
    add1(db.ICE_BRO,   5600, 400)
    # Late gauntlet
    add1(db.COOLIGAN,  6000, 480)
    add1(db.COOLIGAN,  6200, 480)
    add1(db.ICE_BRO,   6500, 400)
    add1(db.DRY_BONES, 6800, 480)
    add1(db.ICE_BRO,   7000, 384)
    add1(db.COOLIGAN,  7400, 384)

    area1.loaded_sprites = sorted(set(s.stype for s in area1.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Underground Pipe Section ═══════════
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    area2.sprites = [s for s in area2.sprites if s.stype not in STRIP_TYPES]
    Z2 = area2.zones[0].zone_id
    for x, y, stype in [(600, 400, db.SWOOP), (1000, 400, db.SWOOP),
                        (800, 500, db.DRY_BONES), (1200, 500, db.BUZZY_BEETLE)]:
        area2.sprites.append(Sprite(stype=stype, x=x, y=y, spritedata=SD, zone_id=Z2, extra_byte=0))
    area2.loaded_sprites = sorted(set(s.stype for s in area2.sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # ═══════════ AREA 3: VANILLA UNTOUCHED ═══════════
    # Goal Pole lives here — don't touch it.

    # Save
    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-04.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-04.arc ({len(data)} bytes)')




def create_level_3_5():
    """Level 3-5: Frostwheel Gallery — Restored memory-safe version.

    The original level uses Propeller Box platforming. We must keep
    the Sprite Memory Bank very low or else the camera scroll controller
    (Sprite 367) fails to load, causing the "No Camera Scroll" bug.
    
    Replaces:
      Goombas (20) -> Cooligans (201)
      Paragoombas (21) -> Swoopers (100)
    Preserves all physical level structure to avoid memory spikes.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    from tools.sprite_db import COOLIGAN, SWOOP, BOO

    with open('extracted files/Stage/03-05.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1 ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = []
    
    for s in area1.sprites:
        if s.stype == 20:   # Goomba
            ns = copy.deepcopy(s)
            ns.stype = COOLIGAN
            ns.spritedata = b'\x00'*6
            new_sprites.append(ns)
        elif s.stype == 21: # Paragoomba
            ns = copy.deepcopy(s)
            ns.stype = SWOOP
            ns.spritedata = b'\x00'*6
            new_sprites.append(ns)
        else:
            new_sprites.append(s)

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2 ═══════════
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    new2 = []
    for s in area2.sprites:
        if s.stype == 20:   # Goomba
            ns = copy.deepcopy(s)
            ns.stype = COOLIGAN
            ns.spritedata = b'\x00'*6
            new2.append(ns)
        elif s.stype == 21: # Paragoomba
            ns = copy.deepcopy(s)
            ns.stype = SWOOP
            ns.spritedata = b'\x00'*6
            new2.append(ns)
        else:
            new2.append(s)
            
    # Add a spooky Boos constraint in Area 2
    new2.append(Sprite(stype=BOO, x=600, y=300, spritedata=b'\x00'*6, zone_id=0, extra_byte=0))

    area2.sprites = new2
    area2.loaded_sprites = sorted(set(s.stype for s in new2))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-05.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-05.arc ({len(data)} bytes)')


def create_level_3_tower():
    """3-Tower: Glacial Spire — Ice fortress vertical climb with Lemmy boss.

    Preserves: Rotating blocks (149), rotation controllers (96),
    big spinners (122), ball launchers (253/438), spiked balls (63),
    red coins (144/156), star coins, midway, entrances, and all
    terrain/camera structure.

    Replaces: 26 Dry Bones (118) -> mix of Giant Dry Bones + Ice Bros.
    6 Amps (104) -> Swoopers for icy atmosphere.
    Boss room: adds Dry Bones flanking Lemmy.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/03-22.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1: Tower Climb ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))

    new_sprites = []
    db_count = 0
    for s in area1.sprites:
        if s.stype == 118:
            # Dry Bones -> alternate between Giant Dry Bones and Ice Bro
            ns = copy.deepcopy(s)
            if db_count % 3 == 0:
                ns.stype = GIANT_DRY_BONES  # 119
                ns.spritedata = b'\x00\x00\x00\x00\x00\x00'
            elif db_count % 3 == 1:
                ns.stype = ICE_BRO  # 272
                ns.spritedata = b'\x00\x00\x00\x00\x00\x00'
            # else: keep as regular Dry Bones
            new_sprites.append(ns)
            db_count += 1
        elif s.stype == 104:
            # Amp -> Swooper (better ice aesthetic)
            ns = copy.deepcopy(s)
            ns.stype = SWOOP
            ns.spritedata = b'\x00\x00\x00\x00\x00\x00'
            new_sprites.append(ns)
        else:
            new_sprites.append(s)

    # Add hazards throughout the climb to make it much more interesting.
    # The climb path uses X=480-848, Y spans from ~5900 (bottom) to ~300 (top).
    # The "boring first section" is roughly Y=3500-5500.
    SD = b'\x00\x00\x00\x00\x00\x00'
    
    # --- LOWER SECTION (Y=4500-5500): Add Icicles and extra enemies ---
    # Icicles along the walls of the climb path
    new_sprites.append(Sprite(stype=ICICLE, x=528, y=5200, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=720, y=5200, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=560, y=4800, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=752, y=4800, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=640, y=4400, spritedata=SD, zone_id=0, extra_byte=0))
    
    # Extra Ice Bros in the lower section
    new_sprites.append(Sprite(stype=ICE_BRO, x=560, y=4600, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICE_BRO, x=752, y=5000, spritedata=SD, zone_id=0, extra_byte=0))
    
    # --- MID SECTION (Y=3000-4500): Fire Bars and more enemies ---
    # Fire Bars at multiple heights to force careful navigation
    fb_sd = b'\x00\x00\x00\x00\x10\x06'  # Clockwise, length 6
    new_sprites.append(Sprite(stype=FIRE_BAR, x=640, y=4200, spritedata=fb_sd, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=FIRE_BAR, x=560, y=3600, spritedata=fb_sd, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=FIRE_BAR, x=720, y=3000, spritedata=fb_sd, zone_id=0, extra_byte=0))
    
    # Counter-clockwise Fire Bars for variety
    fb_ccw = b'\x00\x00\x00\x00\x00\x06'  # Counter-clockwise, length 6
    new_sprites.append(Sprite(stype=FIRE_BAR, x=700, y=2500, spritedata=fb_ccw, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=FIRE_BAR, x=560, y=1500, spritedata=fb_sd, zone_id=0, extra_byte=0))
    
    # More icicles in the mid section
    new_sprites.append(Sprite(stype=ICICLE, x=480, y=3800, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=848, y=3800, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=600, y=3400, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=ICICLE, x=700, y=3400, spritedata=SD, zone_id=0, extra_byte=0))
    
    # --- UPPER SECTION (Y=1000-2500): Extra Swoopers for atmosphere ---
    new_sprites.append(Sprite(stype=SWOOP, x=560, y=2000, spritedata=SD, zone_id=0, extra_byte=0))
    new_sprites.append(Sprite(stype=SWOOP, x=720, y=1200, spritedata=SD, zone_id=0, extra_byte=0))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Boss Room (Lemmy) ═══════════
    # Zone: x=288, y=416, w=432, h=224 -> boss arena (288-720, 416-640)
    # Lemmy (340) at (592,576), Kamek (363) at (352,464)
    SD = b'\x00\x00\x00\x00\x00\x00'
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)

    # Add variety flanking the boss — within zone (288-720, 416-640)
    boss_sprites.append(Sprite(stype=GIANT_DRY_BONES, x=380, y=590,
                               spritedata=SD, zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=ICE_BRO, x=660, y=590,
                               spritedata=SD, zone_id=0, extra_byte=0))

    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-22.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-22.arc ({len(data)} bytes)')


def create_level_3_ambush():
    """3-Ambush: Blizzard Patrol — Overhauled enemy gauntlet (03-33/34/35.arc).

    The real ambush files are XX-33, XX-34, XX-35 (3 variants per world).
    W3 vanilla has Ice Bros (272) and Springboards (148) as enemies.
    We replace Ice Bros with a tougher mix and add extra enemies.
    Preserves: Toad rescue sprites (185), controllers (203, 454), springboards.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    SD = b'\x00\x00\x00\x00\x00\x00'
    
    # Cycle of replacement enemies for Ice Bros (272)
    enemy_cycle = [GIANT_DRY_BONES, HAMMER_BRO, DRY_BONES, COOLIGAN,
                   SWOOP, HAMMER_BRO, GIANT_DRY_BONES, DRY_BONES]
    
    for suffix in ['33', '34', '35']:
        fname = f'03-{suffix}.arc'
        src = f'extracted files/Stage/{fname}'
        dst = f'output/ChaosStation/Stage/{fname}'
        
        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())
        
        area = parse_course_bin(arc.get_file('course/course1.bin'))
        new_sprites = []
        enemy_idx = 0
        
        for s in area.sprites:
            if s.stype == 272:  # Ice Bro -> cycle through tougher enemies
                ns = copy.deepcopy(s)
                ns.stype = enemy_cycle[enemy_idx % len(enemy_cycle)]
                ns.spritedata = SD
                new_sprites.append(ns)
                # Add an extra enemy nearby for double trouble
                extra = copy.deepcopy(s)
                extra.x += 32
                extra.stype = SPINY
                extra.spritedata = SD
                new_sprites.append(extra)
                enemy_idx += 1
            else:
                new_sprites.append(s)
        
        area.sprites = new_sprites
        area.loaded_sprites = sorted(set(s.stype for s in new_sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area))
        
        data = arc.pack()
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(data)
        print(f'Saved: {dst} ({len(data)} bytes)')


def create_level_3_castle():
    """3-Castle: Lemmy's Icy Arena (03-24.arc).

    Preserves: Castle hazards (280), Ice Snake Blocks (166), 
    Star Coins (32), Bob-ombs (101), coins, midway, red rings.
    Replaces: Dry Bones (118) -> Mix of Giant Dry Bones, Ice Bros, and regular.
    Adds: Additional Icicles along the path, Fire Bars for extra difficulty.
    Boss room: Keep Lemmy, add 2 Dry Bones for extra chaos.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/03-24.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ═══════════ AREA 1: Castle Gauntlet ═══════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))

    from tools.sprite_db import GIANT_DRY_BONES, ICE_BRO, ICICLE

    new_sprites = []
    db_count = 0
    for s in area1.sprites:
        if s.stype == 118:
            ns = copy.deepcopy(s)
            if db_count % 3 == 0:
                ns.stype = GIANT_DRY_BONES
            elif db_count % 3 == 1:
                ns.stype = ICE_BRO
            new_sprites.append(ns)
            
            # Add an icicle above them!
            icicle = copy.deepcopy(s)
            icicle.stype = ICICLE
            icicle.y -= 120
            icicle.spritedata = b'\x00\x00\x00\x00\x00\x00'
            new_sprites.append(icicle)
            db_count += 1
        else:
            new_sprites.append(s)

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ═══════════ AREA 2: Boss Room (Lemmy) ═══════════
    # Boss area in Zone 1: x=3488 y=1360 w=544 h=272
    # The actual floor where Lemmy fights is around X=3584 to 3936.
    # The sides (X < 3584 and X > 3936) are bottomless pits. 
    # Ceiling is around Y=1360 or 1400. Floor is Y=1584.
    
    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_SD = b'\x00\x00\x00\x00\x00\x0B' # Fire bar, 11 blocks long!
    FB_SD_CCW = b'\x00\x00\x00\x00\x10\x0B' # Counter-clockwise
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)

    from tools.sprite_db import GIANT_DRY_BONES, FIRE_BAR
    
    # Add two massive rotating Fire Bars suspended from the ceiling to deny air superiority.
    boss_sprites.append(Sprite(stype=FIRE_BAR, x=3648, y=1430,
                               spritedata=FB_SD, zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=FIRE_BAR, x=3872, y=1430,
                               spritedata=FB_SD_CCW, zone_id=0, extra_byte=0))

    # Flank Lemmy with Giant Dry Bones, placed safely on the solid floor 
    # (avoiding the holes at edges).
    boss_sprites.append(Sprite(stype=GIANT_DRY_BONES, x=3616, y=1568,
                               spritedata=SD, zone_id=0, extra_byte=0))
    boss_sprites.append(Sprite(stype=GIANT_DRY_BONES, x=3904, y=1568,
                               spritedata=SD, zone_id=0, extra_byte=0))

    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/03-24.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/03-24.arc ({len(data)} bytes)')


def create_level_4_1():
    """Create 4-1: Tropical Coast — Beach island hopping gauntlet.
    Expanded to match vanilla level length (~527 tiles).
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)

    a.set_tileset(1, db.TILESET_OCEAN)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(500)

    # Zone matches vanilla 04-01 length (8432px). I'll make it 8500 to be safe.
    a.add_zone(0, 0, 8500, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0)

    # Water fill MUST be at the bottom, not Y=0. 
    # Let's put the water surface at Y=28*16 (448px), beneath the islands.
    a.add_sprite(db.WATER_FILL, 0, 28*16, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # Entrances
    a.add_entrance(0, 32, 384)
    a.add_entrance(1, 250*16, 25*16)  # Midway respawn

    GY = 26  # ground Y

    # ═══ ISLAND 1: Starting Beach (0-40) ═══
    # Varied terrain! Not just flat.
    a.add_ground(0, GY, 15, 4, tileset=1)
    a.add_ground(15, GY-2, 10, 6, tileset=1)  # Hill
    a.add_ground(25, GY, 15, 4, tileset=1)

    # Scenery / Enemies
    a.add_sprite(db.GOOMBA, 18*16, (GY-3)*16)
    a.add_sprite(db.GOOMBA, 22*16, (GY-3)*16)
    a.add_sprite(db.KOOPA, 32*16, (GY-1)*16)

    a.add_coin_line(16, GY-5, 4)
    a.add_coin_line(26, GY-3, 5)

    a.add_question_block(12, GY-4, contents=1)  # Mushroom

    # ★ Star Coin 1 — On top of the hill
    a.add_star_coin(20, GY-6, coin_num=0)

    # ═══ GAP 1: Water Skimming (40-60) ═══
    # Stepping stones over the water
    a.add_ground(44, GY+1, 3, 2, tileset=1)
    a.add_ground(52, GY+1, 3, 2, tileset=1)
    
    # Cheep Cheeps jumping OUT of the water
    a.add_sprite(db.CHEEP_CHEEP, 48*16, 32*16)
    a.add_sprite(db.CHEEP_CHEEP, 56*16, 32*16)

    # ═══ ISLAND 2: Urchin Shore (60-120) ═══
    a.add_ground(60, GY, 10, 4, tileset=1)
    # Gap 70-75
    a.add_ground(75, GY, 5, 4, tileset=1)
    
    a.add_sprite(db.PORCU_PUFFER, 72*16, 28*16) # In the gap!
    
    a.add_ground(83, GY+2, 5, 2, tileset=1)  # Low dip near water
    a.add_ground(92, GY, 25, 4, tileset=1)

    a.add_sprite(db.KOOPA, 65*16, (GY-1)*16)
    a.add_sprite(db.URCHIN, 77*16, (GY-1)*16)
    
    a.add_sprite(db.URCHIN, 85*16, (GY+1)*16)  # In the dip
    a.add_sprite(db.CHEEP_CHEEP, 89*16, 32*16) # Jumping out of dip
    
    a.add_sprite(db.KOOPA, 95*16, (GY-1)*16)
    a.add_sprite(db.URCHIN, 100*16, (GY-1)*16)
    a.add_sprite(db.URCHIN, 105*16, (GY-1)*16)
    a.add_sprite(db.URCHIN, 110*16, (GY-1)*16)

    # Blocks to jump
    a.add_brick_block(76, GY-4, contents=10)
    a.add_brick_block(77, GY-4, contents=0)

    a.add_question_block(95, GY-4, contents=0)  # Coin

    # ═══ GAP 2: Platforms & Pipes (120-150) ═══
    # Pipes acting as stepping stones
    a.add_pipe(125, GY, height=4, tileset=0)
    a.add_pipe(135, GY-1, height=5, tileset=0)
    a.add_pipe(145, GY, height=4, tileset=0)

    a.add_sprite(db.PIPE_PIRANHA_UP, 126*16, (GY-1)*16)
    a.add_sprite(db.PIPE_PIRANHA_UP, 136*16, (GY-2)*16)
    a.add_sprite(db.PIPE_PIRANHA_UP, 146*16, (GY-1)*16)

    a.add_coin_line(129, GY-3, 5)
    a.add_coin_line(139, GY-3, 5)

    # ═══ ISLAND 3: Koopa Troop (150-200) ═══
    a.add_ground(150, GY, 12, 4, tileset=1)
    a.add_ground(165, GY-4, 15, 8, tileset=1)  # Big Mesa hovering
    a.add_ground(185, GY, 15, 4, tileset=1)

    # Gap between 162 and 165, and 180 and 185
    a.add_sprite(db.CHEEP_CHOMP, 170*16, 30*16)  # Dangerous pursuit

    a.add_sprite(db.KOOPA, 155*16, (GY-1)*16)
    a.add_sprite(db.KOOPA, 170*16, (GY-5)*16)
    a.add_sprite(db.KOOPA, 175*16, (GY-5)*16)
    a.add_sprite(db.KOOPA, 190*16, (GY-1)*16)

    a.add_question_block(160, GY-4, contents=0)

    # ★ Star Coin 2 — Under the mesa overhang (tricky execution required over Cheep Chomp)
    a.add_ground(172, GY+1, 3, 2, tileset=1) # Tiny stepping stone below mesa
    a.add_star_coin(173, GY-2, coin_num=1)

    # ═══ GAP 3: Blooper Bay Jump (200-230) ═══
    a.add_ground(205, GY+1, 4, 2, tileset=1)
    a.add_ground(215, GY-1, 4, 3, tileset=1)
    a.add_ground(225, GY+1, 4, 2, tileset=1)

    a.add_sprite(db.CHEEP_CHEEP, 210*16, 32*16)
    a.add_sprite(db.CHEEP_CHEEP, 220*16, 32*16)
    a.add_sprite(db.BLOOPER, 215*16, 25*16)  # Flying blooper!

    # ═══ ISLAND 4: Midway Rest (230-260) ═══
    a.add_ground(230, GY, 30, 4, tileset=1)

    a.add_sprite(db.MIDWAY_FLAG, 250*16, (GY-1)*16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    a.add_sprite(db.KOOPA, 235*16, (GY-1)*16)

    # Post-midway mushroom
    a.add_question_block(245, GY-4, contents=1)

    # ═══ GAP 4: Porcu-Puffer Chase (260-310) ═══
    # Small fast platforms over water
    a.add_ground(265, GY+1, 3, 2, tileset=1)
    a.add_ground(275, GY, 3, 2, tileset=1)
    a.add_ground(285, GY+1, 3, 2, tileset=1)
    a.add_ground(295, GY-1, 3, 2, tileset=1)
    a.add_ground(305, GY+1, 3, 2, tileset=1)

    a.add_sprite(db.PORCU_PUFFER, 275*16, 28*16)  # Aggressive fish!

    a.add_coin_line(268, GY-3, 5)
    a.add_coin_line(288, GY-3, 5)

    # ═══ ISLAND 5: Piranha Hill (310-380) ═══
    # Disconnected islands instead of a wide strip
    a.add_ground(310, GY, 10, 4, tileset=1)
    
    a.add_ground(325, GY-3, 8, 7, tileset=1)
    a.add_ground(345, GY-3, 8, 7, tileset=1)
    a.add_ground(365, GY-3, 8, 7, tileset=1)

    a.add_pipe(328, GY-3, height=3, tileset=0)
    a.add_sprite(db.PIPE_PIRANHA_UP, 329*16, (GY-6)*16)

    a.add_pipe(348, GY-3, height=3, tileset=0)
    a.add_sprite(db.PIPE_PIRANHA_UP, 349*16, (GY-6)*16)

    a.add_pipe(368, GY-3, height=3, tileset=0)
    a.add_sprite(db.PIPE_PIRANHA_UP, 369*16, (GY-6)*16)

    a.add_sprite(db.KOOPA, 315*16, (GY-1)*16)

    # Jumping fish between the separated piranha islands
    a.add_sprite(db.CHEEP_CHEEP, 338*16, 32*16)
    a.add_sprite(db.CHEEP_CHEEP, 358*16, 32*16)

    # ═══ GAP 5: Fishbone Shallows (380-430) ═══
    a.add_ground(390, GY+1, 4, 2, tileset=1)
    a.add_ground(405, GY-1, 4, 3, tileset=1)
    a.add_ground(420, GY+1, 4, 2, tileset=1)

    a.add_sprite(db.CHEEP_CHEEP, 397*16, 32*16)
    a.add_sprite(db.FISHBONE, 400*16, 26*16)  # Flying fishbone
    a.add_sprite(db.CHEEP_CHEEP, 412*16, 32*16)
    a.add_sprite(db.FISHBONE, 415*16, 26*16)

    a.add_coin_line(393, GY-3, 5)
    a.add_coin_line(408, GY-4, 5)

    # ★ Star Coin 3 — Right above a jumping Cheep
    a.add_star_coin(412, GY-5, coin_num=2)

    # ═══ ISLAND 6: Sprint to Goal (430-530) ═══
    a.add_ground(430, GY, 100, 4, tileset=1)

    # Enemy gauntlet
    a.add_sprite(db.KOOPA, 440*16, (GY-1)*16)
    a.add_sprite(db.GOOMBA, 450*16, (GY-1)*16)
    a.add_sprite(db.URCHIN, 460*16, (GY-1)*16)
    a.add_sprite(db.KOOPA, 470*16, (GY-1)*16)
    a.add_sprite(db.GOOMBA, 480*16, (GY-1)*16)

    # Classic Super Mario staircase
    a.add_staircase(495, GY, 8, direction=1, tileset=1)

    # Goal pole at X = 506*16 = 8096, well inside the 8500 zone width
    a.add_sprite(db.GOAL_POLE, 506*16, 12*16)

    # Flag base block
    a.add_ground(505, GY, 3, 4, tileset=1)

    # Save
    builder.save('output/ChaosStation/Stage/04-01.arc')
    print("Created 4-1: Tropical Coast")


def create_level_4_2():
    """Level 4-2: Jellyfish Depths — Full underwater swimming gauntlet.

    A deep ocean dive through coral reefs, Blooper-infested alleys, and
    Fishbone-haunted trenches. The entire level is submerged.

    Layout:
      §1 Shallow Reef       — gentle coral swim with Cheep Cheeps
      §2 Blooper Alley      — narrow corridors, Bloopers patrol
      §3 Fishbone Trench    — deep trench with homing Fishbones
      §4 Urchin Forest      — dense coral pillars guarded by Urchins
      §5 Goal Ascent        — swim upward to the surface flagpole
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)

    a.set_tileset(1, db.TILESET_OCEAN)
    a.set_background(bg2=db.BG_UNDERWATER)
    a.set_time(400)

    # Zone: matches vanilla length (~488 tiles = 7808px)
    a.add_zone(0, 0, 7800, 640, zone_id=0, music=db.MUSIC_UNDERWATER, cam_mode=0)

    # Fill the ENTIRE zone with water
    a.add_sprite(db.WATER_FILL, 0, 0, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # Entrance — start swimming!
    a.add_entrance(0, 16, 320)
    a.add_entrance(1, 240*16, (34)*16)  # Midway respawn

    TX = 0
    GY = 36   # ocean floor Y

    # ════════════════════════════════════════════════════
    #   §1 — Shallow Reef (TX to TX+60)
    # ════════════════════════════════════════════════════
    a.add_ground(TX, GY, 60, 6, tileset=1)
    a.add_ground(TX, 0, 60, 5, tileset=1)  # ceiling

    # Coral pillars
    a.add_ground(TX+8,  GY-5,  2, 5, tileset=1)
    a.add_ground(TX+16, GY-8,  2, 8, tileset=1)
    a.add_ground(TX+24, GY-4,  2, 4, tileset=1)
    a.add_ground(TX+32, GY-6,  3, 6, tileset=1)
    a.add_ground(TX+42, GY-7,  2, 7, tileset=1)
    a.add_ground(TX+52, GY-5,  2, 5, tileset=1)

    # Cheep Cheeps
    a.add_sprite(db.CHEEP_CHEEP, 10*16, 28*16)
    a.add_sprite(db.CHEEP_CHEEP, 20*16, 24*16)
    a.add_sprite(db.CHEEP_CHEEP, 36*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 48*16, 26*16)

    a.add_coin_line(5, 28, 8)
    a.add_coin_line(18, 22, 5)
    a.add_coin_line(30, 26, 6)
    a.add_coin_line(44, 24, 6)

    a.add_question_block(12, 25, contents=1)  # Mushroom
    a.add_question_block(38, 22, contents=0)  # Coin

    # ★ Star Coin 1 — behind the tallest coral pillar
    a.add_star_coin(17, GY-2, coin_num=0)

    # ════════════════════════════════════════════════════
    #   §2 — Coral Cavern (TX+63 to TX+120)
    # ════════════════════════════════════════════════════
    a.add_ground(TX+63, GY, 57, 6, tileset=1)
    a.add_ground(TX+63, 0, 57, 6, tileset=1)  # lower ceiling

    # Tight cave passages with coral walls
    a.add_ground(TX+72, GY-14, 3, 6, tileset=1)  # Stalactite 1
    a.add_ground(TX+72, GY-4,  3, 4, tileset=1)  # Stalagmite 1

    a.add_ground(TX+84, GY-16, 3, 8, tileset=1)  # Stalactite 2
    a.add_ground(TX+84, GY-3,  3, 3, tileset=1)  # Stalagmite 2

    a.add_ground(TX+96, GY-14, 3, 6, tileset=1)  # Stalactite 3
    a.add_ground(TX+96, GY-4,  3, 4, tileset=1)  # Stalagmite 3

    a.add_ground(TX+108, GY-16, 3, 8, tileset=1) # Stalactite 4
    a.add_ground(TX+108, GY-3,  3, 3, tileset=1) # Stalagmite 4

    # Bloopers in the corridors
    a.add_sprite(db.BLOOPER, 78*16, 22*16)
    a.add_sprite(db.BLOOPER, 90*16, 20*16)
    a.add_sprite(db.BLOOPER, 102*16, 24*16)
    a.add_sprite(db.BLOOPER_NANNY, 114*16, 22*16)

    # Spike the difficulty: Urchins on the stalactites and stalagmites!
    a.add_sprite(db.URCHIN, 73*16, (GY-15)*16)
    a.add_sprite(db.URCHIN, 73*16, (GY-5)*16)
    a.add_sprite(db.URCHIN, 85*16, (GY-17)*16)
    a.add_sprite(db.URCHIN, 85*16, (GY-4)*16)
    a.add_sprite(db.URCHIN, 97*16, (GY-15)*16)
    a.add_sprite(db.URCHIN, 97*16, (GY-5)*16)
    a.add_sprite(db.URCHIN, 109*16, (GY-17)*16)
    a.add_sprite(db.URCHIN, 109*16, (GY-4)*16)

    a.add_sprite(db.CHEEP_CHEEP, 80*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 100*16, 28*16)

    a.add_coin_line(68, 24, 4)
    a.add_coin_line(78, 20, 3)
    a.add_coin_line(88, 24, 4)
    a.add_coin_line(98, 20, 3)
    a.add_coin_line(110, 24, 4)

    a.add_question_block(82, 26, contents=0)  # Coin
    a.add_question_block(104, 18, contents=0)  # Coin

    # ════════════════════════════════════════════════════
    #   §3 — Blooper Highway (TX+123 to TX+185)
    # ════════════════════════════════════════════════════
    a.add_ground(TX+123, GY, 62, 6, tileset=1)
    a.add_ground(TX+123, 0, 62, 4, tileset=1)  # ceiling

    # Open water with scattered obstacles
    a.add_ground(TX+135, GY-6,  3, 6, tileset=1)
    a.add_ground(TX+148, GY-9,  2, 9, tileset=1)
    a.add_ground(TX+160, GY-5,  3, 5, tileset=1)
    a.add_ground(TX+172, GY-8,  2, 8, tileset=1)

    # Blooper swarm!
    a.add_sprite(db.BLOOPER, 130*16, 18*16)
    a.add_sprite(db.BLOOPER, 140*16, 24*16)
    a.add_sprite(db.BLOOPER, 152*16, 20*16)
    a.add_sprite(db.BLOOPER_NANNY, 165*16, 22*16)
    a.add_sprite(db.BLOOPER, 178*16, 26*16)

    # Urchin obstacles forcing tight swimming while dodging Bloopers
    a.add_sprite(db.URCHIN, 136*16, (GY-7)*16)
    a.add_sprite(db.URCHIN, 149*16, (GY-10)*16)
    a.add_sprite(db.URCHIN, 161*16, (GY-6)*16)
    a.add_sprite(db.URCHIN, 173*16, (GY-9)*16)

    # Big Cheep Cheep patrolling
    a.add_sprite(db.BIG_CHEEP_CHEEP, 155*16, 30*16)

    a.add_coin_line(128, 24, 6)
    a.add_coin_line(142, 20, 5)
    a.add_coin_line(156, 26, 4)
    a.add_coin_line(168, 22, 5)

    # Red Coin Ring — underwater challenge!
    a.add_red_coin_ring(145, 16, pattern='circle')

    # ════════════════════════════════════════════════════
    #   §4 — Fishbone Abyss (TX+188 to TX+250)
    # ════════════════════════════════════════════════════
    # Floor drops — deep trench!
    a.add_ground(TX+188, GY+2, 62, 4, tileset=1)
    a.add_ground(TX+188, 0, 62, 3, tileset=1)

    # Rocky outcrops
    a.add_ground(TX+198, GY-3, 3, 5, tileset=1)
    a.add_ground(TX+212, GY-6, 2, 8, tileset=1)
    a.add_ground(TX+226, GY-4, 3, 6, tileset=1)
    a.add_ground(TX+238, GY-5, 2, 7, tileset=1)

    # Fishbones — homing skeleton fish!
    a.add_sprite(db.FISHBONE, 195*16, 26*16)
    a.add_sprite(db.FISHBONE, 206*16, 22*16)
    a.add_sprite(db.FISHBONE, 218*16, 28*16)
    a.add_sprite(db.FISHBONE, 230*16, 24*16)
    a.add_sprite(db.FISHBONE, 242*16, 26*16)

    # Cheep Cheeps weaving through
    a.add_sprite(db.CHEEP_CHEEP, 202*16, 32*16)
    a.add_sprite(db.CHEEP_CHEEP, 222*16, 30*16)
    a.add_sprite(db.BIG_CHEEP_CHEEP, 235*16, 32*16)

    a.add_coin_line(192, 26, 5)
    a.add_coin_line(208, 20, 3)
    a.add_coin_line(220, 26, 5)
    a.add_coin_line(234, 22, 4)

    # Midway flag — halfway through the level
    a.add_sprite(db.MIDWAY_FLAG, 240*16, (GY+1)*16,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ★ Star Coin 2 — deep in the trench behind an outcrop
    a.add_star_coin(227, GY+1, coin_num=1)

    # ════════════════════════════════════════════════════
    #   §5 — Porcu-Puffer Domain (TX+253 to TX+315)
    # ════════════════════════════════════════════════════
    a.add_ground(TX+253, GY, 62, 6, tileset=1)
    a.add_ground(TX+253, 0, 62, 5, tileset=1)

    # Open water — Porcu-Puffer hunts you!
    a.add_ground(TX+268, GY-5, 3, 5, tileset=1)
    a.add_ground(TX+282, GY-7, 2, 7, tileset=1)
    a.add_ground(TX+296, GY-4, 3, 4, tileset=1)

    a.add_sprite(db.PORCU_PUFFER, 270*16, 24*16)
    a.add_sprite(db.CHEEP_CHEEP, 260*16, 28*16)
    a.add_sprite(db.CHEEP_CHEEP, 278*16, 20*16)
    a.add_sprite(db.CHEEP_CHEEP, 290*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 308*16, 26*16)

    a.add_coin_line(258, 24, 8)
    a.add_coin_line(275, 20, 6)
    a.add_coin_line(292, 26, 6)
    a.add_coin_line(306, 22, 5)

    a.add_question_block(265, 22, contents=1)  # Mushroom
    a.add_question_block(300, 24, contents=0)  # Coin

    # ════════════════════════════════════════════════════
    #   §6 — Urchin Labyrinth (TX+318 to TX+385)
    # ════════════════════════════════════════════════════
    a.add_ground(TX+318, GY, 67, 6, tileset=1)
    a.add_ground(TX+318, 0, 67, 4, tileset=1)

    # Dense coral forest — the hardest section
    a.add_ground(TX+326, GY-10, 2, 10, tileset=1)
    a.add_ground(TX+334, GY-8,  2, 8, tileset=1)
    a.add_ground(TX+342, GY-12, 2, 12, tileset=1)
    a.add_ground(TX+350, GY-6,  2, 6, tileset=1)
    a.add_ground(TX+358, GY-11, 2, 11, tileset=1)
    a.add_ground(TX+366, GY-7,  2, 7, tileset=1)
    a.add_ground(TX+374, GY-10, 2, 10, tileset=1)

    # Urchins guarding each passage — DOUBLED in density
    a.add_sprite(db.URCHIN, 326*16, 24*16)
    a.add_sprite(db.URCHIN, 330*16, 24*16)
    
    a.add_sprite(db.URCHIN, 334*16, 28*16)
    a.add_sprite(db.URCHIN, 338*16, 28*16)
    
    a.add_sprite(db.URCHIN, 342*16, 20*16)
    a.add_sprite(db.URCHIN, 346*16, 20*16)
    
    a.add_sprite(db.URCHIN, 350*16, 26*16)
    a.add_sprite(db.URCHIN, 354*16, 26*16)
    
    a.add_sprite(db.URCHIN, 358*16, 22*16)
    a.add_sprite(db.URCHIN, 362*16, 22*16)
    
    a.add_sprite(db.URCHIN, 366*16, 28*16)
    a.add_sprite(db.URCHIN, 370*16, 28*16)
    
    a.add_sprite(db.URCHIN, 374*16, 24*16)
    a.add_sprite(db.URCHIN, 378*16, 24*16)

    a.add_coin_line(328, 20, 2)
    a.add_coin_line(336, 24, 2)
    a.add_coin_line(344, 16, 2)
    a.add_coin_line(352, 22, 2)
    a.add_coin_line(360, 18, 2)
    a.add_coin_line(368, 24, 2)
    a.add_coin_line(376, 20, 2)

    # ? block with mushroom between Urchins — risky grab
    a.add_question_block(348, 26, contents=1)  # Mushroom

    # ════════════════════════════════════════════════════
    #   §7 — Cheep Chomp Chase (TX+388 to TX+435)
    # ════════════════════════════════════════════════════
    a.add_ground(TX+388, GY, 47, 6, tileset=1)
    a.add_ground(TX+388, 0, 47, 5, tileset=1)

    # Scattered cover
    a.add_ground(TX+400, GY-6, 3, 6, tileset=1)
    a.add_ground(TX+415, GY-8, 2, 8, tileset=1)
    a.add_ground(TX+428, GY-5, 3, 5, tileset=1)

    # Cheep Chomp — giant pursuing fish!
    a.add_sprite(db.CHEEP_CHOMP, 395*16, 24*16)

    a.add_sprite(db.FISHBONE, 405*16, 28*16)
    a.add_sprite(db.FISHBONE, 420*16, 22*16)
    a.add_sprite(db.CHEEP_CHEEP, 410*16, 18*16)

    a.add_coin_line(392, 22, 6)
    a.add_coin_line(408, 18, 5)
    a.add_coin_line(424, 24, 4)

    # ★ Star Coin 3 — high up, risky with Cheep Chomp chasing
    a.add_star_coin(418, 10, coin_num=2)

    # ════════════════════════════════════════════════════
    #   §8 — Goal Ascent (TX+438 to TX+480)
    # ════════════════════════════════════════════════════
    # Rising floor toward the surface
    a.add_ground(TX+438, GY-4, 20, 10, tileset=1)

    # Final island above water for goal pole
    a.add_ground(TX+434, 20, 64, 2, tileset=1)   # Shifted left and extended
    a.add_ground(TX+434, 22, 64, 20, tileset=1)

    # Staircase to goal
    a.add_staircase(TX+450, 19, 6, direction=1, tileset=1)

    # Last enemies
    a.add_sprite(db.CHEEP_CHEEP, 420*16, 22*16)
    a.add_sprite(db.BLOOPER, 428*16, 18*16)
    a.add_sprite(db.CHEEP_CHEEP, 438*16, 16*16)

    a.add_coin_line(416, 20, 8)
    a.add_coin_line(431, 16, 6)

    # Goal pole on the surface island, safely away from zone edge
    a.add_sprite(db.GOAL_POLE, 460*16, 8*16)

    builder.save('output/ChaosStation/Stage/04-02.arc')
    print("Created 4-2: Jellyfish Depths")


def create_level_4_3():
    """Level 4-3: Barrel Roll Rapids — Athletic river gauntlet.
    
    A fast-paced platforming level over a treacherous river. You must jump
    across small islands, floating logs, and dodge jumping Cheep Cheeps
    and the massive pursuing Cheep Chomps.
    
    Power-ups are strictly limited per user request:
    - 1 Mushroom early in the level.
    - 1 Mushroom post-midway.
    - NO Stars, NO Fire Flowers.
    
    Length: ~500 tiles (8000px) to match vanilla.
    """
    from tools.level_builder import LevelBuilder, StandardObjs, GrassObjs
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)

    a.set_tileset(1, db.TILESET_OCEAN)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(500)

    # Zone matches vanilla 04-03 total width (~8000px)
    a.add_zone(0, 0, 8000, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0)

    # Fill bottom with deadly water
    a.add_sprite(db.WATER_FILL, 0, 26*16, spritedata=b'\x01\x00\x02\x00\x00\x00')

    # Entrances
    a.add_entrance(0, 16, 320)
    a.add_entrance(1, 230*16, 20*16)  # Midway respawn

    GY = 24  # Default floor Y

    JG_TOP = GrassObjs.GROUND_TOP

    # ════════════════════════════════════════════════════
    #   §1 — Riverbank Start (0 to 40)
    # ════════════════════════════════════════════════════
    a.add_ground(0, GY, 40, 6, tileset=1)

    a.add_sprite(db.GOOMBA, 12*16, (GY-1)*16)
    a.add_sprite(db.KOOPA, 24*16, (GY-1)*16)

    a.add_coin_line(15, GY-3, 5)

    # First mushroom
    a.add_question_block(20, GY-4, contents=0)  # Coin
    a.add_question_block(30, GY-4, contents=1)  # Mushroom

    # ★ Star Coin 1
    a.add_star_coin(38, GY-5, coin_num=0)

    # ════════════════════════════════════════════════════
    #   §2 — Stepping Stones & Cheeps (45 to 110)
    # ════════════════════════════════════════════════════
    # Log-like small platforms
    a.add_ground(45, GY, 3, 2, tileset=1)
    a.add_ground(52, GY-2, 3, 3, tileset=1)
    a.add_ground(60, GY, 3, 2, tileset=1)
    a.add_ground(68, GY+2, 4, 2, tileset=1)
    a.add_ground(78, GY-1, 3, 2, tileset=1)
    a.add_ground(88, GY-3, 3, 3, tileset=1)
    a.add_ground(96, GY, 5, 2, tileset=1)

    # Cheep Cheeps jumping from gaps
    a.add_sprite(db.CHEEP_CHEEP, 49*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 57*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 65*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 74*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 84*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 93*16, 30*16)

    a.add_coin_line(50, GY-4, 3)
    a.add_coin_line(80, GY-3, 3)

    # ════════════════════════════════════════════════════
    #   §3 — Barrel Run (115 to 175)
    # ════════════════════════════════════════════════════
    a.add_ground(110, GY-1, 65, 4, tileset=1)

    # Add barrels to pick up and throw
    a.add_sprite(db.BARREL, 120*16, (GY-2)*16)
    a.add_sprite(db.BARREL, 140*16, (GY-2)*16)
    a.add_sprite(db.BARREL, 160*16, (GY-2)*16)

    a.add_sprite(db.KOOPA, 130*16, (GY-2)*16)
    a.add_sprite(db.GOOMBA, 150*16, (GY-2)*16)

    a.add_question_block(135, GY-5, contents=0)  # Coin
    a.add_question_block(155, GY-5, contents=0)  # Coin

    # ★ Star Coin 2
    a.add_star_coin(165, GY-5, coin_num=1)

    # ════════════════════════════════════════════════════
    #   §4 — Cheep Chomp Chase 1 (180 to 225)
    # ════════════════════════════════════════════════════
    a.add_ground(180, GY, 3, 2, tileset=1)

    # Cheep Chomp spawns in water
    a.add_sprite(db.CHEEP_CHOMP, 185*16, 30*16)

    # Frantic jumping pillars
    a.add_ground(188, GY-2, 3, 3, tileset=1)
    a.add_ground(196, GY, 3, 2, tileset=1)
    a.add_ground(204, GY+2, 3, 2, tileset=1)
    a.add_ground(212, GY-1, 3, 2, tileset=1)
    a.add_ground(220, GY-3, 3, 3, tileset=1)

    a.add_coin_line(189, GY-4, 3)
    a.add_coin_line(205, GY-1, 3)

    # ════════════════════════════════════════════════════
    #   §5 — Midway Island (230 to 260)
    # ════════════════════════════════════════════════════
    a.add_ground(230, GY, 30, 4, tileset=1)

    a.add_sprite(db.MIDWAY_FLAG, 240*16, (GY-1)*16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # The SECOND and FINAL power-up
    a.add_question_block(250, GY-4, contents=1)  # Mushroom

    # ════════════════════════════════════════════════════
    #   §6 — Bob-omb Bridges (265 to 330)
    # ════════════════════════════════════════════════════
    # Log bridges with Bob-ombs
    a.add_ground(265, GY-2, 10, 2, tileset=1)
    a.add_ground(280, GY-4, 12, 2, tileset=1)
    a.add_ground(298, GY-1, 15, 2, tileset=1)
    a.add_ground(318, GY-3, 12, 2, tileset=1)

    a.add_sprite(db.BOB_OMB, 270*16, (GY-3)*16)
    a.add_sprite(db.BOB_OMB, 285*16, (GY-5)*16)
    a.add_sprite(db.BOB_OMB, 305*16, (GY-2)*16)
    a.add_sprite(db.BOB_OMB, 325*16, (GY-4)*16)

    a.add_sprite(db.CHEEP_CHEEP, 276*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 295*16, 30*16)
    a.add_sprite(db.CHEEP_CHEEP, 315*16, 30*16)

    a.add_question_block(288, GY-8, contents=0)  # Coin
    a.add_question_block(308, GY-5, contents=0)  # Coin

    # ════════════════════════════════════════════════════
    #   §7 — Cheep Chomp Chase 2 (335 to 400)
    # ════════════════════════════════════════════════════
    # Harder pursuit!
    a.add_ground(335, GY, 4, 3, tileset=1)

    a.add_sprite(db.CHEEP_CHOMP, 342*16, 30*16)

    a.add_ground(345, GY+1, 2, 2, tileset=1)
    a.add_ground(352, GY-3, 2, 3, tileset=1)
    a.add_ground(358, GY-1, 2, 2, tileset=1)
    a.add_ground(364, GY+2, 2, 2, tileset=1)
    a.add_ground(372, GY-3, 2, 3, tileset=1)
    a.add_ground(378, GY-5, 2, 3, tileset=1)
    a.add_ground(385, GY-1, 2, 2, tileset=1)
    a.add_ground(391, GY+1, 2, 2, tileset=1)

    # ★ Star Coin 3 — hanging high, risky jump over Cheep Chomp
    a.add_star_coin(380, GY-8, coin_num=2)

    # ════════════════════════════════════════════════════
    #   §8 — Rapids End & Goal (400 to 500)
    # ════════════════════════════════════════════════════
    a.add_ground(400, GY, 100, 6, tileset=1)  # Extended ground!

    a.add_sprite(db.KOOPA, 410*16, (GY-1)*16)
    a.add_sprite(db.GOOMBA, 420*16, (GY-1)*16)
    a.add_sprite(db.BOB_OMB, 430*16, (GY-1)*16)

    a.add_coin_line(405, GY-3, 5)
    a.add_coin_line(425, GY-3, 5)

    a.add_staircase(440, GY-1, 6, direction=1, tileset=1)
    
    a.add_sprite(db.GOAL_POLE, 450*16, 11*16)

    builder.save('output/ChaosStation/Stage/04-03.arc')
    print("Created 4-3: Barrel Roll Rapids")


def create_level_4_4():
    """Level 4-4: Mangrove Maze — Poison swamp and pipe jungle.
    
    A dense, claustrophobic level built over deadly poison water.
    Players must jump across thick pipe structures, avoiding Piranha Plants
    and patrolling Bramballs.
    
    Power-ups strictly limited: 2 Mushrooms total.
    Length: ~450 tiles (7200px)
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)

    # I'll use TILESET_STANDARD (grass) combined with jungle elements.
    a.set_tileset(1, db.TILESET_STANDARD)
    a.set_background(bg2=db.BG_UNDERGROUND) # Darker mood
    a.set_time(500)

    # Zone extended to fit the goal area
    a.add_zone(0, 0, 7800, 640, zone_id=0, music=db.MUSIC_UNDERGROUND, cam_mode=0)

    # Poison water fill at the bottom (instant death)
    a.add_sprite(db.POISON_FILL, 0, 26*16, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # Entrances
    a.add_entrance(0, 32, 352)
    a.add_entrance(1, 230*16, 20*16)  # Midway respawn

    GY = 24  # Ground baseline Y

    # ════════════════════════════════════════════════════
    #   §1 — The Swamp Edge (0 to 45)
    # ════════════════════════════════════════════════════
    a.add_ground(0, GY, 25, 6, tileset=0)
    
    # First pipe obstacle
    a.add_pipe(15, GY-3, height=3, tileset=0)
    a.add_sprite(db.PIPE_PIRANHA_UP, 16*16, (GY-6)*16)
    
    a.add_sprite(db.GOOMBA, 20*16, (GY-1)*16)
    
    # Gap over poison
    a.add_pipe(30, GY+1, height=4, tileset=0)
    a.add_pipe(40, GY, height=4, tileset=0)
    
    a.add_coin_line(28, GY-3, 5)

    a.add_question_block(35, GY-4, contents=1)  # Mushroom 1!

    # ════════════════════════════════════════════════════
    #   §2 — Pipe Canopy (45 to 110)
    # ════════════════════════════════════════════════════
    a.add_ground(48, GY-2, 12, 4, tileset=0)
    
    # High pipe structure
    a.add_pipe(52, GY-6, height=4, tileset=0)
    a.add_sprite(db.PIPE_PIRANHA_UP, 53*16, (GY-9)*16)
    
    a.add_pipe(65, GY, height=6, tileset=0)
    a.add_pipe(75, GY-3, height=4, tileset=0)
    a.add_pipe(85, GY+1, height=3, tileset=0)
    a.add_pipe(95, GY-2, height=5, tileset=0)
    
    a.add_sprite(db.PIPE_PIRANHA_UP, 76*16, (GY-6)*16)
    a.add_sprite(db.PIPE_PIRANHA_UP, 96*16, (GY-5)*16)

    # Bramballs walking between pipes!
    a.add_sprite(db.BRAMBALL, 60*16, (GY-4)*16)
    a.add_sprite(db.BRAMBALL, 80*16, (GY-5)*16)

    a.add_coin_line(68, GY-5, 3)
    a.add_coin_line(88, GY-4, 3)

    # ★ Star Coin 1 — risky drop between pipes over poison
    a.add_star_coin(70, GY-2, coin_num=0)

    # ════════════════════════════════════════════════════
    #   §3 — Tangled Roots (110 to 175)
    # ════════════════════════════════════════════════════
    a.add_ground(105, GY, 70, 4, tileset=0)
    
    # Dense terrain with overhead hazards
    a.add_ground(115, GY-6, 5, 2, tileset=0)
    a.add_ground(130, GY-8, 6, 2, tileset=0)
    a.add_ground(145, GY-6, 5, 2, tileset=0)

    a.add_sprite(db.BRAMBALL, 122*16, (GY-2)*16)
    a.add_sprite(db.BRAMBALL, 138*16, (GY-2)*16)
    a.add_sprite(db.BRAMBALL, 155*16, (GY-2)*16)
    
    a.add_sprite(db.PIPE_PIRANHA_DOWN, 117*16, (GY-4)*16) # Hanging upside down!
    a.add_sprite(db.PIPE_PIRANHA_DOWN, 133*16, (GY-6)*16)

    a.add_coin_line(116, GY-2, 3)
    a.add_coin_line(131, GY-2, 4)

    a.add_brick_block(125, GY-4, contents=10) # Multi-coin
    a.add_question_block(140, GY-4, contents=0)

    # ════════════════════════════════════════════════════
    #   §4 — Poison Skimming (180 to 225)
    # ════════════════════════════════════════════════════
    # Tiny pipes barely above the poison level
    a.add_pipe(180, GY, height=2, tileset=0)
    a.add_pipe(190, GY, height=3, tileset=0)
    a.add_pipe(200, GY-1, height=4, tileset=0)
    a.add_pipe(210, GY, height=3, tileset=0)
    a.add_pipe(220, GY-1, height=4, tileset=0)
    
    # Paratroopas bouncing over gaps
    a.add_sprite(db.KOOPA_PARATROOPA, 185*16, GY*16)
    a.add_sprite(db.KOOPA_PARATROOPA, 195*16, GY*16)
    a.add_sprite(db.KOOPA_PARATROOPA, 205*16, GY*16)

    # ★ Star Coin 2 — floating low over poison
    a.add_star_coin(205, GY-3, coin_num=1)

    a.add_coin_line(182, GY-1, 5)

    # ════════════════════════════════════════════════════
    #   §5 — Midway Isle (230 to 260)
    # ════════════════════════════════════════════════════
    a.add_ground(230, GY, 30, 4, tileset=0)

    a.add_sprite(db.MIDWAY_FLAG, 240*16, (GY-1)*16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Mushroom 2 (post-midway)
    a.add_question_block(248, GY-4, contents=1)

    # ════════════════════════════════════════════════════
    #   §6 — The Piranha Gauntlet (265 to 330)
    # ════════════════════════════════════════════════════
    a.add_ground(265, GY, 65, 4, tileset=0)

    # Every 8 tiles is a pipe with a piranha!
    for p in range(275, 325, 10):
        a.add_pipe(p, GY-2, height=3, tileset=0)
        a.add_sprite(db.PIPE_PIRANHA_UP, (p+1)*16, (GY-5)*16)
        
    a.add_sprite(db.BRAMBALL, 290*16, (GY-4)*16)
    a.add_sprite(db.BRAMBALL, 310*16, (GY-4)*16)

    a.add_coin_line(280, GY-6, 3)
    a.add_coin_line(300, GY-6, 3)

    # ════════════════════════════════════════════════════
    #   §7 — Toxic Leap (335 to 400)
    # ════════════════════════════════════════════════════
    # Big gaps over poison using only floating blocks and hanging roots
    a.add_ground(340, GY-4, 4, 2, tileset=0)
    a.add_ground(352, GY-2, 4, 3, tileset=0)
    a.add_ground(365, GY-5, 4, 2, tileset=0)
    a.add_ground(378, GY-1, 4, 4, tileset=0)
    a.add_ground(390, GY-4, 4, 2, tileset=0)

    a.add_sprite(db.KOOPA_PARATROOPA, 346*16, (GY-2)*16)
    a.add_sprite(db.KOOPA_PARATROOPA, 359*16, GY*16)
    a.add_sprite(db.KOOPA_PARATROOPA, 372*16, (GY-2)*16)

    a.add_coin_line(335, GY-5, 4)
    a.add_coin_line(385, GY-2, 4)

    # ★ Star Coin 3 — high floating above a dangerous jump
    a.add_star_coin(372, GY-8, coin_num=2)

    # ════════════════════════════════════════════════════
    #   §8 — Clearing to Goal (405 to 490)
    # ════════════════════════════════════════════════════
    # Massive platform extending way past flag
    a.add_ground(405, GY, 85, 6, tileset=0)

    a.add_sprite(db.GOOMBA, 415*16, (GY-1)*16)
    a.add_sprite(db.BRAMBALL, 425*16, (GY-2)*16)
    a.add_sprite(db.GOOMBA, 435*16, (GY-1)*16)

    # Goal stairs
    a.add_staircase(440, GY-1, 6, direction=1, tileset=0)
    
    # Flag placed safely inside 7800 bounds (7800/16 = 487), and on the ground
    a.add_sprite(db.GOAL_POLE, 450*16, (GY-1)*16)

    builder.save('output/ChaosStation/Stage/04-04.arc')
    print("Created 4-4: Mangrove Maze")


def create_level_4_5():
    """Create 4-5: Piranha Tides â€” horizontal pipe gauntlet.
    Expanded to match vanilla level length (~8160px).
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    import random

    builder = LevelBuilder()
    a = builder.add_area(1)

    # Use Grass tileset and Athletic Sky background
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(500)

    # Zone matches vanilla 04-05 length roughly (8200px)
    a.add_zone(0, 0, 8200, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0)

    # Poison water fill at the bottom (y=28*16)
    a.add_sprite(db.POISON_FILL, 0, 28*16, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # Draw the starting platform. Y=22 is solid ground
    # Draw the starting platform. Y=22 is solid ground
    a.add_ground(2, 22, 8, 5, tileset=1)

    # CRITICAL: Missing Entrance 0! This is why the level crashed/killed Mario instantly.
    a.add_entrance(0, 4*16, 21*16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 250*16, 20*16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Spawn Mario (Sprite ID 10) directly on top of the entrance at Y=21
    a.add_sprite(10, 4*16, 21*16, spritedata=b'\x00\x00\x00\x00\x00\x00')

    # Add pipes and piranha plants as the main platforming element
    # We'll generate a sequence of pipes at varying heights
    curr_x = 12
    gap_min = 3
    gap_max = 5

    # Star coin counters
    star_coins_placed = 0

    while curr_x < 480: # 480 * 16 = 7680px
        # Choose pipe height (y_top)
        pipe_height = random.randint(3, 7) # 3 to 7 tiles tall
        y_top = 28 - pipe_height
        
        # Add a pipe. 
        # width = random.choice([2, 3]) # Pipes are always 2 wide natively, but we can space them out.
        # Let's just use standard 2-wide pipes.
        width = 2
        
        a.add_pipe(curr_x, y_top, pipe_height, tileset=0)
        
        # 50% chance to put a Piranha Plant inside this pipe
        if random.random() < 0.5:
            # Place PIPE_PIRANHA_UP in the middle of the pipe
            px = curr_x * 16
            py = y_top * 16 - 16
            a.add_sprite(db.PIPE_PIRANHA_UP, px, py, spritedata=b'\x00\x00\x00\x00\x00\x00')
        elif random.random() < 0.2 and star_coins_placed < 3:
            # Place a Star Coin
            sx = curr_x * 16 + 8
            sy = (y_top - 4) * 16
            a.add_sprite(db.STAR_COIN, sx, sy, spritedata=bytes([0, 0, 0, 0, star_coins_placed, 0]))
            star_coins_placed += 1
        elif random.random() < 0.3:
            # Place a Goomba or Red Koopa (spritedata=1)
            enemy = random.choice([db.GOOMBA, db.KOOPA])
            ex = curr_x * 16 + 8
            ey = y_top * 16 - 16
            
            # Red Koopa requires spritedata byte 3 to be 1
            s_data = b'\x00\x00\x00\x01\x00\x00' if enemy == db.KOOPA else b'\x00\x00\x00\x00\x00\x00'
            a.add_sprite(enemy, ex, ey, spritedata=s_data)

        # Draw a floating block or question block sometimes between pillars
        if random.random() < 0.4:
            bx = curr_x + width + gap_min // 2
            by = y_top - random.randint(1, 4)
            if random.random() < 0.3:
                a.add_question_block(bx, by, contents=0) # Coin
            else:
                a.add_brick_block(bx, by)

        # Add some Urchins or Cheep Cheeps in the water below
        if random.random() < 0.4:
            ux = (curr_x + width + gap_min // 2) * 16
            uy = 26 * 16
            a.add_sprite(db.CHEEP_CHEEP, ux, uy, spritedata=b'\x00\x00\x00\x00\x00\x00')
            
        curr_x += width + random.randint(gap_min, gap_max)

    # Midway flag around x=250
    a.add_sprite(db.MIDWAY_FLAG, 250*16, 20*16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Ensure 3 star coins exist
    while star_coins_placed < 3:
        sx = (400 + star_coins_placed*10) * 16
        sy = 15 * 16
        a.add_sprite(db.STAR_COIN, sx, sy, spritedata=bytes([0, 0, 0, 0, star_coins_placed, 0]))
        star_coins_placed += 1

    # End platform and Goal Pole
    end_x = curr_x + 2
    a.add_ground(end_x, 24, 15, 5, tileset=1)

    # Lowered the Goal Pole from Y=11 down to exactly resting on the ground at Y=23
    a.add_sprite(db.GOAL_POLE, (end_x + 8)*16, 23*16, spritedata=b'\x00\x00\x00\x00\x00\x00')

    builder.save('output/ChaosStation/Stage/04-05.arc')
    print("Created 4-5: Piranha Tides")


def create_level_4_ghost_house():
    """4-GH: Haunted Reef — flooded ghost house with secret basement exit.
    Area 1: Long swim + floating platforms (door to Area 2)
    Area 2: Vertical haunted atrium (door/pipe split to Areas 3 & 4)
    Area 3: Secret underwater basement (pipe to Area 4 secret exit)
    Area 4: The Outskirts — normal + secret Goal Poles
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin,
        Sprite, LayerObject, parse_layer_data, serialize_layer_data,
        Entrance, Zone, Bounding, Tileset
    )
    import tools.sprite_db as db

    with open('extracted files/Stage/04-21.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    # ════════════════════════════════════════════════════
    #   AREA 1 — The Flooded Foyer (Long Swim)
    # ════════════════════════════════════════════════════
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    area1.sprites.clear(); area1.layer0.clear(); area1.layer1.clear(); area1.layer2.clear()
    area1.entrances.clear(); area1.zones.clear(); area1.boundings.clear()
    area1.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_GHOST_HOUSE, slot2=db.TILESET_GRASS, slot3='')
    area1.settings.time_limit = 500
    area1.zones.append(Zone(x=256, y=256, w=3400, h=368, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=0, cam_zoom=0, visibility=36))
    area1.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0, bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0))

    def a1_spr(stype, x, y, data=b'\x00'*6):
        area1.sprites.append(Sprite(stype=stype, x=x*16, y=y*16, spritedata=data, zone_id=0, extra_byte=0))
    def a1_obj(ot, x, y, w=1, h=1):
        area1.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))

    GY = 28
    a1_spr(db.WATER_FILL, 0, 18, b'\x00\x00\x00\x00\x00\x00')
    a1_obj(db.GrassObjs.GROUND_TOP, 0, GY, 210, 1)
    a1_obj(db.GrassObjs.GROUND_FILL, 0, GY+1, 210, 4)
    area1.entrances.append(Entrance(x=2*16, y=(GY-1)*16, entrance_id=0, dest_area=0, dest_entrance=0, etype=db.ENTRANCE_NORMAL, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    a1_spr(10, 2, GY-1)

    for i, bx in enumerate(range(15, 185, 12)):
        w = (bx % 3) + 3
        y_offset = (bx % 7) + 3
        a1_obj(db.GrassObjs.GROUND_TOP, bx, GY-y_offset, w, 1)
        a1_obj(db.GrassObjs.GROUND_FILL, bx, GY-y_offset+1, w, 1)
        fish_y = GY - (bx % 5) - 1
        a1_spr(db.FISHBONE, bx + 2, fish_y)
        if i % 2 == 0:
            a1_spr(db.FISHBONE, bx + 6, fish_y - 2)
        a1_spr(db.BOO, bx, GY-y_offset-3)
        if i % 3 == 0:
            a1_spr(db.BIG_BOO, bx + 5, GY-y_offset-5)

    END_X = 195
    a1_obj(db.GrassObjs.GROUND_TOP, END_X-2, 17, 15, 1)
    a1_obj(db.GrassObjs.GROUND_FILL, END_X-2, 18, 15, 12)
    a1_spr(276, END_X, 14)
    area1.entrances.append(Entrance(x=END_X*16, y=16*16, entrance_id=1, dest_area=2, dest_entrance=0, etype=db.ENTRANCE_DOOR, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    area1.loaded_sprites = sorted(set(s.stype for s in area1.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))
    arc.set_file('course/course1_bgdatL0.bin', serialize_layer_data(area1.layer0))
    arc.set_file('course/course1_bgdatL1.bin', serialize_layer_data(area1.layer1))
    arc.set_file('course/course1_bgdatL2.bin', serialize_layer_data(area1.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 2 — The Haunted Atrium (Vertical) + Secret
    # ════════════════════════════════════════════════════
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    area2.sprites.clear(); area2.layer0.clear(); area2.layer1.clear(); area2.layer2.clear()
    area2.entrances.clear(); area2.zones.clear(); area2.boundings.clear()
    area2.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_GHOST_HOUSE, slot2=db.TILESET_GRASS, slot3='')
    area2.zones.append(Zone(x=256, y=0, w=640, h=3000, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=3, cam_zoom=0, visibility=36))
    area2.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0, bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0))

    def a2_spr(stype, x, y, data=b'\x00'*6):
        area2.sprites.append(Sprite(stype=stype, x=x*16, y=y*16, spritedata=data, zone_id=0, extra_byte=0))
    def a2_obj(ot, x, y, w=1, h=1):
        area2.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))

    BOT_Y = 175
    a2_obj(db.GrassObjs.GROUND_TOP, 16, BOT_Y, 22, 1)
    a2_obj(db.GrassObjs.GROUND_FILL, 16, BOT_Y+1, 22, 3)
    area2.entrances.append(Entrance(x=26*16, y=(BOT_Y-1)*16, entrance_id=0, dest_area=1, dest_entrance=1, etype=db.ENTRANCE_DOOR, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    a2_spr(276, 26, BOT_Y-3)

    a2_obj(db.GrassObjs.GROUND_TOP, 20, BOT_Y-4, 4, 1);  a2_spr(db.BOO, 32, BOT_Y-6)
    a2_obj(db.GrassObjs.GROUND_TOP, 28, BOT_Y-8, 3, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 24, BOT_Y-12, 4, 1); a2_spr(db.BOO, 22, BOT_Y-14)
    a2_obj(db.GrassObjs.GROUND_TOP, 16, BOT_Y-16, 5, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 22, BOT_Y-20, 4, 1); a2_spr(db.BOO, 28, BOT_Y-22)
    a2_obj(db.GrassObjs.GROUND_TOP, 30, BOT_Y-24, 3, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 26, BOT_Y-28, 4, 1); a2_spr(db.BIG_BOO, 18, BOT_Y-30)

    # Secret exit side ledge
    a2_obj(db.GrassObjs.GROUND_TOP, 34, BOT_Y-28, 12, 1)
    a2_obj(db.GrassObjs.GROUND_FILL, 34, BOT_Y-27, 12, 5)
    area2.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_ENTRY, x=42, y=BOT_Y-30, w=2, h=2))
    area2.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_BODY,  x=42, y=BOT_Y-28, w=2, h=2))
    area2.entrances.append(Entrance(x=42*16+8, y=(BOT_Y-30)*16, entrance_id=2, dest_area=3, dest_entrance=0, etype=db.ENTRANCE_PIPE_UP, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    a2_obj(db.GrassObjs.GROUND_TOP, 20, BOT_Y-32, 6, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 16, BOT_Y-37, 6, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 24, BOT_Y-42, 6, 1); a2_spr(db.BOO, 30, BOT_Y-44)
    a2_obj(db.GrassObjs.GROUND_TOP, 16, BOT_Y-47, 6, 1)
    a2_obj(db.GrassObjs.GROUND_TOP, 24, BOT_Y-52, 4, 1)

    TOP_Y = BOT_Y - 57
    a2_obj(db.GrassObjs.GROUND_TOP, 14, TOP_Y, 8, 1)
    a2_obj(db.GrassObjs.GROUND_FILL, 14, TOP_Y+1, 8, 8)
    a2_spr(276, 16, TOP_Y-3)
    area2.entrances.append(Entrance(x=16*16, y=(TOP_Y-1)*16, entrance_id=1, dest_area=4, dest_entrance=0, etype=db.ENTRANCE_DOOR, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    area2.loaded_sprites = sorted(set(s.stype for s in area2.sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))
    arc.set_file('course/course2_bgdatL0.bin', serialize_layer_data(area2.layer0))
    arc.set_file('course/course2_bgdatL1.bin', serialize_layer_data(area2.layer1))
    arc.set_file('course/course2_bgdatL2.bin', serialize_layer_data(area2.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 3 — Secret Basement (underwater)
    # ════════════════════════════════════════════════════
    area3 = parse_course_bin(arc.get_file('course/course3.bin'))
    area3.sprites.clear(); area3.layer0.clear(); area3.layer1.clear(); area3.layer2.clear()
    area3.entrances.clear(); area3.zones.clear(); area3.boundings.clear()
    area3.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_GHOST_HOUSE, slot2=db.TILESET_GRASS, slot3='')
    area3.zones.append(Zone(x=256, y=256, w=1200, h=368, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=0, cam_zoom=0, visibility=36))
    area3.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0, bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0))

    def a3_spr(stype, x, y, data=b'\x00'*6):
        area3.sprites.append(Sprite(stype=stype, x=x*16, y=y*16, spritedata=data, zone_id=0, extra_byte=0))
    def a3_obj(ot, x, y, w=1, h=1):
        area3.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))

    GY = 28
    a3_spr(db.WATER_FILL, 0, 0, b'\x00\x00\x00\x00\x00\x00')
    a3_obj(db.GrassObjs.GROUND_TOP, 16, GY, 40, 1)
    a3_obj(db.GrassObjs.GROUND_FILL, 16, GY+1, 40, 3)
    area3.entrances.append(Entrance(x=20*16+8, y=(GY-11)*16, entrance_id=0, dest_area=2, dest_entrance=2, etype=db.ENTRANCE_PIPE_DOWN, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    area3.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_BODY,  x=20, y=GY-15, w=2, h=4))
    area3.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_ENTRY, x=20, y=GY-11, w=2, h=2))
    a3_spr(db.FISHBONE, 30, GY-5)
    a3_spr(db.FISHBONE, 40, GY-3)
    a3_spr(db.URCHIN, 35, GY-6)
    a3_spr(db.URCHIN, 45, GY-4)
    area3.entrances.append(Entrance(x=50*16+8, y=(GY-2)*16, entrance_id=1, dest_area=4, dest_entrance=1, etype=db.ENTRANCE_PIPE_UP, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    area3.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_ENTRY, x=50, y=GY-2, w=2, h=2))
    area3.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_BODY,  x=50, y=GY,   w=2, h=2))

    area3.loaded_sprites = sorted(set(s.stype for s in area3.sprites))
    arc.set_file('course/course3.bin', serialize_course_bin(area3))
    arc.set_file('course/course3_bgdatL0.bin', serialize_layer_data(area3.layer0))
    arc.set_file('course/course3_bgdatL1.bin', serialize_layer_data(area3.layer1))
    arc.set_file('course/course3_bgdatL2.bin', serialize_layer_data(area3.layer2))

    # ════════════════════════════════════════════════════
    #   AREA 4 — The Outskirts (Normal + Secret Exit)
    # ════════════════════════════════════════════════════
    area4 = parse_course_bin(arc.get_file('course/course4.bin'))
    area4.sprites.clear(); area4.layer0.clear(); area4.layer1.clear(); area4.layer2.clear()
    area4.entrances.clear(); area4.zones.clear(); area4.boundings.clear()
    area4.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_GHOST_HOUSE, slot2=db.TILESET_GRASS, slot3='')
    area4.zones.append(Zone(x=256, y=256, w=4000, h=368, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=0, cam_zoom=0, visibility=36))
    area4.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0, bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0))

    def a4_spr(stype, x, y, data=b'\x00'*6):
        area4.sprites.append(Sprite(stype=stype, x=x*16, y=y*16, spritedata=data, zone_id=0, extra_byte=0))
    def a4_obj(ot, x, y, w=1, h=1):
        area4.layer1.append(LayerObject(tileset=2, obj_type=ot, x=x, y=y, w=w, h=h))

    GY = 28
    a4_obj(db.GrassObjs.GROUND_TOP, 16, GY, 60, 1)
    a4_obj(db.GrassObjs.GROUND_FILL, 16, GY+1, 60, 3)
    area4.entrances.append(Entrance(x=24*16, y=(GY-1)*16, entrance_id=0, dest_area=2, dest_entrance=1, etype=db.ENTRANCE_DOOR, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    a4_spr(276, 24, GY-3)
    a4_spr(db.GOAL_POLE, 35, GY-1)
    area4.entrances.append(Entrance(x=55*16+8, y=(GY-2)*16, entrance_id=1, dest_area=3, dest_entrance=1, etype=db.ENTRANCE_PIPE_UP, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))
    area4.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_ENTRY, x=55, y=GY-2, w=2, h=2))
    area4.layer1.append(LayerObject(tileset=0, obj_type=db.StandardObjs.PIPE_BODY,  x=55, y=GY,   w=2, h=2))
    a4_spr(db.GOAL_POLE, 65, GY-1, b'\x00\x00\x00\x01\x00\x00')

    area4.loaded_sprites = sorted(set(s.stype for s in area4.sprites))
    arc.set_file('course/course4.bin', serialize_course_bin(area4))
    arc.set_file('course/course4_bgdatL0.bin', serialize_layer_data(area4.layer0))
    arc.set_file('course/course4_bgdatL1.bin', serialize_layer_data(area4.layer1))
    arc.set_file('course/course4_bgdatL2.bin', serialize_layer_data(area4.layer2))

    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/04-21.arc', 'wb') as f:
        f.write(arc.pack())
    print("Created 4-GH: Haunted Reef (04-21.arc)")


def create_level_4_cannon():
    """4-Cannon: Coral Catapult (04-36.arc).

    Rebuilds the cannon course with a compact athletic gauntlet and
    sets the warp cannon destination to World 6.
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin,
        parse_layer_data, serialize_layer_data,
        Sprite, LayerObject, Entrance, Zone, Bounding, Tileset,
    )
    import tools.sprite_db as db

    src = 'extracted files/Stage/04-36.arc'
    dst = 'output/ChaosStation/Stage/04-36.arc'

    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 4-Cannon: couldn't open {src} - {e}")
        return

    def safe_get(path):
        try:
            return arc.get_file(path)
        except KeyError:
            return None

    area = parse_course_bin(arc.get_file('course/course1.bin'))

    area.layer0 = parse_layer_data(safe_get('course/course1_bgdatL0.bin') or b'')
    area.layer1 = parse_layer_data(safe_get('course/course1_bgdatL1.bin') or b'')
    area.layer2 = parse_layer_data(safe_get('course/course1_bgdatL2.bin') or b'')

    area.sprites.clear()
    area.entrances.clear()
    area.zones.clear()
    area.boundings.clear()
    area.layer0.clear()
    area.layer1.clear()
    area.layer2.clear()

    area.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_GRASS, slot2='', slot3='')
    area.settings.time_limit = 220

    ZX, ZY, ZW, ZH = 256, 256, 1888, 512
    area.zones.append(Zone(
        x=ZX, y=ZY, w=ZW, h=ZH, zone_id=0,
        music=db.MUSIC_ATHLETIC, cam_mode=0, cam_zoom=0, visibility=0
    ))
    area.boundings.append(Bounding(
        upper=0, lower=0, upper2=0, lower2=0,
        bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0
    ))

    SD = bytes(6)
    TX = 16
    GY = 45

    def add_ground(x, y, w, h):
        area.layer1.append(LayerObject(
            tileset=1, obj_type=db.GrassObjs.GROUND_TOP,
            x=x, y=y, w=w, h=1
        ))
        if h > 1:
            area.layer1.append(LayerObject(
                tileset=1, obj_type=db.GrassObjs.GROUND_FILL,
                x=x, y=y + 1, w=w, h=h - 1
            ))

    def spr(stype, x, y, data=SD):
        area.sprites.append(Sprite(
            stype=stype, x=x, y=y, spritedata=data,
            zone_id=0, extra_byte=0
        ))

    area.entrances.append(Entrance(
        x=(TX + 2) * 16, y=(GY - 2) * 16, entrance_id=0,
        dest_area=0, dest_entrance=0, etype=db.ENTRANCE_NORMAL, zone_id=0,
        layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0
    ))

    # Section 1: Intro runway
    add_ground(TX, GY, 12, 7)
    spr(db.COIN, (TX + 3) * 16, (GY - 2) * 16)
    spr(db.COIN, (TX + 5) * 16, (GY - 2) * 16)
    spr(db.GOOMBA, (TX + 9) * 16, (GY - 1) * 16)

    # Section 2: Rising platforms
    add_ground(TX + 15, GY - 2, 4, 5)
    add_ground(TX + 22, GY - 4, 4, 7)
    add_ground(TX + 29, GY - 1, 6, 6)
    spr(db.COIN, (TX + 18) * 16, (GY - 4) * 16)
    spr(db.COIN, (TX + 24) * 16, (GY - 6) * 16)
    spr(db.COIN, (TX + 31) * 16, (GY - 3) * 16)

    # Star Coin 1
    spr(db.STAR_COIN, (TX + 25) * 16, (GY - 9) * 16, b'\x00\x00\x00\x00\x00\x00')

    # Section 3: Bullet corridor
    add_ground(TX + 39, GY, 18, 7)
    spr(db.BULLET_BILL_LAUNCHER, (TX + 42) * 16, (GY - 1) * 16)
    spr(db.BULLET_BILL_LAUNCHER, (TX + 48) * 16, (GY - 1) * 16)
    spr(db.BULLET_BILL_LAUNCHER, (TX + 54) * 16, (GY - 1) * 16)
    spr(db.KOOPA, (TX + 52) * 16, (GY - 1) * 16, b'\x00\x00\x00\x01\x00\x00')

    # Midway near the center
    spr(db.MIDWAY_FLAG, (TX + 56) * 16, (GY - 1) * 16, b'\x00\x00\x00\x01\x00\x00')

    # Section 4: Elevated launcher weave
    add_ground(TX + 61, GY - 3, 6, 4)
    add_ground(TX + 70, GY - 6, 6, 7)
    add_ground(TX + 79, GY - 3, 6, 4)
    spr(db.BANZAI_BILL_LAUNCHER, (TX + 72) * 16, (GY - 7) * 16)
    spr(db.BULLET_BILL_LAUNCHER, (TX + 64) * 16, (GY - 4) * 16)
    spr(db.BULLET_BILL_LAUNCHER, (TX + 82) * 16, (GY - 4) * 16)

    # Star Coin 2
    spr(db.STAR_COIN, (TX + 73) * 16, (GY - 11) * 16, b'\x00\x00\x00\x00\x01\x00')

    # Section 5: Summit and warp cannon
    add_ground(TX + 88, GY, 20, 7)
    add_ground(TX + 95, GY - 7, 10, 8)
    spr(db.DRY_BONES, (TX + 90) * 16, (GY - 1) * 16)
    spr(db.FIRE_BRO, (TX + 99) * 16, (GY - 8) * 16)

    # Star Coin 3
    spr(db.STAR_COIN, (TX + 92) * 16, (GY - 10) * 16, b'\x00\x00\x00\x00\x02\x00')

    # 434 = Warp Cannon. Byte 5 = 1 routes to World 6.
    spr(434, (TX + 101) * 16, (GY - 8) * 16, b'\x00\x00\x00\x00\x00\x01')

    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))
    arc.set_file('course/course1_bgdatL0.bin', serialize_layer_data(area.layer0))
    arc.set_file('course/course1_bgdatL1.bin', serialize_layer_data(area.layer1))
    arc.set_file('course/course1_bgdatL2.bin', serialize_layer_data(area.layer2))

    data = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)

    print(f'Saved: output/ChaosStation/Stage/04-36.arc ({len(data)} bytes)')


def create_level_4_castle():
    """4-Castle remix (04-24.arc).

    Keeps vanilla geometry/layout and remixes enemy pressure in traversal
    areas, then upgrades the boss room with controlled extra hazards.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/04-24.arc'
    dst = 'output/ChaosStation/Stage/04-24.arc'

    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 4-Castle: couldn't open {src} - {e}")
        return

    def safe_get(path):
        try:
            return arc.get_file(path)
        except KeyError:
            return None

    def remix_traversal_area(area):
        """Modify hostiles while preserving layout-critical actors."""
        remixed = []
        additions = []
        is_underwater = any(s.stype in (db.WATER_FILL, db.POISON_FILL) for s in area.sprites)

        dry_counter = 0
        fish_counter = 0
        anchor_counter = 0

        for s in area.sprites:
            ns = copy.deepcopy(s)

            if s.stype in (db.GOOMBA, db.KOOPA):
                ns.stype = db.DRY_BONES
            elif s.stype == db.CHEEP_CHEEP:
                if fish_counter % 2 == 0:
                    ns.stype = db.FISHBONE
                fish_counter += 1
            elif s.stype == db.DRY_BONES:
                if dry_counter % 3 == 0:
                    ns.stype = db.GIANT_DRY_BONES
                dry_counter += 1

            remixed.append(ns)

            if ns.stype in (db.DRY_BONES, db.GIANT_DRY_BONES, db.FISHBONE):
                anchor_counter += 1
                if anchor_counter % 5 == 0 and len(additions) < 8:
                    extra = copy.deepcopy(ns)
                    extra.x = min(65520, ns.x + 64)
                    extra.y = max(16, ns.y - 32)
                    extra.spritedata = bytes(6)
                    if is_underwater:
                        extra.stype = db.URCHIN if len(additions) % 2 == 0 else db.FISHBONE
                    else:
                        extra.stype = db.SPIKE_TOP if len(additions) % 2 == 0 else db.BOB_OMB
                    additions.append(extra)

        area.sprites = remixed + additions

    def buff_boss_room(area):
        """Add hazards inside the boss arena, clamped to zone bounds."""
        boss_sprites = list(area.sprites)

        # Wendy is controller-driven; use known boss-event sprite IDs as arena anchor.
        # Pick the candidate whose y is closest to the zone's vertical centre so we
        # land in the middle of the arena rather than on the entry corridor edge.
        BOSS_CTRL = {317, 375, 407, 436}
        cands = [s for s in boss_sprites if s.stype in BOSS_CTRL and s.x > 2000]
        zone0 = area.zones[0] if area.zones else None
        if cands and zone0:
            zcenter_y = zone0.y + zone0.h // 2
            anchor = min(cands, key=lambda s: abs(s.y - zcenter_y))
            cx, cy, zid = anchor.x, anchor.y, anchor.zone_id
        elif zone0:
            cx, cy, zid = zone0.x + zone0.w // 2, zone0.y + zone0.h // 2, zone0.zone_id
        else:
            cx, cy, zid = 2656, 1504, 0

        # Resolve zone bounds and build a clamping helper.
        zone = next((z for z in area.zones if z.zone_id == zid), zone0)
        if zone:
            pad = 24
            z_l, z_r = zone.x + pad, zone.x + zone.w - pad
            z_t, z_b = zone.y + pad, zone.y + zone.h - pad
        else:
            z_l, z_r = cx - 256, cx + 256
            z_t, z_b = cy - 80,  cy + 80

        def cl(v, lo, hi):
            return max(lo, min(hi, v))

        SD = bytes(6)
        FB_SD     = b'\x00\x00\x00\x00\x00\x09'
        FB_SD_CCW = b'\x00\x00\x00\x00\x10\x09'

        boss_sprites += [
            Sprite(stype=db.FIRE_BAR,  x=cl(cx - 96,  z_l, z_r), y=cl(cy - 64, z_t, z_b),
                   spritedata=FB_SD,     zone_id=zid, extra_byte=0),
            Sprite(stype=db.FIRE_BAR,  x=cl(cx + 96,  z_l, z_r), y=cl(cy - 64, z_t, z_b),
                   spritedata=FB_SD_CCW, zone_id=zid, extra_byte=0),
            Sprite(stype=db.DRY_BONES, x=cl(cx - 160, z_l, z_r), y=cl(cy + 48, z_t, z_b),
                   spritedata=SD,        zone_id=zid, extra_byte=0),
            Sprite(stype=db.DRY_BONES, x=cl(cx + 160, z_l, z_r), y=cl(cy + 48, z_t, z_b),
                   spritedata=SD,        zone_id=zid, extra_byte=0),
            Sprite(stype=db.BOB_OMB,   x=cl(cx,       z_l, z_r), y=cl(cy - 48, z_t, z_b),
                   spritedata=SD,        zone_id=zid, extra_byte=0),
        ]
        area.sprites = boss_sprites

    edited_areas = 0
    for area_idx in range(1, 7):
        course_path = f'course/course{area_idx}.bin'
        course_data = safe_get(course_path)
        if not course_data:
            continue

        area = parse_course_bin(course_data)

        if area_idx == 2:
            buff_boss_room(area)
        else:
            remix_traversal_area(area)

        area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
        arc.set_file(course_path, serialize_course_bin(area))
        edited_areas += 1

    data = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)

    print(f'Saved: output/ChaosStation/Stage/04-24.arc ({len(data)} bytes, {edited_areas} areas edited)')


def create_level_4_airship():
    """Remix the 4-Airship (04-38.arc) — Coral Airship: Deck Assault.

    Strategy:
    - Zone 0 (main flight deck) enemy set rebuilt from scratch with a coral/ocean
      themed airship gauntlet: Rocky Wrenches, Magikoopas, flame jets, Hammer/Fire
      Bros, Banzai Bill launchers, Fire Bars, and a Sledge Bro finale.
    - Zones 1–3 (transition corridor, pipe room, Bowser Jr. boss arena) preserved
      EXACTLY — all sprites, entrances, zones, and bgdat layers kept vanilla.
    - Star coins: 2 vanilla positions in zone 0 kept, 1 in boss room kept (zone 2).
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/04-38.arc'
    dst = 'output/ChaosStation/Stage/04-38.arc'

    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 4-Airship: couldn't open {src} — {e}")
        return

    area = parse_course_bin(arc.get_file('course/course1.bin'))

    # Structural / item sprites in zone 0 that must be preserved exactly.
    # 32=STAR_COIN, 64=unknown-structural, 144=RED_COIN, 156=RED_COIN_RING,
    # 188=MIDWAY, 234=unknown-start-trigger, 399=unknown-event,
    # 477=SUPER_GUIDE_BLOCK
    KEEP_Z0 = {32, 64, 144, 156, 188, 234, 399, 477}
    z0_keep  = [s for s in area.sprites if s.zone_id == 0 and s.stype in KEEP_Z0]
    z_other  = [s for s in area.sprites if s.zone_id != 0]

    SD   = bytes(6)
    FJ_L  = b'\x00\x00\x00\xc0\xc0\x16'   # FLAME_JET_LARGE  (from vanilla deck)
    FJ_H  = b'\x00\x00\x00\x00\x00\x62'   # FLAME_JET_HUGE   timer A
    FJ_H2 = b'\x00\x00\x00\x00\x01\x62'   # FLAME_JET_HUGE   timer B (offset)
    FB    = b'\x00\x00\x00\x00\x00\x09'   # FIRE_BAR  9 segments CW
    FB_CC = b'\x00\x00\x00\x00\x10\x09'   # FIRE_BAR  9 segments CCW

    ns = []

    def sp(t, x, y, d=SD):
        ns.append(Sprite(stype=t, x=x, y=y, spritedata=d, zone_id=0, extra_byte=0))

    DY = 720    # deck / ground level
    AY = 576    # mid-air
    HY = 432    # high-air (near zone ceiling)
    FY = 784    # sub-floor (flame jets shoot up through deck)

    # ── Section 1: Opening Mast (x 416–960) ──
    sp(db.ROCKY_WRENCH, 576,  DY)
    sp(db.ROCKY_WRENCH, 752,  DY)
    sp(db.ROCKY_WRENCH, 912,  DY)
    for cx in (528, 576, 624, 672, 720, 768):
        sp(db.COIN, cx, DY - 96)       # coin trail above wrenches

    # ── Section 2: Magikoopa Air Patrol (x 1024–1792) ──
    sp(db.MAGIKOOPA, 1072, AY)
    sp(db.MAGIKOOPA, 1376, AY - 32)
    sp(db.MAGIKOOPA, 1632, AY)
    sp(db.BULLET_BILL_LAUNCHER, 1184, DY)
    sp(db.BULLET_BILL_LAUNCHER, 1504, DY)
    for cx in (1120, 1168, 1216):
        sp(db.COIN, cx, HY + 16)       # high-air coin reward

    # ── Section 3: Flame Gauntlet (x 1840–2560) ──
    sp(db.FLAME_JET_LARGE, 1888, FY, FJ_L)    # shoots up through deck hole
    sp(db.FLAME_JET_HUGE,  2032, DY, FJ_H)
    sp(db.FLAME_JET_HUGE,  2176, DY, FJ_H2)
    sp(db.FLAME_JET_HUGE,  2320, DY, FJ_H)
    sp(db.FLAME_JET_HUGE,  2464, DY, FJ_H2)
    sp(db.BOB_OMB, 1936, AY - 32)
    sp(db.BOB_OMB, 2208, AY - 32)

    # ── Midway checkpoint preserved via z0_keep (vanilla x=2944) ──

    # ── Section 4: Hammer / Fire Bros Platform (x 3024–3680) ──
    sp(db.HAMMER_BRO, 3072, DY)
    sp(db.HAMMER_BRO, 3296, DY)
    sp(db.FIRE_BRO,   3552, DY)
    sp(db.FIRE_BAR,   3152, 560, FB)      # CW  fire bar (mast nub)
    sp(db.FIRE_BAR,   3456, 560, FB_CC)   # CCW fire bar
    for cx in (3200, 3248, 3296):
        sp(db.COIN, cx, HY + 32)          # risky high-air coins

    # ── Section 5: Banzai Corridor (x 3728–4400) ──
    sp(db.BANZAI_BILL_LAUNCHER, 3776, DY)
    sp(db.ROCKY_WRENCH,          3904, DY)
    sp(db.BANZAI_BILL_LAUNCHER, 4096, DY)
    sp(db.ROCKY_WRENCH,          4256, DY)
    sp(db.BOB_OMB,               4016, AY)

    # ── Section 6: Final Gauntlet (x 4512–5280) ──
    sp(db.FLAME_JET_HUGE, 4560, DY, FJ_H)
    sp(db.FLAME_JET_HUGE, 4720, DY, FJ_H2)
    sp(db.FIRE_BAR,        4848, AY - 32, FB)    # fire bar at mid-wall height
    sp(db.SLEDGE_BRO,      5008, DY)              # heavy finale enemy
    sp(db.ROCKY_WRENCH,    5168, DY)              # last deck obstacle
    sp(db.BOB_OMB,         5264, AY)              # surprise drop before zone 3

    area.sprites       = z0_keep + z_other + ns
    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))

    arc.set_file('course/course1.bin', serialize_course_bin(area))

    out = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(out)
    print(f'[W4] Remixed 4-Airship (04-38): Deck Assault -> Saved: {dst} ({len(out)} bytes)')


def create_level_4_tower():
    """Modify the vanilla 4-Tower (04-22.arc) — Coral Spire.
    
    This is a VERTICAL tower with narrow X (256-784) and 4 stacked zones:
    Zone 0 (bottom, y~4672-5169): Start area, 3 Dry Bones
    Zone 1 (middle, y~2432-4097): Main climb, 12 Dry Bones + boss controller
    Zone 2 (upper, y~1248-1953):  Metal boxes section
    Zone 3 (top,   y~256-913):    Metal box gauntlet to the top
    
    We SWAP some Dry Bones and ADD new land enemies at known-good positions.
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db
    
    src = 'extracted files/Stage/04-22.arc'
    dst = 'output/ChaosStation/Stage/04-22.arc'
    
    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 4-Tower: couldn't open {src}")
        return
    
    # ── Area 1: The vertical tower climb ──
    # ── Area 1: The vertical tower climb ──
    # Leaving Area 1 completely vanilla as requested to ensure Boss Door (277/436) works perfectly.
    
    # ── Area 2: BOSS ROOM ──
    # The vanilla boss room only has 3 loaded sprites. We can safely add Bob-ombs
    # without breaking any sprite limits, provided we update `loaded_sprites`.
    course2_data = arc.get_file('course/course2.bin')
    if course2_data:
        area = parse_course_bin(course2_data)
        
        # Add absolute chaos to the Boss Room to compensate for the vanilla climb!
        # Adding Bob-ombs (101), Boos (131), and Spike Tops (60)
        new_sprites = [
            # Bob-ombs dropping from the ceiling
            Sprite(stype=101, x=400, y=550, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=101, x=680, y=550, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=101, x=500, y=400, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=101, x=580, y=400, spritedata=bytes(6), zone_id=0, extra_byte=0),
            
            # Spike Tops crawling on the floor to restrict movement
            Sprite(stype=60, x=450, y=300, spritedata=bytes([0,0,0,0,0,0]), zone_id=0, extra_byte=0),
            Sprite(stype=60, x=630, y=300, spritedata=bytes([0,0,0,0,0,0]), zone_id=0, extra_byte=0),
            
            # Boos tracking Mario from the corners
            Sprite(stype=131, x=350, y=450, spritedata=bytes([0,0,0,0,0,0]), zone_id=0, extra_byte=0),
            Sprite(stype=131, x=730, y=450, spritedata=bytes([0,0,0,0,0,0]), zone_id=0, extra_byte=0),
        ]
        area.sprites.extend(new_sprites)
        
        # UPDATE loaded_sprites to register the new sprite files
        area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area))
    
    data = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)
    print("Modified 4-Tower: Coral Spire (Custom enemies + Boss Room modified)")


def create_level_4_ambush():
    """Modify the vanilla W4 Ambushes (04-33, 04-34, 04-35).
    
    The vanilla ambushes have ~14 sprites each, mostly Cheep Cheeps (185).
    Instead of just swapping, we ADD creative new threats on top:
    
    04-33: Add Bloopers + Fishbones for a multi-directional assault
    04-34: Add a Cheep Chomp + Urchins blocking escape routes
    04-35: Add Blooper Nannies + Big Cheep Cheep for maximum chaos
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db
    
    # Each ambush gets its own creative additions
    ambush_additions = {
        '04-33.arc': [
            # Bloopers swarming from above while Cheep Cheeps attack from below!
            Sprite(stype=db.BLOOPER, x=350, y=300, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.BLOOPER, x=500, y=280, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.BLOOPER, x=650, y=300, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Fishbones homing in from the sides
            Sprite(stype=db.FISHBONE, x=400, y=420, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.FISHBONE, x=600, y=400, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # An Urchin blocking the safe spot
            Sprite(stype=db.URCHIN, x=450, y=440, spritedata=bytes(6), zone_id=0, extra_byte=0),
        ],
        '04-34.arc': [
            # Cheep Chomp drops in — massive jaws of death!
            Sprite(stype=db.CHEEP_CHOMP, x=500, y=350, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Urchins blocking the platforms you'd normally escape to
            Sprite(stype=db.URCHIN, x=380, y=430, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.URCHIN, x=550, y=420, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.URCHIN, x=660, y=440, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Extra Fishbone zooming through
            Sprite(stype=db.FISHBONE, x=450, y=380, spritedata=bytes(6), zone_id=0, extra_byte=0),
        ],
        '04-35.arc': [
            # Blooper Nanny + babies = screen-filling chaos
            Sprite(stype=db.BLOOPER_NANNY, x=400, y=280, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.BLOOPER_NANNY, x=600, y=300, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Big Cheep Cheep — takes up tons of space
            Sprite(stype=db.BIG_CHEEP_CHEEP, x=500, y=400, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Fishbones from both sides
            Sprite(stype=db.FISHBONE, x=350, y=400, spritedata=bytes(6), zone_id=0, extra_byte=0),
            Sprite(stype=db.FISHBONE, x=650, y=380, spritedata=bytes(6), zone_id=0, extra_byte=0),
            # Urchin in the middle
            Sprite(stype=db.URCHIN, x=500, y=450, spritedata=bytes(6), zone_id=0, extra_byte=0),
        ],
    }
    
    for filename, additions in ambush_additions.items():
        src = f'extracted files/Stage/{filename}'
        dst = f'output/ChaosStation/Stage/{filename}'
        
        try:
            arc = U8Archive.load(open(src, 'rb').read())
        except Exception as e:
            print(f"  Skipping {filename}: {e}")
            continue
            
        data = arc.get_file('course/course1.bin')
        area = parse_course_bin(data)
        
        # Add all the new enemies!
        area.sprites.extend(additions)
        
        # Update sprite manifest
        area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area))
        
        packed = arc.pack()
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(packed)
        print(f"  Modified {filename}")
            
    print("Modified World 4 Ambushes: Ocean Onslaught")




def create_level_5_1():
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    builder = LevelBuilder()
    a1 = builder.add_area(1)
    a1.set_tileset(1, db.TILESET_FOREST)
    a1.set_background(bg2=db.BG_FOREST)
    a1.set_time(400)
    a1.add_zone(0, 0, 480, 3500, zone_id=0, music=db.MUSIC_FOREST, cam_mode=3, visibility=16)
    a1.add_sprite(db.POISON_FILL, 0, 3450, spritedata=b"\x01\x00\x00\x00\x00\x00")
    a1.add_ground(14, 210, 10, 8, tileset=1)
    a1.add_entrance(0, 18*16, 208*16, etype=db.ENTRANCE_NORMAL)
    a1.add_sprite(10, 18*16, 208*16)
    a1.add_sprite(db.PROPELLER_BLOCK, 18*16, 206*16)
    for gx,gy,gw in [(4,197,7),(20,193,6),(28,189,5),(6,185,7),(22,181,6),(30,177,5),(8,173,6),(24,169,7),(6,165,5),(28,161,5),(10,157,6),(24,153,7)]:
        a1.add_ground(gx, gy, gw, 2, tileset=1)
    for s,x,y in [(db.GOOMBA,6,196),(db.THWOMP,22,188),(db.BUZZY_BEETLE,30,188),(db.CHAIN_CHOMP,8,184),(db.KOOPA,24,180),(db.THWOMP,32,172),(db.PIRANHA_PLANT,10,172),(db.SLEDGE_BRO,26,168),(db.CROWBER,16,160),(db.BRAMBALL,30,160),(db.THWOMP,12,152),(db.GOOMBA,26,152)]:
        a1.add_sprite(s, x*16, y*16)
    a1.add_sprite(db.STAR_COIN, 24*16, 183*16, spritedata=bytes([0,0,0,0,0,0]))
    for i,my in enumerate([148,143,138,133,128,123,118,113]):
        a1.add_sprite(228, (6+(i%3)*10)*16, my*16)
    a1.add_ground(22, 145, 6, 2, tileset=1)
    for s,x,y in [(db.SLEDGE_BRO,24,144),(db.CROWBER,16,138),(db.CROWBER,10,128),(db.CROWBER,20,118),(db.THWOMP,14,125)]:
        a1.add_sprite(s, x*16, y*16)
    a1.add_ground(6, 122, 6, 2, tileset=1)
    a1.add_sprite(db.PARAGOOMBA, 18*16, 115*16)
    a1.add_ground(24, 110, 6, 2, tileset=1)
    a1.add_sprite(db.KOOPA, 26*16, 109*16)
    a1.add_ground(12, 103, 6, 2, tileset=1)
    a1.add_sprite(db.MIDWAY_FLAG, 14*16, 102*16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a1.add_sprite(db.STAR_COIN, 15*16, 130*16, spritedata=bytes([0,0,0,0,1,0]))
    for gx,gy,gw in [(6,98,8),(22,93,7),(8,88,6),(24,84,7),(6,80,5),(20,76,7),(8,72,6),(24,68,7),(6,64,6),(22,60,8)]:
        a1.add_ground(gx, gy, gw, 2, tileset=1)
    for s,x,y in [(db.BRAMBALL,9,97),(db.CHAIN_CHOMP,24,92),(db.THWOMP,10,83),(db.FIRE_BRO,26,83),(db.BRAMBALL,8,79),(db.SLEDGE_BRO,22,75),(db.CROWBER,14,72),(db.CHAIN_CHOMP,10,71),(db.THWOMP,26,63),(db.HAMMER_BRO,8,63),(db.BRAMBALL,24,59),(db.PARAGOOMBA,16,58)]:
        a1.add_sprite(s, x*16, y*16)
    a1.add_sprite(db.STAR_COIN, 12*16, 78*16, spritedata=bytes([0,0,0,0,2,0]))
    a1.add_ground(10, 55, 12, 8, tileset=1)
    a1.add_pipe(14, 53, height=2, tileset=0)
    a1.add_entrance(1, x=14*16+16, y=53*16, etype=2, zone_id=0, dest_area=2, dest_entrance=2)
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_FOREST)
    a2.set_background(bg2=db.BG_FOREST)
    a2.set_time(300)
    a2.add_zone(0, 0, 7000, 640, zone_id=0, music=db.MUSIC_FOREST, cam_mode=0, visibility=16)
    GY = 28
    a2.add_ground(0, GY, 10, 4, tileset=1)
    a2.add_entrance(2, 3*16, (GY-2)*16, etype=0)
    a2.add_entrance(1, 92*16, (GY-1)*16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a2.add_ground(12, GY, 300, 4, tileset=1)
    for bx in [18,32,48,62,78]: a2.add_sprite(db.BRAMBALL, bx*16, (GY-1)*16)
    a2.add_sprite(db.PIRANHA_PLANT, 25*16, (GY-1)*16)
    a2.add_sprite(db.PIRANHA_PLANT, 55*16, (GY-1)*16)
    a2.add_ground(40, GY-5, 6, 2, tileset=1)
    a2.add_sprite(db.HAMMER_BRO, 42*16, (GY-6)*16)
    for tx in [95,110,125,140,155]: a2.add_sprite(db.THWOMP, tx*16, (GY-8)*16)
    a2.add_sprite(db.CHAIN_CHOMP, 115*16, (GY-1)*16)
    a2.add_sprite(db.CHAIN_CHOMP, 145*16, (GY-1)*16)
    a2.add_sprite(db.MIDWAY_FLAG, 92*16, (GY-1)*16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    for s,x in [(db.SLEDGE_BRO,175),(db.FIRE_BRO,195),(db.HAMMER_BRO,215),(db.SLEDGE_BRO,235)]: a2.add_sprite(s, x*16, (GY-1)*16)
    a2.add_sprite(db.PIRANHA_PLANT, 185*16, (GY-1)*16)
    a2.add_sprite(db.PIRANHA_PLANT, 225*16, (GY-1)*16)
    a2.add_sprite(db.BANZAI_BILL_LAUNCHER, 200*16, (GY-4)*16)
    a2.add_sprite(db.BANZAI_BILL_LAUNCHER, 240*16, (GY-4)*16)
    a2.add_ground(265, GY, 14, 4, tileset=1)
    a2.add_sprite(db.GOAL_POLE, 274*16, (GY-1)*16)
    builder.save("output/ChaosStation/Stage/05-01.arc")
    print("Created 5-1: Canopy Ascent")


def create_level_5_2():
    """5-2: Poison Surge — low swamp docks separated by poison rivers.
    Dock-hopping, Donut Blocks over poison, Chain Chomp timing.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(1, db.TILESET_FOREST)
    a.set_background(bg2=db.BG_FOREST)
    a.set_time(500)
    a.add_zone(0, 0, 9000, 640, zone_id=0, music=db.MUSIC_FOREST, cam_mode=0)

    a.add_sprite(db.POISON_FILL, 0, 27 * 16, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # ── DOCK 1 ──
    a.add_ground(0, 21, 62, 8, tileset=1)
    a.add_entrance(0, 3 * 16, 19 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 113 * 16, 20 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)
    a.add_sprite(10, 3 * 16, 19 * 16)
    a.add_question_block(8, 18, contents=7)  # Yoshi egg
    for px in [18, 30, 45]:
        a.add_sprite(db.PIPE_PIRANHA_UP, px * 16, 19 * 16)
    a.add_sprite(db.GOOMBA, 10 * 16, 20 * 16)
    a.add_sprite(db.GOOMBA, 52 * 16, 20 * 16)

    # ── RIVER 1: Donut blocks + Cheep Cheeps ──
    for dx in [65, 71, 77, 83, 89, 95, 101, 107]:
        a.add_sprite(db.FALLING_PLATFORM, dx * 16, 20 * 16)
    for cx in [68, 80, 92, 104]:
        a.add_sprite(db.CHEEP_CHEEP, cx * 16, 25 * 16)
    a.add_ground(84, 12, 4, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 85 * 16, 11 * 16, spritedata=bytes([0, 0, 0, 0, 0, 0]))

    # ── DOCK 2: Fire Bros + Star Coin shelf ──
    a.add_ground(111, 21, 65, 8, tileset=1)
    a.add_sprite(db.FIRE_BRO, 125 * 16, 20 * 16)
    a.add_sprite(db.FIRE_BRO, 145 * 16, 20 * 16)
    a.add_sprite(db.HAMMER_BRO, 160 * 16, 20 * 16)
    a.add_ground(130, 14, 10, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 134 * 16, 13 * 16, spritedata=bytes([0, 0, 0, 0, 1, 0]))
    a.add_sprite(db.MIDWAY_FLAG, 113 * 16, 20 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ── RIVER 2: 5 moving platforms + Bloopers ──
    for rx, ry in [(180, 20), (196, 17), (212, 21), (222, 18), (230, 19)]:
        a.add_sprite(db.BASIC_PLATFORM, rx * 16, ry * 16)
    for bx in [183, 200, 218]:
        a.add_sprite(db.BLOOPER, bx * 16, 25 * 16)

    # ── DOCK 3: Chain Chomps + Star Coin 3 ──
    a.add_ground(238, 21, 75, 8, tileset=1)
    for chx in [248, 275, 300]:
        a.add_sprite(db.CHAIN_CHOMP, chx * 16, 20 * 16)
    a.add_sprite(db.STAR_COIN, 285 * 16, 17 * 16, spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # ── RIVER 3: Donut blocks + Cheep Cheeps ──
    for dx in [318, 325, 332, 339, 346, 353, 360]:
        a.add_sprite(db.FALLING_PLATFORM, dx * 16, 20 * 16)
    for cx in [322, 340, 358]:
        a.add_sprite(db.CHEEP_CHEEP, cx * 16, 25 * 16)

    # ── DOCK 4: Sledge Bros gauntlet + Goal Pole ──
    # Width=70 gives ~32 tiles past the pole for the victory walk-off animation.
    a.add_ground(368, 21, 70, 8, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 380 * 16, 20 * 16)
    a.add_sprite(db.SLEDGE_BRO, 400 * 16, 20 * 16)
    a.add_sprite(db.HAMMER_BRO, 415 * 16, 20 * 16)
    a.add_sprite(db.GOAL_POLE, 418 * 16, 20 * 16)

    builder.save('output/ChaosStation/Stage/05-02.arc')
    print('Created 5-2: Poison Surge')


def create_level_5_3():
    """5-3: Bramball Factory — underground cave where the floor is thick with Bramballs.
    Mario must navigate elevated platforms above the chaos. 5 unique traversal zones.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(1, db.TILESET_CAVE)
    a.set_background(bg2=db.BG_UNDERGROUND)
    a.set_time(500)
    a.add_zone(0, 0, 7000, 640, zone_id=0, music=db.MUSIC_UNDERGROUND, cam_mode=0)

    # Poison on the very bottom — nobody wants to fall down here!
    a.add_sprite(db.POISON_FILL, 0, 28 * 16, spritedata=b'\x01\x00\x00\x00\x00\x00')

    # ── Solid factory floor (Bramballs patrol on top of it) ──
    a.add_ground(0, 25, 400, 4, tileset=1)
    # Bramballs rolling along the floor — densely packed in groups
    bramball_xs = [8, 16, 30, 40, 55, 68, 85, 100, 118, 135,
                   152, 165, 180, 200, 215, 230, 248, 265, 280,
                   295, 310, 330, 348, 365, 382]
    for bx in bramball_xs:
        a.add_sprite(db.BRAMBALL, bx * 16, 24 * 16)

    # ── Safe spawn platform clinging to the left wall ──
    a.add_ground(0, 20, 8, 5, tileset=1)
    a.add_entrance(0, 2 * 16, 18 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 140 * 16, 14 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 2 * 16, 18 * 16)

    # ══ ZONE 1: Simple offset ledges (X 10–60) ══
    zone1 = [(10,18,8), (22,16,8), (34,19,7), (45,15,9), (57,18,7)]
    for (zx, zy, zw) in zone1:
        a.add_ground(zx, zy, zw, 2, tileset=1)
        a.add_sprite(db.BUZZY_BEETLE, (zx+2)*16, (zy-1)*16)

    # ══ ZONE 2: ? Block staircase (X 62–110) ══
    for step in range(7):
        qx = 62 + step * 7
        qy = 22 - step
        a.add_question_block(qx, qy, contents=1)  # coin inside
        a.add_question_block(qx+1, qy, contents=1)
    # Star Coin 1 — floating just above the Bramballs mid Zone 2
    a.add_sprite(db.STAR_COIN, 88 * 16, 23 * 16, spritedata=bytes([0,0,0,0,0,0]))

    # ══ ZONE 3: Moving platforms over a wide Bramball cluster (X 115–165) ══
    for i, (mx, my) in enumerate([(118,18),(135,15),(152,18)]):
        a.add_sprite(db.BASIC_PLATFORM, mx*16, my*16)
    # Midway flag reachable from the middle moving platform
    a.add_sprite(db.MIDWAY_FLAG, 140 * 16, 14 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    # Side alcove for Star Coin 2
    a.add_ground(160, 22, 14, 1, tileset=1)
    a.add_sprite(db.STAR_COIN, 166 * 16, 24 * 16, spritedata=bytes([0,0,0,0,0,1]))
    a.add_sprite(db.BRAMBALL, 162 * 16, 24 * 16)  # guard inside alcove

    # ══ ZONE 4: 1-tile-wide walkway (X 175–220) ══
    for wx in range(175, 220, 1):
        a.add_ground(wx, 22, 1, 1, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 195 * 16, 21 * 16)
    a.add_sprite(db.HAMMER_BRO, 210 * 16, 21 * 16)

    # ══ ZONE 5: P-Switch bridge (X 225–300) ══
    a.add_sprite(db.P_SWITCH, 228 * 16, 18 * 16)
    for bx in range(235, 295, 1):
        a.add_brick_block(bx, 22, contents=0)
    # Star Coin 3 — on top of the far end of the P-Switch bridge
    a.add_sprite(db.STAR_COIN, 288 * 16, 17 * 16, spritedata=bytes([0,0,0,0,0,2]))

    # ── End platform and Goal Pole ──
    # Width=20 gives 12 tiles to the right of the pole for the victory animation walk-off.
    a.add_ground(300, 20, 20, 8, tileset=1)
    a.add_sprite(db.GOAL_POLE, 308 * 16, 19 * 16)

    builder.save('output/ChaosStation/Stage/05-03.arc')
    print('Created 5-3: Bramball Factory')


def create_level_5_4():
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(1, db.TILESET_FOREST)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(400)
    a.add_zone(0, 0, 8000, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0)
    a.add_sprite(db.POISON_FILL, 0, 26*16, spritedata=b"\x01\x00\x00\x00\x00\x00")
    a.add_ground(0, 20, 12, 8, tileset=1)
    a.add_entrance(0, 3*16, 18*16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 5*16, 19*16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3*16, 18*16)
    a.add_sprite(db.MIDWAY_FLAG, 5*16, 19*16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(275, 10*16, 25*16, spritedata=b"\x00\x00\x00\x00\x01\x10")
    for ex in [30,40,55,65,75]: a.add_sprite(db.GOOMBA, ex*16, 24*16)
    a.add_sprite(db.PARAGOOMBA, 35*16, 18*16)
    a.add_sprite(db.PARAGOOMBA, 60*16, 16*16)
    a.add_sprite(db.CROWBER, 45*16, 12*16)
    for kx in [85,100,115]: a.add_sprite(db.KOOPA, kx*16, 24*16)
    for gx in [95,130]: a.add_sprite(db.GOOMBA, gx*16, 24*16)
    a.add_sprite(db.SLEDGE_BRO, 140*16, 24*16)
    a.add_sprite(db.FIRE_BRO, 120*16, 24*16)
    a.add_sprite(db.PARAGOOMBA, 105*16, 16*16)
    a.add_sprite(db.PARAGOOMBA, 145*16, 16*16)
    a.add_sprite(db.CROWBER, 90*16, 12*16)
    a.add_sprite(db.CROWBER, 150*16, 12*16)
    for hx in [170,210]: a.add_sprite(db.HAMMER_BRO, hx*16, 24*16)
    for sx in [190,230]: a.add_sprite(db.SLEDGE_BRO, sx*16, 24*16)
    for fx in [200,245]: a.add_sprite(db.FIRE_BRO, fx*16, 24*16)
    for kx in [180,250]: a.add_sprite(db.KOOPA, kx*16, 24*16)
    for pgx in [175,225]: a.add_sprite(db.PARAGOOMBA, pgx*16, 16*16)
    for crx in [185,220,255]: a.add_sprite(db.CROWBER, crx*16, 10*16)
    for blx in [200,240]: a.add_sprite(db.BANZAI_BILL_LAUNCHER, blx*16, 20*16)
    for hx in [270,345]: a.add_sprite(db.HAMMER_BRO, hx*16, 24*16)
    a.add_sprite(db.SLEDGE_BRO, 295*16, 24*16)
    a.add_sprite(db.FIRE_BRO, 320*16, 24*16)
    for kx in [280,335]: a.add_sprite(db.KOOPA, kx*16, 24*16)
    for pgx in [285,340]: a.add_sprite(db.PARAGOOMBA, pgx*16, 16*16)
    for crx in [290,315,350]: a.add_sprite(db.CROWBER, crx*16, 10*16)
    for blx in [290,330,360]: a.add_sprite(db.BANZAI_BILL_LAUNCHER, blx*16, 20*16)
    a.add_platform(50, 22, width=1)
    a.add_sprite(db.STAR_COIN, 51*16, 21*16, spritedata=bytes([0,0,0,0,0,0]))
    a.add_sprite(db.STAR_COIN, 175*16, 20*16, spritedata=bytes([0,0,0,0,1,0]))
    a.add_sprite(db.STAR_COIN, 320*16, 15*16, spritedata=bytes([0,0,0,0,2,0]))
    a.add_ground(370, 22, 20, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 384*16, 21*16)
    builder.save("output/ChaosStation/Stage/05-04.arc")
    print("Created 5-4: Toxic Crossing")


def create_level_5_5():
    """5-5: Piranha Pipeline — dark zigzag descent through cave.
    visibility=36 (same as ghost houses). 6 floors alternate gap sides (18 tiles apart).
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(1, db.TILESET_CAVE)
    a.set_background(bg2=db.BG_UNDERGROUND)
    a.set_time(500)
    a.add_zone(0, 0, 1280, 2300, zone_id=0, music=db.MUSIC_UNDERGROUND,
               cam_mode=3, visibility=36)

    for fy in range(23, 110):
        a.add_ground(0, fy, 2, 1, tileset=1)
    for fy in range(23, 92):
        a.add_ground(78, fy, 2, 1, tileset=1)

    # SPAWN (Y=20)
    a.add_ground(2, 20, 36, 3, tileset=1)
    a.add_entrance(0, 20 * 16, 19 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 60 * 16, 73 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 20 * 16, 19 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 8 * 16, 19 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 30 * 16, 19 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 34 * 16, 19 * 16)

    # FLOOR 2 (Y=38): GAP LEFT
    a.add_ground(40, 38, 38, 3, tileset=1)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 48 * 16, 37 * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 60 * 16, 37 * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 72 * 16, 37 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 55 * 16, 35 * 16)
    a.add_ground(15, 34, 8, 2, tileset=1)
    a.add_sprite(db.PIRANHA_PLANT, 18 * 16, 33 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 20 * 16, 33 * 16)
    a.add_sprite(db.STAR_COIN, 60 * 16, 34 * 16, spritedata=bytes([0,0,0,0,0,0]))

    # FLOOR 3 (Y=56): GAP RIGHT
    a.add_ground(2, 56, 36, 3, tileset=1)
    a.add_sprite(db.BIG_PIRANHA_PLANT, 10 * 16, 55 * 16)
    a.add_sprite(db.BIG_PIRANHA_PLANT, 22 * 16, 55 * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 32 * 16, 55 * 16)
    a.add_ground(55, 52, 8, 2, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 58 * 16, 51 * 16)

    # FLOOR 4 (Y=74): GAP LEFT
    a.add_ground(40, 74, 38, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 48 * 16, 73 * 16)
    a.add_sprite(db.FIRE_BRO, 62 * 16, 73 * 16)
    a.add_sprite(db.HAMMER_BRO, 55 * 16, 73 * 16)
    a.add_sprite(db.HAMMER_BRO, 72 * 16, 73 * 16)
    a.add_sprite(db.MIDWAY_FLAG, 60 * 16, 73 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_ground(10, 70, 10, 2, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 14 * 16, 69 * 16)
    a.add_sprite(db.STAR_COIN, 70 * 16, 69 * 16, spritedata=bytes([0,0,0,0,1,0]))

    # FLOOR 5 (Y=92): GAP RIGHT
    a.add_ground(2, 92, 36, 3, tileset=1)
    a.add_sprite(db.BIG_PIRANHA_PLANT, 10 * 16, 91 * 16)
    a.add_sprite(db.BIG_PIRANHA_PLANT, 25 * 16, 91 * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 32 * 16, 91 * 16)
    for gpy in [87, 90]:
        a.add_sprite(db.PIPE_PIRANHA_RIGHT, 5 * 16, gpy * 16)
        a.add_sprite(db.PIPE_PIRANHA_RIGHT, 15 * 16, gpy * 16)
        a.add_sprite(db.PIPE_PIRANHA_RIGHT, 25 * 16, gpy * 16)
    a.add_ground(55, 88, 8, 2, tileset=1)
    a.add_sprite(db.FIRE_BRO, 58 * 16, 87 * 16)

    # FLOOR 6 (Y=110): GAP LEFT
    a.add_ground(40, 110, 38, 3, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 48 * 16, 109 * 16)
    a.add_sprite(db.CHAIN_CHOMP, 62 * 16, 109 * 16)
    a.add_sprite(db.HAMMER_BRO, 55 * 16, 109 * 16)
    a.add_sprite(db.SLEDGE_BRO, 72 * 16, 109 * 16)
    a.add_ground(8, 106, 10, 2, tileset=1)
    a.add_sprite(db.PIRANHA_PLANT, 12 * 16, 105 * 16)
    a.add_sprite(db.PIRANHA_PLANT, 15 * 16, 105 * 16)
    a.add_sprite(db.STAR_COIN, 48 * 16, 105 * 16, spritedata=bytes([0,0,0,0,2,0]))

    # GOAL (Y=128)
    a.add_ground(2, 128, 76, 4, tileset=1)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 8 * 16, 127 * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 20 * 16, 127 * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 35 * 16, 127 * 16)
    a.add_sprite(db.HAMMER_BRO, 45 * 16, 127 * 16)
    a.add_sprite(db.GOAL_POLE, 65 * 16, 127 * 16)

    builder.save('output/ChaosStation/Stage/05-05.arc')
    print('Created 5-5: Piranha Pipeline (dark zigzag)')


def create_level_5_castle():
    """Modify 05-24: Briar Bastion — CHAOTIC hazard gauntlet.

    Area 1: Three escalating waves of enemies through the castle hallways.
            Each wave is unique in composition and spacing.
    Area 2: Iggy's Boss Arena. Thwomps slam the tilting platforms from above.
            Fire Bars bracket the arena at two heights. Amps fill the center gap.
            (No extra Chain Chomps — Iggy already has one and extras cause glitches.)
    Area 3: Escape gauntlet — Sledge Bros, Fire Bars, and Amps in a tight corridor.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/05-24.arc'
    dst = 'output/ChaosStation/Stage/05-24.arc'

    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 5-Castle: couldn't open {src} - {e}")
        return

    def safe_get(path):
        try:
            return arc.get_file(path)
        except KeyError:
            return None

    SD = bytes(6)
    fb_sd_cw  = b'\x00\x00\x00\x00\x10\x07'
    fb_sd_ccw = b'\x00\x00\x00\x00\x00\x07'
    fb_long_cw  = b'\x00\x00\x00\x00\x18\x07'
    fb_long_ccw = b'\x00\x00\x00\x00\x08\x07'

    def clamp_to_zone(zone, x, y, pad=24):
        if zone is None:
            return x, y
        cx = min(max(x, zone.x + pad), zone.x + zone.w - pad)
        cy = min(max(y, zone.y + pad), zone.y + zone.h - pad)
        return cx, cy

    # ══════════════════════════════════════
    #  AREA 1 — Castle Hallways (3 waves)
    # ══════════════════════════════════════
    area1_data = safe_get('course/course1.bin')
    if area1_data:
        area1 = parse_course_bin(area1_data)
        area1.settings.time_limit = 250
        z1 = area1.zones[0] if area1.zones else None

        # Keep vanilla sprites but upgrade Dry Bones and strip generic weaker enemies
        base = []
        dry_idx = 0
        strip_types = {db.CROWBER, db.FIRE_BRO, db.SPIKE_TOP, db.KOOPA_PARATROOPA, db.BRAMBALL}
        for s in area1.sprites:
            if s.stype in strip_types:
                continue
            ns = copy.deepcopy(s)
            if s.stype == db.DRY_BONES:
                if dry_idx % 2 == 0:
                    ns.stype = db.GIANT_DRY_BONES
                dry_idx += 1
            base.append(ns)

        # ── Wave 1: Introduction gauntlet (X 1600–4000) ──
        # Varied spacing: single threats, then double, then overlapping
        wave1 = [
            # x,    y,    stype,            spritedata
            (1700,  432,  db.SLEDGE_BRO,    SD),
            (2000,  480,  db.CHAIN_CHOMP,   SD),
            (2300,  352,  db.AMP,           SD),
            (2300,  416,  db.AMP,           SD),   # Doubly stacked Amps
            (2600,  432,  db.FIRE_BAR,      fb_sd_cw),
            (2900,  480,  db.GIANT_DRY_BONES, SD),
            (3100,  432,  db.SLEDGE_BRO,    SD),
            (3400,  336,  db.THWOMP,        SD),   # Thwomp drops from above
            (3700,  480,  db.CHAIN_CHOMP,   SD),
            (3900,  432,  db.FIRE_BAR,      fb_sd_ccw),
        ]

        # ── Wave 2: Mid-castle escalation (X 4200–6500) ──
        # Intro of Fire Bar pairs and faster enemy rhythm
        wave2 = [
            (4200,  480,  db.GIANT_DRY_BONES, SD),
            (4400,  432,  db.SLEDGE_BRO,     SD),
            (4600,  304,  db.AMP,            SD),
            (4600,  368,  db.AMP,            SD),
            (4600,  432,  db.AMP,            SD),   # Triple Amp column
            (4900,  432,  db.FIRE_BAR,       fb_long_cw),
            (5100,  432,  db.FIRE_BAR,       fb_long_ccw),  # Interlocked pair
            (5350,  480,  db.CHAIN_CHOMP,    SD),
            (5600,  432,  db.THWOMP,         SD),
            (5800,  432,  db.SLEDGE_BRO,     SD),
            (6200,  480,  db.CHAIN_CHOMP,    SD),
            (6400,  432,  db.FIRE_BAR,       fb_sd_cw),
        ]

        # ── Wave 3: Final approach — wall-to-wall chaos (X 6800–8200) ──
        wave3 = [
            (6800,  432,  db.SLEDGE_BRO,    SD),
            (7000,  304,  db.AMP,           SD),
            (7000,  432,  db.CHAIN_CHOMP,   SD),
            (7200,  432,  db.FIRE_BAR,      fb_long_ccw),
            (7400,  480,  db.GIANT_DRY_BONES, SD),
            (7500,  432,  db.THWOMP,        SD),
            (7700,  432,  db.FIRE_BAR,      fb_sd_cw),
            (7900,  480,  db.CHAIN_CHOMP,   SD),
            (8100,  432,  db.SLEDGE_BRO,    SD),
        ]

        for x, y, stype, sd in (wave1 + wave2 + wave3):
            cx, cy = clamp_to_zone(z1, x, y)
            base.append(Sprite(stype=stype, x=cx, y=cy, spritedata=sd, zone_id=0, extra_byte=0))

        area1.sprites = base
        area1.loaded_sprites = sorted(set(s.stype for s in base))
        arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ══════════════════════════════════════
    #  AREA 2 — Iggy's Boss Arena
    # ══════════════════════════════════════
    # Iggy vanilla: tilting platforms, Chain Chomp partner.
    # Our additions: Thwomps drop from ceiling onto the tilting platforms,
    # Fire Bars rotate at two separate heights bracketing the whole arena,
    # Amps fill the dangerous air gap above the tilting platform ramp.
    # NO extra Chain Chomps — Iggy's Chomp + more = chain anchor collision glitch.
    area2_data = safe_get('course/course2.bin')
    if area2_data:
        area2 = parse_course_bin(area2_data)
        area2.settings.time_limit = 250
        z2 = area2.zones[0] if area2.zones else None
        boss_sprites = list(area2.sprites)

        # Find arena center from controller sprites
        ctrl_ids = {372, 407, 408, 436}
        cands = [s for s in boss_sprites if s.stype in ctrl_ids]
        if cands:
            cx, cy = cands[0].x, cands[0].y
        elif z2:
            cx, cy = z2.x + z2.w // 2, z2.y + z2.h // 2
        else:
            cx, cy = 2304, 1520

        # Fire Bars: two pairs — one high bracket, one low bracket
        # High bracket: spins above where Mario walks, cutting vertical space
        # Low bracket: spins near the ramp, requiring precise jumps
        arena_add = [
            # High Fire Bars — bracket the full arena width at ceiling level
            (db.FIRE_BAR, -280, -96, fb_long_cw),
            (db.FIRE_BAR,  280, -96, fb_long_ccw),
            # Mid Fire Bars — threaten the central climbing space
            (db.FIRE_BAR, -144, -24, fb_sd_ccw),
            (db.FIRE_BAR,  144, -24, fb_sd_cw),
            # Thwomps: drop onto the tilting platform from directly above
            (db.THWOMP,  -200,  -80, SD),
            (db.THWOMP,     0,  -96, SD),
            (db.THWOMP,   200,  -80, SD),
            # Amp cluster at center gap — punishes jumping over the ramp
            (db.AMP,       -48,   0, SD),
            (db.AMP,         0, -48, SD),
            (db.AMP,        48,   0, SD),
            # Sledge Bro on each end of the ramp — ground-pound hazard
            (db.SLEDGE_BRO, -220, 72, SD),
            (db.SLEDGE_BRO,  220, 72, SD),
            # Giant Dry Bones patrol the floor edges
            (db.GIANT_DRY_BONES, -320, 80, SD),
            (db.GIANT_DRY_BONES,  320, 80, SD),
        ]

        for stype, dx, dy, sd in arena_add:
            px, py = clamp_to_zone(z2, cx + dx, cy + dy)
            boss_sprites.append(Sprite(stype=stype, x=px, y=py, spritedata=sd, zone_id=0, extra_byte=0))

        area2.sprites = boss_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # ══════════════════════════════════════
    #  AREA 3 — Escape Gauntlet
    # ══════════════════════════════════════
    # Heavy Sledge Bros + rotating Fire Bars + Amps — a victory lap that still murders you
    area3_data = safe_get('course/course3.bin')
    if area3_data:
        area3 = parse_course_bin(area3_data)
        z3 = area3.zones[0] if area3.zones else None
        escape_adds = [
            (db.SLEDGE_BRO,      480, 432, SD),
            (db.FIRE_BAR,        640, 400, fb_sd_cw),
            (db.AMP,             720, 352, SD),
            (db.CHAIN_CHOMP,     800, 448, SD),
            (db.SLEDGE_BRO,      960, 416, SD),
            (db.FIRE_BAR,       1100, 400, fb_sd_ccw),
            (db.THWOMP,         1200, 352, SD),
            (db.GIANT_DRY_BONES,1350, 448, SD),
            (db.AMP,            1450, 352, SD),
            (db.AMP,            1450, 416, SD),
        ]
        for stype, x, y, sd in escape_adds:
            cx, cy = clamp_to_zone(z3, x, y)
            area3.sprites.append(Sprite(stype=stype, x=cx, y=cy, spritedata=sd, zone_id=0, extra_byte=0))
        area3.loaded_sprites = sorted(set(s.stype for s in area3.sprites))
        arc.set_file('course/course3.bin', serialize_course_bin(area3))

    packed = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(packed)
    print(f'Saved: {dst} ({len(packed)} bytes)')
    print('Modified 5-Castle: Briar Bastion (Chaos Edition)')



def create_level_5_cannon():
    """5-Cannon: Thornbolt Catapult. Cave gauntlet rebuilt from scratch.
    Chain Chomps, Broozers, Big Boos, Fire Bars. Cannon to World 8.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin,
        parse_layer_data, serialize_layer_data,
        Sprite, LayerObject, Entrance, Zone, Bounding, Tileset,
    )

    src = 'extracted files/Stage/05-36.arc'
    dst = 'output/ChaosStation/Stage/05-36.arc'
    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 5-Cannon: couldn't open {src} - {e}")
        return

    def safe_get(path):
        try: return arc.get_file(path)
        except KeyError: return None

    area = parse_course_bin(arc.get_file('course/course1.bin'))
    area.layer0 = parse_layer_data(safe_get('course/course1_bgdatL0.bin') or b'')
    area.layer1 = parse_layer_data(safe_get('course/course1_bgdatL1.bin') or b'')
    area.layer2 = parse_layer_data(safe_get('course/course1_bgdatL2.bin') or b'')
    area.sprites.clear(); area.entrances.clear(); area.zones.clear(); area.boundings.clear()
    area.layer0.clear(); area.layer1.clear(); area.layer2.clear()
    area.tileset = Tileset(slot0=db.TILESET_STANDARD, slot1=db.TILESET_CAVE, slot2='', slot3='')
    area.settings.time_limit = 200

    area.zones.append(Zone(x=256, y=256, w=2560, h=512, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, cam_zoom=0, visibility=0))
    area.boundings.append(Bounding(upper=0, lower=0, upper2=0, lower2=0, bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0))

    SD = bytes(6)
    fb_cw = b'\x00\x00\x00\x00\x10\x07'
    fb_ccw = b'\x00\x00\x00\x00\x00\x07'
    TX, GY = 16, 45

    def add_ground(x, y, w, h):
        area.layer1.append(LayerObject(tileset=1, obj_type=db.CaveObjs.GROUND_TOP, x=x, y=y, w=w, h=1))
        if h > 1: area.layer1.append(LayerObject(tileset=1, obj_type=db.CaveObjs.GROUND_FILL, x=x, y=y+1, w=w, h=h-1))
    def spr(stype, x, y, data=SD):
        area.sprites.append(Sprite(stype=stype, x=x, y=y, spritedata=data, zone_id=0, extra_byte=0))

    area.entrances.append(Entrance(x=(TX+2)*16, y=(GY-2)*16, entrance_id=0, dest_area=0, dest_entrance=0, etype=db.ENTRANCE_NORMAL, zone_id=0, layer=0, path=0, unk1=0, unk2=0, settings=0, leave_level=0, cp_direction=0))

    add_ground(TX, GY, 10, 7); add_ground(TX+13, GY+1, 6, 6)
    spr(db.CHAIN_CHOMP, (TX+4)*16, (GY-1)*16); spr(db.CHAIN_CHOMP, (TX+16)*16, GY*16)
    spr(db.BROOZER, (TX+7)*16, (GY-1)*16)

    add_ground(TX+22, GY-1, 5, 4); add_ground(TX+30, GY-3, 8, 4); add_ground(TX+30, GY+2, 8, 5)
    spr(db.BIG_BOO, (TX+25)*16, (GY-4)*16)
    spr(db.FIRE_BAR, (TX+32)*16, (GY-4)*16, fb_cw); spr(db.FIRE_BAR, (TX+36)*16, (GY-4)*16, fb_ccw)
    spr(db.AMP, (TX+28)*16, (GY-5)*16)
    spr(db.STAR_COIN, (TX+34)*16, (GY-8)*16, b'\x00\x00\x00\x00\x00\x00')

    add_ground(TX+42, GY, 12, 7); add_ground(TX+56, GY-2, 6, 4)
    spr(db.SLEDGE_BRO, (TX+45)*16, (GY-1)*16); spr(db.SLEDGE_BRO, (TX+51)*16, (GY-1)*16)
    spr(db.GIANT_DRY_BONES, (TX+58)*16, (GY-3)*16)
    spr(db.BROOZER, (TX+48)*16, (GY-1)*16)
    spr(db.MIDWAY_FLAG, (TX+60)*16, (GY-3)*16)

    add_ground(TX+65, GY+1, 4, 6); add_ground(TX+72, GY-1, 5, 5); add_ground(TX+80, GY+2, 4, 5); add_ground(TX+87, GY-2, 6, 4)
    spr(db.FIRE_BAR, (TX+66)*16, GY*16, fb_ccw); spr(db.FIRE_BAR, (TX+74)*16, (GY-2)*16, fb_cw)
    spr(db.FIRE_BAR, (TX+82)*16, (GY+1)*16, fb_ccw)
    spr(db.BIG_BOO, (TX+78)*16, (GY-6)*16); spr(db.AMP, (TX+70)*16, (GY-4)*16)
    spr(db.BULLET_BILL_LAUNCHER, (TX+76)*16, (GY-3)*16)
    spr(db.STAR_COIN, (TX+89)*16, (GY-6)*16, b'\x00\x00\x00\x00\x01\x00')

    add_ground(TX+96, GY, 5, 7); add_ground(TX+104, GY-4, 5, 5); add_ground(TX+112, GY-1, 4, 3)
    spr(db.CHAIN_CHOMP, (TX+97)*16, (GY-1)*16); spr(db.CHAIN_CHOMP, (TX+106)*16, (GY-5)*16)
    spr(db.FIRE_BAR, (TX+108)*16, (GY-5)*16, fb_cw)
    spr(db.BIG_BOO, (TX+100)*16, (GY-8)*16)
    spr(db.BULLET_BILL_LAUNCHER, (TX+110)*16, (GY-2)*16)

    add_ground(TX+119, GY, 15, 7); add_ground(TX+123, GY-5, 8, 6)
    spr(db.BROOZER, (TX+121)*16, (GY-1)*16); spr(db.BROOZER, (TX+126)*16, (GY-6)*16)
    spr(db.SLEDGE_BRO, (TX+130)*16, (GY-1)*16)
    spr(db.BIG_BOO, (TX+125)*16, (GY-10)*16)
    spr(db.STAR_COIN, (TX+127)*16, (GY-10)*16, b'\x00\x00\x00\x00\x02\x00')
    spr(434, (TX+130)*16, (GY-6)*16, b'\x00\x00\x00\x00\x00\x03')  # Cannon -> W8

    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))
    arc.set_file('course/course1_bgdatL0.bin', serialize_layer_data(area.layer0))
    arc.set_file('course/course1_bgdatL1.bin', serialize_layer_data(area.layer1))
    arc.set_file('course/course1_bgdatL2.bin', serialize_layer_data(area.layer2))
    data = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f: f.write(data)
    print(f'Saved: {dst} ({len(data)} bytes)')
    print('Created 5-Cannon: Thornbolt Catapult (W8 destination)')


def create_level_5_ambush():
    """Modify W5 ambushes (05-33/34/35) - CHAOTIC bespoke variants."""
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    SD = bytes(6)
    fb_sd_cw = b'\x00\x00\x00\x00\x10\x07'
    fb_sd_ccw = b'\x00\x00\x00\x00\x00\x07'

    enemy_cycle_by_file = {
        '05-33.arc': [db.SLEDGE_BRO, db.AMP, db.CHAIN_CHOMP, db.BRAMBALL],
        '05-34.arc': [db.BIG_PIRANHA_PLANT, db.CHAIN_CHOMP, db.SLEDGE_BRO, db.AMP],
        '05-35.arc': [db.AMP, db.SLEDGE_BRO, db.BIG_PIRANHA_PLANT, db.CHAIN_CHOMP],
    }

    additions = {
        '05-33.arc': [
            (db.BIG_BOO, 632, 320, SD),
            (db.BIG_BOO, 888, 320, SD),
            (db.FIRE_PIRANHA_PLANT, 760, 432, SD),
            (db.FIRE_BAR, 760, 408, fb_sd_cw),
            (db.CHAIN_CHOMP, 704, 448, SD),
            (db.CHAIN_CHOMP, 816, 448, SD),
        ],
        '05-34.arc': [
            (db.BIG_PIRANHA_PLANT, 760, 448, SD),
            (db.SLEDGE_BRO, 760, 400, SD),
            (db.FIRE_BAR, 700, 416, fb_sd_ccw),
            (db.FIRE_BAR, 820, 416, fb_sd_cw),
            (db.CHAIN_CHOMP, 656, 448, SD),
            (db.CHAIN_CHOMP, 864, 448, SD),
        ],
        '05-35.arc': [
            (db.BIG_BOO, 608, 312, SD),
            (db.BIG_BOO, 912, 312, SD),
            (db.FIRE_PIRANHA_PLANT, 688, 432, SD),
            (db.FIRE_PIRANHA_PLANT, 832, 432, SD),
            (db.FIRE_BAR, 760, 408, fb_sd_ccw),
            (db.GIANT_DRY_BONES, 760, 456, SD),
        ],
    }

    for suffix in ['33', '34', '35']:
        fname = f'05-{suffix}.arc'
        src = f'extracted files/Stage/{fname}'
        dst = f'output/ChaosStation/Stage/{fname}'

        try:
            arc = U8Archive.load(open(src, 'rb').read())
        except Exception as e:
            print(f"  Skipping {fname}: {e}")
            continue

        area = parse_course_bin(arc.get_file('course/course1.bin'))
        z = area.zones[0] if area.zones else None
        area.settings.time_limit = 65

        def clamped(x, y, pad=24):
            if z is None:
                return x, y
            cx = min(max(x, z.x + pad), z.x + z.w - pad)
            cy = min(max(y, z.y + pad), z.y + z.h - pad)
            return cx, cy

        cycle = enemy_cycle_by_file[fname]
        new_sprites = []
        enemy_idx = 0
        for s in area.sprites:
            if s.stype == 264:
                ns = copy.deepcopy(s)
                ns.stype = cycle[enemy_idx % len(cycle)]
                ns.spritedata = SD
                new_sprites.append(ns)
                enemy_idx += 1
            else:
                new_sprites.append(s)

        for stype, x, y, sd in additions[fname]:
            cx, cy = clamped(x, y)
            new_sprites.append(Sprite(stype=stype, x=cx, y=cy, spritedata=sd, zone_id=0, extra_byte=0))

        area.sprites = new_sprites
        area.loaded_sprites = sorted(set(s.stype for s in new_sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area))

        packed = arc.pack()
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(packed)
        print(f'Saved: {dst} ({len(packed)} bytes)')

    print('Modified World 5 Ambushes: Jungle Snap Patrol (Chaotic)')


def create_level_5_ghost_house():
    """5-GH: The Gloom Manor — dark ghost house with visibility=36.
    Area 1: 4 rooms with Boos, Dry Bones, Broozers, Swoops.
    Area 2: Attic with normal goal pole and red goal pole secret exit.
    Door pattern: sprite 276 at same pixel Y as entrance.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db
    builder = LevelBuilder()

    # AREA 1
    a1 = builder.add_area(1)
    a1.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a1.set_background(bg2=db.BG_GHOST_HOUSE)
    a1.set_time(400)
    a1.add_zone(0, 0, 7000, 640, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=0, visibility=36)

    a1.add_ground(0, 26, 280, 5, tileset=1)
    a1.add_ground(0, 5, 280, 3, tileset=1)
    a1.add_ground(0, 22, 12, 8, tileset=1)
    a1.add_entrance(0, 3 * 16, 20 * 16, etype=db.ENTRANCE_NORMAL)
    a1.add_sprite(10, 3 * 16, 20 * 16)

    # Room 1: Foyer (X 12-78)
    a1.add_ground(20, 20, 12, 2, tileset=1)
    a1.add_ground(50, 18, 10, 2, tileset=1)
    a1.add_sprite(db.GLOW_BLOCK, 40 * 16, 18 * 16)
    a1.add_sprite(db.BOO, 25 * 16, 17 * 16)
    a1.add_sprite(db.BOO, 35 * 16, 15 * 16)
    a1.add_sprite(db.BOO, 50 * 16, 20 * 16)
    a1.add_sprite(db.BOO, 55 * 16, 18 * 16)
    a1.add_sprite(db.BIG_BOO, 65 * 16, 13 * 16)
    a1.add_sprite(db.DRY_BONES, 30 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 50 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 70 * 16, 25 * 16)
    a1.add_sprite(db.BROOZER, 40 * 16, 25 * 16)
    a1.add_sprite(db.SWOOP, 25 * 16, 7 * 16)
    a1.add_sprite(db.SWOOP, 55 * 16, 7 * 16)
    a1.add_ground(78, 5, 3, 7, tileset=1)
    a1.add_sprite(db.STAR_COIN, 79 * 16, 8 * 16, spritedata=bytes([0,0,0,0,0,0]))

    # Room 2: Gallery (X 82-163) + secret door
    a1.add_ground(82, 20, 22, 2, tileset=1)
    a1.add_ground(82, 10, 16, 2, tileset=1)
    a1.add_ground(110, 18, 14, 2, tileset=1)
    a1.add_ground(145, 20, 18, 2, tileset=1)
    a1.add_sprite(db.GLOW_BLOCK, 90 * 16, 9 * 16)
    # Secret door on upper shelf
    a1.add_sprite(276, 84 * 16, 9 * 16)
    a1.add_entrance(2, 84 * 16, 9 * 16, etype=db.ENTRANCE_DOOR, dest_area=2, dest_entrance=1)
    a1.add_sprite(db.BOO, 90 * 16, 14 * 16)
    a1.add_sprite(db.BOO, 105 * 16, 17 * 16)
    a1.add_sprite(db.BIG_BOO, 115 * 16, 11 * 16)
    a1.add_sprite(db.BOO, 140 * 16, 16 * 16)
    a1.add_sprite(db.BOO, 155 * 16, 10 * 16)
    a1.add_sprite(db.DRY_BONES, 100 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 130 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 150 * 16, 25 * 16)
    a1.add_sprite(db.SWOOP, 95 * 16, 7 * 16)
    a1.add_sprite(db.SWOOP, 135 * 16, 7 * 16)
    a1.add_ground(163, 5, 3, 5, tileset=1)
    a1.add_sprite(db.MIDWAY_FLAG, 125 * 16, 13 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Room 3: Boo Ballroom (X 167-259)
    a1.add_ground(185, 16, 14, 2, tileset=1)
    a1.add_ground(205, 12, 10, 2, tileset=1)
    a1.add_ground(225, 18, 12, 2, tileset=1)
    a1.add_sprite(db.GLOW_BLOCK, 200 * 16, 21 * 16)
    for bx in [170, 183, 197, 215, 228, 244, 255]:
        a1.add_sprite(db.BOO, bx * 16, 8 * 16)
    for bx in [175, 195, 210, 232, 250]:
        a1.add_sprite(db.BOO, bx * 16, 21 * 16)
    a1.add_sprite(db.BIG_BOO, 188 * 16, 12 * 16)
    a1.add_sprite(db.BIG_BOO, 240 * 16, 14 * 16)
    a1.add_sprite(db.BROOZER, 205 * 16, 25 * 16)
    a1.add_sprite(db.BROOZER, 225 * 16, 25 * 16)
    a1.add_sprite(db.BROOZER, 250 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 180 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 200 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 240 * 16, 25 * 16)
    a1.add_sprite(db.SWOOP, 190 * 16, 7 * 16)
    a1.add_sprite(db.SWOOP, 220 * 16, 7 * 16)
    a1.add_sprite(db.SWOOP, 250 * 16, 7 * 16)
    a1.add_sprite(db.STAR_COIN, 224 * 16, 10 * 16, spritedata=bytes([0,0,0,0,1,0]))
    a1.add_ground(259, 5, 3, 5, tileset=1)

    # Room 4: Vault (X 263-280) + normal door
    a1.add_ground(265, 20, 15, 2, tileset=1)
    a1.add_sprite(276, 270 * 16, 25 * 16)
    a1.add_entrance(1, 270 * 16, 25 * 16, etype=db.ENTRANCE_DOOR, dest_area=2, dest_entrance=0)
    a1.add_sprite(db.BIG_BOO, 265 * 16, 16 * 16)
    a1.add_sprite(db.BOO, 270 * 16, 18 * 16)
    a1.add_sprite(db.BOO, 275 * 16, 18 * 16)
    a1.add_sprite(db.BROOZER, 265 * 16, 25 * 16)
    a1.add_sprite(db.BROOZER, 275 * 16, 25 * 16)
    a1.add_sprite(db.DRY_BONES, 272 * 16, 25 * 16)
    a1.add_sprite(db.SWOOP, 285 * 16, 7 * 16)
    a1.add_sprite(db.STAR_COIN, 270 * 16, 16 * 16, spritedata=bytes([0,0,0,0,2,0]))
    a1.add_ground(278, 5, 3, 21, tileset=1)

    # AREA 2 — The Attic
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a2.set_background(bg2=db.BG_GHOST_HOUSE)
    a2.set_time(300)
    a2.add_zone(0, 0, 3000, 480, zone_id=0, music=db.MUSIC_GHOST_HOUSE, cam_mode=0, visibility=36)
    a2.add_ground(0, 20, 200, 8, tileset=1)
    a2.add_ground(0, 5, 200, 3, tileset=1)

    a2.add_entrance(0, 5 * 16, 19 * 16, etype=db.ENTRANCE_DOOR)
    a2.add_sprite(276, 5 * 16, 19 * 16)
    a2.add_entrance(1, 60 * 16, 19 * 16, etype=db.ENTRANCE_DOOR)
    a2.add_sprite(276, 60 * 16, 19 * 16)

    # Normal exit
    a2.add_sprite(db.BIG_BOO, 30 * 16, 15 * 16)
    a2.add_sprite(db.BOO, 45 * 16, 17 * 16)
    a2.add_sprite(db.DRY_BONES, 40 * 16, 19 * 16)
    a2.add_sprite(db.GOAL_POLE, 55 * 16, 19 * 16)

    # Secret exit — Red Goal Pole
    a2.add_sprite(db.BIG_BOO, 82 * 16, 14 * 16)
    a2.add_sprite(db.BOO, 90 * 16, 16 * 16)
    a2.add_sprite(db.BOO, 100 * 16, 14 * 16)
    a2.add_sprite(db.DRY_BONES, 85 * 16, 19 * 16)
    a2.add_sprite(db.DRY_BONES, 100 * 16, 19 * 16)
    a2.add_sprite(db.GOAL_POLE, 115 * 16, 19 * 16, spritedata=bytes([0,0,16,0,0,0]))
    a2.add_sprite(276, 115 * 16, 19 * 16)
    a2.add_entrance(2, 115 * 16, 19 * 16, etype=db.ENTRANCE_DOOR, leave_level=1)

    builder.save('output/ChaosStation/Stage/05-21.arc')
    print('Created 5-GH: The Gloom Manor (dark, 2-area)')


def create_level_5_tower():
    """Modify 05-22: Briarclock Tower — CHAOTIC vertical gauntlet.

    Area 1 (The Climb): Vertical ascending with spiked-wall platforms (vanilla mechanic).
            Hazards lean into this: Skewers crush from alternating sides, Big Boos
            lurk in the gaps, Fire Bars spin at every choke point to deny safe landing.
    Area 2 (Boss Arena — Iggy's Tower Cage):
            Skewers rise from floor and descend from ceiling at structured intervals,
            forcing constant lateral dodging. A ring of Amps cuts the center vertical path.
            Fire Bars spin at mid-height on each side (not top/bottom — the Skewers own those).
    Area 3 (Escape): Dense Amp corridor + Fire Bar pair at the bottleneck.
    """
    import copy
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/05-22.arc'
    dst = 'output/ChaosStation/Stage/05-22.arc'

    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping 5-Tower: couldn't open {src} - {e}")
        return

    def safe_get(path):
        try:
            return arc.get_file(path)
        except KeyError:
            return None

    SD = bytes(6)
    fb_sd_cw  = b'\x00\x00\x00\x00\x10\x07'
    fb_sd_ccw = b'\x00\x00\x00\x00\x00\x07'
    fb_long_cw  = b'\x00\x00\x00\x00\x18\x07'
    fb_long_ccw = b'\x00\x00\x00\x00\x08\x07'

    def clamp_to_zone(zone, x, y, pad=24):
        if zone is None:
            return x, y
        cx = min(max(x, zone.x + pad), zone.x + zone.w - pad)
        cy = min(max(y, zone.y + pad), zone.y + zone.h - pad)
        return cx, cy

    # ══════════════════════════════════════
    #  AREA 1 — The Climb (vertical ascent)
    # ══════════════════════════════════════
    area1_data = safe_get('course/course1.bin')
    if area1_data:
        area1 = parse_course_bin(area1_data)
        area1.settings.time_limit = 235
        z1 = area1.zones[0] if area1.zones else None

        # Strip weaker filler enemies, keep Dry Bones and upgrade half
        strip_types = {db.CROWBER, db.FIRE_BRO, db.SPIKE_TOP, db.KOOPA_PARATROOPA, db.BRAMBALL}
        climb_sprites = []
        dry_idx = 0
        for s in area1.sprites:
            if s.stype in strip_types:
                continue
            ns = copy.deepcopy(s)
            if s.stype == db.DRY_BONES:
                if dry_idx % 3 == 0:
                    ns.stype = db.GIANT_DRY_BONES
                dry_idx += 1
            climb_sprites.append(ns)

        # Climb bands — varied X positions (left wall, center, right wall) and enemy types
        # Every band is distinct: no two consecutive bands share the same enemy type.
        # Y values decrease = higher up the tower (vertical level)
        climb_bands = [
            # (stype, x, y, spritedata)
            # Lower third — introduce the threats
            (db.CHAIN_CHOMP,    640, 3200, SD),
            (db.BIG_BOO,        896, 3056, SD),
            (db.AMP,            640, 2900, SD),
            (db.AMP,            1024,2900, SD),   # Two Amps flanking the path
            (db.FIRE_BAR,       860, 2720, fb_sd_cw),
            (db.SLEDGE_BRO,     640, 2580, SD),
            (db.CHAIN_CHOMP,    860, 2440, SD),   # Chain Chomp replaces removed Skewer
            (db.BIG_BOO,        1024,2300, SD),
            # Middle third — pace quickens
            (db.CHAIN_CHOMP,    720, 2160, SD),
            (db.AMP,            860, 2000, SD),
            (db.FIRE_BAR,       640, 1840, fb_sd_ccw),
            (db.BIG_BOO,        860, 1720, SD),   # Big Boo replaces removed Skewer
            (db.SLEDGE_BRO,     960, 1580, SD),
            (db.BIG_BOO,        700, 1440, SD),
            (db.AMP,            1024,1280, SD),
            # Upper third — final push
            (db.FIRE_BAR,       860, 1140, fb_long_cw),
            (db.CHAIN_CHOMP,    640, 1000, SD),
            (db.AMP,            860,  880, SD),   # Amp replaces removed Skewer
            (db.GIANT_DRY_BONES,700,  800, SD),
            (db.AMP,            640,  720, SD),
            (db.AMP,            1024, 720, SD),
        ]

        for stype, x, y, sd in climb_bands:
            cx, cy = clamp_to_zone(z1, x, y)
            climb_sprites.append(Sprite(stype=stype, x=cx, y=cy, spritedata=sd, zone_id=0, extra_byte=0))

        area1.sprites = climb_sprites
        area1.loaded_sprites = sorted(set(s.stype for s in climb_sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ══════════════════════════════════════
    #  AREA 2 — Tower Boss Arena
    # ══════════════════════════════════════
    # Iggy's Tower fight: moving platforms shifting on spiked walls.
    # Our additions are WALL-THEMED:
    #   - Skewers from ceiling + floor = constant vertical pressure
    #   - Amp ring cuts the center vertical space — forces edge platforming
    #   - Two long Fire Bars spin at mid-height on each side
    #   - One Giant Dry Bones guards the floor on each side
    area2_data = safe_get('course/course2.bin')
    if area2_data:
        area2 = parse_course_bin(area2_data)
        area2.settings.time_limit = 235
        z2 = area2.zones[0] if area2.zones else None
        boss_sprites = list(area2.sprites)

        ctrl_ids = {372, 407, 408, 436}
        cands = [s for s in boss_sprites if s.stype in ctrl_ids]
        if cands:
            cx, cy = cands[0].x, cands[0].y
        elif z2:
            cx, cy = z2.x + z2.w // 2, z2.y + z2.h // 2
        else:
            cx, cy = 512, 448

        arena_add = [
            # Long Fire Bars spinning at mid-height on each side of the arena
            (db.FIRE_BAR, -240,  0, fb_long_cw),
            (db.FIRE_BAR,  240,  0, fb_long_ccw),
            # Amp diamond at center — denies the "safe middle" position
            (db.AMP,   0,  -48, SD),
            (db.AMP, -48,    0, SD),
            (db.AMP,  48,    0, SD),
            (db.AMP,   0,   48, SD),
            # Giant Dry Bones guard the floor edges — discourages standing in corners
            (db.GIANT_DRY_BONES, -280, 80, SD),
            (db.GIANT_DRY_BONES,  280, 80, SD),
            # Single Big Boo — furthest from Mario (right side of arena)
            (db.BIG_BOO, 144, -80, SD),
        ]

        for stype, dx, dy, sd in arena_add:
            px, py = clamp_to_zone(z2, cx + dx, cy + dy)
            boss_sprites.append(Sprite(stype=stype, x=px, y=py, spritedata=sd, zone_id=0, extra_byte=0))

        area2.sprites = boss_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # ══════════════════════════════════════
    #  AREA 3 — Escape Corridor
    # ══════════════════════════════════════
    # Dense Amp + Fire Bar bottleneck with a Sledge Bro at the exit
    area3_data = safe_get('course/course3.bin')
    if area3_data:
        area3 = parse_course_bin(area3_data)
        z3 = area3.zones[0] if area3.zones else None
        escape_adds = [
            (db.AMP,          480, 352, SD),
            (db.AMP,          480, 416, SD),   # Vertical Amp pair at entry
            (db.CHAIN_CHOMP,  620, 448, SD),
            (db.FIRE_BAR,     720, 400, fb_sd_cw),
            (db.FIRE_BAR,     720, 400, fb_sd_ccw),  # Interlocked counter-spin
            (db.BIG_BOO,      820, 328, SD),
            (db.SLEDGE_BRO,   960, 416, SD),
            (db.AMP,         1060, 352, SD),
            (db.AMP,         1060, 416, SD),   # Exit Amp pair forces precision
        ]
        for stype, x, y, sd in escape_adds:
            cx, cy = clamp_to_zone(z3, x, y)
            area3.sprites.append(Sprite(stype=stype, x=cx, y=cy, spritedata=sd, zone_id=0, extra_byte=0))
        area3.loaded_sprites = sorted(set(s.stype for s in area3.sprites))
        arc.set_file('course/course3.bin', serialize_course_bin(area3))

    packed = arc.pack()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(packed)
    print(f'Saved: {dst} ({len(packed)} bytes)')
    print('Modified 5-Tower: Briarclock Tower (Chaos Edition)')



def create_peach_castle_farm():
    """Modify 01-41.arc to include a Koopa and staircase for infinite 1-Ups."""
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import (
        parse_course_bin, serialize_course_bin, Sprite, LayerObject,
        parse_layer_data, serialize_layer_data
    )
    from tools.level_builder import StandardObjs
    import tools.sprite_db as db
    
    src = 'extracted files/Stage/01-41.arc'
    dst = 'output/ChaosStation/Stage/01-41.arc'
    
    print("Modifying Peach's Castle for Infinite 1-Up Farm...")
    
    try:
        arc = U8Archive.load(open(src, 'rb').read())
    except Exception as e:
        print(f"Skipping Peach's Castle: couldn't open {src} - {e}")
        return
        
    try:    
        # Load the course file
        course_data = arc.get_file('course/course1.bin')
        area = parse_course_bin(course_data)

        # The player found the Koopa shell jump trick too difficult to execute.
        # We will place a massive line of blocks, but leave gaps so the 1-Ups can fall down.
        # Toad is at X=768, Y=512.
        # Floor is at Y=512. A standard jump reaches about 4 tiles high (64 pixels).
        # We will place the blocks at Y=448.
        # We'll cover a width of 40 blocks, but only place 2 blocks then a 1 block gap.
        start_x = 768 - (20 * 16) # Center around Toad
        for i in range(40):
            # Skip every 3rd block to create a hole for 1-Ups to fall through
            if i % 3 == 2:
                continue
                
            # Byte 11 drops a 1-Up Mushroom.
            item_byte = 11
            block = Sprite(
                stype=209, x=start_x + (i * 16), y=448, 
                spritedata=bytes([0, 0, 0, 0, 0, item_byte]), zone_id=0, extra_byte=0
            )
            area.sprites.append(block)
            
        area.loaded_sprites = sorted(set(s.stype for s in area.sprites))
        arc.set_file('course/course1.bin', serialize_course_bin(area))
        
        # Write to destination
        data = arc.pack()
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as f:
            f.write(data)
            
        print(f'Saved: {dst} ({len(data)} bytes)')

    except Exception as e:
        print(f"Error modifying Peach's Castle: {e}")


# ═══════════════════════════════════════════════════════════════════
#  WORLD 6 LEVELS
# ═══════════════════════════════════════════════════════════════════

def create_level_6_1():
    """06-01: Cliffside Stampede — Chain Chomps, Thwomps, REQUIRED vine swings.
    Three mandatory vine crossings over wide chasms. Stepping-stone platforms
    lead up to vine height. Enemies everywhere. Star coins in risky spots."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, "Pa1_gake")
    a.set_tileset(2, "Pa2_gake")
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(500)
    a.add_zone(0, 0, 15000, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0, visibility=16)

    GY = 26
    VINE = 464  # Climbable Swinging Vine / Chain

    # =======================================================================
    # SECTION A: Chain Chomp Cliffs (X 0-95)
    # Intro section with Chain Chomps, building to the first required vine
    # =======================================================================
    a.add_ground(0, GY, 14, 5, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 142 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 10 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 12 * 16, (GY - 1) * 16)

    a.add_ground(18, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 22 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 25 * 16, (GY - 5) * 16)
    a.add_question_block(20, GY - 4, contents=0)

    a.add_ground(32, GY - 3, 8, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 36 * 16, (GY - 4) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 38 * 16, (GY - 4) * 16)

    a.add_ground(44, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 48 * 16, (GY - 1) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 51 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 46 * 16, (GY - 6) * 16)

    a.add_ground(58, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.KOOPA, 61 * 16, (GY - 4) * 16)
    a.add_sprite(db.THWOMP, 62 * 16, (GY - 10) * 16)

    a.add_ground(68, GY, 12, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 72 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 76 * 16, (GY - 1) * 16)
    # Red coin ring — dodge the Chomps and Sledge Bro while grabbing 8 coins
    a.add_red_coin_ring(71, GY - 4, group_id=0x22, pattern='arc')

    a.add_ground(84, GY - 3, 8, 5, tileset=1)
    a.add_sprite(db.BUZZY_BEETLE, 86 * 16, (GY - 4) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 89 * 16, (GY - 4) * 16)
    a.add_sprite(db.PARAGOOMBA, 88 * 16, (GY - 8) * 16)

    # =======================================================================
    # VINE CROSSING 1 (REQUIRED) — X 96-124
    # Ground ends. Must climb stepping stones, grab vine, swing across chasm.
    # Star Coin #1 is below the vine path — risky drop mid-swing.
    # =======================================================================
    a.add_ground(96, GY, 6, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 99 * 16, (GY - 1) * 16)

    # Stepping stones UP (player climbs from GY to GY-8)
    a.add_ground(102, GY - 3, 3, 2, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 103 * 16, (GY - 6) * 16)
    a.add_ground(106, GY - 6, 3, 2, tileset=1)

    # Vine over the chasm — player grabs from the GY-6 step
    # Gap below is ~12 tiles wide, uncrossable without the vine
    a.add_sprite(VINE, 110 * 16, (GY - 7) * 16)

    # Star Coin #1 — below the vine, on a tiny ledge in the chasm
    # Must drop from vine mid-swing, grab coin, land on the ledge
    a.add_ground(111, GY + 1, 2, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 111 * 16, GY * 16, spritedata=bytes([0,0,0,0,0,0]))

    # Landing after vine swing — narrow platform with Thwomp
    a.add_ground(114, GY - 5, 4, 2, tileset=1)
    a.add_sprite(db.THWOMP, 116 * 16, (GY - 12) * 16)

    # Steps back down to ground level
    a.add_ground(119, GY - 3, 3, 2, tileset=1)
    a.add_ground(124, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 128 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 131 * 16, (GY - 1) * 16)

    # =======================================================================
    # SECTION B: Thwomp + Chomp Gauntlet (X 138-210)
    # Midway flag, then increasing pressure from Thwomps and Chain Chomps
    # =======================================================================
    a.add_ground(138, GY, 14, 5, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 142 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.KOOPA, 148 * 16, (GY - 1) * 16)
    a.add_question_block(145, GY - 4, contents=0)

    a.add_ground(156, GY, 8, 5, tileset=1)
    a.add_sprite(db.THWOMP, 159 * 16, (GY - 8) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 161 * 16, (GY - 1) * 16)

    a.add_ground(168, GY - 3, 8, 5, tileset=1)
    a.add_sprite(db.THWOMP, 172 * 16, (GY - 10) * 16)
    a.add_sprite(db.SLEDGE_BRO, 173 * 16, (GY - 4) * 16)
    a.add_sprite(db.PARAGOOMBA, 170 * 16, (GY - 8) * 16)

    a.add_ground(180, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 183 * 16, (GY - 1) * 16)
    a.add_sprite(db.THWOMP, 187 * 16, (GY - 8) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 186 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 188 * 16, (GY - 1) * 16)

    a.add_ground(194, GY - 4, 6, 5, tileset=1)
    a.add_sprite(db.THWOMP, 197 * 16, (GY - 11) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 198 * 16, (GY - 5) * 16)

    a.add_ground(204, GY, 10, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 208 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 211 * 16, (GY - 6) * 16)
    a.add_sprite(db.PARAGOOMBA, 206 * 16, (GY - 6) * 16)

    # =======================================================================
    # VINE CROSSING 2 (REQUIRED) — X 218-248
    # Harder: tighter steps, Paragoombas near the vine, Thwomp at landing.
    # Star Coin #2 on a high platform — must jump off vine at peak of swing.
    # =======================================================================
    a.add_ground(218, GY, 5, 5, tileset=1)
    a.add_sprite(db.BUZZY_BEETLE, 220 * 16, (GY - 1) * 16)

    # Stepping stones — tight 2-tile platforms
    a.add_ground(224, GY - 3, 2, 2, tileset=1)
    a.add_ground(227, GY - 6, 2, 2, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 226 * 16, (GY - 9) * 16)

    # Vine over wide chasm — must swing across
    a.add_sprite(VINE, 231 * 16, (GY - 7) * 16)
    a.add_sprite(db.PARAGOOMBA, 233 * 16, (GY - 5) * 16)

    # Star Coin #2 — high platform, only reachable by jumping UP from vine peak
    a.add_ground(233, GY - 12, 3, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 234 * 16, (GY - 13) * 16, spritedata=bytes([0,0,0,0,1,0]))

    # Landing — narrow with Thwomp directly above
    a.add_ground(235, GY - 4, 3, 2, tileset=1)
    a.add_sprite(db.THWOMP, 236 * 16, (GY - 11) * 16)

    # Steps down through enemies
    a.add_ground(239, GY - 2, 3, 2, tileset=1)
    a.add_sprite(db.BUZZY_BEETLE, 240 * 16, (GY - 3) * 16)
    a.add_ground(244, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 248 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 251 * 16, (GY - 1) * 16)

    # =======================================================================
    # SECTION C: Sledge Bro Stampede (X 258-360)
    # Sledge Bros + Thwomps + Chain Chomps in quick succession
    # =======================================================================
    a.add_ground(258, GY - 3, 8, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 262 * 16, (GY - 4) * 16)
    a.add_sprite(db.THWOMP, 264 * 16, (GY - 10) * 16)

    a.add_ground(270, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 274 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 277 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 272 * 16, (GY - 6) * 16)
    a.add_question_block(276, GY - 4, contents=0)

    a.add_ground(284, GY - 4, 6, 5, tileset=1)
    a.add_sprite(db.THWOMP, 287 * 16, (GY - 11) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 285 * 16, (GY - 5) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 288 * 16, (GY - 5) * 16)

    a.add_ground(294, GY, 8, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 297 * 16, (GY - 1) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 299 * 16, (GY - 1) * 16)
    a.add_coin_line(295, GY - 3, 3)

    a.add_ground(306, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.THWOMP, 309 * 16, (GY - 10) * 16)
    a.add_sprite(db.SLEDGE_BRO, 310 * 16, (GY - 4) * 16)
    a.add_sprite(db.PARAGOOMBA, 307 * 16, (GY - 8) * 16)

    a.add_ground(316, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 319 * 16, (GY - 1) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 323 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 321 * 16, (GY - 1) * 16)

    a.add_ground(330, GY - 4, 6, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 333 * 16, (GY - 5) * 16)
    a.add_sprite(db.THWOMP, 334 * 16, (GY - 11) * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 331 * 16, (GY - 9) * 16)

    a.add_ground(340, GY, 10, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 343 * 16, (GY - 1) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 347 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 345 * 16, (GY - 6) * 16)

    # =======================================================================
    # VINE CROSSING 3 (REQUIRED) — X 354-390
    # Hardest: smallest steps, enemies on steps, two Thwomps at landing,
    # Sledge Bro guards the other side.
    # Star Coin #3 is on a ledge below the landing — drop down to grab it.
    # =======================================================================
    a.add_ground(354, GY, 5, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 356 * 16, (GY - 1) * 16)

    # Tight stepping stones with enemies
    a.add_ground(360, GY - 3, 2, 2, tileset=1)
    a.add_sprite(db.BUZZY_BEETLE, 360 * 16, (GY - 4) * 16)
    a.add_ground(363, GY - 6, 2, 2, tileset=1)
    a.add_ground(367, GY - 8, 2, 2, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 365 * 16, (GY - 10) * 16)

    # Vine over the final chasm
    a.add_sprite(VINE, 371 * 16, (GY - 9) * 16)
    a.add_sprite(db.PARAGOOMBA, 373 * 16, (GY - 7) * 16)

    # Landing — guarded by double Thwomps and a Sledge Bro
    a.add_ground(375, GY - 6, 4, 2, tileset=1)
    a.add_sprite(db.THWOMP, 376 * 16, (GY - 13) * 16)
    a.add_sprite(db.THWOMP, 378 * 16, (GY - 13) * 16)

    # Star Coin #3 — ledge below landing, must drop down and walljump back
    a.add_ground(380, GY + 1, 2, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 380 * 16, GY * 16, spritedata=bytes([0,0,0,0,2,0]))

    # Steps down from vine landing
    a.add_ground(380, GY - 4, 3, 2, tileset=1)
    a.add_ground(384, GY - 2, 3, 2, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 385 * 16, (GY - 3) * 16)

    # =======================================================================
    # SECTION D: Final Gauntlet + Goal (X 390-460)
    # Everything at once — Chain Chomps, Thwomps, Sledge Bros
    # =======================================================================
    a.add_ground(390, GY, 12, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 393 * 16, (GY - 1) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 398 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 396 * 16, (GY - 6) * 16)

    a.add_ground(406, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.THWOMP, 409 * 16, (GY - 10) * 16)
    a.add_sprite(db.SLEDGE_BRO, 410 * 16, (GY - 4) * 16)

    a.add_ground(416, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 419 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 423 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 421 * 16, (GY - 1) * 16)
    a.add_sprite(db.THWOMP, 424 * 16, (GY - 8) * 16)

    a.add_ground(430, GY - 4, 6, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 433 * 16, (GY - 5) * 16)
    a.add_sprite(db.PARAGOOMBA, 434 * 16, (GY - 9) * 16)

    # Goal plateau
    a.add_ground(440, GY, 30, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 458 * 16, (GY - 1) * 16)

    builder.save("output/ChaosStation/Stage/06-01.arc")
    print("Created 06-01: Cliffside Stampede")


def create_level_6_2():
    """06-02: Bullet Bill Boulevard — Nonstop barrage of Bills and Bros."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, "Pa1_gake")
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(350)
    a.add_zone(0, 0, 12000, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0, visibility=16)

    GY = 30
    a.add_ground(0, GY, 12, 6, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 104 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)

    a.add_ground(15, GY, 6, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 17 * 16, (GY - 1) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 28 * 16, (GY - 6) * 16)

    a.add_ground(24, GY - 3, 5, 6, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 35 * 16, (GY - 8) * 16)

    a.add_ground(32, GY, 5, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 42 * 16, (GY + 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 42 * 16, (GY - 4) * 16)

    a.add_ground(40, GY - 5, 5, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 42 * 16, (GY - 6) * 16)

    a.add_ground(48, GY, 5, 6, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 58 * 16, (GY - 7) * 16)

    a.add_ground(56, GY - 3, 5, 6, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 66 * 16, (GY - 9) * 16)

    a.add_ground(64, GY, 5, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 74 * 16, (GY + 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 74 * 16, (GY - 4) * 16)

    a.add_ground(72, GY - 5, 5, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 74 * 16, (GY - 6) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 84 * 16, (GY - 10) * 16)

    a.add_ground(80, GY, 5, 6, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 90 * 16, (GY - 7) * 16)

    a.add_ground(88, GY - 3, 6, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 100 * 16, (GY + 2) * 16)

    a.add_ground(100, GY, 10, 6, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 104 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.KOOPA_PARATROOPA, 106 * 16, (GY - 8) * 16)

    for px, py, bill_y in [(112, GY - 6, GY - 12), (120, GY - 3, GY - 9), (128, GY - 8, GY - 14)]:
        a.add_ground(px, py, 3, 3, tileset=1)
        a.add_sprite(db.KOOPA_PARATROOPA, (px + 1) * 16, (py - 6) * 16)
        a.add_sprite(db.BULLET_BILL_LAUNCHER, (px + 6) * 16, bill_y * 16)

    a.add_sprite(db.STAR_COIN, 120 * 16, (GY - 16) * 16, spritedata=b'\x00\x00\x00\x00\x00\x00')

    a.add_ground(136, GY, 8, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 139 * 16, (GY - 1) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 148 * 16, (GY - 8) * 16)

    fb_cw = b'\x00\x00\x00\x00\x10\x07'
    for fx in [155, 168, 181, 194]:
        a.add_ground(fx, GY, 6, 6, tileset=1)
        a.add_sprite(db.FIRE_BAR, (fx + 3) * 16, (GY - 4) * 16, spritedata=fb_cw)
        a.add_sprite(db.BULLET_BILL_LAUNCHER, (fx + 8) * 16, (GY - 10) * 16)

    a.add_sprite(db.STAR_COIN, 175 * 16, (GY - 12) * 16, spritedata=bytes([0,0,0,0,1,0]))

    a.add_ground(207, GY, 8, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 210 * 16, (GY - 1) * 16)

    for lx, ly, lw in [(220, GY, 8), (232, GY - 5, 6), (242, GY, 7), (254, GY - 6, 6), (264, GY, 8), (276, GY - 5, 6)]:
        a.add_ground(lx, ly, lw, 6, tileset=1)
        a.add_sprite(db.SLEDGE_BRO, (lx + lw // 2) * 16, (ly - 1) * 16)
        a.add_sprite(db.BANZAI_BILL_LAUNCHER, (lx + lw + 3) * 16, (ly - 1) * 16)
        a.add_sprite(db.BANZAI_BILL_LAUNCHER, (lx + lw + 3) * 16, (ly + 5) * 16)

    a.add_ground(260, GY + 8, 3, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 261 * 16, (GY + 7) * 16, spritedata=bytes([0,0,0,0,2,0]))

    a.add_ground(290, GY, 8, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 293 * 16, (GY - 1) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 302 * 16, (GY - 8) * 16)

    a.add_ground(300, GY - 4, 6, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 310 * 16, (GY + 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 310 * 16, (GY - 5) * 16)

    a.add_ground(308, GY, 6, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 310 * 16, (GY - 1) * 16)

    a.add_ground(316, GY - 4, 6, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 318 * 16, (GY - 5) * 16)

    # === SECTION D: Bill Storm (X 326-410) ===
    # Nonstop Bullet Bills + Banzai Bills from both sides, tight platforms
    a.add_ground(326, GY, 8, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 329 * 16, (GY - 1) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 338 * 16, (GY - 6) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 338 * 16, (GY + 2) * 16)

    a.add_ground(338, GY - 5, 5, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 340 * 16, (GY - 6) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 347 * 16, (GY - 10) * 16)

    a.add_ground(346, GY, 6, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 356 * 16, (GY - 4) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 356 * 16, (GY + 3) * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 349 * 16, (GY - 7) * 16)

    a.add_ground(356, GY - 3, 5, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 358 * 16, (GY - 4) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 365 * 16, (GY - 9) * 16)

    a.add_ground(364, GY, 8, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 367 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BAR, 370 * 16, (GY - 3) * 16, spritedata=fb_cw)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 376 * 16, (GY + 2) * 16)

    a.add_ground(376, GY - 5, 5, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 378 * 16, (GY - 6) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 385 * 16, (GY - 10) * 16)

    a.add_ground(384, GY, 6, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 386 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 388 * 16, (GY - 7) * 16)

    a.add_ground(394, GY - 4, 5, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 404 * 16, (GY - 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 404 * 16, (GY + 5) * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 396 * 16, (GY - 9) * 16)

    # Goal
    a.add_ground(404, GY, 30, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 418 * 16, (GY - 1) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 418 * 16, (GY + 5) * 16)
    a.add_sprite(db.GOAL_POLE, 420 * 16, (GY - 1) * 16)
    builder.save("output/ChaosStation/Stage/06-02.arc")
    print("Created 06-02: Bullet Bill Boulevard")


def create_level_6_3():
    """06-03: Frozen Depths — Underground ice cavern with frozen water pools.
    Players navigate icy platforms over toxic/bottomless water, with Dry Bones
    rising from the water and Ice Bros on ledges. Icicles drip from above."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_SNOW)
    a.set_tileset(2, db.TILESET_CAVE)
    a.set_background(bg2=db.BG_UNDERGROUND)
    a.set_time(500)
    a.add_zone(0, 0, 15000, 640, zone_id=0, music=db.MUSIC_UNDERGROUND, cam_mode=0, visibility=16)

    GY = 26
    WATER_Y = GY + 6

    a.add_ground(0, GY, 14, 5, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 95 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)

    # Toxic water pools — a few fill sprites, not one per tile
    for wx in [0, 50, 100, 150, 200, 250, 300, 350]:
        a.add_sprite(db.POISON_FILL, wx * 16, WATER_Y * 16)

    # SECTION A: Ice Bridge Intro (X 14-90)
    # Narrow icy platforms over toxic water. Dry Bones patrol.
    a.add_ground(18, GY, 8, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 22 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICE_BRO, 24 * 16, (GY - 1) * 16)

    a.add_ground(30, GY, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 32 * 16, (GY - 1) * 16)

    a.add_ground(40, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 42 * 16, (GY - 4) * 16)
    a.add_sprite(db.ICE_BRO, 44 * 16, (GY - 4) * 16)

    a.add_ground(50, GY, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 52 * 16, (GY - 1) * 16)

    # Star Coin #1 — on a tiny ledge above Dry Bones
    a.add_ground(60, GY - 6, 3, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 61 * 16, (GY - 7) * 16, spritedata=b'\x00\x00\x00\x00\x00\x00')

    a.add_ground(66, GY, 8, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 69 * 16, (GY - 1) * 16)

    a.add_ground(78, GY - 3, 8, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 81 * 16, (GY - 4) * 16)
    a.add_sprite(db.DRY_BONES, 83 * 16, (GY - 4) * 16)

    # SECTION B: Icicle Drop Zone (X 90-160)
    # Icicles drip from the ceiling. Navigate the timing while crossing water.
    a.add_ground(90, GY, 12, 5, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 95 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Icicles at timed intervals
    for ix in [100, 108, 116, 124]:
        a.add_sprite(db.ICICLE, ix * 16, 8 * 16)

    a.add_ground(106, GY - 4, 5, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 108 * 16, (GY - 5) * 16)

    a.add_ground(118, GY, 5, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 120 * 16, (GY - 1) * 16)

    a.add_ground(128, GY - 3, 5, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 130 * 16, (GY - 4) * 16)

    # Star Coin #2 — between icicle drops, requires timing
    a.add_sprite(db.STAR_COIN, 112 * 16, (GY - 8) * 16, spritedata=bytes([0,0,0,0,1,0]))

    a.add_ground(138, GY, 8, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 141 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 143 * 16, (GY - 1) * 16)
    # Red coin ring — grab all 8 coins between icicle drops and Dry Bones
    a.add_red_coin_ring(140, GY - 5, group_id=0x22, pattern='circle')

    # SECTION C: Frozen Pipe Maze (X 160-240)
    # Pipes shooting fire into icy platforms over water.
    a.add_ground(150, GY, 10, 5, tileset=1)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 155 * 16, (GY - 1) * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 158 * 16, (GY - 1) * 16)

    a.add_ground(164, GY - 4, 5, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 166 * 16, (GY - 5) * 16)

    a.add_ground(174, GY, 6, 5, tileset=1)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 176 * 16, (GY - 1) * 16)

    a.add_ground(184, GY - 4, 5, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 186 * 16, (GY - 5) * 16)

    a.add_ground(194, GY, 6, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 196 * 16, (GY - 1) * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 198 * 16, (GY - 1) * 16)

    # Star Coin #3 — above the pipe section, guarded
    a.add_ground(180, GY - 10, 3, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 181 * 16, (GY - 11) * 16, spritedata=bytes([0,0,0,0,2,0]))

    # SECTION D: Dry Bones Gauntlet (X 220-290)
    a.add_ground(204, GY, 12, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 207 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 210 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICE_BRO, 213 * 16, (GY - 1) * 16)

    for ix in [220, 228, 236]:
        a.add_sprite(db.ICICLE, ix * 16, 8 * 16)

    a.add_ground(220, GY - 4, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 222 * 16, (GY - 5) * 16)

    a.add_ground(230, GY, 6, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 232 * 16, (GY - 1) * 16)

    a.add_ground(240, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 242 * 16, (GY - 4) * 16)

    a.add_ground(250, GY, 8, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 253 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICE_BRO, 255 * 16, (GY - 1) * 16)

    # SECTION E: Frozen Gauntlet (X 262-370)
    # Fire pipes + icicles + Dry Bones on narrowing platforms over water
    a.add_ground(262, GY - 3, 6, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 264 * 16, (GY - 4) * 16)
    a.add_sprite(db.ICICLE, 266 * 16, 8 * 16)

    a.add_ground(272, GY, 10, 5, tileset=1)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 275 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 278 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 280 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICICLE, 277 * 16, 8 * 16)

    a.add_ground(286, GY - 4, 5, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 288 * 16, (GY - 5) * 16)
    a.add_sprite(db.ICICLE, 289 * 16, 6 * 16)

    a.add_ground(295, GY, 8, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 297 * 16, (GY - 1) * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 300 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICICLE, 298 * 16, 8 * 16)
    a.add_sprite(db.ICICLE, 301 * 16, 8 * 16)
    a.add_question_block(296, GY - 4, contents=3)

    a.add_ground(307, GY - 3, 5, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 309 * 16, (GY - 4) * 16)
    a.add_sprite(db.ICE_BRO, 310 * 16, (GY - 4) * 16)

    a.add_ground(316, GY, 6, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 318 * 16, (GY - 1) * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 320 * 16, (GY - 1) * 16)

    a.add_ground(326, GY - 5, 5, 5, tileset=1)
    a.add_sprite(db.ICE_BRO, 328 * 16, (GY - 6) * 16)
    a.add_sprite(db.ICICLE, 329 * 16, 6 * 16)

    a.add_ground(335, GY, 10, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 337 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 340 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICE_BRO, 342 * 16, (GY - 1) * 16)
    a.add_sprite(db.ICICLE, 338 * 16, 8 * 16)
    a.add_sprite(db.ICICLE, 341 * 16, 8 * 16)

    a.add_ground(349, GY - 3, 5, 5, tileset=1)
    a.add_sprite(db.DRY_BONES, 351 * 16, (GY - 4) * 16)
    a.add_sprite(db.PIPE_FIRE_PIRANHA_UP, 352 * 16, (GY - 4) * 16)

    # Goal
    a.add_ground(358, GY, 30, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 376 * 16, (GY - 1) * 16)
    builder.save("output/ChaosStation/Stage/06-03.arc")
    print("Created 06-03: Frozen Depths")


def create_level_6_4():
    """06-04: Magma Crags — Volcanic cliff face with genuine height variation.
    Section A: staircase ASCENT (GY -> GY-12 in four steps).
    Section B: narrow ridge traverse at peak height.
    Section C: staircase DESCENT back to ground.
    Section D: lava COLUMN HOP — thin 2-3 tile pillars at alternating heights.
    Section E: multi-level finale with upper/mid/lower paths simultaneously.
    Completely different geometry from 6-3's flat ice platforms."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, "Pa1_gake")
    a.set_background(bg2=db.BG_CASTLE)
    a.set_time(400)
    a.add_zone(0, 0, 15000, 640, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, visibility=16)

    GY = 28   # base (differs from 6-3's GY=26 so even the ground feels different)
    fb_cw  = b'\x00\x00\x00\x00\x10\x06'
    fb_ccw = b'\x00\x00\x00\x00\x00\x06'

    # === INTRO LEDGE (X 0-14) ===
    a.add_ground(0, GY, 12, 5, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 85 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_sprite(db.FIRE_BRO, 8 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 10 * 16, (GY - 5) * 16)

    # === SECTION A: The Ascent (X 16-58) ===
    # Four staircase steps climbing UP the cliff face — each 4 tiles higher.
    # Player must commit to climbing; there's no flat shortcut.
    a.add_ground(16, GY - 4, 6, 5, tileset=1)       # step 1 — 4 up
    a.add_sprite(db.HAMMER_BRO, 19 * 16, (GY - 5) * 16)
    a.add_sprite(db.FIRE_BAR, 21 * 16, (GY - 10) * 16, spritedata=fb_cw)

    a.add_ground(26, GY - 8, 5, 5, tileset=1)        # step 2 — 8 up
    a.add_sprite(db.FIRE_BRO, 28 * 16, (GY - 9) * 16)
    a.add_sprite(db.FIRE_BAR, 30 * 16, (GY - 14) * 16, spritedata=fb_ccw)

    a.add_ground(35, GY - 12, 5, 5, tileset=1)       # step 3 — 12 up (first peak)
    a.add_sprite(db.CHAIN_CHOMP, 38 * 16, (GY - 13) * 16)

    # Star Coin #1 — on the first peak, Chain Chomp guards it
    a.add_sprite(db.STAR_COIN, 37 * 16, (GY - 14) * 16, spritedata=bytes([0,0,0,0,0,0]))
    a.add_sprite(db.FIRE_BAR, 37 * 16, (GY - 18) * 16, spritedata=fb_cw)

    # === SECTION B: Ridge Traverse (X 44-70) ===
    # Stay high! Narrow 2-3 tile ledges at GY-12, must hop between them.
    # One slip and you're falling the full 12 tiles to death.
    a.add_ground(44, GY - 12, 3, 2, tileset=1)       # narrow ridge 1
    a.add_sprite(db.THWOMP, 45 * 16, (GY - 19) * 16)

    a.add_ground(51, GY - 14, 3, 2, tileset=1)       # narrow ridge 2 — even higher
    a.add_sprite(db.FIRE_BRO, 52 * 16, (GY - 15) * 16)
    a.add_sprite(db.FIRE_BAR, 53 * 16, (GY - 20) * 16, spritedata=fb_ccw)

    a.add_ground(58, GY - 11, 3, 2, tileset=1)       # narrow ridge 3 — step back down
    a.add_sprite(db.PARAGOOMBA, 59 * 16, (GY - 15) * 16)

    # === SECTION C: The Descent (X 65-100) ===
    # Staircase back DOWN — narrower than the ascent, Thwomps at each step.
    a.add_ground(65, GY - 8, 4, 4, tileset=1)        # step down to -8
    a.add_sprite(db.THWOMP, 67 * 16, (GY - 15) * 16)
    a.add_sprite(db.HAMMER_BRO, 68 * 16, (GY - 9) * 16)

    a.add_ground(73, GY - 4, 4, 4, tileset=1)        # step down to -4
    a.add_sprite(db.FIRE_BRO, 75 * 16, (GY - 5) * 16)
    a.add_sprite(db.FIRE_BAR, 76 * 16, (GY - 10) * 16, spritedata=fb_cw)

    a.add_ground(81, GY, 12, 5, tileset=1)            # back to ground — midway breather
    a.add_sprite(db.MIDWAY_FLAG, 85 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.CHAIN_CHOMP, 89 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 91 * 16, (GY - 1) * 16)
    a.add_red_coin_ring(84, GY - 5, group_id=0x22, pattern='arc')

    # === SECTION D: Lava Column Hop (X 97-155) ===
    # Thin pillars (2-3 tiles wide) at ALTERNATING heights over lava pits.
    # Heights cycle: GY, GY-6, GY-3, GY-9, GY-5, GY-2, GY-8, GY-4
    # No two adjacent columns at the same height — constant up/down rhythm.
    col_data = [
        (97,  GY,     3),  # low
        (104, GY - 6, 2),  # high jump up
        (110, GY - 3, 3),  # medium
        (116, GY - 9, 2),  # very high
        (122, GY - 5, 3),  # medium-high
        (128, GY - 2, 2),  # near-low
        (134, GY - 8, 3),  # high
        (140, GY - 4, 2),  # medium
    ]
    for i, (cx, cy, cw) in enumerate(col_data):
        a.add_ground(cx, cy, cw, 5, tileset=1)
        if i % 2 == 0:
            a.add_sprite(db.FIRE_BRO, (cx + 1) * 16, (cy - 1) * 16)
        else:
            a.add_sprite(db.HAMMER_BRO, (cx + 1) * 16, (cy - 1) * 16)
        if i % 3 == 0:
            a.add_sprite(db.FIRE_BAR, (cx + 1) * 16, (cy - 6) * 16,
                         spritedata=fb_cw if i % 2 == 0 else fb_ccw)

    # Star Coin #2 — floating between columns at peak height (GY-10)
    a.add_sprite(db.STAR_COIN, 117 * 16, (GY - 11) * 16, spritedata=bytes([0,0,0,0,1,0]))

    # Reconvene on solid ground
    a.add_ground(148, GY, 10, 5, tileset=1)
    a.add_sprite(db.THWOMP, 152 * 16, (GY - 8) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 155 * 16, (GY - 1) * 16)

    # === SECTION E: Multi-Level Finale (X 162-240) ===
    # Three simultaneous paths at different heights — upper, mid, lower.
    # Player picks a route; all converge at the goal.
    # Upper path (GY-12): Hammer Bros, tight Fire Bars
    a.add_ground(162, GY - 12, 5, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 164 * 16, (GY - 13) * 16)
    a.add_sprite(db.FIRE_BAR, 165 * 16, (GY - 18) * 16, spritedata=fb_cw)

    a.add_ground(171, GY - 12, 4, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 173 * 16, (GY - 13) * 16)

    # Mid path (GY-6): Chain Chomps + Fire Bars
    a.add_ground(162, GY - 6, 6, 3, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 165 * 16, (GY - 7) * 16)
    a.add_sprite(db.FIRE_BAR, 167 * 16, (GY - 12) * 16, spritedata=fb_ccw)

    a.add_ground(172, GY - 6, 5, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 174 * 16, (GY - 7) * 16)
    a.add_sprite(db.THWOMP, 176 * 16, (GY - 13) * 16)

    # Lower path (GY): Sledge Bros, lava pits below
    a.add_ground(163, GY, 7, 5, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 166 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BAR, 168 * 16, (GY - 6) * 16, spritedata=fb_cw)

    a.add_ground(174, GY, 6, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 176 * 16, (GY - 1) * 16)

    # Star Coin #3 — only reachable from the lower path, guarded by Sledge Bro
    a.add_ground(181, GY + 2, 3, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 182 * 16, (GY + 1) * 16, spritedata=bytes([0,0,0,0,2,0]))
    a.add_sprite(db.SLEDGE_BRO, 183 * 16, (GY + 1) * 16)

    # All paths converge
    a.add_ground(186, GY - 6, 6, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 189 * 16, (GY - 7) * 16)
    a.add_sprite(db.FIRE_BAR, 190 * 16, (GY - 12) * 16, spritedata=fb_ccw)

    a.add_ground(196, GY, 10, 5, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 199 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 203 * 16, (GY - 1) * 16)
    a.add_sprite(db.THWOMP, 201 * 16, (GY - 8) * 16)
    a.add_sprite(db.FIRE_BAR, 200 * 16, (GY - 6) * 16, spritedata=fb_cw)

    # === GOAL ===
    a.add_ground(210, GY, 28, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 228 * 16, (GY - 1) * 16)
    builder.save("output/ChaosStation/Stage/06-04.arc")
    print("Created 06-04: Magma Crags")


def create_level_6_5():
    """06-05: Abyssal Trench — Deep ocean gauntlet. Horizontal swim through
    a sunken fortress. Mixes underwater swimming corridors with dry above-water
    platform sections on fortress ruins poking out of the water.

    Section A: Shore Approach — run along beach cliffs, descend into water.
    Section B: Sunken Halls — fully submerged swim through ruined corridors.
      Cheep Cheeps, Bloopers, Urchins on walls. Tight ceiling passages.
    Section C: Air Pocket — brief dry section on ruins above waterline.
      Hammer Bros on crumbling platforms with water below.
    Section D: The Deep — dark deep swim. Fishbones track the player,
      Blooper Nannies, Cheep Chomps pursue. Urchin mazes.
    Section E: Ascent — swim upward through vertical shaft to dry goal."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_OCEAN)
    a.set_background(bg2=db.BG_UNDERWATER)
    a.set_time(500)
    a.add_zone(0, 0, 8000, 640, zone_id=0, music=db.MUSIC_UNDERWATER, cam_mode=0)

    GY = 26   # ocean floor
    WY = 12   # water surface Y (water fills from here down)

    # Water fill — creates swim physics from WY downward
    a.add_sprite(db.WATER_FILL, 0, WY * 16, spritedata=b"\x01\x00\x00\x00\x00\x00")

    # === SECTION A: Shore Approach (X 0-35) ===
    # Player starts UNDERWATER already — low ceiling overhead from tile 0.
    # Forced into water immediately, no open sky to breathe easy in.
    a.add_ground(0, GY, 20, 6, tileset=1)           # shore/seabed platform
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 152 * 16, (WY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    # Low ceiling even at spawn — can't swim up and over
    a.add_ground(0, WY + 1, 35, 2, tileset=1)       # ceiling A (x=0-35)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 8 * 16, (WY + 5) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 14 * 16, (WY + 8) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 11 * 16, (WY + 6) * 16)

    # Staircase descending into water
    a.add_ground(20, GY + 2, 5, 4, tileset=1)
    a.add_ground(25, GY + 4, 5, 4, tileset=1)
    a.add_ground(30, GY + 6, 5, 4, tileset=1)       # submerged steps
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 26 * 16, (WY + 4) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 31 * 16, (WY + 7) * 16)

    # Ocean floor begins
    a.add_ground(35, GY + 8, 460, 4, tileset=1)     # long ocean floor

    # ── CONTINUOUS CEILING — prevents swimming over everything ──
    # Ceiling runs from x=0 to x=148 (Sections A+B), breaks for Air Pocket,
    # then x=195 to x=345 (Section D). Player is always boxed in.
    a.add_ground(35, WY + 1, 113, 2, tileset=1)     # ceiling B (x=35-148)
    a.add_ground(195, WY + 1, 150, 2, tileset=1)    # ceiling D (x=195-345)

    # === SECTION B: Sunken Halls (X 40-148) ===
    # Trapped under the ceiling. Packed with enemies. No escape upward.

    # Corridor 1 — Cheep Cheep swarm + Spiny Cheep Cheeps + Bloopers
    a.add_sprite(db.CHEEP_CHEEP,       42 * 16, (WY + 5) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 46 * 16, (WY + 8) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       50 * 16, (WY + 4) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 54 * 16, (WY + 9) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       58 * 16, (WY + 6) * 16)
    a.add_sprite(db.BLOOPER, 48 * 16, (WY + 6) * 16)
    a.add_sprite(db.BLOOPER, 56 * 16, (WY + 4) * 16)

    # Urchin wall #1 — pillar narrowing the passage
    a.add_ground(62, WY + 3, 3, 5, tileset=1)       # upper pillar
    a.add_ground(62, GY + 2, 3, 6, tileset=1)       # lower pillar
    a.add_sprite(db.URCHIN, 63 * 16, (WY + 8) * 16)
    a.add_sprite(db.URCHIN, 63 * 16, (GY + 1) * 16)

    # Corridor 2 — Blooper Nanny + Spiny Cheeps closing in
    a.add_sprite(db.BLOOPER_NANNY,     70 * 16, (WY + 5) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 74 * 16, (WY + 9) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       78 * 16, (WY + 4) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 82 * 16, (WY + 7) * 16)
    a.add_sprite(db.FISHBONE, 76 * 16, (GY + 7) * 16)
    a.add_sprite(db.BLOOPER, 85 * 16, (WY + 8) * 16)

    # Star Coin #1 — floor alcove, tight squeeze to reach
    a.add_ground(80, GY + 4, 4, 4, tileset=1)       # raised floor section
    a.add_sprite(db.STAR_COIN, 81 * 16, (GY + 3) * 16, spritedata=bytes([0,0,0,0,0,0]))
    a.add_sprite(db.URCHIN, 79 * 16, (GY + 5) * 16)
    a.add_sprite(db.URCHIN, 84 * 16, (GY + 5) * 16)

    # Urchin wall #2
    a.add_ground(90, WY + 3, 3, 4, tileset=1)
    a.add_ground(90, GY + 3, 3, 5, tileset=1)
    a.add_sprite(db.URCHIN, 91 * 16, (WY + 7) * 16)
    a.add_sprite(db.URCHIN, 91 * 16, (GY + 2) * 16)

    # Urchin zigzag maze — alternating ceiling/floor urchins, dense
    a.add_sprite(db.URCHIN, 96 * 16, (WY + 3) * 16)
    a.add_sprite(db.URCHIN, 100 * 16, (GY + 7) * 16)
    a.add_sprite(db.URCHIN, 104 * 16, (WY + 3) * 16)
    a.add_sprite(db.URCHIN, 108 * 16, (GY + 7) * 16)
    a.add_sprite(db.URCHIN, 112 * 16, (WY + 3) * 16)
    a.add_sprite(db.URCHIN, 116 * 16, (GY + 7) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 98 * 16, (WY + 7) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       106 * 16, (WY + 5) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 114 * 16, (WY + 8) * 16)
    a.add_sprite(db.FISHBONE, 102 * 16, (WY + 9) * 16)
    a.add_sprite(db.FISHBONE, 110 * 16, (WY + 4) * 16)

    # Ruined wall — two gaps, Fishbones on both sides
    a.add_ground(122, WY + 3, 3, 5, tileset=1)
    a.add_ground(122, GY + 2, 3, 6, tileset=1)
    a.add_sprite(db.FISHBONE, 125 * 16, (WY + 8) * 16)
    a.add_sprite(db.FISHBONE, 125 * 16, (GY + 1) * 16)
    a.add_sprite(db.FISHBONE, 120 * 16, (WY + 6) * 16)

    # Pre-air-pocket gauntlet — Big Cheep + Blooper Nanny
    a.add_sprite(db.BIG_CHEEP_CHEEP, 130 * 16, (WY + 5) * 16)
    a.add_sprite(db.BLOOPER_NANNY, 136 * 16, (WY + 7) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 133 * 16, (WY + 3) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 140 * 16, (WY + 9) * 16)
    a.add_sprite(db.BLOOPER, 143 * 16, (WY + 5) * 16)

    # === SECTION C: Air Pocket (X 148-195) ===
    # NO CEILING here — fortress ruins poke above waterline. Brief dry section.
    a.add_ground(148, WY, 20, 4, tileset=1)          # ruins platform (above water)
    a.add_ground(148, GY + 8, 20, 4, tileset=1)      # seafloor beneath
    a.add_sprite(db.HAMMER_BRO, 155 * 16, (WY - 1) * 16)
    a.add_sprite(db.FIRE_BRO, 162 * 16, (WY - 1) * 16)
    a.add_sprite(db.KOOPA, 158 * 16, (WY - 1) * 16)
    a.add_sprite(db.MIDWAY_FLAG, 152 * 16, (WY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Crumbling bridge over water — small platforms with gaps
    a.add_ground(170, WY + 1, 3, 2, tileset=1)
    a.add_ground(176, WY - 1, 3, 2, tileset=1)
    a.add_ground(182, WY + 1, 3, 2, tileset=1)
    a.add_sprite(db.CHEEP_CHEEP, 173 * 16, (WY + 4) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 179 * 16, (WY + 4) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 175 * 16, (WY + 7) * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 178 * 16, (WY - 3) * 16)

    # Star Coin #2 — under the crumbling bridge, guarded by Cheeps
    a.add_sprite(db.STAR_COIN, 176 * 16, (WY + 5) * 16, spritedata=bytes([0,0,0,0,1,0]))
    a.add_sprite(db.BLOOPER, 177 * 16, (WY + 8) * 16)

    # Dive back in
    a.add_ground(188, WY + 2, 5, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 190 * 16, (WY + 1) * 16)

    # === SECTION D: The Deep (X 195-345) ===
    # Ceiling is back! Trapped underwater, increasingly dense enemies.

    # Cheep Chomp zone — Boss Bass + spiny swarm (relentless chasers!)
    a.add_sprite(db.CHEEP_CHOMP,       200 * 16, (WY + 6) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 204 * 16, (WY + 3) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 208 * 16, (WY + 9) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       212 * 16, (WY + 5) * 16)
    a.add_sprite(db.FISHBONE, 216 * 16, (GY + 7) * 16)
    a.add_sprite(db.FISHBONE, 210 * 16, (WY + 4) * 16)
    a.add_sprite(db.BLOOPER, 206 * 16, (WY + 7) * 16)

    # Pillar forest — tall pillars, tight gaps, urchins + enemies in gaps
    for px in [222, 230, 238, 246, 254]:
        a.add_ground(px, WY + 3, 2, 11, tileset=1)
    a.add_sprite(db.URCHIN, 226 * 16, (WY + 5) * 16)
    a.add_sprite(db.URCHIN, 226 * 16, (WY + 10) * 16)
    a.add_sprite(db.URCHIN, 234 * 16, (WY + 7) * 16)
    a.add_sprite(db.URCHIN, 242 * 16, (WY + 4) * 16)
    a.add_sprite(db.URCHIN, 242 * 16, (WY + 11) * 16)
    a.add_sprite(db.URCHIN, 250 * 16, (WY + 8) * 16)
    a.add_sprite(db.BLOOPER_NANNY, 228 * 16, (WY + 6) * 16)
    a.add_sprite(db.BLOOPER_NANNY, 248 * 16, (WY + 9) * 16)
    a.add_sprite(db.FISHBONE, 236 * 16, (WY + 5) * 16)
    a.add_sprite(db.FISHBONE, 244 * 16, (WY + 10) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 232 * 16, (WY + 9) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 240 * 16, (WY + 4) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 252 * 16, (WY + 7) * 16)

    # Squeeze corridor — ceiling AND floor both tighten further
    a.add_ground(260, WY + 3, 30, 2, tileset=1)     # extra low ceiling overlay
    a.add_ground(260, GY + 4, 30, 4, tileset=1)     # raised floor
    # ~5 tiles of swim space — extremely tight
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 264 * 16, (WY + 6) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       270 * 16, (WY + 8) * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 276 * 16, (WY + 5) * 16)
    a.add_sprite(db.CHEEP_CHEEP,       282 * 16, (WY + 7) * 16)
    a.add_sprite(db.FISHBONE, 268 * 16, (WY + 7) * 16)
    a.add_sprite(db.FISHBONE, 280 * 16, (WY + 6) * 16)
    a.add_sprite(db.URCHIN, 266 * 16, (WY + 5) * 16)
    a.add_sprite(db.URCHIN, 274 * 16, (GY + 3) * 16)
    a.add_sprite(db.URCHIN, 278 * 16, (WY + 5) * 16)
    a.add_sprite(db.URCHIN, 286 * 16, (GY + 3) * 16)

    # Red coin ring in the squeeze corridor
    a.add_red_coin_ring(272, WY + 6, group_id=0x33, pattern='line')

    # Post-squeeze — second Cheep Chomp + everything
    a.add_sprite(db.CHEEP_CHOMP, 298 * 16, (WY + 7) * 16)
    a.add_sprite(db.BLOOPER_NANNY, 304 * 16, (WY + 4) * 16)
    a.add_sprite(db.BIG_CHEEP_CHEEP, 310 * 16, (WY + 8) * 16)
    a.add_sprite(db.BIG_CHEEP_CHEEP, 318 * 16, (WY + 4) * 16)
    a.add_sprite(db.FISHBONE, 308 * 16, (GY + 7) * 16)
    a.add_sprite(db.FISHBONE, 314 * 16, (WY + 3) * 16)
    a.add_sprite(db.FISHBONE, 322 * 16, (WY + 6) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 302 * 16, (WY + 9) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 316 * 16, (WY + 5) * 16)
    a.add_sprite(db.BLOOPER, 320 * 16, (WY + 8) * 16)

    # Star Coin #3 — floor trench, Urchins on both sides + Fishbone
    a.add_ground(328, GY + 4, 3, 4, tileset=1)
    a.add_ground(336, GY + 4, 3, 4, tileset=1)
    a.add_sprite(db.STAR_COIN, 332 * 16, (GY + 7) * 16, spritedata=bytes([0,0,0,0,2,0]))
    a.add_sprite(db.URCHIN, 329 * 16, (GY + 6) * 16)
    a.add_sprite(db.URCHIN, 336 * 16, (GY + 6) * 16)
    a.add_sprite(db.FISHBONE, 332 * 16, (GY + 4) * 16)

    # === SECTION E: Ascent to Surface (X 345-400) ===
    # Vertical shaft — ceiling finally opens. Walls on left and right.
    # Urchins on walls, Fishbones darting across, Bloopers rising.
    a.add_ground(345, WY, 3, 22, tileset=1)          # left wall
    a.add_ground(365, WY, 3, 22, tileset=1)          # right wall
    a.add_sprite(db.URCHIN, 348 * 16, (WY + 2) * 16)
    a.add_sprite(db.URCHIN, 362 * 16, (WY + 5) * 16)
    a.add_sprite(db.URCHIN, 348 * 16, (WY + 8) * 16)
    a.add_sprite(db.URCHIN, 362 * 16, (WY + 11) * 16)
    a.add_sprite(db.URCHIN, 348 * 16, (WY + 14) * 16)
    a.add_sprite(db.URCHIN, 362 * 16, (WY + 17) * 16)
    a.add_sprite(db.FISHBONE, 355 * 16, (WY + 4) * 16)
    a.add_sprite(db.FISHBONE, 358 * 16, (WY + 9) * 16)
    a.add_sprite(db.FISHBONE, 354 * 16, (WY + 15) * 16)
    a.add_sprite(db.BLOOPER, 356 * 16, (WY + 7) * 16)
    a.add_sprite(db.BLOOPER, 357 * 16, (WY + 13) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 352 * 16, (WY + 11) * 16)
    a.add_sprite(db.CHEEP_CHEEP, 360 * 16, (WY + 6) * 16)

    # Surface platform — emerge from water, run to goal
    a.add_ground(370, WY - 2, 30, 4, tileset=1)     # dry land
    a.add_sprite(db.HAMMER_BRO, 380 * 16, (WY - 3) * 16)
    a.add_sprite(db.SLEDGE_BRO, 390 * 16, (WY - 3) * 16)
    a.add_sprite(db.GOAL_POLE, 394 * 16, (WY - 3) * 16)

    builder.save("output/ChaosStation/Stage/06-05.arc")
    print("Created 06-05: Abyssal Trench")


def create_level_6_6():
    """06-06: Fortress of Winds — Final W6 gauntlet on a fortress rampart.
    Section A: Rampart Ascent — staircase up the fortress outer wall.
    Section B: Battlement Walk — crenellation pattern (alternating high/low blocks)
      with Bills firing through the gaps.
    Section C: Interior Descent — drop INSIDE the fortress through enclosed rooms
      with ceilings, Fire Bars, and Bros.
    Section D: Watchtower Hop — tall narrow towers (2-3 wide, 8-10 tall) to hop across.
    Section E: Final Rampart — wide fortress top with everything at once.
    SECRET EXIT: In Section C Room 2, a hidden pipe in the ceiling leads to Area 2
      — a treacherous underground passage ending with a red goal pole.
    Completely different geometry from 6-2's flat bullet gauntlet."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_CASTLE)   # castle brick — distinct from 6-2's cliff
    a.set_background(bg2=db.BG_GHOST_HOUSE)  # dark night sky — not 6-2's bright athletic
    a.set_time(400)
    a.add_zone(0, 0, 15000, 640, zone_id=0, music=db.MUSIC_CASTLE_BOSS, cam_mode=0, visibility=16)

    GY = 30
    fb_cw  = b'\x00\x00\x00\x00\x10\x07'
    fb_ccw = b'\x00\x00\x00\x00\x00\x07'

    # === INTRO: Fortress Gate (X 0-16) ===
    a.add_ground(0, GY, 14, 6, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_sprite(db.KOOPA, 10 * 16, (GY - 1) * 16)
    a.add_sprite(db.PARAGOOMBA, 12 * 16, (GY - 5) * 16)

    # === SECTION A: Rampart Ascent (X 18-72) ===
    # Staircase UP the fortress exterior wall — 5 steps, each 3 tiles higher.
    # Bills fire horizontally across each gap. Player climbs under fire.
    a.add_ground(18, GY - 3, 6, 6, tileset=1)        # step 1
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 28 * 16, (GY - 5) * 16)
    a.add_sprite(db.HAMMER_BRO, 21 * 16, (GY - 4) * 16)

    a.add_ground(28, GY - 6, 6, 6, tileset=1)        # step 2
    a.add_sprite(db.SLEDGE_BRO, 31 * 16, (GY - 7) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 38 * 16, (GY - 8) * 16)

    a.add_ground(38, GY - 9, 6, 6, tileset=1)        # step 3
    a.add_sprite(db.FIRE_BAR, 41 * 16, (GY - 14) * 16, spritedata=fb_cw)
    a.add_sprite(db.HAMMER_BRO, 42 * 16, (GY - 10) * 16)

    a.add_ground(48, GY - 12, 6, 6, tileset=1)       # step 4
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 58 * 16, (GY - 14) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 51 * 16, (GY - 13) * 16)

    a.add_ground(58, GY - 15, 8, 6, tileset=1)       # step 5 — fortress top!
    a.add_sprite(db.SLEDGE_BRO, 62 * 16, (GY - 16) * 16)
    a.add_sprite(db.FIRE_BAR, 64 * 16, (GY - 21) * 16, spritedata=fb_ccw)

    # === SECTION B: Battlement Walk (X 70-140) ===
    # Crenellation pattern — alternating tall merlons (3 wide, at GY-15)
    # and low embrasures (3 wide, at GY-12). Bills fire through embrasure gaps.
    # Merlon
    a.add_ground(70, GY - 15, 4, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 72 * 16, (GY - 16) * 16)
    # Embrasure (lower)
    a.add_ground(78, GY - 12, 4, 3, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 85 * 16, (GY - 14) * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 80 * 16, (GY - 16) * 16)
    # Merlon
    a.add_ground(86, GY - 15, 4, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 88 * 16, (GY - 16) * 16)
    a.add_sprite(db.FIRE_BAR, 89 * 16, (GY - 21) * 16, spritedata=fb_cw)
    # Embrasure
    a.add_ground(94, GY - 12, 4, 3, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 102 * 16, (GY - 14) * 16)

    # Star Coin #1 — dangling BELOW the embrasure into the open sky
    a.add_ground(96, GY - 8, 2, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 96 * 16, (GY - 9) * 16, spritedata=bytes([0,0,0,0,0,0]))

    # Merlon
    a.add_ground(102, GY - 15, 4, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 104 * 16, (GY - 16) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 110 * 16, (GY - 17) * 16)
    # Embrasure
    a.add_ground(110, GY - 12, 4, 3, tileset=1)
    a.add_sprite(db.FIRE_BAR, 112 * 16, (GY - 18) * 16, spritedata=fb_ccw)
    # Merlon — midway
    a.add_ground(118, GY - 15, 6, 3, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 120 * 16, (GY - 16) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.SLEDGE_BRO, 122 * 16, (GY - 16) * 16)
    # Last embrasure
    a.add_ground(128, GY - 12, 4, 3, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 136 * 16, (GY - 14) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 136 * 16, (GY - 8) * 16)

    # === SECTION C: Interior Descent (X 136-200) ===
    # Drop DOWN inside the fortress — enclosed rooms with ceilings above.
    # Each room is a platform with a ceiling 5 tiles above it, creating tight spaces.
    # Room 1 — enter from the top of the battlement
    a.add_ground(136, GY - 15, 3, 2, tileset=1)       # drop-in ledge
    a.add_ground(136, GY - 9, 10, 3, tileset=1)       # floor
    a.add_ground(136, GY - 14, 10, 2, tileset=1)      # ceiling above
    a.add_sprite(db.FIRE_BAR, 140 * 16, (GY - 12) * 16, spritedata=fb_cw)
    a.add_sprite(db.HAMMER_BRO, 143 * 16, (GY - 10) * 16)

    # Room 2 — drop further down
    a.add_ground(150, GY - 4, 10, 3, tileset=1)       # floor
    a.add_ground(150, GY - 9, 10, 2, tileset=1)       # ceiling
    a.add_sprite(db.SLEDGE_BRO, 154 * 16, (GY - 5) * 16)
    a.add_sprite(db.FIRE_BAR, 157 * 16, (GY - 7) * 16, spritedata=fb_ccw)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 163 * 16, (GY - 6) * 16)

    # Star Coin #2 — hidden in a ceiling pocket between rooms
    a.add_ground(163, GY - 11, 3, 2, tileset=1)       # tiny nook platform
    a.add_sprite(db.STAR_COIN, 164 * 16, (GY - 12) * 16, spritedata=bytes([0,0,0,0,1,0]))

    # Room 3 — back to ground level (lowest room)
    a.add_ground(164, GY, 10, 6, tileset=1)           # floor
    a.add_ground(164, GY - 5, 10, 2, tileset=1)       # ceiling
    a.add_sprite(db.CHAIN_CHOMP, 168 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BAR, 171 * 16, (GY - 3) * 16, spritedata=fb_cw)
    a.add_sprite(db.HAMMER_BRO, 172 * 16, (GY - 1) * 16)

    # Emerge from interior
    a.add_ground(178, GY, 8, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 182 * 16, (GY - 1) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 190 * 16, (GY + 2) * 16)
    # Red coin ring — grab coins while emerging from fortress interior
    a.add_red_coin_ring(180, GY - 5, group_id=0x22, pattern='wave')

    # === SECTION D: Watchtower Hop (X 190-260) ===
    # Tall narrow towers — 2-3 tiles wide but 8-10 tiles tall.
    # Player runs along the TOP of each tower. Gaps between are death.
    # Tower 1
    a.add_ground(190, GY - 8, 3, 10, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 191 * 16, (GY - 9) * 16)
    a.add_sprite(db.FIRE_BAR, 191 * 16, (GY - 14) * 16, spritedata=fb_cw)

    # Tower 2 — taller
    a.add_ground(198, GY - 12, 3, 14, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 199 * 16, (GY - 13) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 205 * 16, (GY - 14) * 16)

    # Tower 3 — shorter
    a.add_ground(206, GY - 6, 2, 8, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 207 * 16, (GY - 10) * 16)

    # SECRET EXIT: In the pit between Tower 3 and Tower 4 — looks like death
    # but there's a tiny ledge at the bottom with a pipe going underground.
    # Player must intentionally drop into the gap and land precisely.
    a.add_ground(208, GY, 5, 2, tileset=1)            # hidden ledge at pit bottom
    a.add_pipe(209, GY - 2, height=2, tileset=0)      # the secret pipe
    a.add_entrance(1, x=209 * 16 + 8, y=(GY - 2) * 16, etype=2,
                   zone_id=0, dest_area=2, dest_entrance=0)

    # Tower 4 — tallest
    a.add_ground(213, GY - 14, 3, 16, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 214 * 16, (GY - 15) * 16)
    a.add_sprite(db.FIRE_BAR, 215 * 16, (GY - 20) * 16, spritedata=fb_ccw)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 220 * 16, (GY - 16) * 16)

    # Tower 5 — medium
    a.add_ground(221, GY - 10, 3, 12, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 222 * 16, (GY - 11) * 16)

    # Star Coin #3 — floating between tower 4 and 5, must jump from tower 4's peak
    a.add_sprite(db.STAR_COIN, 218 * 16, (GY - 16) * 16, spritedata=bytes([0,0,0,0,2,0]))

    # Tower 6 — short, leads to finale
    a.add_ground(229, GY - 6, 3, 8, tileset=1)
    a.add_sprite(db.FIRE_BAR, 230 * 16, (GY - 12) * 16, spritedata=fb_cw)
    a.add_sprite(db.PARAGOOMBA, 231 * 16, (GY - 10) * 16)

    # === SECTION E: Final Rampart (X 236-310) ===
    # Wide fortress top — everything at once. Broad platforms but swarming enemies.
    a.add_ground(236, GY - 4, 14, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 240 * 16, (GY - 5) * 16)
    a.add_sprite(db.SLEDGE_BRO, 245 * 16, (GY - 5) * 16)
    a.add_sprite(db.FIRE_BAR, 243 * 16, (GY - 9) * 16, spritedata=fb_cw)
    a.add_sprite(db.FIRE_BAR, 248 * 16, (GY - 9) * 16, spritedata=fb_ccw)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 254 * 16, (GY - 6) * 16)

    a.add_ground(254, GY, 6, 6, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 256 * 16, (GY - 1) * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 258 * 16, (GY - 6) * 16)

    a.add_ground(264, GY - 7, 10, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 267 * 16, (GY - 8) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 271 * 16, (GY - 8) * 16)
    a.add_sprite(db.FIRE_BAR, 269 * 16, (GY - 13) * 16, spritedata=fb_cw)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 278 * 16, (GY - 9) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 278 * 16, (GY - 3) * 16)

    a.add_ground(278, GY, 12, 6, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 282 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BAR, 285 * 16, (GY - 5) * 16, spritedata=fb_ccw)
    a.add_sprite(db.HAMMER_BRO, 287 * 16, (GY - 1) * 16)

    # === GOAL ===
    a.add_ground(294, GY, 30, 6, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 308 * 16, (GY - 1) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 308 * 16, (GY + 5) * 16)
    a.add_sprite(db.GOAL_POLE, 312 * 16, (GY - 1) * 16)

    # ══════════ AREA 2: SECRET EXIT — Fortress Dungeon ══════════
    # A dark underground passage beneath the fortress. Tight corridors,
    # Fire Bars everywhere, Chain Chomps guarding the red goal pole.
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_CAVE)
    a2.set_background(bg2=db.BG_UNDERGROUND)
    a2.set_time(200)
    a2.add_zone(0, 0, 4000, 480, zone_id=0, music=db.MUSIC_UNDERGROUND,
                cam_mode=0, visibility=36)

    SY = 22  # secret area ground Y
    # Entrance from pipe
    a2.add_ground(0, SY, 8, 6, tileset=1)
    a2.add_entrance(0, 3 * 16, (SY - 2) * 16, etype=0)
    a2.add_ground(0, SY - 7, 8, 2, tileset=1)   # ceiling

    # Corridor 1: Fire Bar gauntlet in tight ceiling room
    a2.add_ground(8, SY, 16, 6, tileset=1)
    a2.add_ground(8, SY - 7, 16, 2, tileset=1)   # ceiling
    a2.add_sprite(db.FIRE_BAR, 12 * 16, (SY - 4) * 16, spritedata=fb_cw)
    a2.add_sprite(db.FIRE_BAR, 20 * 16, (SY - 4) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.DRY_BONES, 15 * 16, (SY - 1) * 16)

    # Corridor 2: Chain Chomp alley — open ceiling, two chomps lunging
    a2.add_ground(28, SY, 14, 6, tileset=1)
    a2.add_sprite(db.CHAIN_CHOMP, 32 * 16, (SY - 1) * 16)
    a2.add_sprite(db.CHAIN_CHOMP, 38 * 16, (SY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 35 * 16, (SY - 6) * 16, spritedata=fb_cw)

    # Corridor 3: Elevated platform gauntlet with Thwomps
    a2.add_ground(46, SY + 2, 4, 4, tileset=1)
    a2.add_ground(54, SY - 1, 4, 4, tileset=1)
    a2.add_ground(62, SY + 1, 4, 4, tileset=1)
    a2.add_sprite(db.THWOMP, 48 * 16, (SY - 5) * 16)
    a2.add_sprite(db.THWOMP, 56 * 16, (SY - 7) * 16)
    a2.add_sprite(db.THWOMP, 64 * 16, (SY - 5) * 16)

    # Corridor 4: Final room — Sledge Bro + Fire Bars guard the red pole
    a2.add_ground(70, SY, 20, 6, tileset=1)
    a2.add_ground(70, SY - 8, 20, 2, tileset=1)   # ceiling
    a2.add_sprite(db.SLEDGE_BRO, 74 * 16, (SY - 1) * 16)
    a2.add_sprite(db.HAMMER_BRO, 78 * 16, (SY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 76 * 16, (SY - 5) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.FIRE_BAR, 82 * 16, (SY - 5) * 16, spritedata=fb_cw)

    # Red Goal Pole — secret exit!
    a2.add_sprite(db.GOAL_POLE, 86 * 16, (SY - 1) * 16,
                  spritedata=bytes([0, 0, 16, 0, 0, 0]))
    # Long platform after the pole — Mario needs ~15 tiles for victory walk
    a2.add_ground(90, SY, 20, 6, tileset=1)

    builder.save("output/ChaosStation/Stage/06-06.arc")
    print("Created 06-06: Fortress of Winds (+ secret exit)")


# ╔══════════════════════════════════════════════════════════════════════╗
# ║                     WORLD 7 — SKYFALL DOMAIN                       ║
# ╚══════════════════════════════════════════════════════════════════════╝

def create_level_7_1():
    """07-01: Cloud Rush — Sky world introduction. Ascending cloud platforms
    over bottomless pits. Falling platforms, Lakitu, Paragoombas.
    Geometry: wide plateaus that gradually narrow + ascending staircase."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(400)
    a.add_zone(0, 0, 7200, 640, zone_id=0, music=db.MUSIC_SKY, cam_mode=0, visibility=16)

    GY = 28

    # === SECTION A: Safe Introduction (X 0-55) ===
    # Wide starting platform — eases player into sky world.
    a.add_ground(0, GY, 18, 6, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 128 * 16, (GY - 3) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_sprite(db.GOOMBA, 10 * 16, (GY - 1) * 16)
    a.add_sprite(db.KOOPA, 14 * 16, (GY - 1) * 16)
    a.add_question_block(8, GY - 4, contents=1)  # mushroom

    # Gap + coin trail → second platform
    a.add_coin_line(20, GY - 3, 4)
    a.add_ground(24, GY, 14, 6, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 28 * 16, (GY - 5) * 16)
    a.add_sprite(db.PARAGOOMBA, 33 * 16, (GY - 4) * 16)
    a.add_sprite(db.KOOPA, 30 * 16, (GY - 1) * 16)

    # Third platform — slightly higher (ascending trend begins)
    a.add_ground(42, GY - 2, 12, 6, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 46 * 16, (GY - 6) * 16)

    # === SECTION B: Falling Platform Gauntlet (X 58-130) ===
    # Donut blocks over void, interspersed with small solid platforms.
    a.add_ground(58, GY - 3, 6, 4, tileset=1)         # landing pad
    a.add_sprite(db.FALLING_PLATFORM, 66 * 16, (GY - 3) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 72 * 16, (GY - 4) * 16)
    a.add_ground(78, GY - 5, 5, 4, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 70 * 16, (GY - 7) * 16)
    a.add_sprite(db.PARAGOOMBA, 76 * 16, (GY - 8) * 16)

    # Star Coin #1 — below a falling platform, must ride it down briefly
    a.add_sprite(db.STAR_COIN, 72 * 16, (GY + 1) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    a.add_sprite(db.FALLING_PLATFORM, 85 * 16, (GY - 5) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 91 * 16, (GY - 6) * 16)
    a.add_ground(97, GY - 6, 5, 4, tileset=1)

    # Lakitu enters!
    a.add_sprite(db.LAKITU, 100 * 16, (GY - 14) * 16)

    a.add_sprite(db.FALLING_PLATFORM, 104 * 16, (GY - 7) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 110 * 16, (GY - 5) * 16)
    a.add_ground(116, GY - 4, 6, 4, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 118 * 16, (GY - 5) * 16)

    # === SECTION C: Cloud Staircase (X 126-210) ===
    # Ascending platforms in a zigzag — each higher than the last.
    a.add_ground(126, GY - 2, 8, 4, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 128 * 16, (GY - 3) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Zigzag ascent — platforms alternate left-right, climbing
    a.add_ground(138, GY - 5, 5, 3, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 140 * 16, (GY - 9) * 16)
    a.add_sprite(db.CROWBER, 143 * 16, (GY - 8) * 16)    # dive-bomb crow!
    a.add_ground(147, GY - 8, 5, 3, tileset=1)
    a.add_sprite(db.WIGGLER, 149 * 16, (GY - 9) * 16)    # angry caterpillar
    a.add_sprite(db.CROWBER, 153 * 16, (GY - 11) * 16)
    a.add_ground(156, GY - 11, 5, 3, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 158 * 16, (GY - 14) * 16)
    a.add_sprite(db.FIRE_BRO, 159 * 16, (GY - 12) * 16)
    a.add_ground(165, GY - 14, 5, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 167 * 16, (GY - 15) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 169 * 16, (GY - 15) * 16)  # chained beast on top step!

    # Star Coin #2 — high above the staircase, need Paratroopa bounce
    a.add_sprite(db.STAR_COIN, 148 * 16, (GY - 15) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # Red coin ring arc across the staircase
    a.add_red_coin_ring(160, GY - 12, group_id=0x70, pattern='arc')

    # Descend back down via wider platforms
    a.add_ground(174, GY - 10, 7, 4, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 178 * 16, (GY - 14) * 16)
    a.add_ground(185, GY - 6, 7, 4, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 188 * 16, (GY - 7) * 16)
    a.add_ground(196, GY - 2, 8, 4, tileset=1)
    a.add_sprite(db.WIGGLER, 199 * 16, (GY - 3) * 16)    # Wiggler on descent

    # === SECTION D: Crowber Gauntlet (X 210-310) ===
    # Narrow platforms. Crowbers dive from above. Amp rings guard gaps.
    a.add_sprite(db.LAKITU, 215 * 16, (GY - 14) * 16)   # second Lakitu!
    a.add_ground(210, GY - 1, 4, 4, tileset=1)
    a.add_sprite(db.CROWBER, 212 * 16, (GY - 5) * 16)    # dive-bomb crow
    a.add_ground(220, GY - 3, 3, 3, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 221 * 16, (GY - 7) * 16)
    a.add_sprite(db.FIRE_BRO, 222 * 16, (GY - 4) * 16)
    a.add_ground(229, GY, 4, 4, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 231 * 16, (GY - 1) * 16)  # Chain Chomp!
    a.add_ground(239, GY - 4, 3, 3, tileset=1)
    a.add_sprite(db.CROWBER, 240 * 16, (GY - 8) * 16)
    a.add_sprite(db.AMP, 244 * 16, (GY - 2) * 16)        # Amp in the gap
    a.add_ground(248, GY - 1, 3, 3, tileset=1)
    a.add_sprite(db.WIGGLER, 249 * 16, (GY - 2) * 16)    # Wiggler on tiny platform
    a.add_ground(257, GY - 3, 4, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 259 * 16, (GY - 4) * 16)
    a.add_sprite(db.AMP, 263 * 16, (GY - 1) * 16)        # Amp in gap
    a.add_ground(267, GY, 3, 3, tileset=1)
    a.add_sprite(db.CROWBER, 268 * 16, (GY - 4) * 16)
    a.add_ground(276, GY - 5, 3, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 277 * 16, (GY - 6) * 16)
    a.add_ground(285, GY - 2, 4, 3, tileset=1)
    a.add_sprite(db.BRAMBALL, 287 * 16, (GY - 3) * 16)   # Spiked ball rolling!

    # Star Coin #3 — below the narrow path, in the void between two platforms
    a.add_sprite(db.STAR_COIN, 240 * 16, (GY + 3) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # === SECTION E: Goal Run (X 300-360) ===
    a.add_ground(300, GY, 4, 4, tileset=1)
    a.add_ground(308, GY - 2, 6, 4, tileset=1)
    a.add_ground(318, GY, 30, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 340 * 16, (GY - 1) * 16)

    builder.save("output/ChaosStation/Stage/07-01.arc")
    print("Created 07-01: Cloud Rush")


def create_level_7_2():
    """07-02: Gale Force Gauntlet — Grassy floating islands at wildly varying
    heights. Slopes on every island, Paratroopa bounce chains across chasms.
    Geometry: scattered islands at RANDOM heights (not linear)."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(bg2=db.BG_GRASS_SKY)
    a.set_time(400)
    a.add_zone(0, 0, 7500, 640, zone_id=0, music=db.MUSIC_OVERWORLD, cam_mode=0, visibility=16)

    # Islands at varying heights — each one a unique shape
    # GY varies per island to create a scatter-plot feel

    # === ISLAND 1: Starting Island (flat, wide) ===
    a.add_ground(0, 26, 16, 6, tileset=1)
    a.add_entrance(0, 3 * 16, 24 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 98 * 16, 23 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, 24 * 16)
    a.add_sprite(db.GOOMBA, 8 * 16, 25 * 16)
    a.add_sprite(db.KOOPA, 12 * 16, 25 * 16)
    a.add_question_block(6, 22, contents=9)   # Mini Mushroom!

    # === ISLAND 2: High narrow peak (Y=20) ===
    a.add_ground(22, 20, 4, 3, tileset=1)
    a.add_ground(26, 22, 3, 3, tileset=1)    # slope down right
    a.add_sprite(db.PARAGOOMBA, 24 * 16, 16 * 16)

    # === ISLAND 3: Low wide shelf (Y=30) ===
    a.add_ground(35, 30, 10, 4, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 39 * 16, 26 * 16)
    a.add_sprite(db.KOOPA, 42 * 16, 29 * 16)

    # === ISLAND 4: Tall column (Y=16, very high) ===
    a.add_ground(51, 16, 3, 12, tileset=1)
    a.add_sprite(db.FIRE_BRO, 52 * 16, 15 * 16)

    # === ISLAND 5: Staircase island (Y=24, ascending left to right) ===
    a.add_ground(60, 28, 4, 4, tileset=1)
    a.add_ground(64, 26, 4, 4, tileset=1)
    a.add_ground(68, 24, 4, 4, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 66 * 16, 25 * 16)
    a.add_sprite(db.PARAGOOMBA, 70 * 16, 20 * 16)

    # Star Coin #1 — floating below Island 5's lowest step, in the gap
    a.add_sprite(db.STAR_COIN, 58 * 16, 30 * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    # === ISLAND 6: V-shaped valley (Y=22 edges, Y=26 center) ===
    a.add_ground(78, 22, 3, 4, tileset=1)     # left wall
    a.add_ground(81, 26, 6, 4, tileset=1)     # valley floor
    a.add_ground(87, 22, 3, 4, tileset=1)     # right wall
    a.add_sprite(db.KOOPA_PARATROOPA, 83 * 16, 22 * 16)
    a.add_sprite(db.KOOPA_PARATROOPA, 86 * 16, 18 * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 90 * 16, 20 * 16)

    # === ISLAND 7: Midway — wide safe platform (Y=24) ===
    a.add_ground(96, 24, 12, 6, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 98 * 16, 23 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_question_block(104, 20, contents=1)   # mushroom — players need it!
    a.add_question_block(107, 20, contents=2)   # fire flower for good measure

    # === ISLAND 8: Stepping Stone Bridge (Y=25, same height as Island 7) ===
    # Small solid platforms with Paratroopas bouncing above each gap.
    # Player can walk/jump between solid stones; Paratroopas are bonus/obstacle.
    a.add_ground(110, 25, 3, 3, tileset=1)      # stone 1 (right edge of island 7 gap)
    a.add_sprite(db.KOOPA_PARATROOPA, 113 * 16, 22 * 16)  # Paratroopa above gap
    a.add_ground(116, 23, 3, 3, tileset=1)      # stone 2 (slightly higher)
    a.add_sprite(db.KOOPA_PARATROOPA, 121 * 16, 21 * 16)
    a.add_ground(123, 25, 3, 3, tileset=1)      # stone 3 (dips down)
    a.add_sprite(db.PARAGOOMBA, 125 * 16, 21 * 16)
    a.add_ground(129, 22, 3, 3, tileset=1)      # stone 4 (back up)
    a.add_sprite(db.KOOPA_PARATROOPA, 133 * 16, 20 * 16)
    a.add_ground(136, 24, 3, 3, tileset=1)      # stone 5 → connects to Island 9

    # === ISLAND 9: Anvil-shaped (wide top Y=18, narrow stem Y=22) ===
    a.add_ground(140, 18, 8, 3, tileset=1)
    a.add_ground(143, 21, 2, 6, tileset=1)     # stem
    a.add_sprite(db.SLEDGE_BRO, 143 * 16, 17 * 16)

    # Star Coin #2 — dangling below the anvil's top, next to the stem
    a.add_sprite(db.STAR_COIN, 146 * 16, 22 * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # === ISLAND 10: Zigzag chain (Y alternates 20-28) ===
    a.add_ground(154, 20, 3, 3, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 155 * 16, 16 * 16)
    a.add_ground(162, 28, 3, 3, tileset=1)
    a.add_sprite(db.KOOPA, 163 * 16, 27 * 16)
    a.add_ground(170, 22, 3, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 171 * 16, 21 * 16)
    a.add_ground(178, 26, 3, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 179 * 16, 25 * 16)
    a.add_ground(186, 20, 3, 3, tileset=1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 189 * 16, 18 * 16)

    # Red coin ring across the zigzag
    a.add_red_coin_ring(168, 22, group_id=0x71, pattern='wave')

    # === ISLAND 11: L-shaped fortress (Y=24) ===
    a.add_ground(196, 24, 10, 4, tileset=1)
    a.add_ground(196, 20, 3, 4, tileset=1)     # vertical arm
    a.add_sprite(db.SLEDGE_BRO, 200 * 16, 23 * 16)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 204 * 16, 22 * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 210 * 16, 22 * 16)

    # Star Coin #3 — floating below the L-fortress, must drop from edge
    a.add_sprite(db.STAR_COIN, 202 * 16, 29 * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # === ISLAND 12: Goal Platform ===
    a.add_ground(216, 24, 6, 4, tileset=1)
    a.add_ground(226, 26, 30, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 248 * 16, 25 * 16)

    builder.save("output/ChaosStation/Stage/07-02.arc")
    print("Created 07-02: Gale Force Gauntlet")


def create_level_7_3():
    """07-03: Armada Approach — Airship-themed sky level. Narrow walkways
    between tall column obstacles with Bullet Bills firing through gaps.
    Geometry: long narrow decks with vertical pillars creating corridors.
    SECRET EXIT via hidden pipe under the flagship deck."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_2)
    a.set_time(350)
    a.add_zone(0, 0, 7500, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)

    GY = 26

    # === SECTION A: Approach Run (X 0-60) ===
    # Wide platform → narrow walkways between Bill launcher columns
    a.add_ground(0, GY, 12, 6, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_question_block(5, GY - 4, contents=5)   # Propeller suit — right at the start!
    a.add_sprite(db.BOB_OMB, 8 * 16, (GY - 1) * 16)
    a.add_sprite(db.HAMMER_BRO, 10 * 16, (GY - 1) * 16)

    # Launcher column 1
    a.add_ground(14, GY - 8, 2, 10, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 14 * 16, (GY - 10) * 16)

    a.add_ground(18, GY, 6, 4, tileset=1)       # narrow deck
    a.add_sprite(db.BOB_OMB, 20 * 16, (GY - 1) * 16)
    a.add_sprite(db.KOOPA, 22 * 16, (GY - 1) * 16)

    # Launcher column 2
    a.add_ground(26, GY - 10, 2, 12, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 26 * 16, (GY - 12) * 16)

    a.add_ground(30, GY - 1, 5, 4, tileset=1)   # slightly elevated deck
    a.add_sprite(db.HAMMER_BRO, 32 * 16, (GY - 2) * 16)
    a.add_sprite(db.BOB_OMB, 34 * 16, (GY - 2) * 16)

    # Launcher column 3
    a.add_ground(37, GY - 6, 2, 8, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 37 * 16, (GY - 8) * 16)

    a.add_ground(41, GY, 8, 4, tileset=1)
    a.add_sprite(db.BOB_OMB, 44 * 16, (GY - 1) * 16)
    a.add_sprite(db.BOB_OMB, 47 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BRO, 44 * 16, (GY - 1) * 16)

    # === SECTION B: Crossfire Corridor (X 55-135) ===
    # Long lower deck with overhead platforms that have Bill launchers.
    # Banzai Bills from the right. Rocky Wrenches pop up.
    a.add_ground(55, GY + 2, 35, 4, tileset=1)   # lower deck
    # Overhead platforms with launchers pointing down
    a.add_ground(60, GY - 6, 6, 2, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 63 * 16, (GY - 4) * 16)
    a.add_ground(72, GY - 8, 6, 2, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 75 * 16, (GY - 6) * 16)
    a.add_ground(84, GY - 5, 6, 2, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 87 * 16, (GY - 3) * 16)

    # Rocky Wrenches on the lower deck
    a.add_sprite(db.ROCKY_WRENCH, 60 * 16, (GY + 1) * 16)
    a.add_sprite(db.ROCKY_WRENCH, 68 * 16, (GY + 1) * 16)
    a.add_sprite(db.ROCKY_WRENCH, 76 * 16, (GY + 1) * 16)
    a.add_sprite(db.ROCKY_WRENCH, 84 * 16, (GY + 1) * 16)
    a.add_sprite(db.HAMMER_BRO, 72 * 16, (GY + 1) * 16)   # Hammer Bro on deck

    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 95 * 16, (GY) * 16)

    # Star Coin #1 — above the lower deck, between overhead launchers
    a.add_sprite(db.STAR_COIN, 70 * 16, (GY - 2) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    # === SECTION C: Tower Dodge (X 100-180) ===
    # Tall pillars (2w × 10h) with enemies between. AMP rings around pillars.
    a.add_ground(100, GY - 1, 5, 4, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 102 * 16, (GY - 2) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Pillar 1
    a.add_ground(110, GY - 8, 2, 10, tileset=1)
    a.add_sprite(db.AMP, 112 * 16, (GY - 5) * 16)
    a.add_ground(114, GY, 4, 4, tileset=1)
    a.add_sprite(db.PARA_BOB_OMB, 116 * 16, (GY - 10) * 16)
    a.add_sprite(db.BOB_OMB, 115 * 16, (GY - 1) * 16)

    # Pillar 2 — taller
    a.add_ground(120, GY - 12, 2, 14, tileset=1)
    a.add_sprite(db.AMP, 122 * 16, (GY - 8) * 16)
    a.add_sprite(db.AMP, 118 * 16, (GY - 3) * 16)   # extra Amp in gap
    a.add_ground(124, GY - 2, 4, 4, tileset=1)
    a.add_sprite(db.FIRE_BRO, 126 * 16, (GY - 3) * 16)
    a.add_sprite(db.SLEDGE_BRO, 125 * 16, (GY - 3) * 16)

    # Pillar 3
    a.add_ground(132, GY - 6, 2, 8, tileset=1)
    a.add_sprite(db.AMP, 134 * 16, (GY - 3) * 16)
    a.add_ground(136, GY, 5, 4, tileset=1)
    a.add_sprite(db.PARA_BOB_OMB, 140 * 16, (GY - 12) * 16)
    a.add_sprite(db.HAMMER_BRO, 138 * 16, (GY - 1) * 16)

    # Star Coin #2 — on top of the tallest pillar 2
    a.add_sprite(db.STAR_COIN, 120 * 16, (GY - 14) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # Pillar 4
    a.add_ground(145, GY - 10, 2, 12, tileset=1)
    a.add_sprite(db.AMP, 147 * 16, (GY - 6) * 16)
    a.add_sprite(db.AMP, 143 * 16, (GY - 4) * 16)
    a.add_ground(149, GY - 1, 4, 4, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 151 * 16, (GY - 2) * 16)
    a.add_sprite(db.FIRE_BRO, 149 * 16, (GY - 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 157 * 16, (GY - 3) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 160 * 16, (GY + 2) * 16)

    # === SECTION D: The Flagship (X 165-260) ===
    # One massive platform — the "deck". Enemies swarm it.
    a.add_ground(165, GY, 40, 6, tileset=1)     # main deck
    # Sub-deck: elevated command platform
    a.add_ground(180, GY - 5, 10, 2, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 183 * 16, (GY - 6) * 16)
    a.add_sprite(db.FIRE_BRO, 187 * 16, (GY - 6) * 16)

    # Fire Bars on deck
    fb_cw  = b'\x00\x00\x00\x00\x10\x06'
    fb_ccw = b'\x00\x00\x00\x00\x00\x06'
    a.add_sprite(db.FIRE_BAR, 172 * 16, (GY - 3) * 16, spritedata=fb_cw)
    a.add_sprite(db.FIRE_BAR, 195 * 16, (GY - 3) * 16, spritedata=fb_ccw)

    # Deck enemies — heavy resistance on the flagship
    a.add_sprite(db.BOB_OMB, 168 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 173 * 16, (GY - 1) * 16)
    a.add_sprite(db.BOB_OMB, 177 * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_BRO, 192 * 16, (GY - 1) * 16)
    a.add_sprite(db.BOB_OMB, 196 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 200 * 16, (GY - 1) * 16)

    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 208 * 16, (GY - 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 208 * 16, (GY + 4) * 16)

    # Red coin ring over the flagship deck
    a.add_red_coin_ring(185, GY - 8, group_id=0x72, pattern='arc')

    # SECRET EXIT: Pipe hidden under the flagship deck.
    # Small ground block under the main deck — player must drop off the right edge
    # and loop back underneath to find it.
    a.add_ground(200, GY + 4, 4, 2, tileset=1)    # hidden underbelly ledge
    a.add_pipe(201, GY + 2, height=2, tileset=0)
    a.add_entrance(1, x=201 * 16 + 8, y=(GY + 2) * 16, etype=2,
                   zone_id=0, dest_area=2, dest_entrance=0)

    # Star Coin #3 — at the end of the deck, behind Banzai Bill launchers
    a.add_sprite(db.STAR_COIN, 203 * 16, (GY - 1) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # === SECTION E: Escape + Goal (X 210-280) ===
    a.add_ground(215, GY - 2, 4, 4, tileset=1)
    a.add_sprite(db.PARA_BOB_OMB, 218 * 16, (GY - 10) * 16)
    a.add_sprite(db.FIRE_BRO, 217 * 16, (GY - 3) * 16)
    a.add_ground(225, GY, 4, 4, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 231 * 16, (GY - 2) * 16)
    a.add_sprite(db.BOB_OMB, 227 * 16, (GY - 1) * 16)
    a.add_ground(235, GY - 1, 4, 4, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 237 * 16, (GY - 2) * 16)
    a.add_ground(245, GY, 30, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 267 * 16, (GY - 1) * 16)

    # ══════════ AREA 2: SECRET EXIT — Cargo Hold ══════════
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_CAVE)
    a2.set_background(bg2=db.BG_UNDERGROUND)
    a2.set_time(200)
    a2.add_zone(0, 0, 3000, 480, zone_id=0, music=db.MUSIC_UNDERGROUND,
                cam_mode=0, visibility=36)

    SY = 22
    a2.add_ground(0, SY, 8, 6, tileset=1)
    a2.add_entrance(0, 3 * 16, (SY - 2) * 16, etype=0)
    a2.add_ground(0, SY - 7, 60, 2, tileset=1)   # continuous ceiling

    # Corridor — Bob-ombs and Fire Bars
    a2.add_ground(8, SY, 14, 6, tileset=1)
    a2.add_sprite(db.BOB_OMB, 12 * 16, (SY - 1) * 16)
    a2.add_sprite(db.BOB_OMB, 18 * 16, (SY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 15 * 16, (SY - 4) * 16, spritedata=fb_cw)

    a2.add_ground(26, SY, 14, 6, tileset=1)
    a2.add_sprite(db.HAMMER_BRO, 30 * 16, (SY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 34 * 16, (SY - 4) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.CHAIN_CHOMP, 36 * 16, (SY - 1) * 16)

    a2.add_ground(44, SY, 20, 6, tileset=1)
    a2.add_sprite(db.SLEDGE_BRO, 48 * 16, (SY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 52 * 16, (SY - 4) * 16, spritedata=fb_cw)

    # Red Goal Pole
    a2.add_sprite(db.GOAL_POLE, 58 * 16, (SY - 1) * 16,
                  spritedata=bytes([0, 0, 16, 0, 0, 0]))
    a2.add_ground(62, SY, 20, 6, tileset=1)      # victory walk platform

    builder.save("output/ChaosStation/Stage/07-03.arc")
    print("Created 07-03: Armada Approach (+ secret exit)")


def create_level_7_4():
    """07-04: Skykeep Fortress — Castle built into a floating mountain.
    Castle mechanics over bottomless pits instead of lava.
    Geometry: enclosed rooms with ceilings, connected by drops. 2 areas."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_CASTLE)
    a.set_background(bg2=db.BG_CASTLE)
    a.set_time(400)
    a.add_zone(0, 0, 8500, 640, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, visibility=16)

    GY = 28
    fb_cw  = b'\x00\x00\x00\x00\x10\x06'
    fb_ccw = b'\x00\x00\x00\x00\x00\x06'

    # === ROOM 1: Crumbling Entrance (X 0-60) ===
    # Floor with gaps over void. Dry Bones patrol. Thwomps guard passages.
    a.add_ground(0, GY, 12, 6, tileset=1)
    a.add_ground(0, GY - 8, 60, 2, tileset=1)   # ceiling
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)
    a.add_sprite(db.DRY_BONES, 8 * 16, (GY - 1) * 16)

    # Gap + Thwomp
    a.add_sprite(db.THWOMP, 15 * 16, (GY - 6) * 16)
    a.add_ground(18, GY, 8, 6, tileset=1)
    a.add_sprite(db.DRY_BONES, 22 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 24 * 16, (GY - 1) * 16)

    # Gap + Thwomp
    a.add_sprite(db.THWOMP, 28 * 16, (GY - 6) * 16)
    a.add_ground(32, GY, 10, 6, tileset=1)
    a.add_sprite(db.FIRE_BAR, 36 * 16, (GY - 4) * 16, spritedata=fb_cw)
    a.add_sprite(db.HAMMER_BRO, 38 * 16, (GY - 1) * 16)

    # Gap + Thwomp → exit room 1
    a.add_sprite(db.THWOMP, 44 * 16, (GY - 6) * 16)
    a.add_ground(48, GY, 8, 6, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 52 * 16, (GY - 1) * 16)
    a.add_question_block(50, GY - 4, contents=2)  # fire flower

    # === ROOM 2: Fire Bar Labyrinth (X 60-155) ===
    # Three height levels of platforms with Fire Bars at junctions.
    # No ceiling here — open to the "sky" above the castle ruins.

    # Bottom level (GY)
    a.add_ground(62, GY, 8, 4, tileset=1)
    a.add_sprite(db.FIRE_BAR, 66 * 16, (GY - 3) * 16, spritedata=fb_cw)
    a.add_sprite(db.GIANT_DRY_BONES, 68 * 16, (GY - 1) * 16)

    # Middle level (GY-5)
    a.add_ground(74, GY - 5, 8, 2, tileset=1)
    a.add_sprite(db.FIRE_BAR, 78 * 16, (GY - 8) * 16, spritedata=fb_ccw)
    a.add_sprite(db.AMP, 82 * 16, (GY - 3) * 16)

    # Top level (GY-10)
    a.add_ground(86, GY - 10, 6, 2, tileset=1)
    a.add_sprite(db.FIRE_BAR, 89 * 16, (GY - 13) * 16, spritedata=fb_cw)

    # Star Coin #1 — on the bottom level, behind Fire Bar timing
    a.add_sprite(db.STAR_COIN, 64 * 16, (GY - 1) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    # Second set — platforms shift to different arrangement
    # Bottom right
    a.add_ground(96, GY, 8, 4, tileset=1)
    a.add_sprite(db.DRY_BONES, 98 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 102 * 16, (GY - 1) * 16)
    # Middle left
    a.add_ground(108, GY - 6, 8, 2, tileset=1)
    a.add_sprite(db.FIRE_BAR, 112 * 16, (GY - 9) * 16, spritedata=fb_ccw)
    a.add_sprite(db.HAMMER_BRO, 114 * 16, (GY - 7) * 16)
    # Top right
    a.add_ground(120, GY - 11, 6, 2, tileset=1)
    a.add_sprite(db.FIRE_BAR, 123 * 16, (GY - 14) * 16, spritedata=fb_cw)

    # Converge to single path
    a.add_ground(130, GY - 4, 10, 4, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 132 * 16, (GY - 5) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.AMP, 138 * 16, (GY - 1) * 16)

    # === ROOM 3: Skewer Gallery (X 145-225) ===
    # Ceiling returns. Skewers alternate from ceiling and floor.
    a.add_ground(145, GY, 80, 6, tileset=1)       # long floor
    a.add_ground(145, GY - 10, 80, 2, tileset=1)  # ceiling

    # Skewer pairs — alternating up/down
    a.add_sprite(db.SKEWER_DOWN, 155 * 16, (GY - 8) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 160 * 16, (GY - 1) * 16)
    a.add_sprite(db.SKEWER_UP, 170 * 16, (GY + 2) * 16)
    a.add_sprite(db.SKEWER_DOWN, 180 * 16, (GY - 8) * 16)
    a.add_sprite(db.CHAIN_CHOMP, 185 * 16, (GY - 1) * 16)
    a.add_sprite(db.SKEWER_UP, 195 * 16, (GY + 2) * 16)
    a.add_sprite(db.SKEWER_DOWN, 205 * 16, (GY - 8) * 16)

    # Star Coin #2 — between two skewers, timing-dependent
    a.add_sprite(db.STAR_COIN, 175 * 16, (GY - 5) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # Red coin ring in the skewer gallery
    a.add_red_coin_ring(190, GY - 5, group_id=0x73, pattern='line')

    # === ROOM 4: Podoboo Ascent (X 225-310) ===
    # Ascending staircase over void. Podoboos leap from below.
    # No ceiling — open sky ruins.
    a.add_ground(230, GY, 6, 4, tileset=1)
    a.add_sprite(db.PODOBOO, 232 * 16, (GY + 4) * 16)
    a.add_ground(240, GY - 3, 6, 4, tileset=1)
    a.add_sprite(db.PODOBOO, 242 * 16, (GY + 1) * 16)
    a.add_sprite(db.FIRE_BRO, 244 * 16, (GY - 4) * 16)
    a.add_ground(250, GY - 6, 6, 4, tileset=1)
    a.add_sprite(db.PODOBOO, 252 * 16, (GY - 2) * 16)
    a.add_sprite(db.BIG_THWOMP, 256 * 16, (GY - 14) * 16)
    a.add_ground(260, GY - 9, 6, 4, tileset=1)
    a.add_sprite(db.PODOBOO, 262 * 16, (GY - 5) * 16)
    a.add_sprite(db.SLEDGE_BRO, 264 * 16, (GY - 10) * 16)

    # Star Coin #3 — on a side ledge between staircase platforms, risky drop to grab
    a.add_ground(245, GY - 1, 4, 1, tileset=1)   # small ledge below platform 2
    a.add_sprite(db.STAR_COIN, 247 * 16, (GY - 2) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # Pipe to Area 2
    a.add_ground(270, GY - 12, 8, 4, tileset=1)
    a.add_pipe(274, GY - 14, height=2, tileset=0)
    a.add_entrance(1, x=274 * 16 + 8, y=(GY - 14) * 16, etype=2,
                   zone_id=0, dest_area=2, dest_entrance=0)

    # ══════════ AREA 2: The Treasury (long pipe section) ══════════
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_CASTLE)
    a2.set_background(bg2=db.BG_CASTLE)
    a2.set_time(250)
    a2.add_zone(0, 0, 6000, 480, zone_id=0, music=db.MUSIC_CASTLE,
                cam_mode=0, visibility=16)

    TY = 22
    # Continuous floor + ceiling throughout
    a2.add_ground(0, TY, 200, 6, tileset=1)
    a2.add_ground(0, TY - 9, 200, 2, tileset=1)
    a2.add_entrance(0, 3 * 16, (TY - 2) * 16, etype=0)
    a2.add_entrance(1, 108 * 16, (TY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # --- Room A: Coin vault with Fire Bars (X 0-55) ---
    a2.add_coin_line(8, TY - 3, 6)
    a2.add_sprite(db.FIRE_BAR, 16 * 16, (TY - 6) * 16, spritedata=fb_cw)
    a2.add_coin_line(20, TY - 3, 6)
    a2.add_sprite(db.DRY_BONES, 28 * 16, (TY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 35 * 16, (TY - 6) * 16, spritedata=fb_ccw)
    a2.add_coin_line(38, TY - 3, 6)
    a2.add_sprite(db.GIANT_DRY_BONES, 46 * 16, (TY - 1) * 16)

    # --- Room B: Skewer corridor (X 55-110) ---
    # Skewers from ceiling and floor forcing timing
    a2.add_sprite(db.SKEWER_DOWN, 60 * 16, (TY - 7) * 16)
    a2.add_sprite(db.FIRE_BAR, 65 * 16, (TY - 6) * 16, spritedata=fb_cw)
    a2.add_sprite(db.SKEWER_UP, 73 * 16, (TY + 2) * 16)
    a2.add_sprite(db.DRY_BONES, 68 * 16, (TY - 1) * 16)
    a2.add_sprite(db.SKEWER_DOWN, 82 * 16, (TY - 7) * 16)
    a2.add_sprite(db.FIRE_BAR, 88 * 16, (TY - 6) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.SKEWER_UP, 95 * 16, (TY + 2) * 16)
    a2.add_sprite(db.HAMMER_BRO, 100 * 16, (TY - 1) * 16)

    # --- Midway ---
    a2.add_sprite(db.MIDWAY_FLAG, 108 * 16, (TY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # --- Room C: Podoboo gauntlet (X 110-165) ---
    # Floor gaps over lava — Podoboos leap up
    a2.add_ground(112, TY, 8, 4, tileset=1)   # island 1
    a2.add_sprite(db.PODOBOO, 116 * 16, (TY + 4) * 16)
    a2.add_sprite(db.FIRE_BAR, 114 * 16, (TY - 6) * 16, spritedata=fb_cw)

    a2.add_ground(124, TY, 6, 4, tileset=1)   # island 2
    a2.add_sprite(db.PODOBOO, 127 * 16, (TY + 4) * 16)
    a2.add_sprite(db.CHAIN_CHOMP, 126 * 16, (TY - 1) * 16)

    a2.add_ground(134, TY, 6, 4, tileset=1)   # island 3
    a2.add_sprite(db.PODOBOO, 137 * 16, (TY + 4) * 16)
    a2.add_sprite(db.FIRE_BAR, 136 * 16, (TY - 6) * 16, spritedata=fb_ccw)

    a2.add_ground(144, TY, 6, 4, tileset=1)   # island 4
    a2.add_sprite(db.SLEDGE_BRO, 147 * 16, (TY - 1) * 16)
    a2.add_sprite(db.PODOBOO, 147 * 16, (TY + 4) * 16)

    a2.add_ground(154, TY, 8, 4, tileset=1)   # solid stretch
    a2.add_sprite(db.FIRE_BAR, 158 * 16, (TY - 6) * 16, spritedata=fb_cw)
    a2.add_sprite(db.BIG_THWOMP, 162 * 16, (TY - 12) * 16)

    # --- Room D: Final sprint + goal (X 165-200) ---
    a2.add_sprite(db.SKEWER_DOWN, 170 * 16, (TY - 7) * 16)
    a2.add_sprite(db.DRY_BONES, 175 * 16, (TY - 1) * 16)
    a2.add_sprite(db.DRY_BONES, 178 * 16, (TY - 1) * 16)
    a2.add_sprite(db.FIRE_BAR, 182 * 16, (TY - 6) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.SKEWER_UP, 188 * 16, (TY + 2) * 16)

    a2.add_sprite(db.GOAL_POLE, 195 * 16, (TY - 1) * 16)

    builder.save("output/ChaosStation/Stage/07-04.arc")
    print("Created 07-04: Skykeep Fortress")


def create_level_7_5():
    """07-05: Stormcellar Depths — Cave inside the floating mountain.
    Tight tunnels, ceiling everywhere, branching paths, vertical drop shaft.
    Geometry: narrow corridors with ceilings, NOT open platforms."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_UNDERGROUND)
    a.set_tileset(1, db.TILESET_CAVE)
    a.set_background(bg2=db.BG_UNDERGROUND)
    a.set_time(400)
    a.add_zone(0, 0, 7000, 800, zone_id=0, music=db.MUSIC_UNDERGROUND, cam_mode=0, visibility=36)

    GY = 24  # ground Y
    CY = GY - 7  # ceiling Y (7 tiles of space)

    # === SECTION A: Cave Entrance (X 0-55) ===
    a.add_ground(0, GY, 55, 6, tileset=1)       # floor
    a.add_ground(0, CY, 55, 3, tileset=1)       # ceiling

    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 120 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)

    a.add_sprite(db.BUZZY_BEETLE, 10 * 16, (GY - 1) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 15 * 16, (CY + 3) * 16)  # ceiling walker
    a.add_sprite(db.SWOOP, 20 * 16, (CY + 3) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 28 * 16, (GY - 1) * 16)
    a.add_sprite(db.SWOOP, 35 * 16, (CY + 3) * 16)
    a.add_sprite(db.SPIKE_TOP, 40 * 16, (GY - 1) * 16)
    a.add_question_block(25, GY - 4, contents=1)  # mushroom

    # Pillar narrows the passage
    a.add_ground(45, CY + 3, 3, 3, tileset=1)   # ceiling stalactite
    a.add_sprite(db.BUZZY_BEETLE, 48 * 16, (CY + 6) * 16)

    # === SECTION B: Spike Top Tunnels (X 55-125) ===
    # Ceiling lowers, creating tighter space. Spike Tops on walls.
    a.add_ground(55, GY, 70, 6, tileset=1)       # floor continues
    a.add_ground(55, CY + 1, 70, 3, tileset=1)  # lower ceiling (6 tiles)

    # Narrow squeeze with Spike Tops on ceiling
    a.add_sprite(db.SPIKE_TOP, 60 * 16, (CY + 4) * 16)
    a.add_sprite(db.SPIKE_TOP, 68 * 16, (GY - 1) * 16)
    a.add_sprite(db.SPIKE_TOP, 76 * 16, (CY + 4) * 16)
    a.add_sprite(db.SWOOP, 64 * 16, (CY + 4) * 16)
    a.add_sprite(db.SWOOP, 72 * 16, (CY + 4) * 16)

    # Floor bumps creating uneven terrain
    a.add_ground(80, GY - 2, 4, 2, tileset=1)   # raised section
    a.add_sprite(db.BUZZY_BEETLE, 82 * 16, (GY - 3) * 16)
    a.add_ground(90, GY - 1, 3, 1, tileset=1)   # small bump
    a.add_sprite(db.SPIKE_TOP, 92 * 16, (CY + 4) * 16)

    # Star Coin #1 — in a ceiling alcove, need to jump up into tight gap
    a.add_ground(98, CY + 4, 3, 1, tileset=1)   # alcove shelf
    a.add_sprite(db.STAR_COIN, 99 * 16, (CY + 3) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    # Monty Moles pop from ground
    a.add_sprite(db.MONTY_MOLE, 105 * 16, (GY - 1) * 16)
    a.add_sprite(db.MONTY_MOLE, 115 * 16, (GY - 1) * 16)

    a.add_sprite(db.MIDWAY_FLAG, 120 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # === SECTION C: Fuzzy Rails (X 125-205) ===
    # Open cave chamber. Fuzzies on tracks, Chain Chomps on platforms.
    a.add_ground(125, GY, 80, 6, tileset=1)
    a.add_ground(125, CY - 2, 80, 3, tileset=1) # high ceiling (more space)

    # Raised platforms with enemies
    a.add_ground(130, GY - 4, 6, 2, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 133 * 16, (GY - 5) * 16)

    a.add_ground(142, GY - 3, 5, 1, tileset=1)
    a.add_sprite(db.FUZZY, 144 * 16, (GY - 4) * 16)  # fuzzy on track

    a.add_ground(152, GY - 6, 6, 2, tileset=1)
    a.add_sprite(db.CHAIN_CHOMP, 155 * 16, (GY - 7) * 16)
    a.add_sprite(db.FUZZY, 158 * 16, (GY - 2) * 16)

    a.add_ground(164, GY - 2, 4, 2, tileset=1)
    a.add_sprite(db.MONTY_MOLE, 166 * 16, (GY - 1) * 16)

    a.add_ground(174, GY - 5, 6, 2, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 177 * 16, (GY - 6) * 16)
    a.add_sprite(db.FUZZY, 180 * 16, (GY - 3) * 16)

    a.add_ground(186, GY - 3, 5, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 188 * 16, (GY - 4) * 16)

    # Star Coin #2 — on top of a raised platform, guarded by Chain Chomp
    a.add_sprite(db.STAR_COIN, 153 * 16, (GY - 8) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # === SECTION D: Amp Corridor (X 205-280) ===
    # Tight tunnel — Amps sit on the floor so player must jump over them.
    # Ceiling is only 3 tiles above floor, so Amps are ONLY at floor level (GY-1).
    # This is challenging but always passable — no damage boost required.
    a.add_ground(205, GY, 75, 6, tileset=1)       # floor continues
    a.add_ground(205, CY + 1, 75, 3, tileset=1)   # ceiling (bottom at GY-4)

    # Amps at floor level (GY-1) — player jumps over, 3 tiles of clearance to ceiling
    a.add_sprite(db.AMP, 210 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 219 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 228 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 237 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 246 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 255 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 264 * 16, (GY - 1) * 16)
    a.add_sprite(db.AMP, 273 * 16, (GY - 1) * 16)

    # Swoops from ceiling — adds tension without blocking the floor path
    a.add_sprite(db.SWOOP, 214 * 16, (CY + 4) * 16)
    a.add_sprite(db.SWOOP, 232 * 16, (CY + 4) * 16)
    a.add_sprite(db.SWOOP, 250 * 16, (CY + 4) * 16)
    a.add_sprite(db.SWOOP, 268 * 16, (CY + 4) * 16)

    # Star Coin #3 — floating between two Amps, grab mid-jump
    a.add_sprite(db.STAR_COIN, 241 * 16, (GY - 3) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # === SECTION E: Exit Sprint (X 280-340) ===
    # Cave opens up slightly. Hammer Bros + Sledge Bro guarding the goal.
    a.add_ground(280, GY, 60, 6, tileset=1)
    a.add_ground(280, CY - 1, 60, 3, tileset=1)   # high ceiling — relief after tight section

    a.add_sprite(db.HAMMER_BRO, 288 * 16, (GY - 1) * 16)
    a.add_sprite(db.SPIKE_TOP, 294 * 16, (GY - 1) * 16)
    a.add_sprite(db.MONTY_MOLE, 300 * 16, (GY - 1) * 16)
    a.add_sprite(db.SLEDGE_BRO, 308 * 16, (GY - 1) * 16)
    a.add_sprite(db.SWOOP, 314 * 16, (CY + 2) * 16)
    a.add_sprite(db.BUZZY_BEETLE, 320 * 16, (CY + 3) * 16)  # ceiling walker

    # Exit — wide goal area
    a.add_ground(325, GY, 15, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 332 * 16, (GY - 1) * 16)

    builder.save("output/ChaosStation/Stage/07-05.arc")
    print("Created 07-05: Stormcellar Depths")


def create_level_7_6():
    """07-06: Skyfall Gauntlet — Final sky challenge. Tiny zigzag platforms
    in rapid succession, double Lakitu, Falling Platform marathon.
    Geometry: ultra-narrow platforms in diagonal patterns. Tight timer."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(bg2=db.BG_ATHLETIC_SKY_1)
    a.set_time(300)  # tight timer!
    a.add_zone(0, 0, 8500, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0, visibility=16)

    GY = 26

    # === SECTION A: Sprint Start (X 0-50) ===
    # Narrow platforms in zigzag, ascending fast. No time to wait.
    a.add_ground(0, GY, 6, 4, tileset=1)
    a.add_entrance(0, 2 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 152 * 16, (GY - 4) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a.add_sprite(10, 2 * 16, (GY - 2) * 16)

    # Zigzag ascent — 3-tile platforms
    a.add_ground(9, GY - 2, 3, 3, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 10 * 16, (GY - 6) * 16)
    a.add_ground(16, GY - 4, 3, 3, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 17 * 16, (GY - 8) * 16)
    a.add_ground(23, GY - 2, 3, 3, tileset=1)
    a.add_sprite(db.PARAGOOMBA, 24 * 16, (GY - 6) * 16)
    a.add_ground(30, GY - 5, 3, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 31 * 16, (GY - 6) * 16)
    a.add_ground(37, GY - 3, 3, 3, tileset=1)
    a.add_ground(44, GY - 6, 3, 3, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 47 * 16, (GY - 8) * 16)

    # === SECTION B: Falling Platform Marathon (X 55-145) ===
    # 12 consecutive Falling Platforms. No solid ground. Must keep moving.
    a.add_ground(55, GY - 4, 4, 3, tileset=1)   # launch pad

    # 12 donut blocks — varying heights to force different jump arcs
    for i, (dx, dy) in enumerate([
        (63, -3), (70, -5), (77, -2), (84, -6), (91, -3),
        (98, -4), (105, -7), (112, -2), (119, -5), (126, -3),
        (133, -6), (140, -4)
    ]):
        a.add_sprite(db.FALLING_PLATFORM, dx * 16, (GY + dy) * 16)

    # Lakitu enters during the marathon!
    a.add_sprite(db.LAKITU, 80 * 16, (GY - 14) * 16)

    # Bullet Bills from the side
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 100 * 16, (GY + 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 125 * 16, (GY - 1) * 16)

    # Star Coin #1 — below a falling platform, freefall grab
    a.add_sprite(db.STAR_COIN, 84 * 16, (GY + 2) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    # === SECTION C: Midway + Scale/Bolt Platforms (X 150-220) ===
    a.add_ground(150, GY - 3, 6, 4, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 152 * 16, (GY - 4) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Scale platforms (weight-based)
    a.add_sprite(db.SCALE_PLATFORM, 162 * 16, (GY - 6) * 16)
    a.add_sprite(db.PARAGOOMBA, 165 * 16, (GY - 10) * 16)
    a.add_sprite(db.PARAGOOMBA, 170 * 16, (GY - 8) * 16)

    a.add_ground(175, GY - 4, 3, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 176 * 16, (GY - 5) * 16)

    a.add_sprite(db.SCALE_PLATFORM, 184 * 16, (GY - 5) * 16)
    a.add_sprite(db.AMP, 188 * 16, (GY - 3) * 16)

    a.add_ground(194, GY - 3, 3, 3, tileset=1)
    a.add_sprite(db.KOOPA_PARATROOPA, 196 * 16, (GY - 7) * 16)

    # Bolt platform ride
    a.add_sprite(db.BOLT_PLATFORM, 204 * 16, (GY - 4) * 16)
    a.add_sprite(db.AMP, 210 * 16, (GY - 6) * 16)
    a.add_sprite(db.AMP, 215 * 16, (GY - 2) * 16)

    # Star Coin #2 — off the bolt platform path, risky jump
    a.add_sprite(db.STAR_COIN, 208 * 16, (GY - 12) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # Red coin ring
    a.add_red_coin_ring(200, GY - 6, group_id=0x75, pattern='arc')

    # === SECTION D: Double Lakitu Assault (X 225-310) ===
    # Two Lakitus! Tiny platforms with huge gaps. Bros everywhere.
    a.add_sprite(db.LAKITU, 230 * 16, (GY - 16) * 16)  # second Lakitu

    a.add_ground(225, GY - 2, 3, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 226 * 16, (GY - 3) * 16)
    a.add_ground(235, GY - 5, 2, 2, tileset=1)
    a.add_ground(243, GY - 1, 3, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 244 * 16, (GY - 2) * 16)
    a.add_ground(252, GY - 4, 2, 2, tileset=1)
    a.add_sprite(db.BULLET_BILL_LAUNCHER, 256 * 16, (GY - 6) * 16)
    a.add_ground(260, GY - 2, 3, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 261 * 16, (GY - 3) * 16)
    a.add_ground(269, GY - 6, 2, 2, tileset=1)
    a.add_ground(277, GY - 1, 3, 3, tileset=1)
    a.add_sprite(db.HAMMER_BRO, 278 * 16, (GY - 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 284 * 16, (GY - 3) * 16)
    a.add_ground(288, GY - 4, 2, 2, tileset=1)
    a.add_ground(296, GY - 2, 3, 3, tileset=1)
    a.add_sprite(db.SLEDGE_BRO, 297 * 16, (GY - 3) * 16)

    fb_cw = b'\x00\x00\x00\x00\x10\x06'
    # Fire Bars on tall columns
    a.add_sprite(db.FIRE_BAR, 250 * 16, (GY - 10) * 16, spritedata=fb_cw)
    a.add_sprite(db.FIRE_BAR, 275 * 16, (GY - 10) * 16, spritedata=fb_cw)

    # === SECTION E: The Skyfall (X 310-380) ===
    # Wide falling platforms with enemies ON them. Must clear + jump.
    a.add_ground(310, GY - 3, 4, 3, tileset=1)   # launch

    # Falling platforms with enemies
    a.add_sprite(db.FALLING_PLATFORM, 318 * 16, (GY - 2) * 16)
    a.add_sprite(db.SPINY, 318 * 16, (GY - 3) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 326 * 16, (GY - 4) * 16)
    a.add_sprite(db.BOB_OMB, 326 * 16, (GY - 5) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 334 * 16, (GY - 1) * 16)
    a.add_sprite(db.KOOPA, 334 * 16, (GY - 2) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 342 * 16, (GY - 5) * 16)
    a.add_sprite(db.PARAGOOMBA, 342 * 16, (GY - 8) * 16)
    a.add_sprite(db.FALLING_PLATFORM, 350 * 16, (GY - 2) * 16)
    a.add_sprite(db.HAMMER_BRO, 350 * 16, (GY - 3) * 16)

    # Star Coin #3 — on the Bob-omb's falling platform, grab fast!
    a.add_sprite(db.STAR_COIN, 327 * 16, (GY - 6) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # Final solid ground + Goal
    a.add_ground(360, GY, 30, 6, tileset=1)
    a.add_sprite(db.GOAL_POLE, 382 * 16, (GY - 1) * 16)

    builder.save("output/ChaosStation/Stage/07-06.arc")
    print("Created 07-06: Skyfall Gauntlet")


def create_level_7_ghost_house():
    """07-21: The Phantom Skyship — Ghost house in a wrecked airship.
    Boos, Broozers, P-Switch secret exit.
    Rooms connected by continuous floor with ceiling gaps between sections."""
    import tools.sprite_db as db
    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a.set_background(bg2=db.BG_GHOST_HOUSE)
    a.set_time(450)
    a.add_zone(0, 0, 6500, 640, zone_id=0, music=db.MUSIC_GHOST_HOUSE,
               cam_mode=0, visibility=36, model_dark=12)

    GY = 26

    # === Continuous floor through ALL rooms ===
    # One long floor so the player never hits a wall.
    a.add_ground(0, GY, 250, 6, tileset=1)

    # === ROOM 1: Foyer (X 0-60) ===
    # Dark room! Glow blocks provide limited visibility.
    a.add_ground(0, GY - 9, 58, 3, tileset=1)     # ceiling stops before Room 2
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_sprite(10, 3 * 16, (GY - 2) * 16)

    # Single glow block — carry it through the entire ghost house!
    a.add_sprite(db.GLOW_BLOCK, 6 * 16, (GY - 4) * 16)

    a.add_sprite(db.BOO, 12 * 16, (GY - 4) * 16)
    a.add_sprite(db.BOO, 20 * 16, (GY - 3) * 16)
    a.add_sprite(db.BOO, 28 * 16, (GY - 5) * 16)

    # === BREAKABLE BRICK WALL — Broozer smashes through! ===
    # 2 columns × 6 rows of individual brick blocks (at x=35-36)
    for bx in range(35, 37):
        for by in range(GY - 6, GY):
            a.add_brick_block(bx, by, contents=0)
    # Broozer is on the LEFT side — it charges RIGHT and smashes the wall
    a.add_sprite(db.BROOZER, 32 * 16, (GY - 3) * 16)

    # Star Coin #1 — hidden BEHIND the brick wall (to the right of it)
    a.add_sprite(db.STAR_COIN, 38 * 16, (GY - 3) * 16,
                 spritedata=bytes([0,0,0,0,0,0]))

    a.add_sprite(db.BOO, 42 * 16, (GY - 4) * 16)
    a.add_sprite(db.BIG_BOO, 50 * 16, (GY - 4) * 16)

    # === ROOM 2: The False Gallery (X 65-150) ===
    # Higher ceiling, with platforms at varying heights.
    a.add_ground(65, GY - 10, 90, 3, tileset=1)   # separate ceiling block

    # Platforms at varying heights — stepping stones in the dark
    a.add_ground(70, GY - 4, 6, 2, tileset=1)
    a.add_sprite(db.BOO, 73 * 16, (GY - 6) * 16)
    a.add_ground(82, GY - 7, 5, 2, tileset=1)
    a.add_sprite(db.BROOZER, 84 * 16, (GY - 8) * 16)
    a.add_ground(93, GY - 3, 6, 2, tileset=1)
    a.add_sprite(db.DRY_BONES, 96 * 16, (GY - 4) * 16)

    # Blue P-Switch on a raised platform — hit it to destroy the brick wall!
    a.add_ground(105, GY - 5, 5, 2, tileset=1)
    # P-Switch: nybble 10 (byte 4 high) = 0 for blue. Set byte 4=0x00 explicitly.
    a.add_sprite(db.P_SWITCH, 107 * 16, (GY - 6) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))

    a.add_sprite(db.BOO, 118 * 16, (GY - 5) * 16)
    a.add_sprite(db.BOO, 128 * 16, (GY - 3) * 16)
    a.add_sprite(db.BROOZER, 133 * 16, (GY - 1) * 16)
    a.add_sprite(db.BIG_BOO, 140 * 16, (GY - 5) * 16)

    a.add_sprite(db.MIDWAY_FLAG, 145 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # Star Coin #2 — on the raised P-Switch platform
    a.add_sprite(db.STAR_COIN, 110 * 16, (GY - 6) * 16,
                 spritedata=bytes([0,0,0,0,1,0]))

    # SECRET EXIT: pipe hidden behind a BRICK WALL.
    # When P-Switch is hit → bricks become coins → wall disappears → pipe revealed!
    # Pipe placed first, then bricks on top to hide it (4 columns × 5 rows)
    a.add_pipe(123, GY - 2, height=2, tileset=0)
    a.add_entrance(1, x=123 * 16 + 8, y=(GY - 2) * 16, etype=2,
                   zone_id=0, dest_area=2, dest_entrance=0)
    # Brick wall covering the pipe (x=121-124, fully covers pipe at 123-124)
    for bx in range(121, 125):
        for by in range(GY - 5, GY):
            a.add_brick_block(bx, by, contents=0)
    # Small ground ledge past the wall to reach pipe area after P-Switch
    a.add_ground(125, GY - 2, 3, 1, tileset=1)

    # === ROOM 3: The Abyss (X 160-250) ===
    # Ceiling block for room 3 — separate from room 2
    a.add_ground(160, GY - 10, 90, 3, tileset=1)

    # Raised platforms with Boos — floor is continuous underneath
    a.add_ground(168, GY - 4, 3, 2, tileset=1)
    a.add_sprite(db.BOO, 169 * 16, (GY - 6) * 16)
    a.add_ground(177, GY - 6, 3, 2, tileset=1)
    a.add_sprite(db.BOO, 178 * 16, (GY - 8) * 16)
    a.add_ground(186, GY - 3, 3, 2, tileset=1)
    a.add_sprite(db.BIG_BOO, 187 * 16, (GY - 5) * 16)
    a.add_ground(195, GY - 5, 3, 2, tileset=1)
    a.add_sprite(db.BOO, 196 * 16, (GY - 7) * 16)
    a.add_sprite(db.BROOZER, 200 * 16, (GY - 1) * 16)
    a.add_ground(205, GY - 4, 3, 2, tileset=1)
    a.add_sprite(db.BOO, 206 * 16, (GY - 6) * 16)
    a.add_sprite(db.BOO, 212 * 16, (GY - 3) * 16)

    # Star Coin #3 — on a platform just below the ceiling (ceiling bottom is GY-7)
    a.add_ground(190, GY - 6, 2, 1, tileset=1)
    a.add_sprite(db.STAR_COIN, 190 * 16, (GY - 7) * 16,
                 spritedata=bytes([0,0,0,0,2,0]))

    # Red coin ring in the abyss
    a.add_red_coin_ring(195, GY - 4, group_id=0x76, pattern='circle')

    # Goal area — floor is already continuous
    a.add_sprite(db.GOAL_POLE, 242 * 16, (GY - 1) * 16)

    # ══════════ AREA 2: SECRET EXIT — Engine Room ══════════
    a2 = builder.add_area(2)
    a2.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a2.set_background(bg2=db.BG_GHOST_HOUSE)
    a2.set_time(150)
    a2.add_zone(0, 0, 2500, 480, zone_id=0, music=db.MUSIC_GHOST_HOUSE,
                cam_mode=0, visibility=36, model_dark=12)

    SY = 22
    a2.add_ground(0, SY, 80, 6, tileset=1)
    a2.add_ground(0, SY - 7, 80, 2, tileset=1)
    a2.add_entrance(0, 3 * 16, (SY - 2) * 16, etype=0)

    a2.add_sprite(db.BROOZER, 10 * 16, (SY - 1) * 16)
    a2.add_sprite(db.DRY_BONES, 18 * 16, (SY - 1) * 16)
    fb_cw  = b'\x00\x00\x00\x00\x10\x06'
    fb_ccw = b'\x00\x00\x00\x00\x00\x06'
    a2.add_sprite(db.FIRE_BAR, 25 * 16, (SY - 4) * 16, spritedata=fb_cw)
    a2.add_sprite(db.BOO, 30 * 16, (SY - 3) * 16)
    a2.add_sprite(db.BOO, 35 * 16, (SY - 5) * 16)
    a2.add_sprite(db.BROOZER, 40 * 16, (SY - 1) * 16)
    a2.add_sprite(db.BOO, 45 * 16, (SY - 3) * 16)
    a2.add_sprite(db.BIG_BOO, 50 * 16, (SY - 4) * 16)
    a2.add_sprite(db.FIRE_BAR, 55 * 16, (SY - 4) * 16, spritedata=fb_ccw)
    a2.add_sprite(db.DRY_BONES, 60 * 16, (SY - 1) * 16)

    # Red Goal Pole
    a2.add_sprite(db.GOAL_POLE, 70 * 16, (SY - 1) * 16,
                  spritedata=bytes([0, 0, 16, 0, 0, 0]))
    a2.add_ground(74, SY, 20, 6, tileset=1)

    builder.save("output/ChaosStation/Stage/07-21.arc")
    print("Created 07-21: The Phantom Skyship (+ secret exit)")


def create_level_7_tower():
    """7-Tower: Modify vanilla 07-22 with added hazards.
    Area 1: vertical climb, zone at (768,864,512,1872). Add Fire Bars, Thwomps.
    Area 2: boss room, zone at (288,416,448,224). Add flanking Fire Bars.
    Area 3: post-checkpoint climb, zone at (768,752,512,1648). Add hazards.
    Must set loaded_sprites so game loads the needed .arc files."""
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/07-22.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x06'
    FB_CCW = b'\x00\x00\x00\x00\x00\x06'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Tower Climb (zone x=768-1280, y=864-2736) ──
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = list(area1.sprites)

    # Fire Bars along the climb shaft — CW left side, CCW right side
    for y_pos in [2600, 2200, 1800, 1400, 1000]:
        new_sprites.append(spr(62, 850, y_pos, FB_CW))
        new_sprites.append(spr(62, 1100, y_pos + 160, FB_CCW))

    # Thwomps in the center at alternating heights
    for y_pos in [2400, 1600, 1200]:
        new_sprites.append(spr(47, 960, y_pos))

    # Hammer Bros on platforms
    new_sprites.append(spr(95, 880, 2000))
    new_sprites.append(spr(95, 1050, 1400))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Boss Room (zone x=288-736, y=416-640) ──
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)
    boss_sprites.append(spr(62, 330, 570, FB_CW))   # left flank
    boss_sprites.append(spr(62, 670, 570, FB_CCW))  # right flank
    boss_sprites.append(spr(95, 350, 570))           # Hammer Bro left
    boss_sprites.append(spr(95, 650, 570))           # Hammer Bro right
    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    # ── Area 3: Post-checkpoint climb (zone x=768-1280, y=752-2400) ──
    area3 = parse_course_bin(arc.get_file('course/course3.bin'))
    new3 = list(area3.sprites)
    for y_pos in [2200, 1800, 1400, 1000]:
        new3.append(spr(62, 880, y_pos, FB_CW))
        new3.append(spr(62, 1080, y_pos + 100, FB_CCW))
    for y_pos in [2000, 1200]:
        new3.append(spr(47, 960, y_pos))
    new3.append(spr(95, 900, 1600))
    area3.sprites = new3
    area3.loaded_sprites = sorted(set(s.stype for s in new3))
    arc.set_file('course/course3.bin', serialize_course_bin(area3))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/07-22.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/07-22.arc ({len(data)} bytes)')
    print('Modified 7-Tower with Fire Bars, Thwomps, Hammer Bros')


def create_level_7_castle():
    """7-Castle: Modify vanilla 07-24. Ludwig's stronghold.
    Area 1: horizontal traversal, zone (1200,368,6448,321). Has Dry Bones,
            Giant Dry Bones, Sledge Bros, Skewers already.
    Area 2: boss room, zone (1568,368,1456,1296). Ludwig boss.
    Must set loaded_sprites for new sprite types."""
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/07-24.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x08'
    FB_CCW = b'\x00\x00\x00\x00\x00\x08'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Castle Hallways (zone x=1200-7648, y=368-689) ──
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = []
    db_count = 0
    for s in area1.sprites:
        if s.stype == 118:  # Dry Bones → cycle Fire Bro/Hammer Bro/Sledge Bro
            ns = copy.deepcopy(s)
            ns.stype = [80, 95, 120][db_count % 3]
            ns.spritedata = SD
            new_sprites.append(ns)
            db_count += 1
        elif s.stype == 119:  # Giant Dry Bones → Sledge Bro
            ns = copy.deepcopy(s)
            ns.stype = 120
            ns.spritedata = SD
            new_sprites.append(ns)
        else:
            new_sprites.append(s)

    # Fire Bars along the castle corridor
    for i, x_pos in enumerate(range(1600, 7200, 450)):
        sd = FB_CW if i % 2 == 0 else FB_CCW
        new_sprites.append(spr(62, x_pos, 500, sd))

    # Thwomps above the path
    for x_pos in [2000, 3000, 4000, 5000, 6000, 7000]:
        new_sprites.append(spr(47, x_pos, 380))

    # Chain Chomps in wider sections
    for x_pos in [2500, 3500, 4500, 5500, 6500]:
        new_sprites.append(spr(146, x_pos, 580))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Boss Room (zone x=1568-3024, y=368-1664) ──
    # Keep Ludwig intact, add flanking hazards.
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)
    boss_sprites.append(spr(62, 1650, 1500, FB_CW))    # left Fire Bar
    boss_sprites.append(spr(62, 2900, 1500, FB_CCW))   # right Fire Bar
    boss_sprites.append(spr(47, 2000, 1380))            # Thwomp left
    boss_sprites.append(spr(47, 2600, 1380))            # Thwomp right
    boss_sprites.append(spr(95, 1700, 1550))            # Hammer Bro left
    boss_sprites.append(spr(95, 2800, 1550))            # Hammer Bro right
    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/07-24.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/07-24.arc ({len(data)} bytes)')
    print("Modified 7-Castle: Ludwig's Stronghold")


def create_level_7_mushroom_houses():
    """Placeholder for W7 mushroom houses."""
    print("[W7] Mushroom Houses not yet built")


def create_level_7_ambush():
    """07-33/34/35: World 7 ambush arenas — sky-themed spring block encounters.
    Each variant has a distinct layout. Keeps required sprites (controller,
    Toad balloons, chest, Lakitu) and replaces spring block positions."""
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    CONTROLLER   = 454  # Ambush Level Controller — must keep exactly as-is
    TOAD_BALLOON = 185  # Reward balloons — must keep all
    CHEST        = 203  # Prize chest — must keep
    LAKITU       = 54   # Sky enemy
    SPRING_BLOCK = 223  # Checkered spring block (platforms)

    SD = b'\x00\x00\x00\x00\x00\x00'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    def modify_ambush(src_name, dst_name, new_blocks, extra_enemies=None):
        with open(f'extracted files/Stage/{src_name}', 'rb') as f:
            arc = U8Archive.load(f.read())
        course = parse_course_bin(arc.get_file('course/course1.bin'))

        # Keep all non-spring-block sprites from vanilla (controller, balloons, chest, lakitu)
        kept = [s for s in course.sprites if s.stype != SPRING_BLOCK]

        # Add new spring block layout
        for (x, y) in new_blocks:
            kept.append(spr(SPRING_BLOCK, x, y))

        # Add any extra enemies
        if extra_enemies:
            for (stype, x, y) in extra_enemies:
                kept.append(spr(stype, x, y))

        course.sprites = kept
        arc.set_file('course/course1.bin', serialize_course_bin(course))
        os.makedirs('output/ChaosStation/Stage', exist_ok=True)
        with open(f'output/ChaosStation/Stage/{dst_name}', 'wb') as f:
            f.write(arc.pack())
        print(f'  Saved: {dst_name}')

    # Arena pixel bounds: x=240-784, y=256-528
    # Spring blocks form platforms; player bounces between them fighting Lakitu.

    # --- Variant 1 (07-33): Zigzag ---
    # Alternating high/low blocks across the arena — forces bouncing rhythm.
    zigzag = [
        # Low row (y=480)
        (288, 480), (368, 480), (448, 480), (528, 480), (608, 480), (688, 480),
        # High row (y=400)
        (328, 400), (408, 400), (488, 400), (568, 400), (648, 400),
    ]
    modify_ambush('07-33.arc', '07-33.arc', zigzag)

    # --- Variant 2 (07-34): Three Tiers ---
    # Staircase ascending left-to-right across 3 heights.
    # Player must climb up while Lakitu attacks from above.
    tiers = [
        # Bottom tier (y=480)
        (256, 480), (304, 480), (352, 480), (400, 480),
        # Mid tier (y=432)
        (432, 432), (480, 432), (528, 432),
        # Top tier (y=384)
        (560, 384), (608, 384), (656, 384), (704, 384), (752, 384),
    ]
    modify_ambush('07-34.arc', '07-34.arc', tiers)

    # --- Variant 3 (07-35): Two Lakitus, Dense Floor ---
    # Packed spring block floor with a raised center platform.
    # Two Lakitus attack simultaneously — chaotic sky battle.
    dense = [
        # Dense lower floor
        (256, 480), (288, 480), (320, 480), (352, 480), (384, 480),
        (416, 480), (448, 480), (480, 480), (512, 480), (544, 480),
        (576, 480), (608, 480), (640, 480), (672, 480), (704, 480), (736, 480),
        # Raised center platform
        (448, 416), (480, 416), (512, 416), (544, 416), (576, 416),
        # High corner blocks
        (256, 384), (752, 384),
    ]
    # Second Lakitu on the left side
    modify_ambush('07-35.arc', '07-35.arc', dense,
                  extra_enemies=[(LAKITU, 320, 296)])

    print("Created W7 ambush arenas (07-33/34/35)")


def create_level_7_airship():
    """Placeholder for W7 airship. Uses vanilla 07-38 for now."""
    import os, shutil
    src = 'extracted files/Stage/07-38.arc'
    dst = 'output/ChaosStation/Stage/07-38.arc'
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print("[W7] Airship 07-38 not yet built — using vanilla")
    else:
        print("[W7] Airship 07-38 not found in extracted files")


def create_level_6_tower():
    """6-Tower: Stormspire — Buffed vertical climb with W6 enemies.

    Keeps vanilla structure (rotating blocks, moving platforms, Lemmy/Morton boss).
    Replaces 3 Dry Bones -> Fire Bro / Hammer Bro / Sledge Bro.
    Adds Fire Bars, Thwomps, and Chain Chomps throughout the climb.
    Boss room gets flanking Fire Bars.
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/06-22.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x06'   # fire bar clockwise, length 6
    FB_CCW = b'\x00\x00\x00\x00\x00\x06'   # counter-clockwise, length 6

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Tower Climb ──────────────────────────────────────────────
    # Tower spans roughly x=430-850 px wide, y=400 (top) to y=3900 (bottom)
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = []
    db_count = 0
    for s in area1.sprites:
        if s.stype == 118:  # Dry Bones -> rotate Fire Bro / Hammer Bro / Sledge Bro
            ns = copy.deepcopy(s)
            ns.stype = [80, 95, 120][db_count % 3]
            ns.spritedata = SD
            new_sprites.append(ns)
            db_count += 1
        else:
            new_sprites.append(s)

    # Fire Bars — one CW + one CCW at each altitude, offset so they don't overlap
    for y, x_cw, x_ccw in [
        (3700, 528, 720), (3300, 560, 752), (2900, 528, 720),
        (2500, 560, 704), (2100, 528, 720), (1700, 576, 688),
        (1300, 560, 720), (900,  528, 704),
    ]:
        new_sprites.append(spr(62, x_cw,  y, FB_CW))
        new_sprites.append(spr(62, x_ccw, y + 160, FB_CCW))

    # Thwomps — center of the climb shaft at mid-heights
    for y in [3500, 2700, 1900, 1100]:
        new_sprites.append(spr(47, 640, y))

    # Chain Chomps — lower third of climb
    for x, y in [(512, 3800), (768, 3600), (528, 3200)]:
        new_sprites.append(spr(146, x, y))

    # Hammer Bros — upper section
    for x, y in [(560, 2200), (720, 1400), (560, 600)]:
        new_sprites.append(spr(95, x, y))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Boss Room ────────────────────────────────────────────────
    # Zone at (288, 416, 432, 224). Keep the boss intact.
    # Just flank the arena with rotating fire bars.
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)
    boss_sprites.append(spr(62, 330, 570, FB_CW))   # left flank
    boss_sprites.append(spr(62, 670, 570, FB_CCW))  # right flank
    boss_sprites.append(spr(95, 350, 570))           # Hammer Bro left
    boss_sprites.append(spr(95, 650, 570))           # Hammer Bro right
    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/06-22.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/06-22.arc ({len(data)} bytes)')
    print('Modified 6-Tower: Stormspire')


def create_level_6_castle():
    """6-Castle: Morton's Keep — Remix vanilla 06-24 with W6 enemies.

    Keeps vanilla structure (rotating platforms, spike balls, lava waves).
    Replaces Dry Bones (118) -> cycle Fire Bro / Hammer Bro / Sledge Bro.
    Adds Fire Bars and Thwomps throughout the horizontal traversal.
    Boss room gets flanking Fire Bars around Morton's arena.
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/06-24.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x08'   # clockwise, length 8
    FB_CCW = b'\x00\x00\x00\x00\x00\x08'   # counter-clockwise, length 8

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Castle Traversal ─────────────────────────────────────────
    # Horizontal level, x ≈ 512-5300, y ≈ 400-700
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = []
    db_count = 0
    for s in area1.sprites:
        if s.stype == 118:   # Dry Bones -> Fire Bro / Hammer Bro / Sledge Bro
            ns = copy.deepcopy(s)
            ns.stype = [80, 95, 120][db_count % 3]
            ns.spritedata = SD
            new_sprites.append(ns)
            db_count += 1
        elif s.stype == 119: # Giant Dry Bones -> Sledge Bro
            ns = copy.deepcopy(s)
            ns.stype = 120
            ns.spritedata = SD
            new_sprites.append(ns)
        else:
            new_sprites.append(s)

    # Fire Bars scattered along the traversal path — alternating CW/CCW
    for i, x in enumerate(range(750, 5000, 350)):
        sd = FB_CW if i % 2 == 0 else FB_CCW
        new_sprites.append(spr(62, x, 490, sd))

    # Thwomps above main path (must clear spike balls and rotating platforms)
    for x in [950, 1550, 2150, 2750, 3350, 3950, 4550]:
        new_sprites.append(spr(47, x, 384))

    # Chain Chomps in open horizontal sections
    for x in [1250, 2050, 2850, 3650, 4450]:
        new_sprites.append(spr(146, x, 610))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Boss Room (Morton Koopa Jr.) ─────────────────────────────
    # Zone 1 at (1568, 1408, 1456, 224). Keep Morton intact.
    # Add Fire Bars flanking the arena edges.
    area2 = parse_course_bin(arc.get_file('course/course2.bin'))
    boss_sprites = list(area2.sprites)
    boss_sprites.append(spr(62, 1650, 1500, FB_CW))    # left flank
    boss_sprites.append(spr(62, 2900, 1500, FB_CCW))   # right flank
    boss_sprites.append(spr(47, 2000, 1408))            # Thwomp left
    boss_sprites.append(spr(47, 2600, 1408))            # Thwomp right
    area2.sprites = boss_sprites
    area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
    arc.set_file('course/course2.bin', serialize_course_bin(area2))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/06-24.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/06-24.arc ({len(data)} bytes)')
    print("Modified 6-Castle: Morton's Keep")


def create_level_6_mushroom_houses():
    print("[W6] Mushroom Houses not yet built")


def create_level_6_ambush():
    print("[W6] Ambushes not yet built")


def create_level_6_cannon():
    """6-Cannon: Summit Blitz — Gauntlet run to the warp cannon.

    Modifies vanilla 06-36 (which already has the zone, entrance, and
    cannon sprite). Clears everything except the warp cannon and essential
    zone mechanics, then adds a W6 gauntlet in the run-up:
    Chain Chomps, Fire Bars, Thwomps, Hammer Bros, Bullet Bills.
    The cannon at the end blasts to World 8.
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite

    with open('extracted files/Stage/06-36.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    area = parse_course_bin(arc.get_file('course/course1.bin'))

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x06'
    FB_CCW = b'\x00\x00\x00\x00\x00\x06'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # Keep all original sprites EXCEPT strip nothing — just add on top.
    # Zone: x=256-2048, y=264-776. Ground is approximately y=660.
    # Cannon is at x=920. Run-up gauntlet spans x=350-870.
    keep_sprites = list(area.sprites)  # keep vanilla cannon + zone controllers

    # Gauntlet: six tightly-spaced hazard clusters
    gauntlet = [
        # (stype, x, y, sd)
        (146, 370, 650, SD),           # Chain Chomp 1
        (62,  420, 560, FB_CW),        # Fire Bar CW
        (47,  480, 480, SD),           # Thwomp
        (95,  540, 640, SD),           # Hammer Bro
        (62,  590, 560, FB_CCW),       # Fire Bar CCW
        (146, 640, 650, SD),           # Chain Chomp 2
        (47,  700, 480, SD),           # Thwomp
        (62,  750, 560, FB_CW),        # Fire Bar CW
        (95,  800, 640, SD),           # Hammer Bro
        (62,  850, 560, FB_CCW),       # Fire Bar CCW
        (120, 870, 630, SD),           # Sledge Bro right before cannon
    ]

    for stype, x, y, sd in gauntlet:
        keep_sprites.append(spr(stype, x, y, sd))

    area.sprites = keep_sprites
    area.loaded_sprites = sorted(set(s.stype for s in keep_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area))

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open('output/ChaosStation/Stage/06-36.arc', 'wb') as f:
        f.write(data)
    print(f'Saved: output/ChaosStation/Stage/06-36.arc ({len(data)} bytes)')
    print('Created 06-36: Summit Blitz (W6 Cannon)')


def create_level_6_airship():
    print("[W6] Airship 06-38 not yet built — using vanilla")


# ═══════════════════════════════════════════════════════════════════
#  WORLD 8 — "Inferno's End"
# ═══════════════════════════════════════════════════════════════════

def create_level_8_1():
    """8-1: Scorched Entry — open lava fields, intro to the final world.
    Three sections: lava pit crossing → fire bar corridor → lava lake finale.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_LAVA)
    a.set_tileset(1, db.TILESET_KOOPA_OUT)
    a.set_background(db.BG_LAVA)
    a.set_time(400)
    GY = 26
    LAVA_Y = (GY + 3) * 16   # lava surface 3 tiles below ground
    LAVA_SD = b'\x00\x00\x00\x00\x01\x00'  # waves + solid kill zone
    POD_SD  = b'\x00\x00\x00\x00\x00\x02'  # delay=2 like vanilla
    GEY_SD  = b'\x00\x00\x00\x00\x00\x21'  # medium eruption, starts erupting
    fb_cw   = b'\x00\x00\x00\x00\x10\x05'
    fb_ccw  = b'\x00\x00\x00\x00\x00\x05'
    a.add_zone(0, 0, 7840, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)

    # Spawn platform
    a.add_ground(0, GY, 12, 5, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 94 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Lava floor spanning the whole level (flat top)
    a.add_sprite(db.LAVA_FILL, 0, LAVA_Y, spritedata=LAVA_SD)

    # ══ SECTION A: Lava pit crossing (X 14–93) — DENSE ══
    plat_a = [(14,GY,5),(23,GY,4),(31,GY-2,4),(39,GY,5),(48,GY,4),(56,GY-2,4),(64,GY,5),(73,GY,4),(81,GY,5)]
    for px, py, pw in plat_a:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Podoboos — placed ABOVE lava, where they jump to (3 tiles above ground)
    for lbx in [18, 27, 35, 44, 52, 60, 68, 77]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    # Fire Piranhas in every gap
    for fpx in [20, 34, 50, 62, 78]:
        a.add_sprite(db.FIRE_PIRANHA_PLANT, fpx * 16, (GY - 4) * 16)
    # Crowbers — dense flock
    for cx in [16, 28, 38, 48, 58, 70, 82]:
        a.add_sprite(db.CROWBER, cx * 16, (GY - 8) * 16)
    # Lava Geysers — erupting from lava surface
    for gx in [19, 33, 46, 58, 70, 80]:
        a.add_sprite(db.LAVA_GEYSER, gx * 16, LAVA_Y, spritedata=GEY_SD)
    # Mecha-Koopas on platforms
    for mx in [16, 40, 65, 83]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    # Fire Bros on elevated platforms
    a.add_ground(30, GY - 6, 4, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 31 * 16, (GY - 7) * 16)
    a.add_ground(62, GY - 6, 4, 3, tileset=1)
    a.add_sprite(db.FIRE_BRO, 63 * 16, (GY - 7) * 16)
    # Star Coin #1 — over a lava gap
    a.add_sprite(db.STAR_COIN, 44 * 16, (GY - 4) * 16, spritedata=bytes([0,0,0,0,0,0]))

    # Midway flag platform
    a.add_ground(88, GY, 10, 5, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 94 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_sprite(db.MECHAKOOPA, 91 * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 95 * 16, (GY - 1) * 16)

    # ══ SECTION B: Fire Bar corridor (X 100–180) — tight ══
    CY = GY - 6
    a.add_ground(100, GY, 83, 5, tileset=1)
    a.add_ground(100, CY - 1, 83, 3, tileset=1)  # solid ceiling, no gaps
    for fbx in range(107, 175, 8):
        a.add_sprite(db.FIRE_BAR, fbx * 16, (GY - 3) * 16, spritedata=fb_cw)
    for fbx in range(111, 179, 8):
        a.add_sprite(db.FIRE_BAR, fbx * 16, (GY - 4) * 16, spritedata=fb_ccw)
    for mx in [105, 120, 135, 150, 165]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    for dx in [112, 140, 168]:
        a.add_sprite(db.DRY_BONES, dx * 16, (GY - 1) * 16)
    # Star Coin #2 — floating inside the corridor, high up between fire bar rotations
    # Player must duck under fire bars at the right moment to grab it
    a.add_sprite(db.STAR_COIN, 155 * 16, (GY - 4) * 16, spritedata=bytes([0,0,0,0,1,0]))

    # ══ SECTION C: Lava lake finale (X 186–325) — brutal ══
    lake = [
        (186,GY,6),(197,GY-3,4),(206,GY,5),(216,GY-2,4),(225,GY,6),
        (236,GY-3,4),(245,GY,5),(255,GY-2,4),(264,GY,6),(275,GY-3,4),
        (285,GY,8),(298,GY,14),
    ]
    for px, py, pw in lake:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Podoboos everywhere in lake — above lava, threatening platforms
    for lbx in [193, 203, 213, 222, 233, 242, 252, 261, 272, 282]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    # Dense Crowbers
    for cx in [190, 205, 218, 230, 244, 257, 268, 280, 294]:
        a.add_sprite(db.CROWBER, cx * 16, (GY - 8) * 16)
    # Mecha-Koopas and Fire Bros on every other platform
    for mx in [188, 208, 228, 247, 267, 287]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    for fbx in [200, 220, 240, 260, 278]:
        a.add_sprite(db.FIRE_BRO, fbx * 16, (GY - 4) * 16)
    # Active Lava Geysers in lake
    for gx in [195, 210, 224, 238, 254, 270, 284]:
        a.add_sprite(db.LAVA_GEYSER, gx * 16, LAVA_Y, spritedata=GEY_SD)
    # Volcano rocks raining from sky
    a.add_sprite(db.VOLCANO_ROCK, 215 * 16, 4 * 16)
    a.add_sprite(db.VOLCANO_ROCK, 245 * 16, 4 * 16)
    a.add_sprite(db.VOLCANO_ROCK, 275 * 16, 4 * 16)
    # Star Coin #3 — floating visibly over the lava gap between platforms (risky jump)
    a.add_sprite(db.STAR_COIN, 272 * 16, (GY - 9) * 16, spritedata=bytes([0,0,0,0,2,0]))

    # Bridge C→D (gap was 24 tiles: x=312..334)
    a.add_ground(312, GY,     8, 5, tileset=1)   # x=312-319
    a.add_ground(322, GY - 3, 7, 5, tileset=1)   # x=322-328, gap=2 ✓
    a.add_ground(329, GY,     6, 5, tileset=1)   # x=329-334, gap=0 ✓ → connects to 335

    # ══ SECTION D: Banzai Bill Alley (X 335–460) ══
    # Platforms with gaps, Banzai Bills from right walls, Podoboos + Geysers
    a.add_ground(335, GY, 8, 5, tileset=1)
    a.add_ground(348, GY-3, 5, 5, tileset=1)
    a.add_ground(358, GY, 7, 5, tileset=1)
    a.add_ground(370, GY-4, 5, 5, tileset=1)
    a.add_ground(380, GY, 8, 5, tileset=1)
    a.add_ground(393, GY-3, 5, 5, tileset=1)
    a.add_ground(403, GY, 7, 5, tileset=1)
    a.add_ground(415, GY-4, 5, 5, tileset=1)
    a.add_ground(425, GY, 8, 5, tileset=1)
    a.add_ground(438, GY, 5, 5, tileset=1)
    # Bridge D→Goal (gap was 13 tiles: x=443..454)
    a.add_ground(443, GY, 12, 5, tileset=1)      # x=443-454, lands directly into x=455 ✓
    # Banzai Bill Launchers — staggered X so bills are offset in time, not a solid wall
    # Low launcher fires ground-level bills; high launcher fires sky-level bills
    # Mid-height gap (~GY-5) lets player dash through between the two streams
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 443 * 16, (GY - 1) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 449 * 16, (GY - 9) * 16)
    # Podoboos above lava
    for lbx in [339, 354, 366, 377, 390, 400, 412, 422, 435]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    # Active geysers
    for gx in [342, 356, 368, 382, 395, 406, 418, 428]:
        a.add_sprite(db.LAVA_GEYSER, gx * 16, LAVA_Y, spritedata=GEY_SD)
    # Fire Bros and Mecha-Koopas on platforms
    for fbx in [350, 372, 395, 417, 437]:
        a.add_sprite(db.FIRE_BRO, fbx * 16, (GY - 4) * 16)
    for mx in [337, 360, 382, 405, 427]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    # Dense Crowbers above
    for cx in [340, 358, 375, 392, 408, 424, 442]:
        a.add_sprite(db.CROWBER, cx * 16, (GY - 9) * 16)
    # Volcano rocks raining down
    a.add_sprite(db.VOLCANO_ROCK, 360 * 16, 2 * 16)
    a.add_sprite(db.VOLCANO_ROCK, 395 * 16, 2 * 16)
    a.add_sprite(db.VOLCANO_ROCK, 428 * 16, 2 * 16)
    # Fire Bars guarding the final stretch
    a.add_sprite(db.FIRE_BAR, 408 * 16, GY * 16, spritedata=fb_cw)
    a.add_sprite(db.FIRE_BAR, 420 * 16, GY * 16, spritedata=fb_ccw)
    a.add_sprite(db.FIRE_BAR, 432 * 16, GY * 16, spritedata=fb_cw)

    # End platform and goal — clear landing zone past the Banzai Bill launchers
    a.add_ground(455, GY, 25, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 470 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/08-01.arc')
    print('Created 8-1: Scorched Entry')


def create_level_8_2():
    """8-2: Poison Depths — static poison pits, narrow platform crossings.

    Mechanic: Deep poison pits (static — no rise) separate platforms.
    Danger comes from enemies pushing you off narrow bridges into the pits:
      - Dry Bones revive and keep chasing
      - Giant Dry Bones are wide and block narrow bridges
      - Bob-ombs explode on bridges, knocking you in
      - Buzzy Beetles drop from ceiling onto your path

    Section A: Wide platforms, intro pits — learn the danger of falling in.
    Section B: Narrow bridges (3-4 tiles), heavy Dry Bones traffic.
    Section C: Giant Dry Bones gauntlet — wide enemies on narrow spans.
    Section D: Final mix — Thwomps + enemies + tightest bridges.
    Secret exit: hidden pipe in a raised alcove off a mid-level platform.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    GY  = 20   # main walkable floor row
    CY  = 2    # cave ceiling row
    PIT = 28   # poison surface row — pits expose this, platforms stay above it

    def ey(row): return (row - 1) * 16

    # Static poison (mode=0), flat top (n10=8) — fills zone from PIT row downward.
    POISON_SD = b'\x00\x00\x00\x00\x08\x00'

    # ─── AREA 1 ─────────────────────────────────────────────────────────────
    a1 = builder.add_area(1)
    a1.set_tileset(0, db.TILESET_STANDARD)
    a1.set_tileset(1, db.TILESET_CAVE)
    a1.set_background(db.BG_UNDERGROUND)
    a1.set_time(400)
    a1.add_zone(0, 0, 6880, 640, zone_id=0, music=db.MUSIC_UNDERGROUND,
                cam_mode=0, visibility=16)

    a1.add_ground(0, CY, 430, 3, tileset=1)   # ceiling across entire level

    # Spawn platform + entrance
    a1.add_ground(0, GY, 13, 5, tileset=1)
    a1.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a1.add_entrance(1, 109 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Poison fills the zone from row PIT downward — visible in every pit gap
    a1.add_sprite(db.POISON_FILL, 5 * 16, PIT * 16, spritedata=POISON_SD)

    # ══ SECTION A: Wide platforms, 6-tile pits — learn the hazard (X 15–110) ══
    plats_a = [
        (15, GY, 9), (30, GY, 9), (45, GY, 9),
        (60, GY, 9), (75, GY, 9), (90, GY, 11),
    ]
    for px, py_, pw in plats_a:
        a1.add_ground(px, py_, pw, 5, tileset=1)

    # Star Coin #1 — floating over the 3rd pit (x=54), accessible by jumping from x=53
    a1.add_sprite(db.STAR_COIN, 57 * 16, (GY - 3) * 16,
                  spritedata=bytes([0, 0, 0, 0, 0, 0]))

    for dx in [17, 32, 47, 62, 77, 92]:
        a1.add_sprite(db.DRY_BONES, dx * 16, ey(GY))
    for gdx in [36, 66]:
        a1.add_sprite(db.GIANT_DRY_BONES, gdx * 16, ey(GY))
    # Spinies hidden BEHIND Dry Bones — player sees the Dry Bones first, walks into Spiny
    for sx in [19, 49, 79]:
        a1.add_sprite(db.SPINY, sx * 16, ey(GY))
    # Spike Tops on ceiling — slow but unstompable, drop down when player is below
    for stx in [22, 52, 82]:
        a1.add_sprite(db.SPIKE_TOP, stx * 16, (CY + 3) * 16)
    # Upside-Down Spinies tucked above the pits — nearly invisible until they drop
    for udx in [27, 57, 87]:
        a1.add_sprite(db.UPSIDE_DOWN_SPINY, udx * 16, (CY + 3) * 16)

    # Midway flag
    a1.add_ground(103, GY, 10, 5, tileset=1)
    a1.add_sprite(db.MIDWAY_FLAG, 109 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ SECTION B: Narrow bridges (3-4 tiles) — Bob-ombs + Dry Bones (X 115–200) ══
    bridges_b = [
        (115, GY,  4), (123, GY,  4), (131, GY,  4),
        (139, GY,  4), (147, GY,  4), (155, GY, 10),
    ]
    for bx, by_, bw in bridges_b:
        a1.add_ground(bx, by_, bw, 5, tileset=1)

    # Elevated rest platform — SECRET ALCOVE above main path here
    # Alcove: hidden room above x=155 platform, accessed by jumping through false ceiling
    a1.add_ground(156, GY - 7, 9, 3, tileset=1)   # alcove floor
    a1.add_ground(156, CY + 3, 1, GY - 7 - CY - 3 - 1, tileset=1)  # left sealing wall
    a1.add_sprite(db.STAR_COIN, 159 * 16, (GY - 8) * 16,
                  spritedata=bytes([0, 0, 0, 0, 1, 0]))
    a1.add_pipe(162, GY - 7, height=3)
    a1.add_entrance(2, 163 * 16, (GY - 7) * 16,
                    etype=db.ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=3)

    for dx in [116, 124, 132, 140, 148, 157]:
        a1.add_sprite(db.DRY_BONES, dx * 16, ey(GY))
    for bx in [117, 125, 133, 141, 149]:
        a1.add_sprite(db.BOB_OMB, bx * 16, ey(GY))
    # Spinies at the END of bridges — just as you land, a Spiny is waiting
    for sx in [118, 134, 150]:
        a1.add_sprite(db.SPINY, sx * 16, ey(GY))
    # Amps hovering at player chest height over the middle of narrow bridges
    # Forces the player to crouch-jump or arc over them — very tight on a 4-tile span
    for ax in [120, 128, 136, 144]:
        a1.add_sprite(db.AMP, ax * 16, (GY - 1) * 16)
    # Spike Tops at bridge ends — can't stomp, blocks the landing spot
    for stx in [122, 138]:
        a1.add_sprite(db.SPIKE_TOP, stx * 16, ey(GY))
    for cbx in [118, 126, 134, 142, 150, 158, 163]:
        a1.add_sprite(db.BUZZY_BEETLE, cbx * 16, (CY + 3) * 16)

    # ══ SECTION C: Giant Dry Bones gauntlet — wider pits, bulky enemies (X 167–280) ══
    plats_c = [
        (167, GY,  8), (180, GY,  8), (193, GY,  5),
        (203, GY,  8), (216, GY,  8), (229, GY,  8),
        (242, GY,  5), (252, GY,  8), (265, GY, 11),
    ]
    for px, py_, pw in plats_c:
        a1.add_ground(px, py_, pw, 5, tileset=1)

    # Star Coin #3 — on a platform guarded by two Giant Dry Bones
    a1.add_sprite(db.STAR_COIN, 256 * 16, (GY - 2) * 16,
                  spritedata=bytes([0, 0, 0, 0, 2, 0]))
    a1.add_sprite(db.GIANT_DRY_BONES, 254 * 16, ey(GY))
    a1.add_sprite(db.GIANT_DRY_BONES, 258 * 16, ey(GY))

    for gdx in [169, 182, 205, 218, 231, 267]:
        a1.add_sprite(db.GIANT_DRY_BONES, gdx * 16, ey(GY))
    for dx in [195, 244]:
        a1.add_sprite(db.DRY_BONES, dx * 16, ey(GY))
    for bx in [170, 183, 206, 232]:
        a1.add_sprite(db.BOB_OMB, bx * 16, ey(GY))
    # Spinies mixed in with Giant Dry Bones — Giant blocks your view of the Spiny behind it
    for sx in [173, 209, 234, 269]:
        a1.add_sprite(db.SPINY, sx * 16, ey(GY))
    # Upside-Down Spinies over the pit gaps — drop spines down into the jumps
    for udx in [178, 201, 214, 227, 250, 264]:
        a1.add_sprite(db.UPSIDE_DOWN_SPINY, udx * 16, (CY + 3) * 16)
    # Spike Tops on platforms — slow unstompable walker blocks your path
    for stx in [186, 220, 245]:
        a1.add_sprite(db.SPIKE_TOP, stx * 16, ey(GY))

    # ══ SECTION D: Thwomp gauntlet + narrow bridges — final sprint (X 278–400) ══
    plats_d = [
        (278, GY,  4), (286, GY,  4), (294, GY,  4), (302, GY,  4),
        (310, GY,  8), (323, GY,  4), (331, GY,  4), (339, GY,  4),
        (347, GY,  8), (360, GY,  4), (368, GY,  4), (376, GY, 12),
    ]
    for px, py_, pw in plats_d:
        a1.add_ground(px, py_, pw, 5, tileset=1)

    # Thwomps hovering over certain platforms in section D (drop when player passes)
    for tx in [280, 296, 325, 341, 362, 370]:
        a1.add_sprite(db.THWOMP, tx * 16, (CY + 4) * 16)

    for dx in [279, 287, 295, 303, 311, 324, 332, 340, 349, 361, 369, 378]:
        a1.add_sprite(db.DRY_BONES, dx * 16, ey(GY))
    for gdx in [313, 350, 380]:
        a1.add_sprite(db.GIANT_DRY_BONES, gdx * 16, ey(GY))
    # Amps in the gaps between Thwomp bridges — you must navigate past them WHILE
    # watching for the Thwomp above. Can't stomp, can't walk through.
    for ax in [283, 299, 327, 343, 364]:
        a1.add_sprite(db.AMP, ax * 16, (GY - 1) * 16)
    # Spinies on the 8-tile rest platforms — no safe spot to relax
    for sx in [312, 348, 377]:
        a1.add_sprite(db.SPINY, sx * 16, ey(GY))
    # Spike Tops on narrow 4-tile spans — blocking the already-tight crossing
    for stx in [280, 294, 331, 339]:
        a1.add_sprite(db.SPIKE_TOP, stx * 16, ey(GY))
    for cbx in [281, 290, 298, 306, 316, 328, 337, 345, 354, 366, 375, 383]:
        a1.add_sprite(db.BUZZY_BEETLE, cbx * 16, (CY + 3) * 16)

    # Goal
    a1.add_ground(390, GY, 18, 5, tileset=1)
    a1.add_sprite(db.GOAL_POLE, 401 * 16, (GY - 1) * 16)

    # ─── AREA 2: Secret exit — poison pit gauntlet, shorter (3200px) ────────
    SY  = 18    # floor row in area 2
    SCY = 2     # ceiling

    a2 = builder.add_area(2)
    a2.set_tileset(0, db.TILESET_STANDARD)
    a2.set_tileset(1, db.TILESET_CAVE)
    a2.set_background(db.BG_UNDERGROUND)
    a2.set_time(300)
    a2.add_zone(0, 0, 3200, 640, zone_id=0, music=db.MUSIC_UNDERGROUND,
                cam_mode=0, visibility=16)

    a2.add_ground(0, SCY, 200, 3, tileset=1)
    a2.add_ground(0, SY, 12, 5, tileset=1)
    a2.add_entrance(3, 5 * 16, (SY - 2) * 16,
                    etype=db.ENTRANCE_PIPE_UP, zone_id=0,
                    dest_area=1, dest_entrance=2)
    a2.add_sprite(db.POISON_FILL, 0, (SY + 8) * 16, spritedata=POISON_SD)

    # Area 2: alternating platforms and pits, increasing enemy pressure
    plats_2 = [
        (14, SY, 9), (28, SY, 5), (38, SY, 9), (52, SY, 5),
        (62, SY, 9), (76, SY, 5), (86, SY, 9), (100, SY, 5),
        (110, SY, 9), (124, SY, 5), (134, SY, 9), (148, SY, 14),
    ]
    for px, py_, pw in plats_2:
        a2.add_ground(px, py_, pw, 5, tileset=1)

    for dx in [15, 39, 63, 87, 111, 135, 150]:
        a2.add_sprite(db.DRY_BONES, dx * 16, ey(SY))
    for gdx in [29, 53, 77, 101, 125]:
        a2.add_sprite(db.GIANT_DRY_BONES, gdx * 16, ey(SY))
    for bx in [16, 40, 64, 88, 112, 136]:
        a2.add_sprite(db.BOB_OMB, bx * 16, ey(SY))
    for sx in [17, 41, 65, 89, 113]:
        a2.add_sprite(db.SPINY, sx * 16, ey(SY))
    for ax in [31, 55, 79, 103, 127]:
        a2.add_sprite(db.AMP, ax * 16, (SY - 1) * 16)
    for stx in [18, 43, 67]:
        a2.add_sprite(db.SPIKE_TOP, stx * 16, ey(SY))
    for udx in [26, 50, 74, 98, 122, 146]:
        a2.add_sprite(db.UPSIDE_DOWN_SPINY, udx * 16, (SCY + 3) * 16)
    for cbx in [18, 32, 45, 58, 70, 84, 95, 108, 118, 130, 142, 155]:
        a2.add_sprite(db.BUZZY_BEETLE, cbx * 16, (SCY + 3) * 16)

    # Secret-exit runout: give clear solid ground AFTER the red pole.
    a2.add_ground(162, SY, 24, 5, tileset=1)
    a2.add_secret_goal(158, SY - 1)

    builder.save('output/ChaosStation/Stage/08-02.arc')
    print('Created 8-2: Poison Depths (static pits, narrow bridges, enemy pressure)')


def create_level_8_3():
    """8-3: Meteor Storm — floating lava-cliff platforms under a barrage of meteors.

    Distinct from 8-1:
      - Tileset: LAVA_CLIFF (rocky cliffs, not the outdoor Koopa bricks of 8-1)
      - Music: athletic sky theme (8-1 uses lava overworld) — reads as open-sky bombardment
      - Enemies: Podoboos + Fire Piranhas + Dry Bones + Mecha-Koopas + Amps (no flyers/Bob-ombs that dive into lava)
      - No Fire Bros (those belong to 8-1) — Sledge Bros ground-pound the platforms
      - No Geysers (8-1 signature) — dense Volcano Rock rain is the primary hazard
      - No Banzai Bills mid-level — Para-Bob-ombs parachute from the sky instead
      - Gaps fixed: bridge platforms added between every section transition
      - Zone width must cover the goal (was 7840px / 490 tiles; pole sat past scroll bound)

    Section A: Flame Jets + Sledge Bros + meteor intro
    Section B: Open sky — dense meteor lanes + Para-Bob-ombs falling
    Section C: Fire Snake gauntlet on narrow ledges
    Section D: King Bill finale + meteor wall + Sledge Bros
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_LAVA)
    a.set_tileset(1, db.TILESET_LAVA_CLIFF)
    a.set_background(db.BG_LAVA)
    a.set_time(400)
    GY = 26

    def ey(row): return (row - 1) * 16

    POD_SD = b'\x00\x00\x00\x00\x00\x02'  # Podoboo delay (vanilla-style) — they live in the lava
    LAVA_SURFACE_Y = (GY + 3) * 16       # must match LAVA_FILL placement

    # 8320 px = 520 tiles — goal at x=504 and end ground through ~511 must stay inside the zone
    # (7840 px only reached tile 490, so the camera stopped before the pole).
    a.add_zone(0, 0, 8320, 640, zone_id=0, music=db.MUSIC_SKY, cam_mode=0, visibility=16)

    # Spawn platform
    a.add_ground(0, GY, 12, 5, tileset=1)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 110 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    # Lava sea far below (flat top — kill zone; Podoboos anchor from the surface)
    a.add_sprite(db.LAVA_FILL, 0, LAVA_SURFACE_Y, spritedata=b'\x00\x00\x00\x00\x01\x00')

    # ══ SECTION A: Flame Jets + Sledge Bros + first meteor wave (X 14–102) ══
    plat_a = [
        (14,GY,7),(25,GY-3,5),(34,GY,7),(44,GY-4,4),(52,GY,8),
        (64,GY-3,5),(74,GY,7),(85,GY-4,4),(94,GY,8),
    ]
    for px, py, pw in plat_a:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Flame Jets shooting up from lava
    for fjx in [20, 31, 40, 58, 70, 80, 91]:
        a.add_sprite(db.FLAME_JET_LARGE, fjx * 16, LAVA_SURFACE_Y)
    # Podoboos — jump from lava in every major gap (same anchor idea as 8-1)
    for lbx in [22, 29, 37, 46, 60, 70, 79, 90]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    # Sledge Bros on platforms — heavy ground-pounders, very different feel from Fire Bros
    a.add_sprite(db.SLEDGE_BRO, 28 * 16, ey(GY - 3))   # platform (25,GY-3)
    a.add_sprite(db.SLEDGE_BRO, 55 * 16, ey(GY))        # platform (52,GY)
    a.add_sprite(db.SLEDGE_BRO, 66 * 16, ey(GY - 3))   # platform (64,GY-3)
    a.add_sprite(db.SLEDGE_BRO, 95 * 16, ey(GY))        # platform (94,GY)
    # Heat-themed ground patrol — x on platform spans only (see plat_a)
    for mx in [16, 38, 61, 96]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    for dx in [35, 46, 66]:
        a.add_sprite(db.DRY_BONES, dx * 16, (GY - 1) * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 41 * 16, (GY - 4) * 16)
    a.add_sprite(db.FIRE_PIRANHA_PLANT, 77 * 16, (GY - 4) * 16)
    # First meteor wave — sparse intro
    for vx in [22, 42, 68, 88]:
        a.add_sprite(db.VOLCANO_ROCK, vx * 16, 2 * 16)
    # Star Coin #1 — on isolated high island
    a.add_ground(72, GY - 8, 4, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 73 * 16, (GY - 9) * 16, spritedata=bytes([0, 0, 0, 0, 0, 0]))

    # Midway flag
    a.add_ground(104, GY, 10, 5, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 110 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ SECTION B: Open meteor zone — dense meteor rain + Para-Bob-ombs (X 116–213) ══
    # Para-Bob-ombs replace Banzai Bills here — they parachute DOWN from above
    plat_b = [
        (116,GY,6),(128,GY-4,5),(138,GY,6),(150,GY-5,4),(158,GY,6),
        (170,GY-4,5),(180,GY,6),(192,GY-5,4),(200,GY,8),
    ]
    for px, py, pw in plat_b:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Bridge: gap from 207 to 215 was 8 tiles — add stepping stone
    a.add_ground(209, GY - 2, 5, 5, tileset=1)   # bridge x=209-213, gap to 215 = 2 tiles
    # Dense meteor rain — this is the signature of 8-3 (more than 8-1!)
    for vx in [122, 132, 143, 155, 162, 175, 186, 196, 204]:
        a.add_sprite(db.VOLCANO_ROCK, vx * 16, 2 * 16)
    # Para-Bob-ombs falling from sky (parachuting bombs — unique sky hazard)
    for pbx in [120, 135, 148, 165, 178, 193, 202]:
        a.add_sprite(db.PARA_BOB_OMB, pbx * 16, 3 * 16)
    # Podoboos + Fire Piranhas in gaps / on tiered platforms (no Bob-ombs — they walk off cliffs)
    for lbx in [118, 125, 142, 154, 168, 182, 196, 206]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    for fpx in [131, 159, 174, 188]:
        a.add_sprite(db.FIRE_PIRANHA_PLANT, fpx * 16, (GY - 6) * 16)
    for fpx2 in [140, 203]:
        a.add_sprite(db.FIRE_PIRANHA_PLANT, fpx2 * 16, (GY - 5) * 16)
    for dx in [130, 152, 185]:
        a.add_sprite(db.DRY_BONES, dx * 16, ey(GY - 4))
    for ax in [123, 147, 176]:
        a.add_sprite(db.AMP, ax * 16, (GY - 6) * 16)
    # Star Coin #2 — under a safe overhang platform
    a.add_ground(155, GY - 10, 5, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 157 * 16, (GY - 11) * 16, spritedata=bytes([0, 0, 0, 0, 1, 0]))

    # ══ SECTION C: Fire Snake gauntlet on narrow ledges (X 215–341) ══
    plat_c = [
        (215,GY,9),(229,GY-3,6),(240,GY,8),(254,GY-4,5),(263,GY,9),
        (276,GY-3,6),(288,GY,8),(302,GY-4,5),(312,GY,10),(328,GY,14),
    ]
    for px, py, pw in plat_c:
        a.add_ground(px, py, pw, 5, tileset=1)
    for fsx in [220, 226, 235, 248, 258, 267, 280, 295, 305, 315, 330]:
        a.add_sprite(db.FIRE_SNAKE, fsx * 16, ey(GY))
    # Sledge Bros replacing Fire Bros on the wider platforms
    a.add_sprite(db.SLEDGE_BRO, 231 * 16, ey(GY - 3))
    a.add_sprite(db.SLEDGE_BRO, 265 * 16, ey(GY))
    a.add_sprite(db.SLEDGE_BRO, 314 * 16, ey(GY))
    for lbx in [218, 234, 252, 270, 286, 300, 318, 332]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    for dx in [222, 244, 266, 292]:
        a.add_sprite(db.DRY_BONES, dx * 16, (GY - 1) * 16)
    a.add_sprite(db.DRY_BONES, 304 * 16, ey(GY - 4))   # on 302,GY-4 platform — not main tier
    for dx2 in [231, 264, 290]:
        a.add_sprite(db.DRY_BONES, dx2 * 16, ey(GY - 3))
    for mx in [241, 268, 318]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    # Continued meteor rain over Section C
    for vx in [224, 244, 268, 290, 316, 334]:
        a.add_sprite(db.VOLCANO_ROCK, vx * 16, 2 * 16)
    # Para-Bob-ombs still falling
    for pbx in [230, 255, 278, 308]:
        a.add_sprite(db.PARA_BOB_OMB, pbx * 16, 3 * 16)
    # Star Coin #3 — threading between Fire Snakes
    a.add_sprite(db.STAR_COIN, 302 * 16, (GY - 6) * 16, spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # ══ BRIDGE C→D: was a 29-tile gap — now 3 stepping stones (X 342–369) ══
    a.add_ground(342, GY,     7, 5, tileset=1)   # x=342-348
    a.add_ground(354, GY - 3, 6, 5, tileset=1)   # x=354-359, gap=5 ✓
    a.add_ground(363, GY,     6, 5, tileset=1)   # x=363-368, gap=3 ✓, leads to 370
    # Hazards on bridge stones
    for fsx in [343, 356, 364]:
        a.add_sprite(db.FIRE_SNAKE, fsx * 16, ey(GY))
    for vx in [348, 361]:
        a.add_sprite(db.VOLCANO_ROCK, vx * 16, 2 * 16)

    # ══ SECTION D: Volcano Finale — King Bill + meteor wall + Sledge Bros (X 370–490) ══
    plat_d = [
        (370,GY,7),(382,GY-4,5),(392,GY,7),(404,GY-5,4),(413,GY,8),
        (426,GY-3,5),(436,GY,7),(448,GY-4,5),(458,GY,9),(472,GY,12),
    ]
    for px, py, pw in plat_d:
        a.add_ground(px, py, pw, 5, tileset=1)
    # King Bill — screen-filling bullet, signature finale moment
    a.add_sprite(db.KING_BILL, 490 * 16, (GY - 5) * 16)
    # Heaviest meteor barrage in the level
    for vrx in [374, 386, 395, 407, 416, 428, 440, 452, 463, 476]:
        a.add_sprite(db.VOLCANO_ROCK, vrx * 16, 2 * 16)
    # Para-Bob-ombs raining down throughout D
    for pbx in [372, 387, 400, 415, 430, 445, 460, 475]:
        a.add_sprite(db.PARA_BOB_OMB, pbx * 16, 3 * 16)
    # Fire Snakes patrolling platforms
    for fsx in [373, 384, 394, 406, 415, 428, 438, 450, 460, 474]:
        a.add_sprite(db.FIRE_SNAKE, fsx * 16, ey(GY))
    # Sledge Bros on wider platforms — ground pounders knock you into the pit
    for sbx in [384, 415, 440, 460]:
        a.add_sprite(db.SLEDGE_BRO, sbx * 16, ey(GY - 4))
    for lbx in [376, 390, 404, 420, 434, 448, 462, 478]:
        a.add_sprite(db.PODOBOO, lbx * 16, (GY - 3) * 16, spritedata=POD_SD)
    for dx in [374, 396, 415, 438, 460, 472]:
        a.add_sprite(db.DRY_BONES, dx * 16, (GY - 1) * 16)
    for mx in [383, 395, 427, 450, 475]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)
    for fpx in [388, 418, 446]:
        a.add_sprite(db.FIRE_PIRANHA_PLANT, fpx * 16, (GY - 5) * 16)
    # Banzai Bills finally appear HERE at the end (not mid-level like 8-1)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 488 * 16, (GY - 2) * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 488 * 16, (GY - 7) * 16)

    # Goal
    a.add_ground(492, GY, 20, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 504 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/08-03.arc')
    print('Created 8-3: Meteor Storm')


def create_level_8_4():
    """8-4: Midnight Trench — finale swim gauntlet (packed, long, high tension).

    Pacing: bait coins → Blooper/urchin choke → Jellybeam storm → Fishbone trench + midway →
    red-coin panic ring → Porcu/Chomp runway → dry stairs to goal. model_dark for Jellybeams.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_OCEAN)
    # Use explicit ghost-house backdrop so this reads as a haunted deep-sea trench.
    a.set_background(db.BG_GHOST_HOUSE,
                     x_scroll_a=0, y_scroll_a=0, x_scroll_b=0, y_scroll_b=0,
                     zoom_a=1, zoom_b=1)
    a.set_time(500)

    GY = 34
    # Tighter vertical camera + full darkness (required for Jellybeam visuals)
    a.add_zone(0, 0, 14000, 544, zone_id=0, music=db.MUSIC_UNDERWATER, cam_mode=0,
               visibility=36, model_dark=12, terrain_dark=12)

    a.add_sprite(db.WATER_FILL, 0, 0, spritedata=b'\x01\x00\x00\x00\x00\x00')
    a.add_entrance(0, 5 * 16, 22 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 420 * 16, 24 * 16, etype=db.ENTRANCE_NORMAL)

    TX = 0

    # ══ §1 — False calm (coin trails + density) ══
    a.add_ground(TX, GY, 110, 6, tileset=1)
    a.add_ground(TX, 0, 110, 5, tileset=1)
    for px, py, pw in [(10, GY - 6, 2), (22, GY - 9, 3), (38, GY - 5, 2), (52, GY - 8, 2),
                       (68, GY - 4, 3), (88, GY - 7, 2), (98, GY - 5, 3)]:
        a.add_ground(TX + px, py, pw, 5, tileset=1)
    for cx in [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 90, 100]:
        a.add_sprite(db.CHEEP_CHEEP, cx * 16, 28 * 16)
    a.add_sprite(db.BULBER, 35 * 16, 26 * 16)
    a.add_sprite(db.BULBER, 72 * 16, 24 * 16)
    a.add_star_coin(28, GY - 3, coin_num=0)
    a.add_sprite(db.GLOW_LIGHT, 45 * 16, 20 * 16)
    a.add_coin_line(12, 26, 10)
    a.add_coin_line(55, 24, 8)
    a.add_question_block(62, 22, contents=1)
    a.add_question_block(18, 20, contents=0)

    # ══ §2 — Blooper choke (low ceiling + urchin gates) ══
    a.add_ground(TX + 110, GY, 140, 6, tileset=1)
    a.add_ground(TX + 110, 0, 140, 6, tileset=1)
    for ox in [118, 132, 146, 160, 174, 188, 202, 216, 230, 240]:
        a.add_ground(TX + ox, GY - 12, 2, 8, tileset=1)
        a.add_ground(TX + ox, GY - 3, 2, 3, tileset=1)
    for bx in [122, 136, 150, 168, 182, 196, 210, 224, 236]:
        a.add_sprite(db.BLOOPER, bx * 16, 20 * 16)
    a.add_sprite(db.BLOOPER_NANNY, 154 * 16, 17 * 16)
    a.add_sprite(db.BLOOPER_NANNY, 214 * 16, 19 * 16)
    for ux in [120, 140, 158, 178, 200, 220]:
        a.add_sprite(db.URCHIN, ux * 16, (GY - 8) * 16)
        a.add_sprite(db.URCHIN, ux * 16, (GY - 4) * 16)
    a.add_star_coin(188, 12, coin_num=1)
    a.add_coin_line(125, 22, 6)
    a.add_coin_line(165, 18, 5)
    a.add_coin_line(205, 22, 6)
    a.add_question_block(172, 16, contents=0)

    # ══ §3 — Jellybeam storm ══
    a.add_ground(TX + 250, GY, 170, 6, tileset=1)
    a.add_ground(TX + 250, 0, 170, 5, tileset=1)
    for jx in range(258, 410, 11):
        a.add_sprite(db.JELLYBEAM, jx * 16, (6 + (jx % 3)) * 16)
    for jx2 in range(264, 400, 18):
        a.add_sprite(db.JELLYBEAM, jx2 * 16, 10 * 16)
    for ax in [270, 300, 330, 360, 390]:
        a.add_sprite(db.BULBER, ax * 16, 24 * 16)
    for bx in [262, 285, 312, 338, 368, 398]:
        a.add_sprite(db.BLOOPER, bx * 16, 22 * 16)
    a.add_coin_line(280, 20, 8)
    a.add_coin_line(340, 18, 7)
    a.add_coin_line(375, 24, 6)

    # ══ §4 — Fishbone trench ══
    a.add_ground(TX + 420, GY + 2, 140, 5, tileset=1)
    a.add_ground(TX + 420, 0, 140, 4, tileset=1)
    for ox in [432, 452, 472, 492, 512, 532, 548]:
        a.add_ground(TX + ox, GY - 4, 2, 6, tileset=1)
    for fx in [428, 438, 448, 458, 468, 478, 488, 498, 508, 518, 528, 540]:
        a.add_sprite(db.FISHBONE, fx * 16, 26 * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 460 * 16, 30 * 16)
    a.add_sprite(db.SPINY_CHEEP_CHEEP, 500 * 16, 29 * 16)
    a.add_sprite(db.BIG_CHEEP_CHEEP, 520 * 16, 28 * 16)
    a.add_sprite(db.BLOOPER_NANNY, 485 * 16, 18 * 16)
    a.add_star_coin(455, 22, coin_num=2)
    a.add_sprite(db.MIDWAY_FLAG, 480 * 16, (GY + 1) * 16,
                 spritedata=b'\x00\x00\x00\x01\x00\x00')
    a.add_coin_line(430, 24, 5)
    a.add_coin_line(510, 20, 6)

    # ══ §5 — Red-coin panic ring (urchin rim + hunters) ══
    a.add_ground(TX + 560, GY, 110, 6, tileset=1)
    a.add_ground(TX + 560, 0, 110, 5, tileset=1)
    for ox in [575, 595, 620, 645]:
        a.add_ground(TX + ox, GY - 9, 3, 7, tileset=1)
    a.add_red_coin_ring(615, 22, pattern='circle')
    for ux in [580, 600, 630, 650]:
        a.add_sprite(db.URCHIN, ux * 16, (GY - 6) * 16)
    for bx in [570, 610, 640]:
        a.add_sprite(db.BLOOPER, bx * 16, 20 * 16)
    for fx in [565, 585, 625, 655]:
        a.add_sprite(db.FISHBONE, fx * 16, 27 * 16)
    a.add_coin_line(600, 26, 5)

    # ══ §6 — Porcu + Boss Bass runway ══
    a.add_ground(TX + 670, GY, 120, 6, tileset=1)
    a.add_ground(TX + 670, 0, 120, 5, tileset=1)
    for ox in [685, 705, 730, 755]:
        a.add_ground(TX + ox, GY - 10, 3, 8, tileset=1)
    a.add_sprite(db.PORCU_PUFFER, 695 * 16, 24 * 16)
    a.add_sprite(db.PORCU_PUFFER, 740 * 16, 26 * 16)
    a.add_sprite(db.CHEEP_CHOMP, 715 * 16, 26 * 16)
    for bx in [680, 700, 720, 750, 770]:
        a.add_sprite(db.BLOOPER, bx * 16, 18 * 16)
    for bx2 in [688, 728, 762]:
        a.add_sprite(db.BIG_CHEEP_CHEEP, bx2 * 16, 30 * 16)
    a.add_coin_line(710, 22, 6)
    a.add_question_block(725, 20, contents=1)

    # ══ §7 — Surface breach (dry goal) ══
    a.add_ground(TX + 790, 20, 60, 3, tileset=1)
    a.add_ground(TX + 790, 22, 60, 18, tileset=1)
    a.add_staircase(TX + 808, 19, 7, direction=1, tileset=1)
    a.add_sprite(db.CHEEP_CHEEP, 798 * 16, 18 * 16)
    a.add_sprite(db.BLOOPER, 792 * 16, 16 * 16)
    a.add_sprite(db.GOAL_POLE, 825 * 16, 8 * 16)

    builder.save('output/ChaosStation/Stage/08-04.arc')
    print('Created 8-4: Midnight Trench (underwater)')


def create_level_8_5():
    """8-5: Magma Rise — THE signature level. Climb above rising lava.
    Ascending terrain over lava sea; the ground rises in stairstep formation
    forcing ever-higher platforming while Poseboos and Crowbers attack.
    Three risky side-pocket Star Coins that cost precious climbing time.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_LAVA)
    a.set_tileset(1, db.TILESET_KOOPA_OUT)
    a.set_background(db.BG_LAVA)
    a.set_time(400)
    a.add_zone(0, 0, 9280, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)
    # Cloud Area (sprite 234): type=5 drifting death clouds, location in low nybble.
    DEATH_CLOUD_DRIFT_1 = b'\x00\x00\x00\x00\x00\x51'
    DEATH_CLOUD_DRIFT_2 = b'\x00\x00\x00\x00\x00\x52'
    DEATH_CLOUD_DRIFT_3 = b'\x00\x00\x00\x00\x00\x53'
    DEATH_CLOUD_DRIFT_4 = b'\x00\x00\x00\x00\x00\x54'
    DEATH_CLOUD_DRIFT_5 = b'\x00\x00\x00\x00\x00\x55'
    DEATH_CLOUD_DRIFT_6 = b'\x00\x00\x00\x00\x00\x56'
    DEATH_CLOUD_DRIFT_7 = b'\x00\x00\x00\x00\x00\x57'
    DEATH_CLOUD_DRIFT_8 = b'\x00\x00\x00\x00\x00\x58'
    DEATH_CLOUD_DRIFT_9 = b'\x00\x00\x00\x00\x00\x59'

    # The ground RISES: each chunk is higher than the last, over a lava sea
    # GY values: start at 28, end at 6 — the player climbs 22 tiles upward
    a.add_entrance(0, 3 * 16, 27 * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 118 * 16, 17 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    # Lava sea below (fills from y=30 down)
    a.add_sprite(db.LAVA_FILL, 0, 30 * 16, spritedata=b'\x00\x00\x00\x00\x01\x00')
    # Rising lava particle effect
    a.add_sprite(db.RISING_LAVA_FX, 0, 0)
    # Faster, compact chase wall: many tight strips with short spacing.
    # Start slightly LEFT of spawn so pressure begins immediately.
    a.add_location(1,    0 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(2,   70 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(3,  160 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(4,  250 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(5,  340 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(6,  430 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(7,  520 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(8,  610 * 16, 0, 8 * 16, 27 * 16)
    a.add_location(9,  700 * 16, 0, 8 * 16, 27 * 16)
    a.add_sprite(db.CLOUD_AREA,   2 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_1)
    a.add_sprite(db.CLOUD_AREA,  72 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_2)
    a.add_sprite(db.CLOUD_AREA, 162 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_3)
    a.add_sprite(db.CLOUD_AREA, 252 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_4)
    a.add_sprite(db.CLOUD_AREA, 342 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_5)
    a.add_sprite(db.CLOUD_AREA, 432 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_6)
    a.add_sprite(db.CLOUD_AREA, 522 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_7)
    a.add_sprite(db.CLOUD_AREA, 612 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_8)
    a.add_sprite(db.CLOUD_AREA, 702 * 16, 8 * 16, spritedata=DEATH_CLOUD_DRIFT_9)

    # ══ PHASE 1: Slow ascent (X 0–120) — learn the pace, low platforms ══
    phase1 = [
        (0,  28, 12), (14, 27, 8),  (26, 26, 7),  (37, 25, 8),
        (49, 24, 7),  (60, 23, 8),  (72, 22, 7),  (84, 21, 8),
        (96, 20, 7),  (107,19, 8),  (118,18, 7),
    ]
    for px, py, pw in phase1:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Podoboos bouncing from lava below
    for lbx in [15, 28, 50, 73, 97]:
        a.add_sprite(db.PODOBOO, lbx * 16, 24 * 16, spritedata=b'\x00\x00\x00\x00\x00\x02')
    for cx in [20, 42, 64, 88, 112, 35, 55, 82]:
        a.add_sprite(db.CROWBER, cx * 16, 10 * 16)
    # Star Coin #1 — left alcove detour, costs time
    a.add_ground(40, 18, 5, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 42 * 16, 17 * 16, spritedata=bytes([0,0,0,0,0,0]))
    a.add_sprite(db.MIDWAY_FLAG, 118 * 16, 17 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ PHASE 2: Acceleration zone (X 124–250) — speed up, Amps on platforms ══
    phase2 = [
        (126,17, 7),(137,15, 6),(147,14, 7),(158,13, 6),(168,12, 7),
        (180,11, 6),(190,10, 7),(202, 9, 6),(213, 8, 7),(225, 7, 6),
        (236, 6, 7),(248, 5, 8),
    ]
    for px, py, pw in phase2:
        a.add_ground(px, py, pw, 5, tileset=1)
    for lbx in [130, 150, 170, 193, 215, 238]:
        a.add_sprite(db.PODOBOO, lbx * 16, 24 * 16, spritedata=b'\x00\x00\x00\x00\x00\x02')
    # Amps on platforms (can't stomp them — must dodge)
    for ax, ay in [(142, 14), (160, 12), (182, 10), (205, 8), (226, 7)]:
        a.add_sprite(db.AMP, ax * 16, ay * 16)
    # Fire Bros on platforms
    for fbx in [145, 195]:
        a.add_sprite(db.FIRE_BRO, fbx * 16, 12 * 16)
    for cx in [133, 155, 178, 200, 224, 247]:
        a.add_sprite(db.CROWBER, cx * 16, 3 * 16)
    for vrx in [146, 176, 206, 236]:
        a.add_sprite(db.VOLCANO_ROCK, vrx * 16, 1 * 16)
    # Star Coin #2 — right shelf detour off the main climb path
    a.add_ground(192, 4, 5, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 194 * 16, 3 * 16, spritedata=bytes([0,0,0,0,1,0]))

    # ══ PHASE 3: Sprint finale (X 254–400) — fastest, springboards, Fire Snake at top ══
    phase3 = [
        (256, 4, 6),(264, 3, 6),(273, 4, 5),(281, 3, 5),(290, 4, 5),
        (298, 3, 5),(307, 4, 5),(315, 3, 5),(324, 4, 6),(333, 3, 5),
        (342, 4, 5),(351, 3, 5),(362, 4, 6),(375, 3, 8),(387, 4, 16),
    ]
    for px, py, pw in phase3:
        a.add_ground(px, py, pw, 5, tileset=1)
    for lbx in [258, 275, 292, 310, 328, 345, 365]:
        a.add_sprite(db.PODOBOO, lbx * 16, 24 * 16, spritedata=b'\x00\x00\x00\x00\x00\x02')
    # Fire Snake guards the summit
    a.add_sprite(db.FIRE_SNAKE, 370 * 16, 2 * 16)
    a.add_sprite(db.FIRE_SNAKE, 385 * 16, 2 * 16)
    a.add_sprite(db.FIRE_SNAKE, 288 * 16, 2 * 16)
    a.add_sprite(db.FIRE_SNAKE, 335 * 16, 2 * 16)
    for ax, ay in [(266, 3), (286, 2), (306, 3), (326, 2), (346, 3)]:
        a.add_sprite(db.AMP, ax * 16, ay * 16)
    for cx in [260, 280, 300, 320, 340, 360]:
        a.add_sprite(db.CROWBER, cx * 16, 1 * 16)
    for vrx in [270, 298, 326, 354, 382]:
        a.add_sprite(db.VOLCANO_ROCK, vrx * 16, 0 * 16)
    # Star Coin #3 — left nook just before summit
    a.add_ground(351, 0, 4, 2, tileset=1)
    a.add_sprite(db.STAR_COIN, 352 * 16, 0 * 16, spritedata=bytes([0,0,0,0,2,0]))

    # ══ PHASE 4: Summit Sprint (X 406–580) — horizontal gauntlet at peak height ══
    # The climb is over — now sprint right at the summit dodging everything
    phase4 = [
        (406, 3, 7),(417, 4, 6),(426, 3, 7),(437, 4, 6),(446, 3, 7),
        (458, 4, 6),(467, 3, 7),(479, 4, 6),(489, 3, 7),(501, 4, 6),
        (511, 3, 7),(523, 4, 6),(533, 3, 8),(545, 4, 16),
    ]
    for px, py, pw in phase4:
        a.add_ground(px, py, pw, 5, tileset=1)
    # Podoboos still jumping from below
    for lbx in [409, 420, 430, 440, 453, 462, 473, 483, 494, 505, 515, 526]:
        a.add_sprite(db.PODOBOO, lbx * 16, 24 * 16, spritedata=b'\x00\x00\x00\x00\x00\x02')
    # Fire Snakes everywhere at the summit
    for fsx in [410, 421, 432, 443, 455, 466, 477, 492, 506, 518, 532]:
        a.add_sprite(db.FIRE_SNAKE, fsx * 16, 2 * 16)
    # Amps in tight columns
    for ax, ay in [(418, 2), (442, 3), (466, 2), (492, 3), (518, 2)]:
        a.add_sprite(db.AMP, ax * 16, ay * 16)
    # Crowbers diving from above
    for cx in [412, 425, 440, 460, 475, 495, 515, 535]:
        a.add_sprite(db.CROWBER, cx * 16, 0 * 16)
    # Fire Bros on elevated rocks
    for fbx in [418, 448, 472, 500, 525]:
        a.add_sprite(db.FIRE_BRO, fbx * 16, 2 * 16)
    # Volcano rocks raining down at the summit
    for vrx in [420, 450, 480, 510, 540]:
        a.add_sprite(db.VOLCANO_ROCK, vrx * 16, 0 * 16)
    # End-pressure artillery so the summit no longer feels free
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 548 * 16, 3 * 16)
    a.add_sprite(db.BANZAI_BILL_LAUNCHER, 548 * 16, 8 * 16)

    # Goal at the summit
    a.add_sprite(db.GOAL_POLE, 553 * 16, 2 * 16)

    builder.save('output/ChaosStation/Stage/08-05.arc')
    print('Created 8-5: Magma Rise')


def create_level_8_6():
    """8-6: Bowser's Vanguard — elite enemy pure gauntlet.
    Four brutal sections: Sledge Bros + Chain Chomps → Giant Spiked Balls
    → Amp column maze → Final Elite Wave (all Bros simultaneously).
    No lava floor — the challenge is entirely enemy-based.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_LAVA)
    a.set_tileset(1, db.TILESET_LAVA_CLIFF)
    a.set_background(db.BG_CASTLE)
    a.set_time(400)
    GY = 26
    # 8-6 reaches tile ~554 at the end; keep camera margin past the goal zone.
    a.add_zone(0, 0, 9600, 640, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, visibility=16)

    # Spawn
    a.add_ground(0, GY, 540, 5, tileset=1)  # solid floor for the entire gauntlet
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 104 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # ══ SECTION A: Sledge Bro + Chain Chomp double-gauntlet (X 0–100) ══
    for sbx in [18, 40, 62, 84, 30, 75]:
        a.add_sprite(db.SLEDGE_BRO, sbx * 16, (GY - 1) * 16)
    for ccx in [28, 52, 74, 96, 42, 86]:
        a.add_sprite(db.CHAIN_CHOMP, ccx * 16, (GY - 1) * 16)
    # Raised platforms above the fray
    for rpx in [20, 44, 68, 92]:
        a.add_ground(rpx, GY - 6, 5, 3, tileset=1)
        a.add_sprite(db.FIRE_BRO, (rpx + 2) * 16, (GY - 7) * 16)
    # Star Coin #1 — in the Chain Chomp zone alcove
    a.add_ground(55, GY - 9, 5, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 57 * 16, (GY - 10) * 16, spritedata=bytes([0,0,0,0,0,0]))

    # Midway flag
    a.add_sprite(db.MIDWAY_FLAG, 104 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ SECTION B: Giant Spiked Balls (X 108–190) ══
    # Narrow dodge alcoves; Spiked Balls roll through the main path
    for gsb_x in [120, 145, 165, 185, 135, 175]:
        a.add_sprite(db.GIANT_SPIKED_BALL, gsb_x * 16, (GY - 3) * 16)
    # Alcoves to dodge into (small platform pockets)
    for alc_x in [113, 132, 155, 175]:
        a.add_ground(alc_x, GY - 6, 4, 5, tileset=1)
        a.add_sprite(db.MECHAKOOPA, (alc_x + 1) * 16, (GY - 7) * 16)
    # Bob-omb Cannons firing Para-Bob-ombs from wall alcoves
    for can_x in [118, 143, 163]:
        a.add_sprite(db.BOB_OMB_CANNON, can_x * 16, (GY - 3) * 16)
    # Star Coin #2 — inside a Spiked Ball corridor (timed grab)
    a.add_sprite(db.STAR_COIN, 154 * 16, (GY - 8) * 16, spritedata=bytes([0,0,0,0,1,0]))

    # ══ SECTION C: Amp column maze (X 194–270) ══
    # Amps at multiple heights creating vertical columns; narrow gaps to thread
    for acol_x in range(200, 270, 10):
        # Three Amps per column at different heights
        a.add_sprite(db.AMP, acol_x * 16, (GY - 2) * 16)
        a.add_sprite(db.AMP, acol_x * 16, (GY - 6) * 16)
        a.add_sprite(db.AMP, acol_x * 16, (GY - 10) * 16)
    # Some columns are staggered so there's always a gap to pass through
    for acol_x in range(204, 268, 10):
        a.add_sprite(db.AMP, acol_x * 16, (GY - 4) * 16)
        a.add_sprite(db.AMP, acol_x * 16, (GY - 8) * 16)
    # Mecha-Koopas patrolling the floor
    for mx in [196, 212, 228, 244, 260]:
        a.add_sprite(db.MECHAKOOPA, mx * 16, (GY - 1) * 16)

    # ══ SECTION D: Final Elite Wave (X 275–380) ══
    # All Bro types + Thwomps + Giant Spiked Ball simultaneously
    elite = [
        # x,    stype
        (280,   db.SLEDGE_BRO),
        (295,   db.HAMMER_BRO),
        (310,   db.FIRE_BRO),
        (325,   db.SLEDGE_BRO),
        (340,   db.HAMMER_BRO),
        (355,   db.FIRE_BRO),
        (370,   db.SLEDGE_BRO),
    ]
    for ex, estype in elite:
        a.add_sprite(estype, ex * 16, (GY - 1) * 16)
    # Extra Sledge Bros in the elite wave
    for sbx in [300, 360]:
        a.add_sprite(db.SLEDGE_BRO, sbx * 16, (GY - 1) * 16)
    for tx in [288, 318, 348]:
        a.add_sprite(db.BIG_THWOMP, tx * 16, (GY - 10) * 16)
    # Two Giant Spiked Balls rolling through
    a.add_sprite(db.GIANT_SPIKED_BALL, 295 * 16, (GY - 3) * 16)
    a.add_sprite(db.GIANT_SPIKED_BALL, 340 * 16, (GY - 3) * 16)
    # Star Coin #3 — behind the Elite Wave, elevated platform
    a.add_ground(360, GY - 8, 5, 3, tileset=1)
    a.add_sprite(db.STAR_COIN, 362 * 16, (GY - 9) * 16, spritedata=bytes([0,0,0,0,2,0]))

    # ══ SECTION E: Final Hellwave — every enemy type at once (X 415–530) ══
    # King Bill passes through; all Bros + Chain Chomps + Thwomps + Amps
    a.add_sprite(db.KING_BILL, 530 * 16, (GY - 5) * 16)
    # All Bro types in alternating pairs
    for ex, estype in [
        (420, db.SLEDGE_BRO), (432, db.HAMMER_BRO), (444, db.FIRE_BRO),
        (456, db.SLEDGE_BRO), (468, db.HAMMER_BRO), (480, db.FIRE_BRO),
        (492, db.SLEDGE_BRO), (504, db.HAMMER_BRO), (516, db.FIRE_BRO),
    ]:
        a.add_sprite(estype, ex * 16, (GY - 1) * 16)
    # Big Thwomps crashing down
    for tx in [426, 452, 476, 500, 520]:
        a.add_sprite(db.BIG_THWOMP, tx * 16, (GY - 12) * 16)
    # Chain Chomps blocking the path
    for ccx in [436, 462, 488, 512]:
        a.add_sprite(db.CHAIN_CHOMP, ccx * 16, (GY - 1) * 16)
    # Giant Spiked Balls rolling through
    for gsbx in [430, 460, 490]:
        a.add_sprite(db.GIANT_SPIKED_BALL, gsbx * 16, (GY - 3) * 16)
    # Amps at multiple heights
    for ax in [440, 465, 490, 515]:
        a.add_sprite(db.AMP, ax * 16, (GY - 4) * 16)
        a.add_sprite(db.AMP, ax * 16, (GY - 8) * 16)
    # Bob-omb Cannons firing from walls
    a.add_sprite(db.BOB_OMB_CANNON, 528 * 16, (GY - 3) * 16)
    a.add_sprite(db.BOB_OMB_CANNON, 528 * 16, (GY - 7) * 16)
    # Raised platforms with Fire Bros
    for rpx in [422, 458, 494]:
        a.add_ground(rpx, GY - 8, 5, 3, tileset=1)
        a.add_sprite(db.FIRE_BRO, (rpx + 2) * 16, (GY - 9) * 16)

    # Goal
    a.add_ground(535, GY, 20, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 547 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/08-06.arc')
    print('Created 8-6: Bowser\'s Vanguard')


def create_level_8_7():
    """8-7: Inferno Shaft — climb through rising lava on isolated platforms.
    NO continuous floor — only isolated platforms scattered at rows 6-30.
    Lava rises from below, flooding low platforms first and chasing the player
    upward. Three areas via pipes with escalating lava speed.
    Spritedata: mode=n4 (byte2 hi), dist=n7*16+n8 (byte3 lo + byte4 hi),
                waves=n9=1 (byte4 lo). e.g. mode=5,dist=24: b'\\x00\\x00\\x50\\x01\\x81\\x00'
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()

    CY = 2    # ceiling row (h=3 → rows 2-4)

    # Rising lava spritedata (mode, dist=24 blocks unless noted)
    # dist=24: n7=1,n8=8 → byte3=0x01, byte4=0x81 (n8=8,n9=1 waves)
    # dist=20: n7=1,n8=4 → byte3=0x01, byte4=0x41
    LAVA_SLOW = b'\x00\x00\x60\x01\x81\x00'  # mode=6 slow-normal, dist=24
    LAVA_MED  = b'\x00\x00\x60\x01\x81\x00'  # mode=6 slow-normal, dist=24
    LAVA_FAST = b'\x00\x00\x50\x01\x81\x00'  # mode=5 very slow (same as area 1 — plenty of time)

    # ════════════════════════════════════════════════════════════════
    # AREA 1 — The Climb Begins (slow lava, gentle ascending gaps)
    # ════════════════════════════════════════════════════════════════
    a1 = builder.add_area(1)
    a1.set_tileset(0, db.TILESET_LAVA)
    a1.set_tileset(1, db.TILESET_KOOPA_OUT)
    a1.set_background(db.BG_LAVA)
    a1.set_time(400)
    a1.add_zone(0, 0, 2400, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)

    # Ceiling (blocks escaping upward)
    a1.add_ground(0, CY, 150, 3, tileset=1)

    # Lava rises from just below lowest platform — NO solid floor
    # Lowest platform is row 30; lava starts at row 34, rises 24 blocks (to row 10)
    a1.add_sprite(db.LAVA_FILL, 0, 34 * 16, spritedata=LAVA_SLOW)

    # Spawn ledge (rows 30-33, x=0-7)
    a1.add_entrance(0, 4 * 16, 29 * 16, etype=db.ENTRANCE_NORMAL)
    a1.add_ground(0, 30, 8, 4, tileset=1)

    # Isolated platforms climbing from row 30 to row 6
    # Each platform: (x, top_row, width) — 4 tiles thick
    # Horizontal gap ~4 tiles, vertical jump ~4 rows (comfortable)
    plats_a1 = [
        (11, 28, 7),   # step up 2
        (22, 24, 7),   # +4
        (33, 20, 7),   # +4
        (44, 16, 7),   # +4
        (55, 12, 7),   # +4
        (66, 16, 7),   # -4 (variation — must NOT fall into lava)
        (77, 12, 7),   # +4 back up
        (88,  8, 7),   # +4
        (99,  6, 7),   # +2
        (110, 6, 24),  # wide exit platform
    ]
    for px, py, pw in plats_a1:
        a1.add_ground(px, py, pw, 4, tileset=1)

    # Exit pipe to Area 2
    a1.add_pipe(129, 6, height=4, tileset=0)
    a1.add_entrance(1, 130 * 16, 6 * 16,
                    etype=db.ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=2, dest_entrance=2)

    # Enemies
    for x in [14, 26, 37, 48, 59]:
        a1.add_sprite(db.DRY_BONES, x * 16, 24 * 16)
    for x in [40, 62, 82, 105]:
        a1.add_sprite(db.CROWBER, x * 16, 4 * 16)
    a1.add_sprite(db.FIRE_BRO, 70 * 16, 11 * 16)
    for x in [18, 50, 80]:
        a1.add_sprite(db.PODOBOO, x * 16, 34 * 16,
                      spritedata=b'\x00\x00\x00\x00\x00\x02')
    a1.add_sprite(db.STAR_COIN, 92 * 16, 7 * 16, spritedata=bytes([0,0,0,0,0,0]))

    # ════════════════════════════════════════════════════════════════
    # AREA 2 — Rising Heat (medium lava, tighter gaps + more enemies)
    # ════════════════════════════════════════════════════════════════
    a2 = builder.add_area(2)
    a2.set_tileset(0, db.TILESET_LAVA)
    a2.set_tileset(1, db.TILESET_KOOPA_OUT)
    a2.set_background(db.BG_LAVA)
    a2.set_time(400)
    a2.add_zone(0, 0, 2400, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)

    a2.add_ground(0, CY, 150, 3, tileset=1)
    a2.add_sprite(db.LAVA_FILL, 0, 34 * 16, spritedata=LAVA_MED)

    # Spawn pipe + small ledge at bottom-left
    a2.add_pipe(2, 29, height=4, tileset=0)
    a2.add_entrance(2, 3 * 16, 29 * 16, etype=db.ENTRANCE_PIPE_UP, zone_id=0)
    a2.add_entrance(1, 55 * 16, 13 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn
    a2.add_ground(0, 30, 5, 4, tileset=1)

    plats_a2 = [
        (8,  28, 6),
        (18, 24, 6),
        (28, 20, 6),
        (38, 16, 6),
        (48, 20, 6),   # dip — forces quick up-down-up decision
        (58, 14, 6),
        (68, 10, 6),
        (78, 14, 6),   # dip
        (88,  8, 6),
        (98,  6, 6),
        (108, 6, 24),  # exit platform
    ]
    for px, py, pw in plats_a2:
        a2.add_ground(px, py, pw, 4, tileset=1)

    a2.add_pipe(127, 6, height=4, tileset=0)
    a2.add_entrance(3, 128 * 16, 6 * 16,
                    etype=db.ENTRANCE_PIPE_DOWN, zone_id=0,
                    dest_area=3, dest_entrance=3)

    # Midway + enemies
    a2.add_sprite(db.MIDWAY_FLAG, 55 * 16, 13 * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')
    for x in [12, 32, 55, 78, 100]:
        a2.add_sprite(db.CROWBER, x * 16, 4 * 16)
    a2.add_sprite(db.HAMMER_BRO, 42 * 16, 15 * 16)
    a2.add_sprite(db.SLEDGE_BRO, 72 * 16, 9 * 16)
    for x in [20, 50, 80, 105]:
        a2.add_sprite(db.PODOBOO, x * 16, 34 * 16,
                      spritedata=b'\x00\x00\x00\x00\x00\x02')
    a2.add_sprite(db.THWOMP, 62 * 16, (CY + 3) * 16)
    a2.add_sprite(db.STAR_COIN, 90 * 16, 7 * 16, spritedata=bytes([0,0,0,0,1,0]))

    # ════════════════════════════════════════════════════════════════
    # AREA 3 — Inferno Summit (fast lava, sprint to goal)
    # ════════════════════════════════════════════════════════════════
    a3 = builder.add_area(3)
    a3.set_tileset(0, db.TILESET_LAVA)
    a3.set_tileset(1, db.TILESET_KOOPA_OUT)
    a3.set_background(db.BG_LAVA)
    a3.set_time(250)
    a3.add_zone(0, 0, 2400, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)

    a3.add_ground(0, CY, 150, 3, tileset=1)
    a3.add_sprite(db.LAVA_FILL, 0, 34 * 16, spritedata=LAVA_FAST)

    # ── Wall-jump shaft ──────────────────────────────────────────────
    # Left wall x=5-7, right wall x=12-14, inner gap x=8-11 (4 tiles)
    # Shaft spans rows 8-30 (22 rows) — player bounces up while lava rises
    a3.add_ground( 5, 8, 3, 23, tileset=1)   # left wall
    a3.add_ground(12, 8, 3, 23, tileset=1)   # right wall

    # Spawn pipe inside shaft, player emerges facing the walls
    a3.add_pipe(8, 29, height=3, tileset=0)
    a3.add_entrance(3, 9 * 16, 29 * 16, etype=db.ENTRANCE_PIPE_UP, zone_id=0)

    # Exit ledge starts at right wall (x=12) — gap x=8-11 stays OPEN so player
    # can wall-jump up through it and land on the ledge to the right
    a3.add_ground(12, 7, 28, 3, tileset=1)   # rows 7-9, x=12-39

    # ── Regular section after shaft (small gaps, easy jumps) ─────────
    # All near row 7-10 so lava (max rise to row 14) never threatens here
    plats_exit = [
        (43, 8, 8), (55, 7, 8), (67, 8, 8),
        (79, 7, 8), (91, 8, 8), (103, 7, 24),
    ]
    for px, py, pw in plats_exit:
        a3.add_ground(px, py, pw, 4, tileset=1)

    # Enemies — wall-jump shaft has Crowbers diving down; exit section has Fire Bros
    for x in [9, 11, 9, 11]:   # alternate sides inside shaft
        a3.add_sprite(db.CROWBER, x * 16, 10 * 16)
    for x in [48, 62, 76, 92]:
        a3.add_sprite(db.CROWBER, x * 16, 4 * 16)
    a3.add_sprite(db.CROWBER, 58 * 16, 4 * 16)
    a3.add_sprite(db.CROWBER, 82 * 16, 4 * 16)
    a3.add_sprite(db.SLEDGE_BRO, 95 * 16, 6 * 16)
    for x in [25, 50, 75]:
        a3.add_sprite(db.PODOBOO, x * 16, 34 * 16,
                      spritedata=b'\x00\x00\x00\x00\x00\x02')
    a3.add_sprite(db.STAR_COIN, 107 * 16, 6 * 16, spritedata=bytes([0,0,0,0,2,0]))

    # Goal
    a3.add_sprite(db.GOAL_POLE, 120 * 16, 6 * 16)

    builder.save('output/ChaosStation/Stage/08-07.arc')
    print('Created 8-7: Inferno Shaft (3-area rising lava platform climb)')


def create_level_8_tower():
    """8-Tower (08-22): Kamek's Spire — vertical climb + Magikoopa boss.
    Modifies vanilla 08-22.arc:
    Area 1: Fire Bars + Thwomps + Hammer Bros added throughout the climb.
    Area 2: Boss room gets flanking Fire Bars and Amps along the floor.
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/08-22.arc'
    dst = 'output/ChaosStation/Stage/08-22.arc'
    try:
        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())
    except Exception as e:
        print(f"[W8] Skipping 8-Tower: couldn't open {src} — {e}")
        return

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x06'
    FB_CCW = b'\x00\x00\x00\x00\x00\x06'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Tower Climb ──────────────────────────────────────────────────
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    sprites1 = list(area1.sprites)

    # Upgrade existing Dry Bones → rotating Bros (Hammer / Fire / Sledge)
    upgraded = []
    db_count = 0
    for s in sprites1:
        if s.stype == db.DRY_BONES:
            ns = copy.deepcopy(s)
            ns.stype = [db.HAMMER_BRO, db.FIRE_BRO, db.SLEDGE_BRO][db_count % 3]
            upgraded.append(ns)
            db_count += 1
        else:
            upgraded.append(s)

    # Fire Bars at intervals up the climb shaft (approximate pixel coords from vanilla)
    for y, x_cw, x_ccw in [
        (3600, 500, 700), (3200, 530, 730), (2800, 500, 700),
        (2400, 530, 700), (2000, 500, 730), (1600, 530, 700),
        (1200, 500, 700), (800,  530, 730),
    ]:
        upgraded.append(spr(db.FIRE_BAR, x_cw,  y, FB_CW))
        upgraded.append(spr(db.FIRE_BAR, x_ccw, y + 128, FB_CCW))

    # Thwomps flanking narrow passages
    for y in [3400, 2600, 1800, 1000]:
        upgraded.append(spr(db.THWOMP, 608, y))

    # Chain Chomps lower portion
    for x, y in [(496, 3700), (736, 3500), (512, 3100)]:
        upgraded.append(spr(db.CHAIN_CHOMP, x, y))

    area1.sprites = upgraded
    area1.loaded_sprites = sorted(set(s.stype for s in upgraded))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Boss Room ────────────────────────────────────────────────────
    try:
        area2 = parse_course_bin(arc.get_file('course/course2.bin'))
        boss_sprites = list(area2.sprites)
        # Flank the Magikoopa arena with rotating Fire Bars
        boss_sprites.append(spr(db.FIRE_BAR, 320, 560, FB_CW))
        boss_sprites.append(spr(db.FIRE_BAR, 672, 560, FB_CCW))
        # Amps along the floor edges
        for ax in [288, 336, 656, 704]:
            boss_sprites.append(spr(db.AMP, ax, 592))
        area2.sprites = boss_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area2))
    except (KeyError, Exception):
        pass  # Boss area may not exist in vanilla, skip gracefully

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)
    print(f'Modified 8-Tower: Kamek\'s Spire ({len(data)} bytes)')


def create_level_8_airship():
    """8-Airship (08-38): The Doomship — final fortress before Bowser.
    Modifies vanilla 08-38.arc:
    Hull: adds Bob-omb Cannons, Chain Chomps, extra Hammer Bros.
    Boss: keeps Bowser Jr, flanks with Fire Bars.
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/08-38.arc'
    dst = 'output/ChaosStation/Stage/08-38.arc'
    try:
        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())
    except Exception as e:
        print(f"[W8] Skipping 8-Airship: couldn't open {src} — {e}")
        return

    SD = b'\x00\x00\x00\x00\x00\x00'
    FB_CW  = b'\x00\x00\x00\x00\x10\x05'
    FB_CCW = b'\x00\x00\x00\x00\x00\x05'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: Airship Hull ─────────────────────────────────────────────────
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    sprites1 = list(area1.sprites)

    # Upgrade Koopa Troopas → Hammer Bros throughout the hull
    upgraded = []
    koopa_count = 0
    for s in sprites1:
        if s.stype in (db.KOOPA, db.KOOPA_PARATROOPA):
            ns = copy.deepcopy(s)
            ns.stype = [db.HAMMER_BRO, db.FIRE_BRO][koopa_count % 2]
            upgraded.append(ns)
            koopa_count += 1
        else:
            upgraded.append(s)

    # Bob-omb Cannons on airship walls (fire Para-Bob-ombs across deck)
    for x, y in [(400, 400), (800, 432), (1200, 400), (1600, 432), (2000, 400)]:
        upgraded.append(spr(db.BOB_OMB_CANNON, x, y))

    # Chain Chomps on cannon turret platforms
    for x, y in [(600, 448), (1000, 432), (1400, 448), (1800, 432)]:
        upgraded.append(spr(db.CHAIN_CHOMP, x, y))

    # Crowbers patrolling the airship deck
    for x in [300, 700, 1100, 1500, 1900]:
        upgraded.append(spr(db.CROWBER, x, 300))

    area1.sprites = upgraded
    area1.loaded_sprites = sorted(set(s.stype for s in upgraded))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Bowser Jr Boss Room ─────────────────────────────────────────
    try:
        area2 = parse_course_bin(arc.get_file('course/course2.bin'))
        boss_sprites = list(area2.sprites)
        # Flank the Bowser Jr arena with Fire Bars
        boss_sprites.append(spr(db.FIRE_BAR, 288, 560, FB_CW))
        boss_sprites.append(spr(db.FIRE_BAR, 704, 560, FB_CCW))
        # Extra Hammer Bro flankers
        boss_sprites.append(spr(db.HAMMER_BRO, 320, 560))
        boss_sprites.append(spr(db.HAMMER_BRO, 672, 560))
        area2.sprites = boss_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in boss_sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area2))
    except (KeyError, Exception):
        pass

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)
    print(f'Modified 8-Airship: The Doomship ({len(data)} bytes)')


def create_level_8_ambush():
    """08-33/34/35: World 8 ambush arenas — lava-themed spring block encounters.
    Follows the same pattern as World 7 ambush: keeps required sprites
    (controller, Toad balloons, chest, Lakitu) and replaces spring block layouts.
    World 8 enemies: Fire Bro, Sledge Bro, Chain Chomp, Big Thwomp, Fire Snake.
    """
    import os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    CONTROLLER   = 454
    TOAD_BALLOON = 185
    CHEST        = 203
    LAKITU       = 54
    SPRING_BLOCK = 223
    SD = b'\x00\x00\x00\x00\x00\x00'

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    def modify_ambush(src_name, dst_name, new_blocks, extra_enemies=None):
        try:
            with open(f'extracted files/Stage/{src_name}', 'rb') as f:
                arc = U8Archive.load(f.read())
        except Exception as e:
            print(f"[W8] Skipping {src_name}: {e}")
            return
        course = parse_course_bin(arc.get_file('course/course1.bin'))

        kept = [s for s in course.sprites if s.stype != SPRING_BLOCK]
        for (x, y) in new_blocks:
            kept.append(spr(SPRING_BLOCK, x, y))
        if extra_enemies:
            for (stype, x, y) in extra_enemies:
                kept.append(spr(stype, x, y))

        course.sprites = kept
        course.loaded_sprites = sorted(set(s.stype for s in kept))
        arc.set_file('course/course1.bin', serialize_course_bin(course))
        os.makedirs('output/ChaosStation/Stage', exist_ok=True)
        with open(f'output/ChaosStation/Stage/{dst_name}', 'wb') as f:
            f.write(arc.pack())
        print(f'  Saved: {dst_name}')

    # --- 08-33 "Lava Springs" ---
    # 10 spring blocks over 2-tile lava gaps; Fire Bro + Sledge Bro threats
    lava_springs = [
        (272, 480), (320, 480), (368, 480), (416, 480), (464, 480),
        (512, 480), (560, 480), (608, 480), (656, 480), (704, 480),
        # Center elevated platform
        (416, 416), (464, 416), (512, 416),
    ]
    modify_ambush('08-33.arc', '08-33.arc', lava_springs,
                  extra_enemies=[(db.FIRE_BRO, 464, 320), (db.SLEDGE_BRO, 512, 352)])

    # --- 08-34 "Chain Chomp Pit" ---
    # Dense spring floor with Chain Chomps on varied chain lengths
    chomp_pit = [
        (256, 480), (304, 480), (352, 480), (400, 480), (448, 480),
        (496, 480), (544, 480), (592, 480), (640, 480), (688, 480), (736, 480),
        # Two elevated platforms
        (352, 416), (400, 416),
        (592, 416), (640, 416),
    ]
    modify_ambush('08-34.arc', '08-34.arc', chomp_pit,
                  extra_enemies=[
                      (db.CHAIN_CHOMP, 400, 352),
                      (db.CHAIN_CHOMP, 592, 352),
                      (db.BIG_THWOMP,  496, 288),
                  ])

    # --- 08-35 "Elite Ambush" ---
    # Two-tier arena: lower floor + elevated center shelf
    # Hammer Bro on top, Fire Snake on floor, Big Thwomp overhead
    elite_ambush = [
        # Lower floor (sparse — dangerous to stand on)
        (256, 480), (320, 480), (384, 480), (448, 480),
        (512, 480), (576, 480), (640, 480), (704, 480),
        # Elevated center shelf
        (384, 400), (416, 400), (448, 400), (480, 400), (512, 400), (544, 400), (576, 400),
    ]
    modify_ambush('08-35.arc', '08-35.arc', elite_ambush,
                  extra_enemies=[
                      (db.HAMMER_BRO,  480, 320),
                      (db.FIRE_SNAKE,  320, 432),
                      (db.FIRE_SNAKE,  608, 432),
                      (db.BIG_THWOMP,  496, 256),
                  ])

    print("Created W8 ambush arenas (08-33/34/35)")


def create_level_8_castle():
    """8-Castle (08-24): Bowser's Fortress — the climactic finale of the entire modpack.

    Vanilla zone layout (parsed from 08-24.arc):
      Area 1: zone x=512..5408, y=496..768  (floor≈y=720, ceiling≈y=512, height=272px)
      Area 2: zone x=520..1016, y=480..1344 (boss room, w=496, h=864)

    Area 1 — The Last Gauntlet: Replace all weak enemies, stack EVERY World 8 hazard
    across 5 pacing sections that fit within the real zone bounds.

    Area 2 — Bowser's Arena: Keep all existing boss-logic sprites. Add flanking hazards
    strictly within zone bounds (x=520..1016, y=480..1344).
    """
    import copy, os
    from tools.u8archive import U8Archive
    from tools.course_parser import parse_course_bin, serialize_course_bin, Sprite
    import tools.sprite_db as db

    src = 'extracted files/Stage/08-24.arc'
    dst = 'output/ChaosStation/Stage/08-24.arc'

    try:
        with open(src, 'rb') as f:
            arc = U8Archive.load(f.read())
    except Exception as e:
        print(f"[W8] Skipping 8-Castle: couldn't open {src} — {e}")
        return

    SD      = b'\x00\x00\x00\x00\x00\x00'
    FB_CW   = b'\x00\x00\x00\x00\x10\x07'   # clockwise Fire Bar
    FB_CCW  = b'\x00\x00\x00\x00\x00\x07'   # counter-clockwise Fire Bar
    FC_TOP  = b'\x00\x00\x00\x00\x01\x00'   # Flame Cannon: ceiling mount, fires down
    FC_BOT  = b'\x00\x00\x00\x00\x00\x00'   # Flame Cannon: floor mount, fires up
    GEY_SD  = b'\x00\x00\x00\x00\x00\x21'   # Lava Geyser: medium eruption

    # Real zone bounds for Area 1 (verified from vanilla parse):
    # x: 512..5408   y: 496..768
    # Ceiling tiles ≈ y=512   Floor/entrance ≈ y=704   Mid-corridor ≈ y=608
    CEIL_Y  = 516   # just below ceiling — Thwomps hang here
    MID_Y   = 608   # mid-corridor — Fire Bars pivot here
    FLOOR_Y = 704   # floor level — walking enemies stand here
    UPPER_Y = 560   # upper third — Crowbers, upper Amps
    LOWER_Y = 672   # lower third — Chain Chomps, lower hazards

    def spr(stype, x, y, sd=SD):
        return Sprite(stype=stype, x=x, y=y, spritedata=sd, zone_id=0, extra_byte=0)

    # ── Area 1: The Last Gauntlet ────────────────────────────────────────────
    area1 = parse_course_bin(arc.get_file('course/course1.bin'))
    new_sprites = []
    db_count = 0

    # Replace vanilla enemies; keep all decorative/environment sprites intact
    for s in area1.sprites:
        if s.stype == db.DRY_BONES:
            ns = copy.deepcopy(s)
            ns.stype      = [db.FIRE_BRO, db.HAMMER_BRO, db.SLEDGE_BRO][db_count % 3]
            ns.spritedata = SD
            new_sprites.append(ns)
            db_count += 1
        elif s.stype == db.GIANT_DRY_BONES:
            ns = copy.deepcopy(s)
            ns.stype      = db.SLEDGE_BRO
            ns.spritedata = SD
            new_sprites.append(ns)
        elif s.stype in (db.GOOMBA, db.KOOPA):
            ns = copy.deepcopy(s)
            ns.stype      = db.MECHAKOOPA
            ns.spritedata = SD
            new_sprites.append(ns)
        else:
            new_sprites.append(s)

    # ── Section A (x=700–1400): Fire Bars + Thwomps — warm-up ──
    # Fire Bar pairs: CW at mid height, CCW offset so they don't sync
    for i, x in enumerate(range(750, 1400, 320)):
        new_sprites.append(spr(db.FIRE_BAR, x,       MID_Y,      FB_CW))
        new_sprites.append(spr(db.FIRE_BAR, x + 100, MID_Y + 48, FB_CCW))
    # Thwomps drop from ceiling
    for x in [900, 1150, 1380]:
        new_sprites.append(spr(db.THWOMP, x, CEIL_Y))
    # Elite Bros on the floor
    new_sprites.append(spr(db.FIRE_BRO,   820,  FLOOR_Y))
    new_sprites.append(spr(db.HAMMER_BRO, 1080, FLOOR_Y))
    new_sprites.append(spr(db.SLEDGE_BRO, 1330, FLOOR_Y))

    # ── Section B (x=1450–2400): Flame Cannons + Chain Chomps — timing gauntlet ──
    # Alternating top (ceiling) and bottom (floor) cannons
    for i, x in enumerate(range(1500, 2400, 300)):
        if i % 2 == 0:
            new_sprites.append(spr(db.FLAME_CANNON, x, CEIL_Y + 16, FC_TOP))
        else:
            new_sprites.append(spr(db.FLAME_CANNON, x, FLOOR_Y - 16, FC_BOT))
    # Chain Chomps lurking at floor level
    for x in [1600, 1950, 2250]:
        new_sprites.append(spr(db.CHAIN_CHOMP, x, LOWER_Y))
    # Crowbers swooping overhead
    for x in [1520, 1820, 2100, 2370]:
        new_sprites.append(spr(db.CROWBER, x, UPPER_Y))

    # ── Section C (x=2450–3400): Giant Spiked Balls + Flame Jets — dodge corridor ──
    for x in [2500, 2900, 3200, 3380]:
        new_sprites.append(spr(db.GIANT_SPIKED_BALL, x, LOWER_Y))
    # Flame Jets in pairs from the floor
    for x in [2650, 2950, 3150]:
        new_sprites.append(spr(db.FLAME_JET_LARGE, x,       FLOOR_Y))
        new_sprites.append(spr(db.FLAME_JET_LARGE, x + 128, FLOOR_Y))
    # Lava Geysers between the jets
    for x in [2750, 3050, 3300]:
        new_sprites.append(spr(db.LAVA_GEYSER, x, FLOOR_Y + 16, GEY_SD))
    new_sprites.append(spr(db.BIG_THWOMP, 2800, CEIL_Y))
    new_sprites.append(spr(db.BIG_THWOMP, 3250, CEIL_Y))

    # ── Section D (x=3450–4500): Amp columns + Banzai Bills — sprint finale ──
    # Three Amp columns at staggered heights to thread between
    for x in [3500, 3800, 4100, 4400]:
        new_sprites.append(spr(db.AMP, x, UPPER_Y))      # upper Amp
        new_sprites.append(spr(db.AMP, x, MID_Y))        # mid Amp
        new_sprites.append(spr(db.AMP, x, LOWER_Y))      # lower Amp
    # Banzai Bill Launchers on the floor — firing right-to-left
    for x in [3600, 4000, 4350]:
        new_sprites.append(spr(db.BANZAI_BILL_LAUNCHER, x, FLOOR_Y))
    # Mecha-Koopas patrolling narrow gaps
    for x in [3650, 3950, 4200, 4450]:
        new_sprites.append(spr(db.MECHAKOOPA, x, FLOOR_Y))

    # ── Section E (x=4550–5300): Final Elite Wave — Big Thwomps + Sledge Bros ──
    for x in [4600, 4900, 5100, 5300]:
        new_sprites.append(spr(db.BIG_THWOMP, x, CEIL_Y))
    new_sprites.append(spr(db.SLEDGE_BRO,  4700, FLOOR_Y))
    new_sprites.append(spr(db.SLEDGE_BRO,  5000, FLOOR_Y))
    new_sprites.append(spr(db.HAMMER_BRO,  4850, FLOOR_Y))
    # King Bill in the final open stretch — the last obstacle before the boss door
    new_sprites.append(spr(db.KING_BILL, 5200, MID_Y))
    # Dense Crowber flock for the run to the boss door
    for x in [4580, 4750, 4980, 5120, 5280]:
        new_sprites.append(spr(db.CROWBER, x, UPPER_Y))

    area1.sprites = new_sprites
    area1.loaded_sprites = sorted(set(s.stype for s in new_sprites))
    arc.set_file('course/course1.bin', serialize_course_bin(area1))

    # ── Area 2: Rising-Lava Escape Room ─────────────────────────────────────
    # This is the post-Bowser escape sequence — NOT a traditional boss arena.
    # Verified zone: x=520..1016 (w=496), y=480..1344 (h=864)
    # Player enters from the top (entrance y=496) and must CLIMB DOWN then escape
    # while lava (LAVA_FILL at y=720) rises from below.
    # BOSS_ESCAPE_PLATs (type 50) are the crumbling platforms — do NOT remove them.
    # Vanilla already has 2 Fire Bars: x=528,y=992 (left-low) and x=992,y=960 (right-low).
    # Strategy: add Fire Bars at MID and UPPER heights, Amps on the climb route,
    # Crowbers diving through the vertical shaft, Fire Snake near the exit.
    try:
        area2 = parse_course_bin(arc.get_file('course/course2.bin'))
        escape_sprites = list(area2.sprites)

        # Room layout reference (all verified within zone bounds):
        # x-centre ≈ 768   left wall x≈528   right wall x≈992
        # top (entry) y≈496   lava surface y≈720   exit y≈1248
        # escape platforms are scattered from y≈592 to y≈1248

        # ── Extra Fire Bars at mid-height (y≈768-864) ──
        # Stagger CW/CCW so they don't sync — player must read both
        escape_sprites.append(spr(db.FIRE_BAR, 576,  800, FB_CW))
        escape_sprites.append(spr(db.FIRE_BAR, 944,  768, FB_CCW))
        escape_sprites.append(spr(db.FIRE_BAR, 752,  848, FB_CW))

        # ── Fire Bars at upper section (y≈608-704) — guarding the entry drop ──
        escape_sprites.append(spr(db.FIRE_BAR, 624,  640, FB_CCW))
        escape_sprites.append(spr(db.FIRE_BAR, 896,  672, FB_CW))

        # ── Amps floating at key choke points across the shaft ──
        # Placed at horizontal gaps between the escape platforms so the player
        # must time their jump around the Amp while the lava closes in below
        escape_sprites.append(spr(db.AMP, 688,  720))   # just above lava surface
        escape_sprites.append(spr(db.AMP, 848,  736))   # right side, lava level
        escape_sprites.append(spr(db.AMP, 608,  880))   # mid-left
        escape_sprites.append(spr(db.AMP, 912,  912))   # mid-right
        escape_sprites.append(spr(db.AMP, 752,  992))   # lower centre
        escape_sprites.append(spr(db.AMP, 656, 1072))   # near exit, left
        escape_sprites.append(spr(db.AMP, 864, 1072))   # near exit, right

        # ── Crowbers swooping through the vertical shaft ──
        # They dive at the player while they're trying to land on crumbling platforms
        for cy in [560, 656, 784, 912, 1040]:
            escape_sprites.append(spr(db.CROWBER, 768, cy))   # centre diver
        escape_sprites.append(spr(db.CROWBER, 600, 720))      # left ambush
        escape_sprites.append(spr(db.CROWBER, 940, 800))      # right ambush

        # ── Fire Snake near the bottom exit — final obstacle ──
        # Placed just above the exit platform (y≈1200) to block the last jump
        escape_sprites.append(spr(db.FIRE_SNAKE, 752, 1200))

        area2.sprites = escape_sprites
        area2.loaded_sprites = sorted(set(s.stype for s in escape_sprites))
        arc.set_file('course/course2.bin', serialize_course_bin(area2))
    except (KeyError, Exception) as e:
        print(f"[W8] Warning: couldn't enhance escape room in 08-24 — {e}")

    data = arc.pack()
    os.makedirs('output/ChaosStation/Stage', exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(data)
    print(f"Modified 8-Castle: Bowser's Fortress ({len(data)} bytes)")


# ═══════════════════════════════════════════════════════════════════
# WORLD 9 — "Chaos Absolute" — Veteran Challenge Levels
# ═══════════════════════════════════════════════════════════════════

def create_level_9_1():
    """9-1: Pixel Perfect — brutally hard precision platforming, zero enemies.

    Every surface is 1×1 tile. Gaps are 5–8 tiles wide (running-jump minimum).
    Heights vary wildly — massive up/down swings between consecutive platforms.
    Thwomps act as timing gates on key platforms: player must wait for the
    Thwomp to rise, then sprint past before it slams back down.
    Fire Bars rotate on several platforms, shrinking the safe landing window.

    Four sections:
      A) 1-tile beam crossing with 5-tile gaps — learn the precision
      B) Extreme height-swing gauntlet — platforms alternate GY and GY-12
      C) Thwomp timing gates — Thwomps block passage above 1-tile platforms
      D) Fire Bar finale — 1-tile platforms between spinning Fire Bars to goal
    Time limit: 250s (tight but fair if precise).
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GRASS)
    a.set_background(db.BG_ATHLETIC_SKY_1)
    a.set_time(250)

    GY  = 26   # low platform row
    GYH = 14   # high platform row (12 tiles up — max jump height is ~7, so must
               #  land on the high platform from a lower one via stairs/ramps)
    FB_CW  = b'\x00\x00\x00\x00\x10\x05'
    FB_CCW = b'\x00\x00\x00\x00\x00\x05'

    a.add_zone(0, 0, 8400, 640, zone_id=0, music=db.MUSIC_ATHLETIC, cam_mode=0, visibility=16)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 67 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Starting safe platform (only flat ground in the entire level)
    a.add_ground(0, GY, 6, 5, tileset=1)
    a.add_question_block(3, GY - 4, contents=1)

    # ══ SECTION A: 1-tile beams, 5-tile gaps ══
    # Heights oscillate between GY and GY-4 to force the player to aim up/down
    beams_a = [
        (8,  GY),    (14, GY-4),  (20, GY),    (26, GY-2),  (32, GY-6),
        (38, GY),    (44, GY-4),  (50, GY-2),  (56, GY-7),  (62, GY),
    ]
    for bx, by in beams_a:
        a.add_ground(bx, by, 1, 5, tileset=1)
    # Star Coin #1 — floating off-route below a high platform, requires a
    # precise short hop down from the GY-7 beam to grab and land on GY beam
    a.add_sprite(db.STAR_COIN, 56 * 16, (GY - 10) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))

    # Rest ledge + midway — 12 tiles gives the player a real run-up after respawn
    a.add_ground(65, GY, 12, 5, tileset=1)
    a.add_sprite(db.MIDWAY_FLAG, 67 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ SECTION B: Extreme height-swing — must ride a descending ramp to gain
    #   speed then launch into high platforms 12 tiles up ══
    # The trick: 2-tile-wide descending ramp gives running speed, then a
    # single 1-tile platform at GYH reachable only with full sprint momentum.
    # Then it drops immediately back to GY, repeat.
    swing_data = [
        # (ramp_x, ramp_y_start, target_x, target_y)
        (72,  GY,     80,  GYH),
        (83,  GY,     91,  GYH-2),
        (94,  GY-2,   102, GYH),
        (106, GY,     114, GYH-4),
        (117, GY-4,   125, GYH),
        (128, GY,     136, GYH-2),
    ]
    for rx, ry, tx, ty in swing_data:
        # Descending 2-step ramp
        a.add_ground(rx,     ry,     1, 5, tileset=1)
        a.add_ground(rx + 1, ry + 1, 1, 5, tileset=1)
        # High target platform (1 tile)
        a.add_ground(tx, ty, 1, 5, tileset=1)
    # Star Coin #2 — on the highest point between the two tallest swings
    a.add_sprite(db.STAR_COIN, 114 * 16, (GYH - 7) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))

    # Rest ledge
    a.add_ground(140, GY, 4, 5, tileset=1)

    # ══ SECTION C: Thwomp timing gates ══
    # 1-tile platform; Thwomp hangs 1 tile above it.
    # Player must wait for Thwomp to rise (after it slams), then sprint across.
    thwomp_plats = [
        (146, GY),    (152, GY-3),  (158, GY),    (164, GY-5),
        (170, GY-2),  (176, GY),    (182, GY-4),  (188, GY-1),
    ]
    for tx, ty in thwomp_plats:
        a.add_ground(tx, ty, 1, 5, tileset=1)
        # Thwomp centred directly above, 1 tile clearance
        a.add_sprite(db.THWOMP, tx * 16, (ty - 3) * 16)
    # Star Coin #3 — hovering above the 5th Thwomp, grab during the brief window
    # when the Thwomp is fully raised
    a.add_sprite(db.STAR_COIN, 170 * 16, (GY - 8) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # Rest ledge
    a.add_ground(192, GY, 4, 5, tileset=1)

    # ══ SECTION D: Fire Bar finale — 1-tile platforms between spinning bars ══
    # Each platform has a Fire Bar whose pivot is on the platform itself.
    # Player must time the landing between the bar's arms.
    fb_plats = [
        (198, GY,   FB_CW),   (205, GY-4,  FB_CCW),
        (212, GY,   FB_CW),   (219, GY-3,  FB_CCW),
        (226, GY-6, FB_CW),   (233, GY,    FB_CCW),
        (240, GY-2, FB_CW),   (247, GY-5,  FB_CCW),
    ]
    for fx, fy, fb_sd in fb_plats:
        a.add_ground(fx, fy, 1, 5, tileset=1)
        a.add_sprite(db.FIRE_BAR, fx * 16, (fy - 2) * 16, spritedata=fb_sd)

    # Goal platform — wide landing zone so the pole-slide animation has room
    a.add_ground(252, GY, 14, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 257 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/09-01.arc')
    print('Created 9-1: Pixel Perfect (1-tile platforms, Thwomp gates, Fire Bar finale)')


def create_level_9_2():
    """9-2: Enemy Flood — no shells allowed.

    ALL Koopa/Paratroopa/Spiny removed — those drop shells that chain-kill
    everything in a dense level. Every enemy here either can't be stomped
    (Crowbers dive and move on), revives (Dry Bones), explodes (Bob-ombs —
    dangerous to chain), shoots back (Bros), or is too large to shell-skip
    (Chain Chomps, Giant Dry Bones, Sledge Bros, Mecha-Koopas).

    Four waves:
      W1) Goomba/Paragoomba/Dry Bones ground flood — all stomped safely but
          Dry Bones revive so the floor stays dangerous the whole time
      W2) Bros gauntlet — Hammer/Fire/Sledge/Ice on elevated platforms,
          shooting down at the player on the floor
      W3) Aerial assault — Crowbers + Para-Bob-ombs; player can't use a shell
          to clear the sky, must dodge manually
      W4) Elite finale — Chain Chomps + Giant Dry Bones + Mecha-Koopas +
          Sledge Bros; big enemies that each require individual attention
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_CASTLE)
    a.set_background(db.BG_CASTLE)
    a.set_time(500)

    GY = 26
    a.add_zone(0, 0, 7200, 640, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, visibility=16)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 93 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    FLOOR  = (GY - 1) * 16
    LEDGE  = (GY - 10) * 16
    AIR    = (GY - 12) * 16

    # ── Terrain layout ──
    # Wave 1 (x=0–92): solid floor — safe to learn
    a.add_ground(0, GY, 92, 5, tileset=1)

    # Wave 2 (x=92–200): floor with 5-tile pits every 30 tiles — must jump while
    # dodging Bros firing from ledges above
    for seg_start in range(92, 200, 30):
        a.add_ground(seg_start, GY, 25, 5, tileset=1)
        # gap of 5 tiles follows each segment
    # last solid segment connecting to Wave 3
    a.add_ground(197, GY, 5, 5, tileset=1)

    # Wave 3 (x=202–300): narrower platforms with 6-tile pits — aerial enemies
    # converge while the floor is broken
    for seg_start in range(202, 300, 28):
        a.add_ground(seg_start, GY, 22, 5, tileset=1)
    a.add_ground(298, GY, 4, 5, tileset=1)

    # Wave 4 (x=302–430): wide pits (8 tiles) — Chain Chomps on the islands,
    # nowhere to run or wait
    for seg_start in range(302, 430, 24):
        a.add_ground(seg_start, GY, 16, 5, tileset=1)
        # 8-tile pit follows
    # goal platform
    a.add_ground(428, GY, 14, 5, tileset=1)

    a.add_question_block(3, GY - 4, contents=1)

    # Elevated ledges (5 tiles wide) every 30 tiles — Bros fire DOWN from these
    for px in range(30, 420, 30):
        a.add_ground(px, GY - 9, 5, 3, tileset=1)

    # Fire Bars on the elevated ledges — camping on a ledge to avoid a pit is punished
    FB_CW  = b'\x00\x00\x00\x00\x10\x04'
    FB_CCW = b'\x00\x00\x00\x00\x00\x04'
    for i, px in enumerate(range(30, 420, 60)):   # every other ledge
        sd = FB_CW if i % 2 == 0 else FB_CCW
        a.add_sprite(db.FIRE_BAR, (px + 2) * 16, (GY - 10) * 16, spritedata=sd)

    # Thwomps over the pits — hang on ledges directly above the gaps, drop when
    # the player tries to jump across (one Thwomp every other pit in Wave 2+3)
    for px in range(118, 300, 60):
        a.add_sprite(db.THWOMP, px * 16, (GY - 7) * 16)

    # ══ WAVE 1 (x=8–90): ground flood, solid floor — learn pacing ══
    for ex in range(10, 88, 30):
        a.add_sprite(db.GOOMBA, ex * 16, FLOOR)
    for ex in range(22, 88, 30):
        a.add_sprite(db.DRY_BONES, ex * 16, FLOOR)
    for ex in range(16, 88, 36):
        a.add_sprite(db.PARAGOOMBA, ex * 16, AIR)
    a.add_sprite(db.STAR_COIN, 50 * 16, (GY - 5) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))
    a.add_sprite(db.MIDWAY_FLAG, 93 * 16, FLOOR, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ WAVE 2 (x=95–200): Bros on ledges, player jumps pits below them ══
    for ex in range(96, 200, 36):
        a.add_sprite(db.HAMMER_BRO, ex * 16, LEDGE)
    for ex in range(114, 200, 36):
        a.add_sprite(db.FIRE_BRO, ex * 16, LEDGE)
    for ex in range(140, 200, 40):
        a.add_sprite(db.SLEDGE_BRO, ex * 16, FLOOR)
    for ex in range(106, 200, 40):
        a.add_sprite(db.DRY_BONES, ex * 16, FLOOR)
    a.add_sprite(db.STAR_COIN, 152 * 16, (GY - 5) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))

    # ══ WAVE 3 (x=205–300): aerial Crowbers + Mechakoopas, broken floor ══
    for ex in range(206, 300, 28):
        a.add_sprite(db.CROWBER, ex * 16, AIR)
    for ex in range(220, 300, 34):
        a.add_sprite(db.MECHAKOOPA, ex * 16, FLOOR)
    for ex in range(214, 300, 40):
        a.add_sprite(db.DRY_BONES, ex * 16, FLOOR)

    # ══ WAVE 4 (x=305–420): Chain Chomps on pit islands — nowhere to camp ══
    for ex in range(306, 420, 48):
        a.add_sprite(db.CHAIN_CHOMP, ex * 16, FLOOR)
    for ex in range(328, 420, 50):
        a.add_sprite(db.GIANT_DRY_BONES, ex * 16, FLOOR)
    for ex in range(348, 420, 48):
        a.add_sprite(db.SLEDGE_BRO, ex * 16, FLOOR)
    for ex in range(316, 420, 44):
        a.add_sprite(db.CROWBER, ex * 16, AIR)
    a.add_sprite(db.STAR_COIN, 375 * 16, (GY - 5) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # Goal pole — on the final platform, well within zone
    a.add_sprite(db.GOAL_POLE, 432 * 16, FLOOR)

    builder.save('output/ChaosStation/Stage/09-02.arc')
    print('Created 9-2: Enemy Flood (pits + Thwomps + Fire Bars for terrain pressure)')


def create_level_9_3():
    """9-3: Plunge — vertical descent through a Boo-haunted shaft.

    Redesigned from scratch: the original concept (gravity inversion) isn't
    a real NSMBW mechanic. This replacement is genuinely "upside-down" in
    spirit: instead of running right, you must FALL DOWN through a tall vertical
    shaft. The goal pole is at the VERY BOTTOM. Going up is safe; going down
    is dangerous. Wrong jumps = fall past your target platform into enemies.

    Shaft layout (zone is 4 tiles wide, 260 tiles tall):
      Top (y=0):  entrance — player starts here
      Mid (y=130): midway flag on a ledge
      Bottom (y=252): goal pole on the floor
    Platforms are staggered left-right so the player zigzags while falling.
    Big Boos patrol the shaft. Fire Snakes lurk on the wider ledges.
    Star Coins are in dangerous side alcoves that require precision fall-landings.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_CAVE)
    a.set_background(db.BG_UNDERGROUND)
    a.set_time(400)

    # Vertical tower-style zone. cam_mode=3 is the proven vertical mode used by
    # every working tower in this mod (4-tower, 5-tower, etc). cam_mode=1 and a
    # 4096px tall zone crashed on load.
    SHAFT_W = 30   # shaft inner width in tiles (480px — matches 4-tower)
    SHAFT_H = 200  # shaft height in tiles (3200px — safe tower height)
    WALL_T  = 2    # wall thickness in tiles

    a.add_zone(0, 0, SHAFT_W * 16, SHAFT_H * 16, zone_id=0,
               music=db.MUSIC_GHOST_HOUSE, cam_mode=3, visibility=16)

    # Left wall full height. Right wall full height EXCEPT near the bottom
    # where the goal pole needs open space for the victory slide animation.
    a.add_ground(0, 0, WALL_T, SHAFT_H, tileset=1)
    a.add_ground(SHAFT_W - WALL_T, 0, WALL_T, SHAFT_H - 12, tileset=1)

    # Ceiling (top cap)
    a.add_ground(0, 0, SHAFT_W, WALL_T, tileset=1)
    # Floor (bottom)
    a.add_ground(0, SHAFT_H - WALL_T, SHAFT_W, WALL_T + 2, tileset=1)

    # Player entrance at the top, just below the ceiling
    a.add_entrance(0, (SHAFT_W // 2) * 16, (WALL_T + 2) * 16,
                   etype=db.ENTRANCE_NORMAL)
    # Midway respawn: i=11 in loop → right_x=24, plat_y=87; flag at (25,85)
    a.add_entrance(1, 25 * 16, 85 * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)

    # Staggered platforms — alternating left-anchored and right-anchored
    # Each platform is 6 tiles wide, leaving an 10-tile gap on the other side
    # In a 20-tile shaft a 10-tile gap is JUST wide enough for a Big Boo to patrol
    # Narrower platforms (3 tiles instead of 6) and tighter spacing make every
    # landing precise. Fire Bars on most platforms are the real threat — Boos
    # alone are too easy because the player can just keep moving downward.
    PLAT_W = 3
    plat_y = WALL_T + 8

    left_x  = WALL_T + 1
    right_x = SHAFT_W - WALL_T - PLAT_W - 1

    for i in range(22):
        px = left_x if i % 2 == 0 else right_x
        a.add_ground(px, plat_y, PLAT_W, 1, tileset=1)

        # Fire Bar on most platforms — alternating CW/CCW. spritedata byte 4
        # length=2, byte 5 direction.
        if i % 3 != 0:
            direction = 0x10 if i % 2 == 0 else 0x00
            a.add_sprite(db.FIRE_BAR, (px + 1) * 16, (plat_y - 1) * 16,
                         spritedata=bytes([0, 0, 0, 0, direction, 0x02]))

        # Big Boo on every platform — patrols the gap, blocks vertical fall lanes
        boo_x = (right_x + 1) if i % 2 == 0 else (left_x + 1)
        a.add_sprite(db.BIG_BOO, boo_x * 16, (plat_y - 1) * 16)

        if i == 11:
            a.add_sprite(db.MIDWAY_FLAG, (px + 1) * 16, (plat_y - 2) * 16,
                         spritedata=b'\x00\x00\x00\x01\x00\x00')

        plat_y += 7   # tighter vertical spacing — 7 tiles instead of 9

    # Star Coins in tight side alcoves
    sc1_y = WALL_T + 22
    a.add_ground(WALL_T, sc1_y, 3, 1, tileset=1)
    a.add_sprite(db.STAR_COIN, (WALL_T + 1) * 16, (sc1_y - 2) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))

    sc2_y = WALL_T + 90
    a.add_ground(SHAFT_W - WALL_T - 3, sc2_y, 3, 1, tileset=1)
    a.add_sprite(db.STAR_COIN, (SHAFT_W - WALL_T - 2) * 16, (sc2_y - 2) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))

    sc3_y = SHAFT_H - WALL_T - 12
    a.add_ground(SHAFT_W // 2 - 1, sc3_y, 3, 1, tileset=1)
    a.add_sprite(db.STAR_COIN, (SHAFT_W // 2) * 16, (sc3_y - 2) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))
    for bx in [WALL_T + 2, SHAFT_W - WALL_T - 3]:
        a.add_sprite(db.BIG_BOO, bx * 16, sc3_y * 16)

    # Dense Swoopers — every 5 tiles on alternating walls. They wake up when
    # the player passes underneath, so falling slowly = death.
    for idx, sy in enumerate(range(WALL_T + 6, SHAFT_H - 8, 5)):
        wall_x = (WALL_T + 1) if idx % 2 == 0 else (SHAFT_W - WALL_T - 2)
        a.add_sprite(db.SWOOP, wall_x * 16, sy * 16)

    # Goal pole on the shaft floor — placed left-of-center so victory
    # animation has clear space on the right (where the wall has been removed)
    a.add_sprite(db.GOAL_POLE, (WALL_T + 4) * 16,
                 (SHAFT_H - WALL_T - 2) * 16)

    builder.save('output/ChaosStation/Stage/09-03.arc')
    print('Created 9-3: Plunge (vertical descent shaft, Boos, Fire Snakes)')


def create_level_9_4():
    """9-4: Ghost Maze — full darkness, multi-room branching maze.

    A grid of rooms connected by vertical shafts and horizontal passages.
    The player enters at the top-left. The goal is at the bottom-right.
    The maze has multiple paths: three routes lead down through different
    rooms; two dead-end in trap rooms, only one reaches the goal.
    Every room is pitch black and infested with ghosts.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a.set_background(db.BG_GHOST_HOUSE)
    a.set_time(400)

    # Grid: 4 rooms wide × 3 rooms tall
    # Each room: 28 tiles wide × 14 tiles tall (448×224)
    # Walls between rooms: 2 tiles thick
    ROOM_W = 28
    ROOM_H = 14
    COLS   = 4
    ROWS   = 3
    WALL   = 2

    total_w = COLS * (ROOM_W + WALL) + WALL
    total_h = ROWS * (ROOM_H + WALL) + WALL

    a.add_zone(0, 0, total_w * 16, total_h * 16, zone_id=0,
               music=db.MUSIC_GHOST_HOUSE, cam_mode=0, visibility=36,
               model_dark=12, terrain_dark=0)

    def room_origin(cx, cy):
        return (WALL + cx * (ROOM_W + WALL), WALL + cy * (ROOM_H + WALL))

    # Outer walls (top, bottom, left, right)
    a.add_ground(0, 0, total_w, WALL, tileset=1)                 # ceiling
    a.add_ground(0, total_h - WALL, total_w, WALL + 2, tileset=1)  # floor
    a.add_ground(0, 0, WALL, total_h, tileset=1)                 # left
    a.add_ground(total_w - WALL, 0, WALL, total_h, tileset=1)    # right

    # Vertical walls between rooms (every column)
    for c in range(1, COLS):
        vx = WALL + c * (ROOM_W + WALL) - WALL
        a.add_ground(vx, 0, WALL, total_h, tileset=1)
    # Horizontal walls between rows (every row)
    for r in range(1, ROWS):
        vy = WALL + r * (ROOM_H + WALL) - WALL
        a.add_ground(0, vy, total_w, WALL, tileset=1)

    # PASSAGES — carve openings through the walls using LAYER-0 object
    # (we can't "remove" placed tiles, so we re-place FLOOR tiles OVER the
    # wall sections we want to be passable — but this won't work because
    # tiles are additive, not subtractive). Instead we place solid walls
    # only in the SEGMENTS that are NOT passages. Rewrite wall placement:
    # Simpler: skip filling the wall where passages go.

    # Reset: recreate walls with passages this time by not using the bulk add.
    # We will bypass the above full walls by adding coin hints, enemies, and
    # relying on the fact that we just made passages WHERE NEEDED by omitting
    # wall segments in a *different* approach: create walls only with gaps.
    # Since we already added the full walls, we instead punch through with
    # question-less bricks — actually there's no "remove tile" method.
    #
    # Better approach: undo the above and redraw walls segmented.
    # Since Python can't undo, we ADD a second layer of open floors over
    # the passage tiles using layer-0 where tile collisions are ignored... NO.
    #
    # Cleanest: restart — rebuild walls with gaps from scratch. We'll do so
    # by building a fresh list. Clear the builder's layer1 objects that we
    # just added. That's hacky — instead, let's use a cleaner strategy:
    # build the maze with OPEN corridors by only placing wall segments
    # around passages. Below we clear a.layer1 and rebuild.
    a.area.layer1 = []   # wipe the walls we just added

    # Outer boundary (unchanged — full box)
    a.add_ground(0, 0, total_w, WALL, tileset=1)
    a.add_ground(0, total_h - WALL, total_w, WALL + 2, tileset=1)
    a.add_ground(0, 0, WALL, total_h, tileset=1)
    a.add_ground(total_w - WALL, 0, WALL, total_h, tileset=1)

    # Passage layout (col, row, 'right'|'down') — openings to neighbor room
    # Design: S-path from (0,0) → (0,1) → (1,1) → (2,1) → (2,2) → (3,2)
    # Plus some branching dead ends for exploration.
    passages = [
        (0, 0, 'down'),   # enter room (0,0) fall to (0,1)
        (0, 1, 'right'),  # (0,1) → (1,1)
        (0, 1, 'down'),   # (0,1) → (0,2) — DEAD END (star coin 1)
        (1, 1, 'right'),  # (1,1) → (2,1)
        (1, 1, 'down'),   # (1,1) → (1,2) — DEAD END (star coin 2)
        (2, 1, 'right'),  # (2,1) → (3,1) — DEAD END (star coin 3)
        (2, 1, 'down'),   # (2,1) → (2,2)
        (2, 2, 'right'),  # (2,2) → (3,2) GOAL ROOM
    ]
    passage_set = set(passages)

    def has_passage(c, r, direction):
        return (c, r, direction) in passage_set

    # Vertical walls between cols (segmented to allow passages)
    for c in range(1, COLS):
        vx = WALL + c * (ROOM_W + WALL) - WALL
        for r in range(ROWS):
            ry = WALL + r * (ROOM_H + WALL)
            if has_passage(c - 1, r, 'right'):
                # Leave a 4-tile gap in the middle of this wall segment
                gap_top = ry + ROOM_H // 2 - 2
                gap_h   = 4
                # Top piece
                a.add_ground(vx, ry, WALL, gap_top - ry, tileset=1)
                # Bottom piece
                a.add_ground(vx, gap_top + gap_h, WALL,
                             ry + ROOM_H - (gap_top + gap_h), tileset=1)
            else:
                a.add_ground(vx, ry, WALL, ROOM_H, tileset=1)

    # Horizontal walls between rows
    for r in range(1, ROWS):
        vy = WALL + r * (ROOM_H + WALL) - WALL
        for c in range(COLS):
            cx = WALL + c * (ROOM_W + WALL)
            if has_passage(c, r - 1, 'down'):
                gap_left = cx + ROOM_W // 2 - 2
                gap_w    = 5
                a.add_ground(cx, vy, gap_left - cx, WALL, tileset=1)
                a.add_ground(gap_left + gap_w, vy,
                             cx + ROOM_W - (gap_left + gap_w), WALL, tileset=1)
            else:
                a.add_ground(cx, vy, ROOM_W, WALL, tileset=1)

    # Entrance in top-left room
    ox, oy = room_origin(0, 0)
    a.add_entrance(0, (ox + 2) * 16, (oy + ROOM_H - 2) * 16,
                   etype=db.ENTRANCE_NORMAL)

    # Populate every room with ghosts
    for c in range(COLS):
        for r in range(ROWS):
            ox, oy = room_origin(c, r)
            # 2 Big Boos per room, varied positions
            a.add_sprite(db.BIG_BOO, (ox + 6) * 16,           (oy + 4) * 16)
            a.add_sprite(db.BIG_BOO, (ox + ROOM_W - 6) * 16,  (oy + ROOM_H - 4) * 16)
            # Swoopers on the ceiling
            a.add_sprite(db.SWOOP, (ox + ROOM_W // 2) * 16, (oy + 2) * 16)

    # Star coins in the 3 dead-end rooms
    for (c, r, sc_idx) in [(0, 2, 0), (1, 2, 1), (3, 1, 2)]:
        ox, oy = room_origin(c, r)
        a.add_sprite(db.STAR_COIN, (ox + ROOM_W // 2) * 16,
                     (oy + ROOM_H // 2) * 16,
                     spritedata=bytes([0, 0, 0, 0, sc_idx, 0]))

    # Exit pipe in bottom-right room (3,2) — leads to area 2 (goal room)
    # Goal pole crashes with many Big Boos active in area 1.
    ox, oy = room_origin(3, 2)
    pipe_x = ox + ROOM_W - 8
    pipe_y = oy + ROOM_H - 3
    a.add_pipe(pipe_x, pipe_y, height=3)
    # Entrance warp: player enters pipe down, warps to area 2 entrance 0
    a.add_entrance(1, pipe_x * 16, (pipe_y - 1) * 16,
                   etype=db.ENTRANCE_PIPE_DOWN, zone_id=0,
                   dest_area=2, dest_entrance=0)

    # Midway flag in the middle-middle room (1, 1)
    ox, oy = room_origin(1, 1)
    a.add_sprite(db.MIDWAY_FLAG, (ox + ROOM_W // 2) * 16,
                 (oy + ROOM_H - 2) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ── AREA 2: Simple goal room ──
    a2 = builder.add_area(2)
    a2.set_tileset(0, db.TILESET_STANDARD)
    a2.set_tileset(1, db.TILESET_GHOST_HOUSE)
    a2.set_background(db.BG_GHOST_HOUSE)
    a2.set_time(400)
    a2.add_zone(0, 0, 640, 320, zone_id=0, music=db.MUSIC_GHOST_HOUSE,
                cam_mode=0, visibility=36, model_dark=12, terrain_dark=0)
    a2.add_ground(0, 16, 40, 4, tileset=1)                 # floor
    a2.add_ground(0, 0, 40, 2, tileset=1)                  # ceiling
    a2.add_entrance(0, 3 * 16, 15 * 16, etype=db.ENTRANCE_PIPE_UP)
    a2.add_sprite(db.GOAL_POLE, 30 * 16, 15 * 16)

    builder.save('output/ChaosStation/Stage/09-04.arc')
    print('Created 9-4: Ghost Maze (4×3 grid, pipe to goal room)')


def create_level_9_5():
    """9-5: Snowfire — contradictory biome.

    Lava fill at the bottom floor; icicles falling from ice ceiling above.
    Both hazards converge on a narrow middle corridor. Ice Bros and Fire Bros
    face each other on opposite walls, filling the corridor with cross-fire.

    Sections: intro corridor → icicle storm zone → cross-fire section →
    final sprint with icicles + lava geysers + Crowbers.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_SNOW)
    a.set_background(db.BG_SNOW)
    a.set_time(400)

    GY   = 26   # platform floor row
    LAVY = GY + 4   # lava surface row (4 below ground)
    CY   = 4        # ceiling row

    a.add_zone(0, 0, 8000, 640, zone_id=0, music=db.MUSIC_SNOW, cam_mode=0, visibility=16)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 82 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Lava fill at the bottom — instant death if you fall
    a.add_sprite(db.LAVA_FILL, 0, LAVY * 16, spritedata=b'\x00\x00\x00\x00\x01\x00')
    # Ice ceiling slab (split to avoid 500-tile object crash)
    a.add_ground(0,   CY, 250, 3, tileset=1)
    a.add_ground(250, CY, 220, 3, tileset=1)
    # Main platform floor (split to avoid object width cap)
    a.add_ground(0,   GY, 250, 3, tileset=1)
    a.add_ground(250, GY, 220, 3, tileset=1)
    a.add_question_block(3, GY - 4, contents=1)

    # ══ SECTION A (x=0–128): Intro — learn both hazards ══
    # Icicles every 14 tiles (was 8) — learn the rhythm without being overwhelmed
    for ix in range(6, 80, 14):
        a.add_sprite(db.ICICLE, ix * 16, (CY + 3) * 16)
    for gx in range(8, 80, 20):
        a.add_sprite(db.LAVA_GEYSER, gx * 16, (LAVY - 1) * 16,
                     spritedata=b'\x00\x00\x00\x00\x00\x21')
    # Crowbers make the intro feel alive — passive hazards alone feel empty
    for cx in range(12, 78, 18):
        a.add_sprite(db.CROWBER, cx * 16, (GY - 8) * 16)
    a.add_sprite(db.STAR_COIN, 40 * 16, (GY - 4) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))
    a.add_sprite(db.MIDWAY_FLAG, 82 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ══ SECTION B (x=128–256): Icicle storm + meteor shower ══
    # Every 8 tiles so there are gaps to stand in
    for ix in range(82, 162, 8):
        a.add_sprite(db.ICICLE, ix * 16, (CY + 3) * 16)
    # VOLCANO_ROCK meteor spawners — rains falling rocks from above
    for mx in range(90, 162, 20):
        a.add_sprite(db.VOLCANO_ROCK, mx * 16, 0)
    # Ice Bros on floor ledges
    for px in range(86, 162, 22):
        a.add_ground(px, GY - 5, 3, 3, tileset=1)
        a.add_sprite(db.ICE_BRO, px * 16, (GY - 6) * 16)
    for gx in range(92, 162, 24):
        a.add_sprite(db.LAVA_GEYSER, gx * 16, (LAVY - 1) * 16,
                     spritedata=b'\x00\x00\x00\x00\x00\x21')
    a.add_sprite(db.STAR_COIN, 122 * 16, (GY - 3) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))

    # ══ SECTION C (x=256–400): Cross-fire — Ice Bros + Fire Bros on opposite walls ══
    for px in range(165, 252, 20):
        a.add_ground(px, GY - 5, 3, 3, tileset=1)
        a.add_ground(px + 10, GY - 9, 3, 3, tileset=1)
    for bx in range(167, 252, 20):
        a.add_sprite(db.ICE_BRO,  bx * 16,        (GY - 6) * 16)
        a.add_sprite(db.FIRE_BRO, (bx + 10) * 16, (GY - 10) * 16)
    for ix in range(165, 252, 10):
        a.add_sprite(db.ICICLE, ix * 16, (CY + 3) * 16)
    for cx in range(170, 252, 16):
        a.add_sprite(db.CROWBER, cx * 16, (GY - 8) * 16)
    a.add_sprite(db.STAR_COIN, 208 * 16, (GY - 12) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # ══ SECTION D (x=400–500): Final sprint — all hazards at maximum ══
    for ix in range(254, 496, 8):
        a.add_sprite(db.ICICLE, ix * 16, (CY + 3) * 16)
    # Meteor storm in the final section — dodge rocks AND icicles simultaneously
    for mx in range(258, 496, 16):
        a.add_sprite(db.VOLCANO_ROCK, mx * 16, 0)
    for gx in range(256, 496, 16):
        a.add_sprite(db.LAVA_GEYSER, gx * 16, (LAVY - 1) * 16,
                     spritedata=b'\x00\x00\x00\x00\x00\x21')
    for cx in range(260, 496, 18):
        a.add_sprite(db.CROWBER, cx * 16, (GY - 8) * 16)
    for bx in range(262, 496, 28):
        a.add_sprite(db.ICE_BRO,  bx * 16,        (GY - 1) * 16)
        a.add_sprite(db.FIRE_BRO, (bx + 14) * 16, (GY - 1) * 16)
    for hx in range(270, 496, 40):
        a.add_sprite(db.HAMMER_BRO, hx * 16, (GY - 1) * 16)

    # End platform + goal — moved 30 tiles left so pole is fully within zone
    a.add_ground(462, GY, 6, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 465 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/09-05.arc')
    print('Created 9-5: Snowfire (lava + ice simultaneously)')


def create_level_9_6():
    """9-6: King Bill Alley — dodge the unkillable.

    Open lava sky. King Bills continuously cross from right to left in dense
    intervals. The player has only narrow floating island platforms to stand on.
    Must time every move around King Bills that fill the vertical space.
    Banzai Bills add secondary pressure. Podoboos from lava below.

    Sections: single-direction warm-up → dense crossing zone →
    island sprint → sprint to goal while Bills rain.
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_KOOPA_OUT)
    a.set_background(db.BG_LAVA)
    a.set_time(400)

    GY   = 26
    LAVY = (GY + 3) * 16   # lava surface in pixels

    a.add_zone(0, 0, 8800, 640, zone_id=0, music=db.MUSIC_LAVA, cam_mode=0, visibility=16)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 200 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Lava floor
    a.add_sprite(db.LAVA_FILL, 0, LAVY, spritedata=b'\x00\x00\x00\x00\x01\x00')

    # Starting platform
    a.add_ground(0, GY, 8, 5, tileset=1)
    a.add_question_block(4, GY - 4, contents=1)

    # Floating islands — only 1 tile wide. One bad landing = lava.
    # Varied heights so the player can never settle into a comfortable rhythm.
    island_xs = list(range(12, 522, 10))
    island_ys_pattern = [GY, GY - 3, GY - 1, GY - 5, GY - 2, GY - 4, GY - 1, GY]
    for i, ix in enumerate(island_xs):
        iy = island_ys_pattern[i % len(island_ys_pattern)]
        a.add_ground(ix, iy, 1, 4, tileset=1)  # 1 tile wide — no margin for error

    # King Bills every 8 tiles (was 14) — more frequent, harder to time
    king_bill_spacing = 8
    king_bill_ys = [(GY - 12) * 16, (GY - 6) * 16, (GY - 2) * 16]
    for i, kx in enumerate(range(40, 530, king_bill_spacing)):
        kb_y = king_bill_ys[i % 3]
        a.add_sprite(db.KING_BILL, kx * 16, kb_y)

    # Banzai Bills from left side (secondary threat)
    for bx in range(15, 480, 30):
        a.add_sprite(db.BANZAI_BILL_LAUNCHER, bx * 16, (GY - 1) * 16)

    # Podoboos from lava
    for px in range(8, 525, 18):
        a.add_sprite(db.PODOBOO, px * 16, LAVY,
                     spritedata=b'\x00\x00\x00\x00\x00\x02')

    # Crowbers overhead
    for cx in range(20, 510, 14):
        a.add_sprite(db.CROWBER, cx * 16, (GY - 12) * 16)

    # Star Coins — on isolated islands deep in King Bill territory
    a.add_sprite(db.STAR_COIN, 120 * 16, (GY - 6) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))
    a.add_sprite(db.STAR_COIN, 280 * 16, (GY - 2) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))
    a.add_sprite(db.STAR_COIN, 440 * 16, (GY - 10) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))

    a.add_sprite(db.MIDWAY_FLAG, 200 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # End platform + goal — zone is 8800px (550t) so 535t is safely inside
    a.add_ground(530, GY, 10, 5, tileset=1)
    a.add_sprite(db.GOAL_POLE, 535 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/09-06.arc')
    print('Created 9-6: King Bill Alley (screen-filling bullets from all sides)')


def create_level_9_7():
    """9-7: Rotor Hell — the Fire Bar colosseum.

    Redesigned from "Minimal Matter" (too similar to 9-1 Pixel Perfect).
    Here the gimmick is FIRE BAR OVERLOAD: the whole level is a corridor
    filled with dozens of Fire Bars spinning CW/CCW, packed so densely that
    the player must read rotation patterns, time dashes, and duck-slide
    between blades. Wide platforms (so terrain isn't the puzzle — the bars are).

    Sections:
      A) Single-bar warm-up — learn the timing
      B) Paired bars (CW+CCW) — thread the pinch point
      C) Bar tunnel — bars on ceiling AND floor
      D) Bar wheel — one giant cluster, then sprint to goal
    """
    from tools.level_builder import LevelBuilder
    import tools.sprite_db as db

    builder = LevelBuilder()
    a = builder.add_area(1)
    a.set_tileset(0, db.TILESET_STANDARD)
    a.set_tileset(1, db.TILESET_CASTLE)
    a.set_background(db.BG_CASTLE)
    a.set_time(400)

    GY = 26

    # Zone 7600px wide — goal pole at 444t=7104px needs 496px clearance from edge
    a.add_zone(0, 0, 7600, 512, zone_id=0, music=db.MUSIC_CASTLE, cam_mode=0, visibility=16)
    a.add_entrance(0, 3 * 16, (GY - 2) * 16, etype=db.ENTRANCE_NORMAL)
    a.add_entrance(1, 112 * 16, (GY - 1) * 16, etype=db.ENTRANCE_NORMAL, zone_id=0)  # Midway respawn

    # Continuous wide floor + ceiling (split to stay under object width cap)
    a.add_ground(0,   GY, 250, 5, tileset=1)
    a.add_ground(250, GY, 225, 5, tileset=1)
    a.add_ground(0,   2,  250, 3, tileset=1)  # ceiling band
    a.add_ground(250, 2,  225, 3, tileset=1)

    FB_CW_L  = b'\x00\x00\x00\x00\x10\x06'   # long CW bar
    FB_CCW_L = b'\x00\x00\x00\x00\x00\x06'
    FB_CW_S  = b'\x00\x00\x00\x00\x10\x04'   # shorter bar
    FB_CCW_S = b'\x00\x00\x00\x00\x00\x04'

    # ── SECTION A (x=8–110): paired CW+CCW every 8 tiles (no breathing room) ──
    # Bars at two heights per column; player must time both simultaneously
    for i, bx in enumerate(range(10, 110, 8)):
        sd_lo = FB_CW_S  if i % 2 == 0 else FB_CCW_S
        sd_hi = FB_CCW_L if i % 2 == 0 else FB_CW_L
        a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 3) * 16, spritedata=sd_lo)
        a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 9) * 16, spritedata=sd_hi)
    # Hammer Bros between every 3rd pair — can't wait them out, bars keep spinning
    for hx in range(18, 110, 24):
        a.add_sprite(db.HAMMER_BRO, hx * 16, (GY - 1) * 16)
    a.add_sprite(db.STAR_COIN, 60 * 16, (GY - 14) * 16,
                 spritedata=bytes([0, 0, 0, 0, 0, 0]))

    a.add_sprite(db.MIDWAY_FLAG, 112 * 16, (GY - 1) * 16, spritedata=b'\x00\x00\x00\x01\x00\x00')

    # ── SECTION B (x=115–230): ceiling + floor bars (tunnel of death) ──
    # Floor bars sweep upward, ceiling bars sweep down — safe window is 2 tiles tall
    for i, bx in enumerate(range(116, 230, 7)):
        if i % 3 == 0:
            # Triple stacked: floor + mid + ceiling
            a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 2) * 16, spritedata=FB_CW_L)
            a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 7) * 16, spritedata=FB_CCW_L)
            a.add_sprite(db.FIRE_BAR, bx * 16,  5 * 16,        spritedata=FB_CW_S)
        else:
            a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 2) * 16, spritedata=FB_CCW_L)
            a.add_sprite(db.FIRE_BAR, bx * 16,  5 * 16,        spritedata=FB_CW_L)
    for cx in range(122, 230, 20):
        a.add_sprite(db.CHAIN_CHOMP, cx * 16, (GY - 1) * 16)
    a.add_sprite(db.STAR_COIN, 175 * 16, (GY - 6) * 16,
                 spritedata=bytes([0, 0, 0, 0, 1, 0]))

    # ── SECTION C (x=235–350): bar wheels — 3-bar clusters every 14 tiles ──
    # Each cluster: long CW, short CCW, offset long — overlapping arcs
    for i, cx in enumerate(range(238, 350, 14)):
        sd_a = FB_CW_L  if i % 2 == 0 else FB_CCW_L
        sd_b = FB_CCW_S if i % 2 == 0 else FB_CW_S
        sd_c = FB_CW_L  if i % 3 == 0 else FB_CCW_L
        a.add_sprite(db.FIRE_BAR, cx * 16,       (GY - 6) * 16, spritedata=sd_a)
        a.add_sprite(db.FIRE_BAR, cx * 16,       (GY - 6) * 16, spritedata=sd_b)
        a.add_sprite(db.FIRE_BAR, (cx + 3) * 16, (GY - 6) * 16, spritedata=sd_c)
    # Sledge Bros anchor the gaps — player can't idle
    for sx in range(248, 350, 28):
        a.add_sprite(db.SLEDGE_BRO, sx * 16, (GY - 1) * 16)

    # ── SECTION D (x=355–440): sprint gauntlet — single bars every 6 tiles ──
    # Fastest density yet — must move continuously, no standing still
    for i, bx in enumerate(range(358, 438, 6)):
        sd = FB_CW_L if i % 2 == 0 else FB_CCW_L
        a.add_sprite(db.FIRE_BAR, bx * 16, (GY - 5) * 16, spritedata=sd)
    for hx in range(362, 438, 18):
        a.add_sprite(db.HAMMER_BRO, hx * 16, (GY - 1) * 16)
    a.add_sprite(db.STAR_COIN, 398 * 16, (GY - 10) * 16,
                 spritedata=bytes([0, 0, 0, 0, 2, 0]))

    # Goal: open landing past final bar — pole well within zone
    a.add_sprite(db.GOAL_POLE, 444 * 16, (GY - 1) * 16)

    builder.save('output/ChaosStation/Stage/09-07.arc')
    print('Created 9-7: Rotor Hell (Fire Bar colosseum)')


def create_level_9_8():
    """9-8: Chaos Absolute — the true final level of the mod.

    Built on the vanilla 09-08 base to preserve the zone structure and any
    hardcoded game expectations (credits trigger, world-map flags, etc.).
    Vanilla content (sprites + terrain) is wiped and replaced with our
    8-world-callback gauntlet compressed into the vanilla zone dimensions.

    Vanilla zone: x=256, y=384, w=8400, h=384 (16px offset, 24-tile corridor).
    All our tile/sprite coords are given relative to zone origin.
    """
    import copy
    from tools.course_parser import (parse_course_bin, serialize_course_bin,
                                      parse_layer_data, serialize_layer_data,
                                      Sprite, LayerObject, Entrance)
    from tools.u8archive import U8Archive
    import tools.sprite_db as db

    # Load vanilla base — preserves tileset names, zone record, settings block,
    # boundings, and any controller/path data the game needs for 9-8.
    with open('extracted files/Stage/09-08.arc', 'rb') as f:
        arc = U8Archive.load(f.read())

    area = parse_course_bin(arc.get_file('course/course1.bin'))
    layer1 = parse_layer_data(arc.get_file('course/course1_bgdatL1.bin'))

    # Zone origin in tile units (vanilla: x=256px=16t, y=384px=24t)
    ZX = area.zones[0].x // 16   # 16
    ZY = area.zones[0].y // 16   # 24
    ZW = area.zones[0].w // 16   # 525 (8400/16)
    ZH = area.zones[0].h // 16   # 24  (384/16)

    # Time limit
    area.settings.time_limit = 600

    # Keep only vanilla sprites that are pure event controllers (low counts,
    # no active entities). Remove the bulk entity-spawners that overflow the engine:
    #   78  ×61 — unknown bulk entity
    #   175 ×9  — Flying ? Blocks
    #   176 ×1  — Roulette Block
    #   236 ×8  — Cloud
    #   237 ×88 — Cloud spawners (the bounce-cloud flood)
    #   343 ×28 — Fuzzies on track
    #   20  ×14 — vanilla Goombas (replaced by ours)
    #   32  ×2  — vanilla Star Coins (replaced by ours)
    #   113 ×1  — vanilla Goal Pole (replaced by ours)
    # Keep: 41 P-Switch, 44, 91, 144 Red Coins, 147 Coins, 155, 156 Red Ring,
    #        310/326/393/422/446/459 event controllers
    ENTITY_REMOVE = {20, 32, 78, 113, 175, 176, 236, 237, 343}
    area.sprites = [s for s in area.sprites if s.stype not in ENTITY_REMOVE]
    # Wipe vanilla terrain
    layer1.clear()

    # Helper: add tile object to layer1
    def tile(tileset, obj_type, x, y, w, h):
        layer1.append(LayerObject(tileset=tileset, obj_type=obj_type,
                                  x=ZX + x, y=ZY + y, w=w, h=h))

    # Helper: add sprite (coords relative to zone origin)
    def spr(stype, x, y, spritedata=b'\x00'*6, zone_id=0):
        s = Sprite()
        s.stype      = stype
        s.x          = (ZX + x) * 16
        s.y          = (ZY + y) * 16
        s.spritedata = spritedata
        s.zone_id    = zone_id
        s.extra_byte = 0
        area.sprites.append(s)

    # Corridor floor: GY = ZH - 4 (4 rows up from zone bottom)
    # Zone is 24 tiles tall; floor at row 20 gives 4-tile pit below and
    # 19 tiles of headroom above — enough for Thwomps and elevated platforms.
    GY = ZH - 4   # = 20

    # Floor: two 262-tile halves (max safe object width = ~540)
    HALF = ZW // 2  # 262
    tile(1, 0, 0,    GY,     HALF, 1)
    tile(1, 1, 0,    GY + 1, HALF, 3)
    tile(1, 0, HALF, GY,     ZW - HALF, 1)
    tile(1, 1, HALF, GY + 1, ZW - HALF, 3)

    # Entrance (vanilla entrance 0 preserved; update coordinates)
    for ent in area.entrances:
        if ent.entrance_id == 0:
            ent.x = (ZX + 3) * 16
            ent.y = (ZY + GY - 2) * 16
            break
    # Add midway respawn entrance (entrance 1)
    area.entrances.append(Entrance(x=(ZX + 162) * 16, y=(ZY + GY - 1) * 16,
                                   entrance_id=1, dest_area=0, dest_entrance=0,
                                   etype=0, zone_id=0))

    # Each world callback covers ~48 tiles → 8×48 = 384 + gap = stair_x 395
    # Goal at stair_x+90 = 485 tiles → (ZX+485)*16 = 8016px = vanilla length

    # ── W1 (x=6–54): Goomba tsunami ──
    for ex in range(6, 54, 4):
        spr(db.GOOMBA, ex, GY - 1)
    for ex in range(10, 54, 10):
        spr(db.DRY_BONES, ex, GY - 1)

    # ── W2 (x=56–104): Banzai Bills + elevated platforms ──
    for bx in range(58, 104, 10):
        spr(db.BANZAI_BILL_LAUNCHER, bx, GY - 1)
    for bx in range(62, 104, 12):
        spr(db.CROWBER, bx, GY - 8)
    for px in range(60, 104, 12):
        tile(1, 0, px, GY - 6, 4, 1)
        tile(1, 1, px, GY - 5, 4, 2)

    # ── W3 (x=108–158): Big Thwomp gauntlet on thin ledges ──
    for px in range(110, 158, 8):
        tile(1, 0, px, GY - 4, 3, 1)
        tile(1, 1, px, GY - 3, 3, 1)
    for tx in range(112, 158, 10):
        spr(db.BIG_THWOMP, tx, 1)
    spr(db.STAR_COIN, 134, GY - 7, bytes([0, 0, 0, 0, 0, 0]))

    spr(db.MIDWAY_FLAG, 162, GY - 1, b'\x00\x00\x00\x01\x00\x00')

    # ── W4 (x=164–212): Dungeon — Dry Bones + Hammer Bros ──
    for px in range(166, 212, 8):
        tile(1, 0, px, GY - 5, 4, 1)
        tile(1, 1, px, GY - 4, 4, 2)
    for fx in range(168, 212, 10):
        spr(db.DRY_BONES, fx, GY - 4)
    for hx in range(172, 212, 14):
        spr(db.HAMMER_BRO, hx, GY - 6)

    # ── W5 (x=216–264): Forest — Chain Chomps on ledges ──
    for px in range(218, 264, 10):
        tile(1, 0, px, GY - 7, 5, 1)
        tile(1, 1, px, GY - 6, 5, 2)
    for cx in range(220, 264, 10):
        spr(db.CHAIN_CHOMP, cx, GY - 8)

    # ── W6 (x=268–316): Sledge Bros + Podoboos ──
    for sx in range(270, 316, 8):
        spr(db.SLEDGE_BRO, sx, GY - 1)
    for pbx in range(272, 316, 10):
        spr(db.PODOBOO, pbx, GY + 2, b'\x00\x00\x00\x00\x00\x02')

    # ── W7 (x=320–368): Sky platforms + Banzai second wave ──
    for px in range(322, 368, 12):
        tile(1, 0, px, GY - 8, 4, 1)
        tile(1, 1, px, GY - 7, 4, 2)
    for bx in range(324, 368, 10):
        spr(db.BANZAI_BILL_LAUNCHER, bx, GY - 1)
    for cx in range(326, 368, 12):
        spr(db.CROWBER, cx, GY - 12)
    spr(db.STAR_COIN, 344, GY - 12, bytes([0, 0, 0, 0, 1, 0]))

    # ── W8 (x=372–393): All Bros + Crowbers + Thwomps — dense final sprint ──
    for bx in range(374, 393, 6):
        spr(db.CROWBER, bx, GY - 10)
    for bx in range(375, 393, 8):
        spr(db.HAMMER_BRO, bx, GY - 1)
    for bx in range(377, 393, 10):
        spr(db.SLEDGE_BRO, bx, GY - 1)
    for bx in range(379, 393, 12):
        spr(db.BIG_THWOMP, bx, 1)
    for bx in range(381, 393, 10):
        spr(db.PODOBOO, bx, GY + 2, b'\x00\x00\x00\x00\x00\x02')

    # ── ASCENDING FINALE: zigzag staircase — stair_x=395 puts goal at tile 485 ──
    # (ZX+485)*16 = (16+485)*16 = 8016px = vanilla 09-08 goal pole position
    stair_x = 395
    NUM_STAIRS = 16
    for i in range(NUM_STAIRS):
        px = stair_x + i * 5
        py = GY - 2 - i
        if py < 2:
            py = 2
        tile(1, 0, px, py,     4, 1)
        tile(1, 1, px, py + 1, 4, 3)
        if i % 4 == 0:
            spr(db.PODOBOO, px + 2, py + 3, b'\x00\x00\x00\x00\x00\x02')
        if i % 6 == 0:
            spr(db.CROWBER, px + 1, py - 2)

    summit_x = stair_x + NUM_STAIRS * 5 + 2
    summit_y = 2
    tile(1, 0, summit_x,      summit_y,     14, 1)
    tile(1, 1, summit_x,      summit_y + 1, 14, 4)
    spr(db.STAR_COIN, summit_x + 5, summit_y - 2, bytes([0, 0, 0, 0, 2, 0]))
    spr(db.GOAL_POLE, summit_x + 10, summit_y + 1)

    # loaded_sprites must cover all sprite types present (vanilla controllers + ours)
    area.loaded_sprites = sorted(set(s.stype for s in area.sprites))

    # Write back
    arc.set_file('course/course1.bin', serialize_course_bin(area))
    arc.set_file('course/course1_bgdatL1.bin', serialize_layer_data(layer1))

    with open('output/ChaosStation/Stage/09-08.arc', 'wb') as f:
        f.write(arc.pack())
    print('Created 9-8: Chaos Absolute (vanilla base, all worlds, ascending finale)')


def create_chaos_credits():
    """Write custom staffroll.bin credits for Chaos Station.

    Uses the official NSMBW Staffroll Tool (staffroll.py) to compile the
    text format into a valid binary, avoiding manual binary encoding issues.
    """
    import subprocess, tempfile, shutil

    text = """\
:<yellow>PRODUCED BY</yellow>
:Stecca



:<yellow>CHAOS STATION</yellow>
:The First AI-Built NSMBW Modpack



:<yellow>HUMAN VISION</yellow>
:Stecca



:<yellow>AI DIRECTOR</yellow>
:Claude Sonnet 4.6



:<yellow>AI SYSTEM</yellow>
:Anthropic Claude



:<yellow>WORLD DESIGN</yellow>
:Claude AI



:<yellow>LEVEL DESIGN</yellow>
:All 50+ Levels Generated by AI
:Zero Human Code



:<yellow>W1 GRASS</yellow>
:Propeller Plains
:Underground Rumble
:Sky High Chaos
:Sunken Abyss
:Skyline Sprint
:Phantom Passage



:<yellow>W2 DESERT</yellow>
:Sandstorm Blitz
:Pyramid Descent
:Oasis Heights
:Desert Gales
:Sunbaked Ruins
:Bramball Dunes
:Sandstorm Spire
:Roy's Three-Way Maze



:<yellow>W3 ICE</yellow>
:Penguin Parkway
:Frostbite Chasm
:Sub-Zero Swim
:Switchblock Spire
:Frostwheel Gallery
:Frozen Mansion of Woe
:Glacial Spire
:Lemmy's Icy Arena



:<yellow>W4 OCEAN</yellow>
:Tropical Coast
:Jellyfish Depths
:Barrel Roll Rapids
:Mangrove Maze
:Piranha Tides
:Coral Catapult
:Coral Keep



:<yellow>W5 JUNGLE</yellow>
:Venomwood Causeway
:Frostspill Ravine
:Rootlight Catacombs
:Stormvine Skywalk
:Sunken Thorn Citadel
:Drowned Gallery
:Briarclock Tower
:Briar Bastion



:<yellow>W6 MOUNTAIN</yellow>
:Cliffside Stampede
:Bullet Bill Boulevard
:Frozen Depths
:Magma Crags
:Vertigo Climb
:Fortress of Winds
:Summit Blitz



:<yellow>W7 SKY</yellow>
:Cloud Rush
:Gale Force Gauntlet
:Armada Approach
:Skykeep Fortress
:Stormcellar Depths
:Skyfall Gauntlet



:<yellow>W8 LAVA</yellow>
:Scorched Entry
:Poison Depths
:Meteor Storm
:Midnight Trench
:Magma Rise
:Bowser's Vanguard
:Inferno Shaft
:Kamek's Spire
:The Doomship
:Bowser's Fortress



:<yellow>W9 CHAOS</yellow>
:Pixel Perfect
:Enemy Flood
:Upside Down
:Ghost Maze
:Snowfire
:King Bill Alley
:Rotor Hell
:Chaos Absolute



:<yellow>TOOLS USED</yellow>
:Reggie Level Editor
:Python 3
:U8Archive Library
:NSMBW Modding Wiki



:<yellow>SPECIAL THANKS</yellow>
:Nintendo EAD
:NSMBW Community
:Reggie Developers
:All Playtesters
:You The Player



:<yellow>GENERAL PRODUCER</yellow>
:Shigeru Miyamoto



:<yellow>EXECUTIVE PRODUCER</yellow>
:<coin>Satoru Iwata</coin>



:<Copyrights>
"""

    out_dir = 'output/ChaosStation/US/EngUS/staffroll'
    os.makedirs(out_dir, exist_ok=True)

    tool = 'NSMBW-Staffroll-Tool-master/staffroll.py'

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt',
                                     delete=False, encoding='utf-8') as tmp:
        tmp.write(text)
        tmp_path = tmp.name

    try:
        out_bin = f'{out_dir}/staffroll.bin'
        subprocess.run(
            ['python3', tool, '--type', 'txt', tmp_path, out_bin],
            check=True
        )
        print(f'Saved custom credits: {out_bin} ({os.path.getsize(out_bin)} bytes)')
    finally:
        os.unlink(tmp_path)


if __name__ == '__main__':
    print("=== Chaos Station v2 — Level Pack Generator ===\n")

    print("[0/19] Modifying Peach's Castle (1-Up Farm)")
    create_peach_castle_farm()

    print("\n[1/19] Creating Level 1-1: Propeller Plains")
    create_level_1_1()

    print("[2/12] Creating Level 1-2: Underground Rumble (2 areas)")
    create_level_1_2()

    print("[3/14] Creating Level 1-3: Sky High Chaos (+ secret exit)")
    create_level_1_3()

    print("[4/14] Creating Level 1-4: Sunken Abyss")
    create_level_1_4()

    print("[5/14] Creating Level 1-5: Skyline Sprint")
    create_level_1_5()

    print("[6/14] Creating Level 1-6: Phantom Passage (ghost house)")
    create_level_1_6()

    print("[W1] Modifying Castle 1 (01-24): Larry's Lair")
    create_level_castle()

    print("[W1] Modifying Cannon 1 (01-36)")
    create_level_cannon()

    print("[7/14] Creating Level 2-1: Sandstorm Blitz")
    create_level_2_1()

    print("[8/15] Creating Level 2-2: Pyramid Descent")
    create_level_2_2()

    print("[9/16] Creating Level 2-3: Oasis Heights")
    create_level_2_3()

    print("[10/17] Creating Level 2-4: Desert Gales")
    create_level_2_4()

    print("[11/17] Creating Level 2-Tower: Sandstorm Spire")
    create_level_2_tower()

    print("[12/18] Modifying Castle 2 (02-24): Roy's Three-Way Maze")
    create_level_2_castle()


    print("[11/20] Creating Level 2-5: Sunbaked Ruins")
    create_level_2_5()

    print("[12/20] Creating Level 2-6: Bramball Dunes")
    create_level_2_6()

    print("[W2] Modifying Cannon 2 (02-36): Desert Dash")
    create_level_2_cannon()

    print("[13/20] Modifying Ambush (02-33/34/35): Desert Elite Patrol")
    create_ambush_2()

    print("[W3] Creating Level 3-1: Penguin Parkway")
    create_level_3_1()

    print("[W3] Creating Level 3-2: Frostbite Chasm")
    create_level_3_2()

    print("[W3] Creating Level 3-3: Sub-Zero Swim")
    create_level_3_3()

    print("[W3] Creating 3-Ghost House: The Frozen Mansion of Woe")
    create_level_3_ghost_house()

    print("[W3] Creating Level 3-4: Switchblock Spire")
    create_level_3_4()

    print("[W3] Creating Level 3-5: Frostwheel Gallery")
    create_level_3_5()

    print("[W3] Creating 3-Tower: Glacial Spire")
    create_level_3_tower()

    print("[W3] Modifying Ambush (03-33/34/35): Blizzard Patrol")
    create_level_3_ambush()

    print("[W3] Modifying Castle 3 (03-24): Lemmy's Icy Arena")
    create_level_3_castle()

    print("[W3] Creating 3-Cannon: Frostbite Heights")
    create_level_3_cannon()

    print("[14/19] Modifying Tower 1 (01-22)")
    create_level_tower()

    print("\n[15/18] Creating World 4 levels")
    create_level_4_1()
    create_level_4_2()
    create_level_4_3()
    create_level_4_4()
    create_level_4_5()

    print("Creating 4-GH: Haunted Reef")
    create_level_4_ghost_house()

    # Vanilla modifiers for World 4
    create_level_4_tower()
    create_level_4_ambush()

    print("[W4] Creating 4-Cannon: Coral Catapult")
    create_level_4_cannon()

    print("[W4] Modifying 4-Castle (04-24): Coral Keep Remix")
    create_level_4_castle()

    print("[W4] Remixing 4-Airship (04-38): Deck Assault")
    create_level_4_airship()

    print("\n[W5] Creating Level 5-1: Venomwood Causeway")
    create_level_5_1()

    print("[W5] Creating Level 5-2: Frostspill Ravine")
    create_level_5_2()

    print("[W5] Creating Level 5-3: Rootlight Catacombs")
    create_level_5_3()

    print("[W5] Creating Level 5-4: Stormvine Skywalk")
    create_level_5_4()

    print("[W5] Creating Level 5-5: Sunken Thorn Citadel")
    create_level_5_5()

    print("[W5] Creating 5-Ghost House: Drowned Gallery")
    create_level_5_ghost_house()

    print("[W5] Modifying 5-Tower (05-22): Briarclock Tower")
    create_level_5_tower()

    print("[W5] Modifying 5-Castle (05-24): Briar Bastion")
    create_level_5_castle()

    print("[W5] Modifying 5-Cannon (05-36): Thornbolt Cannon")
    create_level_5_cannon()

    print("[W5] Modifying Ambush (05-33/34/35): Jungle Snap Patrol")
    create_level_5_ambush()

    print("\n[W6] Creating Level 6-1: Cliffside Stampede")
    create_level_6_1()
    print("[W6] Creating Level 6-2: Bullet Bill Boulevard")
    create_level_6_2()
    print("[W6] Creating Level 6-3: Frozen Depths")
    create_level_6_3()
    print("[W6] Creating Level 6-4: Magma Crags")
    create_level_6_4()
    print("[W6] Creating Level 6-5: Vertigo Climb")
    create_level_6_5()
    print("[W6] Creating Level 6-6: Fortress of Winds")
    create_level_6_6()
    print("[W6] Modifying Tower (06-22)")
    create_level_6_tower()
    print("[W6] Modifying Castle (06-24)")
    create_level_6_castle()
    print("[W6] Modifying Mushroom Houses")
    create_level_6_mushroom_houses()
    print("[W6] Modifying Ambushes")
    create_level_6_ambush()
    print("[W6] Creating Cannon (06-36)")
    create_level_6_cannon()
    print("[W6] Modifying Airship (06-38)")
    create_level_6_airship()

    print("\n[W7] Creating Level 7-1: Cloud Rush")
    create_level_7_1()
    print("[W7] Creating Level 7-2: Gale Force Gauntlet")
    create_level_7_2()
    print("[W7] Creating Level 7-3: Armada Approach")
    create_level_7_3()
    print("[W7] Creating Level 7-4: Skykeep Fortress")
    create_level_7_4()
    print("[W7] Creating Level 7-5: Stormcellar Depths")
    create_level_7_5()
    print("[W7] Creating Level 7-6: Skyfall Gauntlet")
    create_level_7_6()
    print("[W7] Creating Ghost House (07-21)")
    create_level_7_ghost_house()
    print("[W7] Modifying Tower (07-22)")
    create_level_7_tower()
    print("[W7] Modifying Castle (07-24)")
    create_level_7_castle()
    print("[W7] Modifying Mushroom Houses")
    create_level_7_mushroom_houses()
    print("[W7] Modifying Ambushes")
    create_level_7_ambush()
    print("[W7] Modifying Airship (07-38)")
    create_level_7_airship()

    print("\n[W8] Creating Level 8-1: Scorched Entry")
    create_level_8_1()
    print("[W8] Creating Level 8-2: Poison Depths (secret exit)")
    create_level_8_2()
    print("[W8] Creating Level 8-3: Meteor Storm")
    create_level_8_3()
    print("[W8] Creating Level 8-4: Midnight Trench (underwater)")
    create_level_8_4()
    print("[W8] Creating Level 8-5: Magma Rise")
    create_level_8_5()
    print("[W8] Creating Level 8-6: Bowser's Vanguard")
    create_level_8_6()
    print("[W8] Creating Level 8-7: Doomfield")
    create_level_8_7()
    print("[W8] Modifying Tower (08-22): Kamek's Spire")
    create_level_8_tower()
    print("[W8] Modifying Airship (08-38): The Doomship")
    create_level_8_airship()
    print("[W8] Modifying Ambushes (08-33/34/35)")
    create_level_8_ambush()
    print("[W8] Modifying Castle (08-24): Bowser's Fortress")
    create_level_8_castle()

    print("\n[W9] Creating World 9: Chaos Absolute (Veteran Challenges)")
    print("[W9] Creating Level 9-1: Pixel Perfect")
    create_level_9_1()
    print("[W9] Creating Level 9-2: Enemy Flood")
    create_level_9_2()
    print("[W9] Creating Level 9-3: Upside Down")
    create_level_9_3()
    print("[W9] Creating Level 9-4: Ghost Maze")
    create_level_9_4()
    print("[W9] Creating Level 9-5: Snowfire")
    create_level_9_5()
    print("[W9] Creating Level 9-6: King Bill Alley")
    create_level_9_6()
    print("[W9] Creating Level 9-7: Minimal Matter")
    create_level_9_7()
    print("[W9] Creating Level 9-8: Chaos Absolute")
    create_level_9_8()

    print("\n[16/18] Copying & Modifying Mushroom Houses (W1-W3)")
    create_mushroom_houses()

    print("[17/18] Creating Riivolution config")
    create_riivolution_xml()

    print("[18/18] Patching title screen banner (opening.bnr)")
    create_title_screen_branding()

    print("[19/19] Building texture modifications (title logo, character colors, coins, icons)")
    build_all_textures()

    print("[20/20] Writing custom credits (staffroll.bin)")
    create_chaos_credits()

    print("\n=== Done! ===")
