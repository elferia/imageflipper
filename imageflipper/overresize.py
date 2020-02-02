from argparse import ArgumentParser
from dataclasses import dataclass
from math import ceil

from PIL import Image


def run() -> None:
    parser = ArgumentParser()
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('images', nargs='+')
    args = parser.parse_args()

    resizer = OverResizer(args.width, args.height)
    for filepath in args.images:
        resizer.resize(filepath)


@dataclass
class OverResizer:
    width: int
    height: int

    def resize(self, filepath: str) -> None:
        im = Image.open(filepath)

        new_width = self.width
        ratio = new_width / im.size[0]
        new_height = ceil(im.size[1] * ratio)
        if new_height < self.height:
            new_height = self.height
            ratio = self.height / im.size[1]
            new_width = ceil(im.size[0] * ratio)
            assert new_width >= self.width

        out = im.resize((new_width, new_height), Image.LANCZOS, reducing_gap=3)

        outpath_base, extension = filepath.rsplit('.', maxsplit=1)
        outpath = f'{outpath_base}-resized.{extension}'
        out.save(outpath)
