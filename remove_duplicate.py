def remove_duplicate_lines(input_file, output_file):
    # Mở file đầu vào để đọc
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Loại bỏ các dòng trùng lặp
    unique_lines = list(set(lines))

    # Mở file đầu ra để ghi
    with open(output_file, 'w') as file:
        # Ghi các dòng không trùng lặp vào file mới
        file.writelines(unique_lines)

# Thực hiện loại bỏ dòng trùng lặp từ file text.txt và ghi vào file mới unique_text.txt
remove_duplicate_lines('Text.txt', 'unique_text.txt')
