import os

files = [path for sub in [[os.path.join(w[0], file) for file in w[2]] for w in os.walk('.')] for path in sub]
folders = [path[0] for path in os.walk('.')]
for folder in folders:
    #SendFolder(client, folder)
    print("folder: " + folder)
for file in files:
    #SendFile(client, file)
    print("file: " + file)
