# https://dev.to/aldo/implementing-logging-in-python-via-decorators-1gje
# from zipfile import ZipFile , ZIP_DEFLATED , Path
# import shutil
# import os
# with ZipFile('files.zip' , 'w' , compression=ZIP_DEFLATED) as myzip:
#     myzip.write('../files.py' , arcname='files.py')
#     myzip.write('../sets.py' , arcname='sets.py')

# with ZipFile('files.zip' , 'r') as myzip:
#     # print(myzip.namelist())
#     myzip.extractall('files')

# with ZipFile('files.zip' , 'r') as myzip:
#     myzip.extract('../sets.py','files')

# shutil.make_archive('../files' , 'zip' , '.')#shutil.make_archive(output_filename, 'zip', dir_name)

# shutil.unpack_archive('../files.zip' , 'files')

# def zipdir(folder , zip , test=None):
#     test = test if callable(test) else lambda x: True
#     for root , dirs , files in os.walk(folder):
#         for file in files:
#             if test(file):
#                 file_path = os.path.join(root , file)
#                 zip.write(file_path , arcname=file)

# def zipdir(folder , zip):
#     for root , dirs , files , in os.walk(folder):
#         if root.replace(folder,'') == '':
#             prefix = ''
#         else:
#             prefix = root.replace(folder, '')
#         for file in files:
#             actual_file_path = os.path.join(root , file)
#             zipped_file_path = os.path.join(prefix , file)
#             zip.write( actual_file_path, zipped_file_path )
from __future__ import absolute_import
from pathlib import Path
from struct import unpack
marker_mapping = {
    0xffd8: "Start of Image",
    0xffe0: "Application Default Header",
    0xffdb: "Quantization Table",
    0xffc0: "Start of Frame",
    0xffc4: "Define Huffman Table",
    0xffda: "Start of Scan",
    0xffd9: "End of Image"
}
class JPEG:
    def __init__(self , image_file):
        with image_file.open('rb') as f:
            self.image_data = f.read()
    def decodeHuffman(self, data):
        offset = 0
        header, = unpack("B",data[offset:offset+1])
        offset += 1

        # Extract the 16 bytes containing length data
        lengths = unpack("BBBBBBBBBBBBBBBB", data[offset:offset+16])
        offset += 16

        # Extract the elements after the initial 16 bytes
        elements = []
        for i in lengths:
            elements += (unpack("B"*i, data[offset:offset+i]))
            offset += i

        print("Header: ",header)
        print("lengths: ", lengths)
        print("Elements: ", len(elements))
        data = data[offset:]
    def decode(self):
        data = self.image_data
        while(True):
            marker , = unpack( '>H' , data[:2] )
            print( marker_mapping.get(marker) )

            if marker == 0xffd8:
                data = data[2:]
            elif marker == 0xffd9:
                break
            elif marker == 0xffda:
                data = data[-2:]
            else:
                lenchunk, = unpack(">H", data[2:4])
                lenchunk += 2
                chunk = data[4:lenchunk]
                if marker == 0xffc4:
                    self.decodeHuffman(chunk)
                data = data[lenchunk:]
            if len(data)==0:
                break


# ImageDownloader - Muhammed Shokr its amazing

# USAGE
# Change the URL from where you have to download the image

if __name__ == '__main__':
    # from pathlib import Path

    # img_path = Path('C:/Users/Hussein Sarea/Desktop') / 'husseinsarea1.jpg'
    # img = JPEG(img_path)
    # img.decode()
    from os import path

    dir = path.dirname(__file__)
    others_dir = path.join(dir , 'others')
    print(others_dir)
    # import os
    # import scripts
    # import pickle
    # from scripts.password_generator import Password
    # s = sum( [1 , 2 , 3 , 4 , 5] )
    # print(s)
    # eval()
    # from ...scripts import password_generator
    # print()
    from chardet import *

    pass
    # with ZipFile('zipped.zip' , 'w' , compression=ZIP_DEFLATED) as zip:
    #     zipdir('C:/Users/Hussein Sarea/Desktop/garbage' , zip)
        # shutil.make_archive('zipped' , 'zip' , '../../data_structures')
