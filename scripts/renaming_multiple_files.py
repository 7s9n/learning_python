import os

#chapter12-array-single-dimension.pdf
#12-array single dimension.pdf

def extract_num(s):
    num = ''.join([c if c.isdigit() else '' for c in s])
    return num


if __name__ == '__main__':
    os.chdir('C:/Users/Hussein Sarea/Desktop/Course c++')

    for f in os.listdir():
        file_name , ext = os.path.splitext(f)
        file_number = extract_num(file_name.split('-')[0]).zfill(2)
        file_name = ' '.join(file_name.split('-')[1:]).strip()

        new_name = f'{file_number}-{file_name}{ext}'

        os.rename(f , new_name)
