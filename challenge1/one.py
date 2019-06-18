def count_dictionary(string):
    string_sort = sorted(string)
    output_dictionary = {}
    for i in range(0,len(string_sort)):
        output_dictionary[string_sort[i]] = string_sort.count(string_sort[i])
    return output_dictionary

def count_sum(string):
    output=""
    verifier = ""
    until = len(string)

    for index in range(0,until):
        if index==0:
            verifier += string[index]
            continue 
        elif string[index] != string[index - 1]:
            output += str(verifier.count(string[index -1 ]))
            output += string[index -1]
            verifier = ""
        verifier += string[index]
    output += str(verifier.count(string[index]))
    output += string[index]
    return str(output)

    