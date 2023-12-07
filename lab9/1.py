def create_file():
    try:
        with open("TF19_1.txt", "w") as file:
            file.write("Hello world!\n")
            file.write("Python is awesome\n")
            file.write("A B C D E F\n")
            file.write("123 45 6789\n")
            file.write("SingleLetterWords: a b c d e\n")
    except:
        print("Помилка при створенні файлу TF19_1.txt!")

def process_file():
    try:
        with open("TF19_1.txt", "r") as file_in, open("TF19_2.txt", "w") as file_out:
            for line in file_in:
                words = line.split()
                filtered_words = [word.strip() for word in words if len(word) > 1]
                if filtered_words:
                    new_line = " ".join(filtered_words) + "\n"
                    file_out.write(new_line)
    except:
        print('Файла TF19_2.txt не існує!')

def print_file():
    try:
        with open("TF19_2.txt", "r") as file_in:
            for line in file_in:
                print(line.strip())
    except:
        print('Файла TF19_2.txt не існує!')

#create_file()
#process_file()
print_file()