from PIL import Image
import numpy as np
import os


def rec_search_crop(start_url):
    """"search all sub folders of the start folder for folders containing png data in a animation folder and crop
    them """

    content = [os.path.join(start_url, o) for o in os.listdir(start_url)]
    for c in content:
        if c.endswith('animation'):
            print('cropping {}'.format(c))
            crop_all(c)
        elif os.path.isdir(c):
            rec_search_crop(c)


def crop_all(url):
    """crop all images in url and save them in a new made folder"""

    imgs = [o for o in os.listdir(url) if o.endswith('.png')]
    print('Imgs ' + str(imgs))
    newpath = '{}\\cropped'.format(url)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for img in imgs:
        crop(os.path.join(url, img)).save('{}\\crpd_{}'.format(newpath, img))


def crop(url):
    """crops everything unnecessary from an image away"""

    image = Image.open(url)
    image.load()

    image_data = np.asarray(image)
    image_data_bw = image_data.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0) > 0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1) > 0)[0]
    cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

    image_data_new = image_data[cropBox[0]:cropBox[1] + 1, cropBox[2]:cropBox[3] + 1, :]

    return Image.fromarray(image_data_new)


if __name__ == '__main__':
    base_url = '.'  # TODO change appropiatly
    rec_search_crop(base_url)
