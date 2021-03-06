import os
import uuid
import sys

from to_plaintext import to_plaintext


def getDestFilename(dest, file):
    destFileName = "{}/{}.txt".format(dest, file)
    if os.path.exists(destFileName):
        destFileName = "{}/{}-{}.txt".format(dest, file, str(uuid.uuid4()))
    print("Dest File Name: ", destFileName)
    return destFileName


def valid(file):
    whitelist = [
        ".csv", ".doc", ".docx", ".eml",
        ".epub", ".gif", ".htm", ".html",
        ".jpeg", ".jpg", ".json", ".log",
        ".mp3", ".msg", ".odt", ".ogg", ".pdf",
        ".png", ".pptx", ".ps", ".psv", ".rtf",
        ".tff", ".tif", ".tiff", ".tsv", ".txt",
        ".wav", ".xls", ".xlsx"
    ]
    _, file_extension = os.path.splitext(file)
    return file_extension in whitelist


if __name__ == "__main__":
    source = sys.argv[1]
    dest = sys.argv[2]
    for root, dirs, files in os.walk(source):
        path = root.split(os.sep)

        for file in files:
            print("File: ", file)

            if not valid(file):
                continue

            full_file_name = root + "/" + file

            try:
                text = to_plaintext(full_file_name)
            except:
                logfile = open("errors.log", "a")
                logfile.write("Couldn't convert file: {}\n\r".format(full_file_name))
                logfile.close()

            destFileName = getDestFilename(dest, file)
            destFile = open(destFileName, "wb")
            destFile.write(text)
            destFile.close()
