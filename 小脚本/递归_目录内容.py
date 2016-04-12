def print_directory_content(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_content(sChildPath)
        else:
            print(sChildPath)
