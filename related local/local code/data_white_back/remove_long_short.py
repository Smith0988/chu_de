# Đọc từ file và lọc câu
input_file_path = 'sentence_used.txt'
output_file_path = 'filtered_sentences.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        # Loại bỏ dấu cách và kiểm tra số từ
        words = line.strip().split()
        if 4 <= len(words) <= 10:
            output_file.write(line)

print("Xong! Các câu đã được lọc và ghi vào file", output_file_path)
