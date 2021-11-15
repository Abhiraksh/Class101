import dropbox

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def uploadData(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom, "rb")
        dbx.files_upload(f.read(), fileTo)

def main():
    #access_token = "sl.A8OFZTNtoDWrcNctGU2AQ_-DGtIDTsqRuRV57PTzdptX-1-6w4swSHq7Pc7FAxfQ1xAFkA_LJXdeQV9DHNTLBN93Ko13klG2Di-02yOD0SKUWI025Yyc6aGhkhXQkGo3_6PgRyg"
    access_token = "nhLPwfTl73MAAAAAAAAAAfPh9EzQJbdionSBcIEDPIgvQd2MNrTha_3eXbcQZ2Ox"
    #access_token = "sl.A8MaKHa9vb7YS1EQMxSXeKENhQPq1VdTjO8PFXloKtjRoG4WW1nmsiIx4cv0p5Mf_BpCOyaWzbp-wUAM6bEWVcJ-M2M5hpbVS4BynO8zQN64-a6QCkuvxaHadHRTO7rAzggiB8ST5yvL"
    transferData = TransferData(access_token)
    fileFrom = input("Enter a file path to transfer: ")
    fileTo = input("Enter the full path to upload to dropbox: ")

    transferData.uploadData(fileFrom, fileTo)
    print("Your files have been transfered")

main()