import tempfile
import zipfile
import json
import os
import shutil
from PIL import Image, ImageDraw

from . import texturemap

SUPPORTED = ['1.12.2']
FORMATS = {
    1: '1.6.1 - 1.8.9',
    2: '1.9 - 1.10.2',
    3: '1.11 - 1.12.2',
    4: '1.13 - 1.14.4',
    5: '1.15 - 1.16.1',
    6: '1.16.2 - 1.16.5',
    7: '1.17+'
}


def convert(inpath: str, outpath: str):
    # Setup temporary directory and unzip the textures there
    tmpdir = tempfile.TemporaryDirectory()
    mctmp = os.path.join(tmpdir.name, 'assets')
    cctmp = os.path.join(tmpdir.name, 'classicubetextures')
    os.mkdir(cctmp)

    with zipfile.ZipFile(inpath, 'r') as f:
        f.extractall(tmpdir.name)

    # Check Minecraft version
    with open(os.path.join(tmpdir.name, 'pack.mcmeta')) as f:
        meta = json.load(f)

    ver = meta['pack']['pack_format']
    if ver != 3:
        invalidversion = 'pack version ' + ver
        if ver in FORMATS:
            invalidversion = 'minecraft version ' + FORMATS[ver]
        print(f'Invalid {invalidversion} detected. Supported MC versions: {",".join(SUPPORTED)}')
        return
    print('Detected Minecraft version: ' + FORMATS.get(ver, 'unknown'))

    res = checkresolution(mctmp)
    if not res:
        print('Invalid texturepack: Textures not found.')
        return
    print(f'Detected resolution: {res}x')

    print('Copying textures')
    copytextures(mctmp, cctmp, texturemap.VER3)

    print('Creating terrain.png')
    combinetextures(mctmp, cctmp, res, texturemap.BLOCKS3)

    print('Zipping the textures')
    with zipfile.ZipFile(outpath, "w", zipfile.ZIP_DEFLATED) as cczip:
        for file in os.scandir(cctmp):
            cczip.write(file.path, file.name)

    print('Texture pack converted and saved to ' + outpath)

    # Clean up temporary stuff
    tmpdir.cleanup()


def copytextures(mcdir, ccdir, dictionary):
    # Move files instead of actually copying to make it faster
    for key in dictionary:
        # HACK: except gui.png, which needs to be duplicated
        # WARN: this means that gui.png NEEDS to be before gui_classic.png in dictionary
        if key == 'gui.png':
            shutil.copyfile(os.path.join(mcdir, dictionary[key]), os.path.join(ccdir, key))
        else:
            shutil.move(os.path.join(mcdir, dictionary[key]), os.path.join(ccdir, key))


def combinetextures(mcdir, ccdir, res, arr):
    # TODO: Support extended textures in the future when more blocksets are added

    def texpath(name):
        return os.path.join(mcdir, 'minecraft/textures/blocks/', name + '.png')

    with Image.new('RGBA', (res*16, res*16), (107, 63, 127, 255)) as img:
        draw = ImageDraw.Draw(img)
        for y in range(16):
            for x in range(16):
                val = arr[y*16+x] if y*16+x < len(arr) else None
                if not val:
                    # Draw the little lines when there's no texture
                    # TODO: Drawing once and using paste is probably faster

                    # TODO: Blindly dividing by 16 is scary. What if it's not divisible by 16? Does MC even support that?
                    # Equals to 1/16 of the block, or 1 pixel on 16x textures
                    offset = res / 16

                    # Background colour of original textures are #d67fff
                    # but I'm using #d69fff (214, 159, 255) as a little watermark :)
                    draw.rectangle((x*res+offset, y*res+offset, (x+1)*res, (y+1)*res), (214, 159, 255, 255), None, 0)
                else:
                    # Some textures might have backups in case the original texture is missing
                    if type(val) is tuple:
                        found = None
                        for value in val:
                            if os.path.exists(texpath(value)):
                                found = value
                                break
                        if not found:
                            print('WARNING: None of the following textures were found: ' + val)
                            continue
                        val = found

                    if not os.path.exists(texpath(val)):
                        print('WARNING: Texture not found: ' + val)
                        continue

                    # TODO: Probably faster to not bother unloading the images, just keep them in memory until its completed
                    # ^ Would cause all textures to be in memory at once though..
                    with Image.open(texpath(val)) as tmpimg:
                        img.paste(tmpimg.convert('RGBA').crop((0, 0, res, res)), (x*res, y*res, (x+1)*res, (y+1)*res))

        img.save(os.path.join(ccdir, 'terrain.png'))


def checkresolution(mcpath):
    testpath = os.path.join(mcpath, "minecraft/textures/blocks/dirt.png")
    if not os.path.exists(testpath):
        return None

    with Image.open(testpath) as img:
        if img.width != img.height:
            return None
        return img.width
