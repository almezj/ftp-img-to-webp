from ftplib import FTP
import os


def download_files(host: str, user: str, passw: str, rem_dir: str, loc_dir: str, accepted_image_formats: list=None) -> bool :

    """
    Download files that do not have webp version

    Args:
        host (str): FTP host
        user (str): FTP user
        passw (str): FTP password
        rem_dir (str): FTP remote directory
        loc_dir (str): Local directory to save files
        accepted_image_formats (list): List of image formats to download (default: ['.jpg', '.jpeg', '.png', '.gif'])

    
    Example usgage: download_files('ftp.host.com', 'user', 'pass', '/remote/dir', '/local/dir')
    """

    ftp = FTP(host)
    ftp.login(user, passw)
    ftp.cwd(rem_dir)

    if (accepted_image_formats is None):
        accepted_image_formats = ['.jpg', '.jpeg', '.png', '.gif']

    files = ftp.nlst()
    for file in files:
        if os.path.splitext(file)[1] in accepted_image_formats:
            if has_no_webp(file):
                local_file = f"{loc_dir}/{file}"
                with open(local_file, 'wb') as fp:
                    ftp.retrbinary(f'RETR {file}', fp.write)
                    print(f"Downloaded {file}")

    # Convert files to webp
    for file in os.listdir(loc_dir):
        os.system(f"convert {loc_dir}/{file} -quality 80 -define webp:lossless=false {loc_dir}/{file.split('.')[0]}.webp")
        print(f"Converted {file}")
        os.remove(f"{loc_dir}/{file}")
        print(f"Removed {file}")

    ftp.quit()
    print("Done, files changed: " + str(len(files)))
    return True


def has_no_webp(file):
    """
    Define your own logic to determine if file has no webp version.
    (e.g. range of file numbers, file name pattern, etc.)
    For this example, we will use file numbers, which are in the format: item_XXXXX.jpg
    
    Alternatively, you can return True if you want to download all files.

    Args:
        file (str): File name

    Returns:
        bool: True if file has no webp version
    """
    filename = str(file.split('.')[0])
    filenumber = int(filename.split('_')[1])
    if 22724 <= filenumber <= 23694:
        return True
    return False


if __name__ == "__main__":
    HOST = 'FTP_HOST' # e.g. 'ftp.host.com'
    USER = 'FTP_USER' # e.g. 'user'
    PASSW = 'FTP_PASS' # e.g. 'pass
    REM_DIR = 'Remote directory to download files' # e.g. '/remote/dir/images'
    LOC_DIR = 'Local directory to save files' # e.g. '/local/dir/images'
    # (Optional) IMAGE_FORMATS = ['.jpg', '.jpeg']
    
    # Run the function
    download_files(HOST, USER, PASSW, REM_DIR, LOC_DIR)
