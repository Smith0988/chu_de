# Mở file input.txt trong chế độ đọc
with open('text.txt', 'r') as input_file:
    # Đọc từng dòng trong file
    lines_to_write = [line.strip() for line in input_file if len(line.strip()) < 50]

# Mở hoặc tạo file output.txt trong chế độ ghi
with open('output.txt', 'w') as output_file:
    # Ghi các câu có số ký tự ít hơn 39 vào file output.txt
    for line in lines_to_write:
        output_file.write(line + '\n')
