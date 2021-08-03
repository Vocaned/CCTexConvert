import argparse
import os

from . import converter


def main():
    parser = argparse.ArgumentParser(prog="CCTexConvert",
                                     description='Converts Minecraft texture packs into ClassiCube texture packs',
                                     epilog=f'Supported MC versions: {",".join(converter.SUPPORTED)}')
    parser.add_argument('input', metavar='path',
                        help='Path to input .zip file')
    parser.add_argument('-o', '--output', metavar='path',
                        help='Output path of zip, defaults to [input].cc.zip')
    parser.add_argument('-O', '--overwrite', action='store_true',
                        help='Overwrite output file if it already exists')

    args = parser.parse_args()
    if not args.output:
        args.output = args.input.rstrip('.zip') + '.cc.zip'

    if os.path.exists(args.output) and not args.overwrite:
        print('A file alreay exist with this output name. To overwrite it, add -O/--overwrite to arguments.')
        exit(1)

    converter.convert(args.input, args.output)


if __name__ == "__main__":
    main()
