import argparse
import logging

class FontDownloader:

    def __init__(self, fontname):
        self.fontname = fontname

    def download(self):
        logger = logging.getLogger("Downloader")
        logger.info(f"Downloading font: {self.fontname}")

    def save(self):
        pass

def main():
    logger = logging.getLogger("main")
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Starting FontDownloader')
    parser = argparse.ArgumentParser(description='FontDownloader')
    parser.add_argument("fontname", help="Font name, as stated on google fonts, use double quotes \"")
    parser.add_argument("--output", help="Output directory")
    args = parser.parse_args()
    downloader = FontDownloader(args.fontname)
    downloader.download()



if __name__ == "__main__":
    main()
