from utility import ReadFiles

name = input('Insert Name     : ')
number = input('Insert Numstart : ')
print('Extension'
      '\n1. jpg'
      '\n2. mp4')
method = int(input('Insert extension: '))
if method == 1:
    ext = 'jpg'
elif method == 2:
    ext = 'mp4'
scan = ReadFiles(name, ext, number)
scan.all_rename()