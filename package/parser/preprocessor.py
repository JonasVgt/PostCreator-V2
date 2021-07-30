import re

class Preprocessor:

    @classmethod
    def process(cls,input:str) -> str:
        processed = input.replace('\n',' ')
        processed = re.sub(r' +', ' ', processed)
        processed = re.sub(r'^ ', '', processed)
        processed = re.sub(r' ?$', ' ', processed)
        return processed
