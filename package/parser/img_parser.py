from io import StringIO
from package.parser.base_parser import BaseParser


class ImgParser(BaseParser):

    _identifier = "img"

    def __init__(self, input: str, start: int) -> None:
        super().__init__(input, start)




    def parse(self) -> str:
        src = self.arguments.get("src")
        alt = self.arguments.get("alt")

        cls = "image_centered"

        output = StringIO()
        output.write(f"<div class={cls}>")
        output.write(f"<img src='{src}' alt='{alt}'>")
        output.write("<p>")
        output.write(super().parse())
        output.write("</p>")
        output.write("</div>")
        return output.getvalue()


BaseParser.parsers.append(ImgParser)