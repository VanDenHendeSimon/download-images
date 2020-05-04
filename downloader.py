import requests
import sys
import os
import time


def create_dir(args):
    dirname = os.path.join(os.path.dirname(args[0]), 'images')

    if not os.path.exists(dirname):
        # Create directory if this is necessary
        os.makedirs(dirname)
    else:
        # Remove contents
        [os.remove(os.path.join(dirname, f)) for f in os.listdir(dirname)]

    return dirname


def fetch_images(filepath, amount):
    print("Starting the download of %d pictures" % amount)

    for i in range(1, amount+1):
        fp = os.path.join(filepath, 'image-%s.jpg' % i)
        with open(fp, 'wb') as f:
            f.write(requests.get(
                'https://thispersondoesnotexist.com/image',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
            ).content)

        print("\tDownloaded image %d/%d" % (i, amount))
        time.sleep(2)


def main():
    args = sys.argv

    try:
        amount = int(args[1])
    except Exception:
        amount = 1

    directory = create_dir(args)
    fetch_images(directory, amount)


if __name__ == '__main__':
    main()
