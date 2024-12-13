from datetime import datetime

current_date = datetime.now().strftime('%y-%m-%d')
print(current_date)

with open('file1.txt','w') as file1:
    file1.write(f'This is the content of file 1.\nDate: {current_date}')

with open('file2.txt','w') as file2:
    file2.write(f'This is the content of file 2.\nDate: {current_date}')
print("Files created and data written successfully with the date.")

with open("file1.txt",'r') as file1:
    content1 = file1.read()

with open('file2.txt','r') as file2:
    content2 = file2.read()


with open('final_file.txt','w') as final_file:
    if content1 == content2:
        final_file.write("The files are identical.\n")

    else:
        final_file.write("files are different.\n")
        final_file.write("\n---content of file1.txt---\n")
        final_file.write(content1)
        final_file.write("\n---content of file2.txt----\n")
        final_file.write(content2)

with open("final_file.txt",'r') as final_file:
    content = final_file.read()
    print(content)
