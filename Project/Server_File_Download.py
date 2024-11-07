import ftplib
import os


def download_file(ftp_server, username, password, remote_file_path, local_file_path):
    # Connect to the FTP server
    ftp = ftplib.FTP(ftp_server)
    ftp.login(user=username, passwd=password)

    # Change to the remote directory
    remote_dir, remote_file_name = os.path.split(remote_file_path)
    ftp.cwd(remote_dir)

    # Download the file to the local system
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary(f'RETR {remote_file_name}', local_file.write)

    print(f"File '{remote_file_name}' downloaded successfully to '{local_file_path}'")

    # Close the FTP connection
    ftp.quit()

# Example usage
ftp_server = 'easyrewardzftp.ercx.co'
username = 'datatransfer'
password = 'jpzur2x'
remote_file_path = '/Prakhar/txn.csv'  # Path to the remote file
local_file_path = 'file/txn.csv'  # Local path to save the file

download_file(ftp_server, username, password, remote_file_path, local_file_path)
