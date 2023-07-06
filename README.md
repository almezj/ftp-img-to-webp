# FTP Image Downloader and Converter

This script allows you to download all image files from a specified FTP directory and convert them to the webp format. 

## Features

- Downloads image files from a specified FTP directory
- Converts downloaded images to webp format
- Removes original images after conversion

## Usage

```
python download_files('ftp.host.com', 'user', 'pass', '/remote/dir', '/local/dir')
```

## Parameters

- `host` (str): FTP host
- `user` (str): FTP user
- `passw` (str): FTP password
- `rem_dir` (str): FTP remote directory
- `loc_dir` (str): Local directory to save files
-  (Optional) `accepted_image_formats` (list): List of image formats to download (default: ['.jpg', '.jpeg', '.png', '.gif'])

## Customization

You can define your own logic to determine if a file has no webp version. For this example, we use file numbers, which are in the format: item_XXXXX.jpg. 

Alternatively, you can return True if you want to download all files.

## Dependencies

- Python's built-in `ftplib` and `os` modules
- ImageMagick's `convert` command-line tool

## Installation

1. Ensure you have Python installed on your machine.
2. Install ImageMagick on your machine. You can find the installation instructions [here](https://imagemagick.org/script/download.php).
3. Clone this repository to your local machine.
4. Update the `HOST`, `USER`, `PASSW`, `REM_DIR`, and `LOC_DIR` variables in the script with your FTP details and directories.

## Running the Script

1. Navigate to the directory containing the script.
2. Run the script using the command `python ftp-img-to-webp.py`.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
