courseName = "Introduction to Programming Logic"
print(courseName[16:27])
courseList = ['COP 1500', 'COP 2006', 'COP 3003']
copyList = courseList[1:2]
print(copyList)
word = "hat"
word_list = ['h','a', 't']
word_list[0] = 'c'


def convert_list_string(a_list):
    string_list = ''
    for x in a_list:
        string_list += x
    return string_list


print(word_list)
word_list = convert_list_string(word_list)
print("it works", word_list)
