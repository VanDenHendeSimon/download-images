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

    last_image = None
    i = 1
    while i <= amount:
        response = requests.get(
                'https://thispersondoesnotexist.com/image',
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
            ).content

        # If the response is not equal to the last (=> Not the same image again)
        if response != last_image:
            # Save the file
            fp = os.path.join(filepath, 'image-%s.jpg' % i)
            with open(fp, 'wb') as f:
                f.write(response)

            # Feedback
            print("\tDownloaded image %d/%d" % (i, amount))

            # Next iteration
            i += 1
            last_image = response


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
