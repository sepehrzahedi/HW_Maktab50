# hello
# myname is
# sepehr zahedi
# Maktab50

def line_counter(file_name):
    my_input = open(file_name, "r")
    return my_input


count_line = line_counter("sepehr.txt").read().splitlines()
print("count_line : ", len(count_line))
word_count = 0
char_count = 0

for line in line_counter("sepehr.txt").read().split():
    word_count += 1
    char_count += len(line)
print("char_count :", char_count)
print("word_count :", word_count)


line_counter("sepehr.txt").close()
