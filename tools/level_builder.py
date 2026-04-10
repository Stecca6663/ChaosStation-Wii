"""
Level Builder — High-level API for building NSMBW levels.

Provides a fluent interface for constructing course areas with terrain,
sprites, zones, and entrances. Uses the proven course_parser serialization
to guarantee format correctness.
"""

import struct
from typing import List, Optional

from tools.course_parser import (
    CourseArea, Tileset, AreaSettings, Bounding, UnknownBlock4,
    Background, Entrance, Sprite, Zone, Location, Path, PathNode,
    LayerObject, serialize_course_bin, serialize_layer_data
)
from tools.u8archive import U8Archive
from tools.sprite_db import *


class AreaBuilder:
    """Builder for a single course area."""

    def __init__(self, area_num: int = 1):
        self.area_num = area_num
        self.area = CourseArea()
        # Set defaults
        self.area.tileset = Tileset(slot0=TILESET_STANDARD, slot1=TILESET_GRASS)
        self.area.settings = AreaSettings(time_limit=300, start_entrance=0,
                                          unk1=100, unk2=100, unk3=100)
        self.area.block4 = UnknownBlock4()
        # Default bounding
        self.area.boundings.append(Bounding(
            upper=-16, lower=-8, upper2=0, lower2=0,
            bound_id=0, mp_cam_zoom=15, upper3=0, lower3=0
        ))
        # Default BG
        self.area.bg_a.append(Background(
            bg_id=0, x_scroll=0, y_scroll=0, y_pos=0, x_pos=0,
            bg1=10, bg2=258, bg3=10, zoom=0, unk=0
        ))
        self.area.bg_b.append(Background(
            bg_id=0, x_scroll=0, y_scroll=0, y_pos=0, x_pos=0,
            bg1=10, bg2=258, bg3=10, zoom=0, unk=0
        ))

    def set_tileset(self, slot: int, name: str):
        """Set a tileset slot (0-3)."""
        if slot == 0:
            self.area.tileset.slot0 = name
        elif slot == 1:
            self.area.tileset.slot1 = name
        elif slot == 2:
            self.area.tileset.slot2 = name
        elif slot == 3:
            self.area.tileset.slot3 = name
        return self

    def set_background(self, bg2: int, bg2b: int = None,
                        x_scroll_a: int = 2, y_scroll_a: int = 6,
                        x_scroll_b: int = 1, y_scroll_b: int = 4,
                        zoom_a: int = 1, zoom_b: int = 2):
        """Set the background image ID. Common values:
        258   = World 1 grass/sky
        4098  = underwater (World 4-4 style)
        17666 = athletic sky layer 1
        20994 = athletic sky layer 2
        1026  = desert
        1794  = snow
        10754 = castle
        770   = underground/cave
        If bg2b is provided, a second background entry is also updated.
        """
        entries_a = self.area.bg_a
        entries_b = self.area.bg_b
        for i, bg in enumerate(entries_a):
            bg.bg2 = bg2b if (bg2b is not None and i > 0) else bg2
            bg.x_scroll = x_scroll_a
            bg.y_scroll = y_scroll_a
            bg.zoom = zoom_a
        for i, bg in enumerate(entries_b):
            bg.bg2 = bg2b if (bg2b is not None and i > 0) else bg2
            bg.x_scroll = x_scroll_b
            bg.y_scroll = y_scroll_b
            bg.zoom = zoom_b
        return self

    def set_time(self, seconds: int):
        """Set time limit (100-999)."""
        self.area.settings.time_limit = seconds
        return self

    def set_music(self, music_id: int):
        """Set default music for zone 0."""
        if self.area.zones:
            self.area.zones[0].music = music_id
        return self

    def set_start_entrance(self, entrance_id: int):
        """Set which entrance Mario spawns at."""
        self.area.settings.start_entrance = entrance_id
        return self

    # ──────── Zones ────────

    def add_zone(self, x: int, y: int, w: int, h: int, zone_id: int = 0,
                 music: int = 1, bound_id: int = 0, cam_mode: int = 0,
                 visibility: int = 0, model_dark: int = 0, terrain_dark: int = 0):
        """Add a zone (camera/gameplay boundary).
        cam_mode: 0=normal, 4=underwater (enables swim physics camera),
                  3=vertical (boss rooms), 6=desert-style
        visibility: 0=normal, 16=show sprites at edge of screen
        model_dark: 12=ghost house darkness (standard), 0=normal
        terrain_dark: terrain darkness level, 0=normal
        """
        self.area.zones.append(Zone(
            x=x, y=y, w=w, h=h,
            zone_id=zone_id, bound_id=bound_id,
            cam_mode=cam_mode, cam_zoom=0, visibility=visibility,
            bg_a=0, bg_b=0, cam_track=0,
            music=music, sfx=0,
            model_dark=model_dark, terrain_dark=terrain_dark
        ))
        return self

    # ──────── Entrances ────────

    def add_entrance(self, entrance_id: int, x: int, y: int,
                     etype: int = ENTRANCE_NORMAL, zone_id: int = 0,
                     dest_area: int = 0, dest_entrance: int = 0,
                     settings: int = 0, leave_level: int = 0):
        """Add an entrance/spawn point."""
        self.area.entrances.append(Entrance(
            x=x, y=y, unk1=0, unk2=0,
            entrance_id=entrance_id,
            dest_area=dest_area, dest_entrance=dest_entrance,
            etype=etype, zone_id=zone_id, layer=0, path=0,
            settings=settings, leave_level=leave_level,
            cp_direction=0
        ))
        return self

    # ──────── Sprites ────────

    def add_sprite(self, stype: int, x: int, y: int, zone_id: int = 0,
                   spritedata: bytes = b'\x00' * 6, extra: int = 0):
        """Add a sprite (enemy, item, boss, etc.) at pixel coordinates."""
        self.area.sprites.append(Sprite(
            stype=stype, x=x, y=y,
            spritedata=spritedata, zone_id=zone_id, extra_byte=extra
        ))
        return self

    def add_sprite_tile(self, stype: int, tx: int, ty: int, **kwargs):
        """Add a sprite at tile coordinates (1 tile = 16 pixels)."""
        return self.add_sprite(stype, tx * 16, ty * 16, **kwargs)

    # ──────── Terrain (Layer Objects) ────────

    def add_object(self, layer: int, tileset: int, obj_type: int,
                   x: int, y: int, w: int = 1, h: int = 1):
        """Add a raw terrain object to a layer (tile coordinates)."""
        obj = LayerObject(tileset=tileset, obj_type=obj_type,
                          x=x, y=y, w=w, h=h)
        if layer == 0:
            self.area.layer0.append(obj)
        elif layer == 1:
            self.area.layer1.append(obj)
        elif layer == 2:
            self.area.layer2.append(obj)
        return self

    # ──────── High-level terrain helpers ────────

    def add_ground(self, x: int, y: int, width: int, height: int = 3,
                   tileset: int = 1):
        """Add visible ground: green surface on top, brown fill underneath."""
        # Surface top (grass tileset provides the visible green/brown ground)
        self.add_object(1, tileset, GrassObjs.GROUND_TOP, x, y, width, 1)
        # Fill below
        if height > 1:
            self.add_object(1, tileset, GrassObjs.GROUND_FILL, x, y + 1, width, height - 1)
        return self

    def add_platform(self, x: int, y: int, width: int, tileset: int = 1):
        """Add a small floating ground platform (visible, solid)."""
        self.add_object(1, tileset, GrassObjs.GROUND_TOP, x, y, width, 1)
        self.add_object(1, tileset, GrassObjs.GROUND_FILL, x, y + 1, width, 1)
        return self

    def add_hill(self, x: int, y: int, half_width: int = 3, height: int = 3,
                 tileset: int = 1):
        """Add a decorative hill on layer 0 (no collision).
        x,y = top-center tile position, half_width = width from center to edge.
        Placed on layer 0 so it doesn't block movement or overlap terrain.
        """
        # Left slope (ascending from left) — decorative only
        self.add_object(0, tileset, GrassObjs.SLOPE_LEFT_UP, x - half_width, y,
                        half_width, height)
        # Right slope (descending to right) — decorative only
        self.add_object(0, tileset, GrassObjs.SLOPE_RIGHT_UP, x, y,
                        half_width, height)
        return self

    def add_brick_block(self, x: int, y: int, contents: int = 0, zone_id: int = 0):
        """Add a breakable brick block."""
        # Correct Pa0_jyotyu object IDs (verified against vanilla levels):
        # 26 = Empty Brick (standard breakable)
        # 27 = Brick with Coins
        # 28 = Brick with Adaptive Power-up (Mushroom/Fire)
        # 29 = Brick with Star
        # 31 = Brick with Vine
        # NOTE: Object 20 is an INVISIBLE block, NOT a brick!

        item_map = {
            0: 26, # Empty / standard brick
            1: 28, # Mushroom / Adaptive
            2: 28, # Fire Flower (Native uses Adaptive)
            3: 29, # Star
            4: 28, # 1-Up (Failsafe to Adaptive)
            5: 28, # Propeller Suit (Adaptive)
            6: 28, # Penguin Suit (Adaptive)
            10: 27, # Multi-Coin brick
        }

        tile_id = item_map.get(contents, 26)
        self.add_object(1, 0, tile_id, x, y, 1, 1)

        return self

    def add_pipe(self, x: int, y: int, height: int = 2, tileset: int = 0):
        """Add a vertical green pipe (entry on top)."""
        # Pipe entry
        self.add_object(1, tileset, StandardObjs.PIPE_ENTRY, x, y, 2, 2)
        # Pipe body
        if height > 2:
            self.add_object(1, tileset, StandardObjs.PIPE_BODY, x, y + 2, 2, height - 2)
        return self

    def add_staircase(self, x: int, y_base: int, steps: int,
                      direction: int = 1, tileset: int = 1):
        """Add ascending stairs (visible).
        direction=1 means going up-right, -1 means up-left.
        """
        for i in range(steps):
            step_x = x + (i * direction) if direction > 0 else x + (steps - 1 - i)
            step_y = y_base - i
            self.add_object(1, tileset, GrassObjs.GROUND_TOP, step_x, step_y, 1, 1)
            if i > 0:
                self.add_object(1, tileset, GrassObjs.GROUND_FILL, step_x, step_y + 1, 1, i)
        return self

    def add_gap_bridge(self, x: int, y: int, width: int, tileset: int = 0):
        """Add a row of bricks (breakable bridge over a gap)."""
        self.add_object(1, tileset, StandardObjs.BRICK, x, y, width, 1)
        return self

    def add_question_block(self, x: int, y: int, contents: int = 0, zone_id: int = 0):
        """Add a ? block.
        contents: 0=coin, 1=mushroom, 2=fireflower, 3=star, 4=1up, 5=propeller, 6=penguin
        """
        # Based on extensive native testing of Tileset 0 (Pa0_jyotyu):
        # 38 = Coin
        # 39 = Adaptive Powerup (Mushroom if small, Fire Flower if big)
        # 40 = Star
        # 41 = Coin (again)
        # 42 = Vine
        # 43 = Spring
        # 44 = Mini Mushroom
        # 45 = Propeller Suit
        # 46 = Penguin Suit
        # 47 = Yoshi
        # 48 = Ice Flower

        # The 1-Up is traditionally hidden in invisible blocks, but for physical
        # question blocks, NSMBW often uses standard Adaptive (39) or Coin (38)
        # and relies on Area properties or specific Event tracking for 1-Ups, 
        # or uses Sprite 207 for free-floating/custom ones.
        # We will map standard items to the native Tile IDs.
        
        item_map = {
            0: 38, # Coin
            1: 39, # Mushroom / Adaptive
            2: 39, # Fire Flower (Native uses Adaptive)
            3: 40, # Star
            4: 39, # 1-Up (Failsafe to Adaptive, native 1Ups are complex)
            5: 45, # Propeller Suit
            6: 46, # Penguin Suit
            7: 47, # Yoshi
            8: 48, # Ice Flower
            9: 44, # Mini Mushroom
        }
        
        tile_id = item_map.get(contents, 38)
        
        # Place the physical background tile with the baked-in item attribute
        self.add_object(1, 0, tile_id, x, y, 1, 1)

        return self

    def add_star_coin(self, x: int, y: int, coin_num: int = 0, zone_id: int = 0):
        """Add a star coin. coin_num: 0=first, 1=second, 2=third.
        x, y in tile coordinates.
        """
        sd = bytearray(b'\x00\x00\x00\x00\x00\x00')
        sd[4] = coin_num & 0x03  # byte 4 = star coin number (0, 1, or 2)
        self.add_sprite(STAR_COIN, x * 16, y * 16,
                       zone_id=zone_id, spritedata=bytes(sd))
        return self

    def add_secret_goal(self, x: int, y: int, zone_id: int = 0):
        """Add a secret/red flagpole. Byte 2 = 0x10 flags as secret exit."""
        sd = b'\x00\x00\x10\x00\x00\x00'
        self.add_sprite(GOAL_POLE, x * 16, y * 16,
                       zone_id=zone_id, spritedata=sd)
        return self

    def add_red_coin_ring(self, x: int, y: int, zone_id: int = 0, group_id: int = 0x22, pattern: str = 'arc'):
        """Add a red coin ring with 8 red coins in a specific pattern.
        pattern can be 'arc', 'circle', 'line', 'wave', 'drop'
        x, y in tile coordinates.
        """
        ring_sd = bytearray(b'\x00\x00\x00\x00\x00\x00')
        ring_sd[1] = group_id
        self.add_sprite(RED_COIN_RING, x * 16, y * 16,
                       zone_id=zone_id, spritedata=bytes(ring_sd))

        coin_sd = bytearray(b'\x00\x00\x00\x00\x00\x00')
        coin_sd[1] = group_id

        if pattern == 'circle':
            # Circle around the ring, reduced radius to 48px (~3 tiles) to prevent ground clipping
            pixel_offsets = [
                (0, -48), (34, -34), (48, 0), (34, 34),
                (0, 48), (-34, 34), (-48, 0), (-34, -34)
            ]
        elif pattern == 'line':
            # Straight horizontal line
            pixel_offsets = [(32 + i*24, 0) for i in range(8)]
        elif pattern == 'wave':
            # Sine-like wave length, max drop +32px (safe for GY-3)
            pixel_offsets = [
                (32, 0), (56, -32), (80, 0), (104, 32),
                (128, 0), (152, -32), (176, 0), (200, 32)
            ]
        elif pattern == 'drop':
            # Vertical column centered slightly above ring to prevent ground clipping
            # 8 coins * 16px spacing, ranging from -80px to +32px
            pixel_offsets = [(0, -80 + i*16) for i in range(8)]
        else:
            # Default arc pattern
            pixel_offsets = [
                ( 32,   0), ( 48, -16), ( 64, -32), ( 80, -32),
                ( 96, -32), (112, -16), (128,   0), (144,  16),
            ]
            
        for dx, dy in pixel_offsets:
            self.add_sprite(RED_COIN, x * 16 + dx, y * 16 + dy,
                           zone_id=zone_id, spritedata=bytes(coin_sd))
        return self

    def add_coin_line(self, x: int, y: int, count: int, zone_id: int = 0):
        """Add a horizontal line of coins at tile coordinates."""
        for i in range(count):
            self.add_sprite(COIN, (x + i) * 16, y * 16, zone_id=zone_id)
        return self

    # ──────── Locations ────────

    def add_location(self, loc_id: int, x: int, y: int, w: int, h: int):
        """Add a location rectangle."""
        self.area.locations.append(Location(
            x=x, y=y, w=w, h=h, loc_id=loc_id
        ))
        return self

    # ──────── Paths ────────

    def add_path(self, path_id: int, nodes: list):
        """Add a path with nodes for moving platforms etc.
        nodes = list of (x, y, speed, accel, delay) tuples.
        """
        start_idx = len(self.area.path_nodes)
        for nx, ny, spd, acc, dly in nodes:
            self.area.path_nodes.append(PathNode(
                x=nx, y=ny, speed=spd, accel=acc, delay=dly
            ))
        self.area.paths.append(Path(
            path_id=path_id, unk1=0,
            start_node=start_idx, node_count=len(nodes), unk2=0
        ))
        return self

    # ──────── Build ────────

    def auto_loaded_sprites(self):
        """Auto-populate Block 9 (loaded sprite types) from sprites in Block 8."""
        used_types = sorted(set(s.stype for s in self.area.sprites))
        self.area.loaded_sprites = used_types
        return self

    def build(self):
        """Finalize and return the CourseArea."""
        self.auto_loaded_sprites()
        return self.area


class LevelBuilder:
    """Build a complete NSMBW level (.arc file) with multiple areas."""

    def __init__(self):
        self.areas = {}  # area_num -> AreaBuilder

    def add_area(self, area_num: int = 1) -> AreaBuilder:
        """Add a new area and return its builder."""
        builder = AreaBuilder(area_num)
        self.areas[area_num] = builder
        return builder

    def save(self, filepath: str):
        """Save the level as a .arc file."""
        arc = U8Archive()

        for area_num, builder in sorted(self.areas.items()):
            area = builder.build()

            # Serialize course binary
            course_data = serialize_course_bin(area)
            arc.set_file(f'course/course{area_num}.bin', course_data)

            # Serialize layer data
            l0_data = serialize_layer_data(area.layer0)
            l1_data = serialize_layer_data(area.layer1)
            l2_data = serialize_layer_data(area.layer2)
            arc.set_file(f'course/course{area_num}_bgdatL0.bin', l0_data)
            arc.set_file(f'course/course{area_num}_bgdatL1.bin', l1_data)
            arc.set_file(f'course/course{area_num}_bgdatL2.bin', l2_data)

        # Pack and write
        data = arc.pack()
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(data)
        print(f'Saved: {filepath} ({len(data)} bytes)')
        return filepath
