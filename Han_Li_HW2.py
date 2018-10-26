def List_Dictionary(x = input("Enter the file name:")):
    
    f = open(x, 'r')
    object_file = f.read()
    object_file_lower = object_file.lower()
    object_file_lower_split = object_file_lower.split('\n') #remove the space between each line, and each line only contains string

    
    word = []
    for row in object_file_lower_split: #divide each line into single words, word is a list of list 
        row = row.split()
        word.append(row)
        
    punctuation = ['?', '.' , ';', '!' , ':' , ',']
    single_word_index = [] # take each elements in the list of list, and store it into a new list named single_word_index
    for line in word:
        if line == [""]:
            del line
            continue
        for index in range(len(line)):
                if line[index] == "": #skip the empty element
                    continue
                for s in line[index]: #remove punctuation marks
                    if s in punctuation:
                        line[index] = line[index].replace(s, "")
                single_word_index.append(line[index])
    
    word_dict = {} #build the dict for each single word, the position of the word is (index + 1)
    for index in range(len(single_word_index)):
        if single_word_index[index] not in word_dict:
            word_dict[single_word_index[index]] = [index + 1]
        else:
            word_dict[single_word_index[index]] += [index + 1]
    
    keylist = word_dict.keys()
    keylist = sorted(keylist)
    for key in keylist:
        print("%s: %s" % (key, word_dict[key]))
        
    

List_Dictionary()