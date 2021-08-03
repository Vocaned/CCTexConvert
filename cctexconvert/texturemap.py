# A file containing mappings of CC -> MC file names

# Pack version 3
VER3 = {
    'char.png': 'minecraft/textures/entity/steve.png',
    'chicken.png': 'minecraft/textures/entity/chicken.png',
    'creeper.png': 'minecraft/textures/entity/creeper/creeper.png',
    'pig.png': 'minecraft/textures/entity/pig/pig.png',
    'sheep.png': 'minecraft/textures/entity/sheep/sheep.png',
    'sheep_fur.png': 'minecraft/textures/entity/sheep/sheep_fur.png',
    'skeleton.png': 'minecraft/textures/entity/skeleton/skeleton.png',
    'spider.png': 'minecraft/textures/entity/spider/spider.png',
    'zombie.png': 'minecraft/textures/entity/zombie/zombie.png',
    'default.png': 'minecraft/textures/font/ascii.png',
    'icons.png': 'minecraft/textures/gui/icons.png',
    'gui.png': 'minecraft/textures/gui/widgets.png',
    'gui_classic.png': 'minecraft/textures/gui/widgets.png'
}

# Blocks
BLOCKS3 = [
    # glass_pane_top_brown is substitute for rope
    'grass_top', 'stone', 'dirt', 'grass_side',
    'planks_oak', 'stone_slab_side', 'stone_slab_top', 'brick',
    'tnt_side', 'tnt_top', 'tnt_bottom', ('glass_pane_top_brown', 'glass_pane_top'),
    'flower_rose', 'flower_dandelion', 'water_still', 'sapling_oak',

    'cobblestone', 'bedrock', 'sand', 'gravel',
    'log_oak', 'log_oak_top', 'leaves_oak', 'iron_block',
    'gold_block', 'sandstone_top', 'quartz_block_lines_top', None,
    'mushroom_red', 'mushroom_brown', 'lava_still', 'grass_top',

    # TODO: fire_layer_0 is an animation sheet, only get first frame for terrain.png
    'gold_ore', 'iron_ore', 'coal_ore', 'bookshelf',
    'cobblestone_mossy', 'obsidian', 'fire_layer_0', 'iron_block',
    'gold_block', 'sandstone_normal', 'quartz_block_lines', None,
    None, None, None, None,

    # shulker_top_brown is crate
    'sponge', 'glass', 'snow', 'ice',
    'stonebrick', 'shulker_top_brown', 'quartz_block_side', 'iron_block',
    'gold_block', 'sandstone_bottom', 'quartz_block_lines_top', None,
    None, None, None, None,

    # TODO: Some colours don't exist in modern minecraft, get them from hex colours instead
    'wool_colored_red', 'wool_colored_orange', 'wool_colored_yellow', 'wool_colored_lime',
    'wool_colored_green', 'TEAL', 'wool_colored_light_blue', 'wool_colored_cyan',
    'BLUE', 'wool_colored_purple', 'VIOLET', 'wool_colored_magenta',
    'PINK', 'wool_colored_black', 'wool_colored_gray', 'wool_colored_white',

    'wool_colored_pink', 'FOREST GREEN', 'wool_colored_brown', 'wool_colored_blue',
    'TURQUOISE', None, 'magma'

    # TODO: Are the breaking state textures at the bottom ever used by anyone? Don't transfer them over for now.
]