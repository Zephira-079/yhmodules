import argparse
from pytube import YouTube
import os

def download_video(url, dl_folder):
    try:
        yt = YouTube(url)
        print(f'Downloading {yt.title}...')
        yt.streams.get_highest_resolution().download(dl_folder)
        print(f'Finished downloading {yt.title}.\n')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

def download_videos_from_file(file_path, dl_folder):
    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                download_video(url, dl_folder)

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument('urls', nargs='*', help='YouTube URLs', metavar='URL')
    parser.add_argument('-m', '--multiple', help='File containing multiple YouTube URLs')
    parser.add_argument('-p', '--path', default='./', help='Download folder path')

    args = parser.parse_args()

    if args.urls:
        for url in args.urls:
            download_video(url, args.path)
    elif args.multiple:
        download_videos_from_file(args.multiple, args.path)
    else:
        print("Please provide at least one YouTube URL or a file containing URLs.")

if __name__ == "__main__":
    main()
