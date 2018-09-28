import tempfile
import os


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pos = 0
        try:
            with open(self.file_path, 'r') as f:
                self.lines_count = len(f.readlines())
        except IOError:
            self.lines_count = 0
            with open(self.file_path, 'w') as f:
                f.write('')

    def __str__(self):
        return self.file_path

    def write(self, text):
        self.text = text
        with open(self.file_path, 'w') as f:
            f.write(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos < self.lines_count:
            with open(self.file_path, 'r') as f:
                lines = f.readlines()
            line = lines[self.pos]
            self.pos += 1
            return line
        else:
            raise StopIteration

    def __add__(self, obj):
        tmp_dir = tempfile.gettempdir()
        new_obj = File(os.path.join(tmp_dir, "third.txt"))
        with open(new_obj.file_path, 'w') as f:
            f.write(self.text + obj.text)
        return new_obj


# obj1 = File("/tmp/file4.txt")
# obj2 = File("/tmp/file5.txt")
# obj1.write("first\n")
# obj2.write("second\n")
# obj3 = obj1 + obj2
# print(obj3)
# for line in File("/tmp/third.txt"):
#     print(line)