def fl(file="file.txt"):
    f=open(file,"+at")
    f.writelines(["roll no : 31","\nName : Faizan","\nclass : Sycoa"])
    print("Reading the file ....\n")
    f.seek(0)
    try:
        print(f.readlines())
    except(FileNotFoundError):
        print("the file not yet created...")
    except Exception :
        print(Exception)
fl()