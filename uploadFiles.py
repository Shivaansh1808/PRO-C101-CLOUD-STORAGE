import dropbox
import os

class TransferData():
    
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), file_to)

#not able to do it :(
"""        for root, dirs, files in os.walk(file_from):
            for filename in files:
                    # making full local path
                local_path = os.path.join(root, filename)
                    # making full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))"""

def main():
    access_token = "***************************************"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the upload path in dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File Has Been Uploaded")

main()
