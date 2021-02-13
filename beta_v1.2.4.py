print("You have 1 submission on this account:")
print("1. Developer Mode: Type '/download developer_mode' to install your application.")
print("Infomation about this user:")
print("Member since 6 October, 2020")
installation = input()
if installation == "/download developer_mode":
    for downloading in range(0, 1 + 1, 1):
        if downloading == 0:
            for ProgramSizeLeftToDownload in range(0, 19722 + 1, 1):
                print("Downloading Developer Mode. Downloaded " + str(ProgramSizeLeftToDownload) + "/ 19722 Bytes.")
        else:
            print("You have downloaded 'Developer Mode'.")
            print("Type '/script python.beta-testing.miscellaneous.release_v1.2.1' or '/script' to activate 'Developer Mode'")
else:
    print("Invalid Input")