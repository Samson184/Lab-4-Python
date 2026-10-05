def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

# Частина а) Створення текстового файлу TF1_1.txt із рядків різної довжини зі словами та розділовими знаками
file1_name = "TF1_1.txt"
file_1_w = Open(file1_name, "w")

if file_1_w != None:
    file_1_w.write("Hello, world! This is a test string, designed for practical work number 4. Let's check how it works, student!")
    print("Information was successfully added to TF1_1.txt!")
    file_1_w.close()
    print("File TF1_1.txt was closed!")
