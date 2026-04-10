"""
Sprite ID reference database for NSMBW (New Super Mario Bros. Wii).
Contains sprite type IDs (Profile IDs), arc file associations, tileset names,
music IDs, entrance types, and terrain object IDs.

Data sources:
  - Horizon Wiki (horizon.miraheze.org)
  - Original game analysis (01-01, 01-04, 04-04, etc.)
  - NSMBW Object File Archive technical reference

Arc file → Sprite ID mapping is documented per entry where known.
REL modules:
  d_profileNP.rel — maps Sprite IDs to .arc files
  d_basesNP.rel   — base physics/collision/state machine classes
  d_enemiesNP.rel — standard enemy AI routines
  d_en_bossNP.rel — boss actor logic
"""

# ══════════════════════════════════════════════════════
# SPRITE TYPE IDs (Profile IDs)
# ══════════════════════════════════════════════════════

# ──────── Enemies — Basic ────────
# Arc: multiple (see individual entries)

GOOMBA             = 20    # Standard Goomba
PARAGOOMBA         = 21    # Winged Goomba (parakoopa-style)
MICRO_GOOMBA       = 200   # Mini Goomba swarm (Newer NSMBW specific)
GIANT_GOOMBA       = 198   # Oversized Goomba (Newer specific)
MEGA_GOOMBA        = 199   # Giant Goomba enemy (Newer specific)
CHESTNUT_GOOMBA    = 170   # Goombo — chestnut hat variant

KOOPA              = 57    # Koopa Troopa   nybble 10: 0=Green, 1=Red
KOOPA_PARATROOPA   = 58    # Paratroopa     nybble 10: 0=Green, 1=Red
BUZZY_BEETLE       = 24    # Shell enemy, ceiling walker
SPINY              = 25    # Spiny; thrown by Lakitu
UPSIDE_DOWN_SPINY  = 26    # Spiny on ceiling
SPIKE_TOP          = 60    # Spike-top; slow ceiling/wall walker
BOB_OMB            = 101   # Bob-omb (bombhei.arc)
PARA_BOB_OMB       = 269   # Parachute Bob-omb (bombhei.arc)
BOB_OMB_CANNON     = 270   # Cannon Bob-omb variant (bombhei.arc)
POKEY              = 105   # Cactus stack enemy
AMP                = 104   # Electrified ring hazard (bilikyu.arc)
AMP_RING_CHAIN     = 108   # Amp in a linked ring chain (bilikyu.arc)
SWOOP              = 100   # Swooper bat — hangs from ceiling (basabasa.arc)
FUZZY              = 343   # Spiked soot-ball on track (chorobon.arc)
WIGGLER            = 130   # Wiggler caterpillar
GIANT_WIGGLER      = 385   # Extra-large Wiggler used as platform
BRAMBALL           = 230   # Spiked ball that rolls on walls
CROWBER            = 134   # Crowber crow enemy (distinct from Swoop)
BULBER             = 233   # Deep-sea bulb fish with ambient light (ankou.arc)
BULBER_LIGHT       = 258   # Bulber ambient light circle sprite (ankou.arc)

# ──────── Enemies — Piranha Plants ────────
# Arc: pakkun.arc (standard plants)

PIRANHA_PLANT          = 73   # Standard Piranha Plant (static)
BIG_PIRANHA_PLANT      = 74   # Oversized Piranha Plant
FIRE_PIRANHA_PLANT     = 75   # Fires fireballs periodically
BIG_FIRE_PIRANHA_PLANT = 76   # Giant fire-shooting Piranha
PIPE_PIRANHA_UP        = 65   # Piranha in pipe pointing up
PIPE_PIRANHA_DOWN      = 66   # Piranha in pipe pointing down
PIPE_PIRANHA_RIGHT     = 67   # Piranha in pipe pointing right
PIPE_PIRANHA_LEFT      = 68   # Piranha in pipe pointing left
PIPE_FIRE_PIRANHA_UP   = 69   # Fire-breathing pipe Piranha (up)

# ──────── Enemies — Bros & Large ────────
# Arc: bros.arc (Hammer/Boomerang/Fire/Ice Bros + projectiles)
# Arc: bros_mega.arc (Sledge Bro)

HAMMER_BRO         = 95    # Hammer Brother (bros.arc)
BOOMERANG_BRO      = 94    # Boomerang Brother (bros.arc)
FIRE_BRO           = 80    # Fire Brother (bros.arc)
ICE_BRO            = 272   # Ice Brother (bros.arc)
SLEDGE_BRO         = 120   # Sledge Brother — large ground-pound (bros_mega.arc)
PLATFORM_HAMMER_BRO= 308   # Hammer Bro on a platform (bros.arc)
MONTY_MOLE         = 303   # Monty Mole — pops from ground (choropoo.arc)
ROCKY_WRENCH       = 149   # Rocky Wrench — throws wrenches (choropoo.arc)
LAKITU             = 54    # Lakitu — drops Spiny eggs from cloud
SPYGUY             = 351   # Shy Guy variant (Newer NSMBW specific)

# ──────── Enemies — Aquatic ────────

CHEEP_CHEEP        = 115   # Standard fish; swims in straight line
BIG_CHEEP_CHEEP    = 116   # Larger Cheep Cheep variant
SPINY_CHEEP_CHEEP  = 395   # Spiny Cheep Cheep — relentlessly chases Mario, hard to freeze
PORCU_PUFFER       = 151   # Porcupine Blowfish — expands on approach
CHEEP_CHOMP        = 180   # Cheep Chomp (Boss Bass) — large pursuing fish (bakubaku.arc)
BLOOPER            = 111   # Blooper squid — bounces through water
BLOOPER_NANNY      = 112   # Blooper with baby Bloopers attached
URCHIN             = 193   # Sea urchin — stationary spiny hazard
MEGA_URCHIN        = 194   # Giant Urchin variant (verify ID if 143 is normal)
FISHBONE           = 196   # Fishbone skeleton — tracks player in water (ONLY works underwater!)
CLOUD_AREA         = 234   # Cloud Area controller; type 4/5 = purple death cloud fields
JELLYBEAM          = 425   # Jellybeam — ceiling jellyfish light beams; use zone darkness (full dark zone)
CHAIN_CHOMP        = 146   # Chain Chomp — lunges at player on a chain

# ──────── Enemies — Ice / Snow ────────
COOLIGAN           = 201   # Cooligan — sliding penguin-like enemy (penguin_fish.arc)
ICICLE             = 248   # Falling icicle from ceiling
PENGUIN_SUIT       = 245   # Penguin suit powerup (guess/placeholder if needed)

# ──────── Enemies — Castle / Ghost House / Lava ────────

DRY_BONES          = 118   # Dry Bones — collapses and revives
GIANT_DRY_BONES    = 119   # Oversized Dry Bones variant
BOO                = 131   # Boo — approaches when Mario looks away
BIG_BOO            = 61    # Giant Boo
BROOZER            = 102   # Broozer boxing ghost — destroys breakable walls
THWOMP             = 47    # Thwomp — crushes from above
BIG_THWOMP         = 48    # Oversized Thwomp
PODOBOO            = 46    # Podoboo (Lava Bubble) — leaps from lava (bubble.arc)
FIRE_SNAKE         = 158   # Chain of fire balls in a snake pattern
FIRE_BAR           = 62    # Rotating fire bar hazard (firebar_center.arc)
                            # Arc also contains 2 models for the pivot center
MECHAKOOPA         = 232   # Mechanical Koopa — walks and shoots sparks
FLAME_CANNON       = 114   # Flame-blaster cannon base (fire_cannon.arc)
FLAME_JET_SMALL    = 117   # Small flame jet (fire_cannon.arc)
FLAME_JET_LARGE    = 307   # Large flame jet (fire_cannon.arc)
FLAME_JET_HUGE     = 309   # Huge flame jet (fire_cannon.arc)

# ──────── Bosses ────────
# Arc: d_en_bossNP.rel handles all boss logic

LARRY_KOOPA        = 189   # World 1 Boss — fires magic from platform
ROY_KOOPA          = 375   # World 5 Boss — ground pound stun
WENDY_O_KOOPA      = 241   # World 4 Boss — ring projectiles, flooded arena
IGGY_KOOPA         = 361   # World 3 Boss — Chain Chomp partner
MORTON_KOOPA_JR    = 333   # World 6 Boss — large ground-pound pillars
LEMMY_KOOPA        = 388   # World 2 Boss — circus balls, ice arena
LUDWIG_VON_KOOPA   = 401   # World 7 Boss — homing magic, flutter jump
MAGIKOOPA          = 304   # Magikoopa / Kamek — Tower of W8 boss; also generic
BOWSER_JR          = 405   # Bowser Jr. airship chariot boss
BOWSER             = 431   # Bowser — final boss W8 Castle

# Boss arena objects (Battle/Cutscene category)
BOSS_PROJECTILE    = 211   # Boss fireball effect (boss_ef_attack.arc)
BOSS_KAMECK_BLOCK  = 383   # Colored block spawned by Kamek (boss_kameck_block.arc)
BOSS_BRIDGE        = 456   # Bowser bridge segment (boss_koopa_ashiba.arc)
BOSS_DOOR          = 452   # Ornate door to final battle (boss_koopa_door.arc)
BOSS_PLATFORM      = 23    # Wooden platform (boss_koopa_lift.arc, also used general)
BOSS_ESCAPE_PLAT   = 50    # Skeleton platform for escape sequences (boss_koopa_lift_down.arc)
BOSS_JR_BRIDGE     = 405   # Bridge for Bowser Jr. battles (boss_koopaJr_down_asiba.arc)
BOSS_SHUTTER       = 407   # Heavy pillar that seals boss arena (boss_shutter.arc)
BOSS_SHUTTER_FINAL = 431   # Spiked pillar for final Bowser fight (boss_shutter_koopa.arc)
PEACH_CAGE         = 439   # Fake Peach in Cage cutscene (cage_boss_koopa.arc) — sprite 439

# ──────── Items / Blocks ────────

COIN               = 147
BLUE_COIN          = 160
RED_COIN           = 144   # Must share group_id byte with RED_COIN_RING
STAR_COIN          = 32
QUESTION_BLOCK_SPRITE = 212  # EN_OBJ_HATENA_BLOCK — ? block contents controller (confirmed from 01-01.arc)

                              # Spritedata byte 5: 0x01=mushroom, 0x0f=star, 0x02=fireflower
BRICK_BLOCK_SPRITE = 209      # Brick block sprite version (Newer specific)
INVISIBLE_BLOCK    = 221
ROULETTE_BLOCK     = 176      # Cycles through power-up rewards (block_roulette.arc)
FLYING_QUESTION_BLOCK = 175   # Winged ? block (block_pata.arc)
MUNCHER            = 342      # Invincible black plant; triggers if ice blocks melt (W9-7)
GIANT_BRICK_BLOCK  = 157      # Large brick block; 9 internal models for scaling (big_renga_block.arc)
ICE_BLOCK          = 294      # Meltable ice block; destroyed by fire-type attacks (block_ice.arc)
                               # Used to cage enemies in W9-7; melting releases Munchers
PROPELLER_BLOCK    = 393      # Portable block that grants propeller flight (block_fly.arc)
GLOW_BLOCK         = 391      # Creates dynamic light radius in dark areas (block_light.arc)
SUPER_GUIDE_BLOCK  = 477      # Triggers automated Super Guide assistance (block_help.arc)
HINT_MOVIE_BLOCK   = 443      # Plays pre-recorded gameplay hint movie (block_otehon.arc)
BEANSTALK          = 433      # Growing vine/beanstalk (block_tsuta.arc)
                               # Uses SHP0+SRT0 animation for organic growth effect
POW_BLOCK          = 16       # POW Block — screen-shaking ground pound effect
P_SWITCH           = 41       # Blue P-Switch — converts bricks↔coins
RED_SWITCH         = 42       # Red "!" Switch — turns outlined red blocks solid

# ──────── Controllers / WARNING ────────

# ITEM_BLOCK_CONTENTS = 212  # ⚠️ WRONG! Sprite 212 = AC_FLOOR_GYRATION (rolling hill terrain)
ROLLING_HILL       = 212  # AC_FLOOR_GYRATION — DO NOT USE accidentally, spawns rolling terrain

# ──────── Level Progress / Gimmicks ────────

MIDWAY_FLAG        = 188
GOAL_POLE          = 113
SPRINGBOARD        = 148
RED_COIN_RING      = 156  # Requires exactly 8 RED_COIN sprites with matching group_id
CHECKERED_PLATFORM = 223  # Checkered spring block — vertical boost (block_jump.arc)
ITEM_CHEST         = 203
ONE_WAY_GATE       = 174  # Beta one-way gate (ben.arc) — resembles DS sewer gate
WATER_FILL         = 138  # AC_BG_WATER — creates actual swim physics in a zone.
                           # Sprite 138 placed at zone origin with byte 0=0x01 (flat top)
                           # fills the entire zone with water. cam_mode=0 for scrolling camera.
                           # Do NOT use cam_mode=4 alone — that locks camera to fixed view.
LAVA_FILL          = 139  # Lava zone fill — same settings as WATER_FILL but for lava.
                           # Can be triggered by events to rise (used in W8 lava-rise levels).
POISON_FILL        = 216  # Poison/acid liquid (same role as WATER_FILL but green/toxic)
LAVA_GEYSER        = 268  # Lava geyser — shoots upward from lava surface (seen in W8-1)
RISING_LAVA_FX     = 358  # Effect: rising lava particles — red particles rise from screen bottom;
                           # visual companion to LAVA_FILL event-rise mechanic
VOLCANO_ROCK       = 293  # Volcano Rock Spawn Area — rains falling volcanic rocks/meteors from sky
                           # Used in W8-1 outdoor sections; spritedata controls spawn rate/angle
FIREBALL_SPAWN     = 426  # Fireball Spawn Area — spawns falling/shooting fireballs
KAMEK              = 427  # Kamek (boss-form) — story/boss Kamek; distinct from MAGIKOOPA (304)
GLOW_LIGHT         = 314  # env_underwater.arc — small bubble particles for aquatic atmosphere
SANDSTORM          = 374  # env_wind.arc — sandstorm particle system (internal name: "wind")

# ──────── Artillery / Projectile Launchers ────────

BULLET_BILL_LAUNCHER = 92
BANZAI_BILL_LAUNCHER = 93
KING_BILL          = 440   # King Bill — fills ~half-screen, destroys everything in path (W9-8)
SKEWER_DOWN        = 137   # Crushing pillar from above
SKEWER_UP          = 140   # Crushing pillar from below
SPIKED_BALL        = 63    # Rolling spiked ball
GIANT_SPIKED_BALL  = 98    # Giant rolling spiked ball (Bowser's Castle)

# ──────── Platforms / Mechanical ────────

BASIC_PLATFORM        = 23   # Horizontal/Vertical moving platform via nybble settings
FALLING_PLATFORM      = 50   # Donut Block — falls when stood on
TILT_PLATFORM         = 51   # Platform that tilts with player weight
SCALE_PLATFORM        = 178  # Rope-connected scale balance
SCREW_MUSHROOM_PLATFORM = 172 # Mushroom platform on mechanical screw
WOBBLE_ROCK           = 133  # Rock that wobbles when stood on
STRETCHING_PLATFORM   = 219  # Stretching line block — adjustable length (block_slide.arc)
ICE_SNAKE_BLOCK       = 166  # Snake block on ice-themed path (block_snake_ice.arc)
                              # Standard green snake block (block_snake.arc) is UNUSED in retail
BOLT_PLATFORM         = 315  # Technical screw platform (bolt.arc); World 7+8
METAL_BOX             = 289  # Indestructible metal box (box_iron.arc); 4 model variants
WOODEN_BOX            = 289  # Destructible wooden box (box_wood.arc); Airship theme
                              # SAME ID as METAL_BOX — type determined by tileset/context
LAKITU_CLOUD_BLOCK    = 370  # Temporary cloud platform left by defeated Lakitu (block_cloud.arc)
FLASHLIGHT_RAFT       = 368  # Raft for dark liquid-filled levels (boat_light_wood.arc)
BARREL                = 388  # Stationary barrel obstacle/decoration (block_taru.arc)
BIG_SHELL_CAVE        = 341  # Big Shell Cave — environmental transition (big_shell.arc)

# ══════════════════════════════════════════════════════
# TILESET NAMES (Pa0/Pa1 slot identifiers)
# ══════════════════════════════════════════════════════

TILESET_STANDARD   = "Pa0_jyotyu"        # Common objects: pipes, bricks, ? blocks
TILESET_GRASS      = "Pa1_nohara"        # World 1/overworld ground, vegetation
TILESET_UNDERGROUND= "Pa0_jyotyu_chika"  # Underground Pa0 variant
TILESET_CAVE       = "Pa1_chika"         # Cave/underground walls and ceiling
TILESET_CASTLE     = "Pa1_shiro"         # Castle bricks and lava channels
TILESET_LAVA       = "Pa0_jyotyu_yougan" # World 8 lava variant of standard tileset
TILESET_KOOPA_OUT  = "Pa1_koopa_out"     # Bowser outdoor — World 8 main terrain tileset
TILESET_LAVA_CLIFF = "Pa1_gake_yougan"   # Lava cliff tileset (08-06 style)
TILESET_DESERT     = "Pa1_sabaku"        # Sand, quicksand, desert platforms
TILESET_FOREST     = "Pa1_daishizen"     # Forest / jungle overworld tileset
TILESET_SNOW       = "Pa1_setsugen"      # Snow/ice ground and platforms
TILESET_SKY        = "Pa1_shiro_sora"    # Sky/cloud platforms (World 7)
TILESET_ATHLETIC   = "Pa1_nohara"        # Fallback to Grass (nohara) since athletic is missing
TILESET_OCEAN      = "Pa1_kaigan"        # Ocean/beach tileset (used in W4-4 underwater)
TILESET_GHOST_HOUSE= "Pa1_obake"         # Ghost House tileset
                                          # bg2=4098 for the underwater ocean background

# ══════════════════════════════════════════════════════
# BACKGROUND IDs (bg2 field in Background entries)
# ══════════════════════════════════════════════════════

BG_GRASS_SKY       = 258    # World 1 standard grass/sky (used by 1-1, 1-3, 1-4 original)
BG_FOREST          = 1538   # Flower Forest / jungle background (0x0602)
BG_UNDERGROUND     = 770    # Underground cave / ghost house dark background
BG_UNDERWATER      = 4098   # Ocean underwater (World 4-4; TILESET_OCEAN recommended)
BG_ATHLETIC_SKY_1  = 17666  # Athletic cloud sky — layer 1 (original 1-5)
BG_ATHLETIC_SKY_2  = 20994  # Athletic cloud sky — layer 2 (use with BG_ATHLETIC_SKY_1)
BG_DESERT          = 1026   # Desert sandy sky (World 2)
BG_SNOW            = 1794   # Snowy sky (World 3)
BG_CASTLE          = 10754  # Castle dark background (boss rooms, W1-Castle)
BG_LAVA            = 11010  # World 8 outdoor lava sky background
BG_GHOST_HOUSE     = 3842   # Interior Ghost House dark BG

# ══════════════════════════════════════════════════════
# MUSIC IDs (zone music field)
# ══════════════════════════════════════════════════════

MUSIC_OVERWORLD    = 1
MUSIC_UNDERGROUND  = 2
MUSIC_CASTLE       = 3
MUSIC_ATHLETIC     = 4
MUSIC_GHOST_HOUSE  = 5
MUSIC_DESERT       = 6
MUSIC_SNOW         = 7
MUSIC_LAVA         = 8
MUSIC_BOSS         = 9
MUSIC_SKY          = 10
MUSIC_TOAD_HOUSE   = 11
MUSIC_CASTLE_BOSS  = 12
MUSIC_AIRSHIP      = 13
MUSIC_UNDERWATER   = 15
MUSIC_FOREST       = 18

# ══════════════════════════════════════════════════════
# ENTRANCE TYPES (etype field)
# Verified against original game level data
# ══════════════════════════════════════════════════════

ENTRANCE_NORMAL    = 0   # Standard spawn / teleport destination
ENTRANCE_DOOR      = 1   # Door-type entry (ghost house doors)
ENTRANCE_PIPE_UP   = 2   # Emerge from pipe going upward
ENTRANCE_PIPE_DOWN = 3   # Enter pipe going downward
ENTRANCE_PIPE_LEFT = 4   # Enter/exit pipe going left
ENTRANCE_PIPE_RIGHT= 5   # Enter/exit pipe going right
ENTRANCE_VINE      = 6   # Grab vine / beanstalk entry
ENTRANCE_JUMPING   = 7   # Jump-in entry (falling from above)

# ══════════════════════════════════════════════════════
# TERRAIN OBJECT IDs (per tileset)
# ══════════════════════════════════════════════════════

class GrassObjs:
    """Terrain object IDs for Pa1_nohara (grass/overworld) tileset.
    Used for World 1-style ground, islands, and vegetation.
    """
    GROUND_TOP       = 0   # Top surface of ground (green grass cap)
    GROUND_FILL      = 1   # Interior solid fill below surface
    GROUND_FILL_ALT  = 2   # Alternate fill (used for wall interiors)
    LEFT_WALL        = 3   # Left edge wall
    RIGHT_WALL       = 4   # Right edge wall
    TOP_LEFT_CORNER  = 5   # Corner tile: top-left
    TOP_RIGHT_CORNER = 6   # Corner tile: top-right
    CORNER_INNER_BL  = 7   # Inner corner: bottom-left
    CORNER_INNER_BR  = 8   # Inner corner: bottom-right
    BOTTOM_LEFT      = 9   # Bottom edge: left
    BOTTOM_RIGHT     = 10  # Bottom edge: right
    INTERIOR         = 11  # Fully enclosed interior
    LEDGE            = 13  # Ledge/outcrop detail
    BIG_BLOCK        = 14  # Oversized single block
    SLOPE_RIGHT_UP   = 15  # Slope ascending right
    SLOPE_LEFT_UP    = 16  # Slope ascending left
    SLOPE_EDGE_RIGHT = 17  # Edge of slope: right
    SLOPE_EDGE_LEFT  = 18  # Edge of slope: left
    SLOPE_STEEP_R    = 19  # Steep slope: right
    SLOPE_STEEP_L    = 20  # Steep slope: left
    SLOPE_ALT        = 21  # Alternate slope fill
    SLOPE_FILL       = 22  # Slope interior fill
    SLOPE_GENTLE_R   = 23  # Gentle slope: right
    SLOPE_GENTLE_L   = 24  # Gentle slope: left
    # Water surface tiles (used in original 1-4, Pa1_nohara water objects)
    WATER_SURFACE_L  = 40  # Water surface: left cap
    WATER_SURFACE_MID= 41  # Water surface: middle
    WATER_SURFACE_R  = 42  # Water surface: right cap
    WATER_FILL_TILE  = 43  # Water body fill (below surface)
    # Decorative vegetation
    BUSH_LEFT        = 41
    BUSH_BODY        = 42
    BUSH_CENTER      = 43
    BUSH_RIGHT_A     = 44
    BUSH_RIGHT_B     = 45
    TREE_TRUNK       = 46
    TREE_MID         = 47
    TREE_TOP         = 48
    TREE_BRANCH_L    = 49
    TREE_LEAF_L      = 50
    TREE_BRANCH_R    = 51
    BLOCK_DECO       = 52


class StandardObjs:
    """Terrain object IDs for Pa0_jyotyu (standard/common) tileset.
    Used across all themes for common objects: bricks, pipes, ? blocks.
    Internal BRRES: Pa0_jyotyu.arc — shared by all levels.
    """
    INVISIBLE_BLOCK  = 20   # Invisible block (hidden ? block)
    BRICK            = 26   # Breakable brick block (standard brown)
    BRICK_COIN       = 27   # Brick block with coins
    BRICK_POWERUP    = 28   # Brick block with adaptive power-up
    BRICK_STAR       = 29   # Brick block with star
    BRICK_VINE       = 31   # Brick block with vine
    # Decorative aliases (layer 0 background objects — no collision)
    FLOWER_A         = 97   # Background decoration (small)
    FLOWER_B         = 98   # Background decoration (medium)
    FLOWER_C         = 99   # Background decoration (large)
    QUESTION_BLOCK   = 38   # ? block terrain object (visual only; add sprite 207 for contents)
    FENCE            = 45   # Climbable fence
    CLOUD_PLATFORM   = 55   # Cloud platform (decorative; use BASIC_PLATFORM sprite for physics)
    GROUND_FILL      = 58   # Generic ground fill
    PIPE_BODY        = 65   # Vertical pipe body (2 wide)
    PIPE_ENTRY       = 73   # Pipe entry opening (2×2)
    BG_BUSH          = 97   # Background decorative bush (layer 0, no collision)


class CaveObjs:
    """Terrain object IDs for Pa1_chika (underground/cave) tileset."""
    GROUND_TOP       = 0
    GROUND_FILL      = 1
    LEFT_WALL        = 3
    RIGHT_WALL       = 4
    TOP_LEFT_CORNER  = 5
    TOP_RIGHT_CORNER = 6
    CEILING          = 12  # Solid ceiling
    STALACTITE       = 13  # Hanging cave formation
    COLUMN           = 14  # Vertical cave pillar


class OceanObjs:
    """Terrain object IDs for Pa1_kaigan (ocean/beach) tileset.
    Used in World 4 underwater levels and our custom 1-4 ocean level.
    The water fill for physics is handled by Sprite 138 (WATER_FILL),
    not by terrain tiles. These tiles are for the ocean floor and walls.
    Verified from 04-04.arc layer data:
      ts=1 obj=24: ocean floor surface
      ts=1 obj=25: ocean floor fill
      ts=1 obj=18: coral/rock fill
    """
    FLOOR_SURFACE    = 24  # Ocean floor top surface (verified from 04-04)
    FLOOR_FILL       = 25  # Ocean floor body fill
    ROCK_FILL        = 18  # Coral/rock interior fill
    PILLAR           = 28  # Vertical column/pillar
    PILLAR_TOP       = 26  # Top of pillar
    PILLAR_BASE      = 29  # Base of pillar
    SEAWEED_LEFT     = 40  # Seaweed decoration left
    SEAWEED_RIGHT    = 41  # Seaweed decoration right
SAND_GEYSER        = 140  # Sand pillar that launches player up
LAKITU             = 54   # Throws Spinies
