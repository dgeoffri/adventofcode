#!/usr/bin/env python3

class NSFODException(Exception):
    pass


class File:
    def __init__(self, filename, size):
        self.filename = filename
        self.size = size

    def __repr__(self):
        return f"{self.size} {self.filename}"


class Dir:
    def __init__(self, dirname, parent=None):
        self.dirname = dirname
        self.files = []
        self.dirs = {}
        self.parent = parent

    def __repr__(self):
        return f"dir {self.dirname}"

    @property
    def size(self):
        return sum(file.size for file in self.files) + sum(self.dirs[dir].size for dir in self.dirs)


class Disk:
    def __init__(self):
        self.rootdir = Dir("/")
        self.cwd = self.rootdir

    def cd(self, dirname):
        if dirname == "/":
            self.cwd = self.rootdir
        elif dirname == ".." and self.cwd.parent:
            self.cwd = self.cwd.parent
        else:
            try:
                self.cwd = self.cwd.dirs[dirname]
            except KeyError as e:
                raise NSFODException from e

    def ls(self):
        print("\n".join([f"{dir}" for dir in self.cwd.dirs] + [f"{file}" for file in self.cwd.files]))

    def touch(self, filename, size=0):
        self.cwd.files.append(File(filename, size))

    def mkdir(self, dirname):
        self.cwd.dirs[dirname] = Dir(dirname, self.cwd)

    def du(self, startdir=None):
        if startdir == None:
            startdir = self.rootdir
        yield (startdir.dirname, startdir.size)
        for dir in startdir.dirs.values():
            for innerdir in self.du(dir):
                yield innerdir


class Computer:
    def __init__(self):
        self.disk = Disk()

    def handle_input(self, data):
        for line in data:
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    self.disk.cd(line[2])
            elif line[0] == "dir":
                self.disk.mkdir(line[1])
            else:
                self.disk.touch(line[1], int(line[0]))


if __name__ == "__main__":
    with open("day07.txt", "r") as f:
        data = f.read().splitlines()
    c = Computer()
    c.handle_input(data)
    print(f"Answer is {sum(size for name, size in c.disk.du())}.")
