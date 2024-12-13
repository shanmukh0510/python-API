import shutil

src = r"C:\Users\shanm\Downloads\sample-xls-files-sample1.xls"

des = r"C:\Users\shanm\sample_project1\PythonAPI"

try:
    shutil.copy(src, des)
    print("file copied")

except:
    print("not exist")
