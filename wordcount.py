# put your code here.
def word_count(filename):
    the_file = open(filename)
    
    word_list = []
    count_dict = {}
    

    for line in the_file:
        line = line.rstrip()
        words = line.split(' ')
        word_list.extend(words)
    
    

    the_file.close()
    

word_count("test.txt")



