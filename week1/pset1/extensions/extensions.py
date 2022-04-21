filename = input("File name: ").strip().lower()
filename = filename.split(".")

extensions = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "other": "application/octet-stream"
}

stop = False

for key in extensions.keys():
    if filename[-1] == key:
        print(extensions[key])
        stop = True
        break

if stop == False:
    print(extensions["other"])

