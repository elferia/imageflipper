from argparse import ArgumentParser

from PIL import Image


def run() -> None:
    parser = ArgumentParser()
    parser.add_argument('images', nargs='+')
    args = parser.parse_args()

    for filepath in args.images:
        flip_image(filepath)


def flip_image(filepath: str) -> None:
    im = Image.open(filepath)
    out = im.transpose(Image.FLIP_LEFT_RIGHT)

    outpath_base, extension = filepath.rsplit('.', maxsplit=1)
    outpath = f'{outpath_base}-flipped.{extension}'
    out.save(outpath)
