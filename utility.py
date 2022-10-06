import os
import pathlib


class ReadFiles:
    def __init__(self, path, filename, ext, numstart):
        self.filename = filename
        self.numstart = numstart
        self.path = path
        self.ext = ext

    def all_rename(self):
        # Change Directory
        sel_path = pathlib.Path(self.path)
        os.chdir(sel_path)
        print("Current working directory: {0}".format(os.getcwd()))
        # Num parameter
        num = int(self.numstart)

        for files in os.listdir():
            # Split filename and the extension
            f_name, f_ext = os.path.splitext(files)
            print('Name origins: ' + f_name + f_ext)

            # Processing...
            f_name = self.filename
            f_ext = self.ext
            f_num = str(num).zfill(2)

            # New name format
            f_rename = ('{} {}{}'.format(f_name, f_num, f_ext))
            os.rename(files, f_rename)
            print('Name after  : ' + f_rename)

            # Increment of num
            num += 1
        print('All data successfully renamed!')