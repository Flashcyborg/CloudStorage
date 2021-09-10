import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AzUSW6-jHB7x09OucUBqaADAteTbUHOhDmJN_zCquCYcWgLoaatlzvFALpnrs6Pdz-wDTMdJeEkSyMMxSdQL6WXBn1wG32Y28bfUSzB_ccpAsSA7q41v2NLhqB19cGDGzs51fiz6IGI'
    transferData = TransferData(access_token)

    file_from = input("Enter the File name you want to Upload.")
    file_to = '/MyFirstApp/minecraft4.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()