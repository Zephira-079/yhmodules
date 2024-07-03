# MaidCat: A Personal YouTube Downloader

MaidCat is a command-line tool designed for downloading YouTube videos easily, either from a single URL or from multiple URLs listed in a text file.

## Requirements

Before running MaidCat, ensure you have the following Python packages installed:

```bash
pip install pytube
pip install argparse
pip install pyinstaller
```
# Usage
### Command Line Arguments
<p>MaidCat supports the following command-line arguments:</p>
<li> url: YouTube URL to download a single video. </li>
<li> -m FILE, --multiple FILE: File containing multiple YouTube URLs to download. </li>
<li> -p PATH, --path PATH: Specify the download folder path. Defaults to the current directory (./). </li>

```cmd
python maidcat.py <YouTube_URL>
python maidcat.py -m <file.txt>
python maidcat.py <YouTube_URL> -p <download_folder_path>
```
