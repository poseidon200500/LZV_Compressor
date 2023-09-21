# export PROMPT_DIRTRIM=1
string = "aaabcbbacbcabccbbacbcabcbcbbacbcabccbbacb"
codes = {}
alphabet = "0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ" #36-ая система
special = " |&,./\\!?*^%$#@();:'\"<>`~"

def to_36(num):
    output = ""
    while num >= 36:
        #print(num%36,alphabet[num%36])
        output += alphabet[num%36-1]
        num //= 36
    output += alphabet[num]
    return output[::-1]

def from_36(string):
    string = string[::-1]
    otv = 0
    for ind,sym in enumerate(string):
        otv += (alphabet.find(sym)+1) * (36**ind)
    return otv

def code_string(string,ind,codes):
    now_string = ""
    ind2 = ind
    while ind2 < len(string):
        if string[ind2] in special:
            break
        else:
            now_string += string[ind2]
            if len(now_string) > 2 and codes.get(now_string) == None: #если подстроки нет в словаре
                codes[now_string] = to_36(len(codes)+1)
                break
        ind2+=1

    
    if len(now_string) > 3:
        new_string = codes[now_string[:-1]]
        otv = string[:ind]+"|"+new_string +"|"+string[(ind+len(now_string)+1):]
    else:
        otv = string
    return otv,ind+len(now_string)

def decode_string(strign,ind,codes):
    now_string = ""
    ind2 = ind
    while ind2 < len(string):
        if string[ind2] in special:
            break
        else:
            now_string += string[ind2]
            if len(now_string) > 2 and codes.get(now_string) == None: #если подстроки нет в словаре
                codes[now_string] = to_36(len(codes)+1)
                break
        ind2+=1

    
    otv = string
    return otv,ind+len(now_string)


def coder(): 
    codes = {}
    new_file = open("coded_file","w")
    with open("test_file.txt","r") as file:
        while string := file.readline():
            ind = 0
            while ind < len(string)-3:
                string,ind = code_string(string,ind,codes)
            new_file.write(string)
            if string != '' and string[-1] != '\n':
                new_file.write('\n')
            #print(string)

    print(codes)
    new_file.close()


def decoder():
    codes = {}
    new_file = open("decoded_file","w")
    with open("coded_file.txt","r") as file:
        while string := file.readline():
            ind = 0
            while ind < len(string)-3:
                string,ind = new_check(string,ind,codes)
            new_file.write(string)
            if string != '' and string[-1] != '\n':
                new_file.write('\n')
            #print(string)

    print(codes)
    new_file.close()


def main():
    print("Выберите режим работы")
    mod = int(input())
    if mod == 1:
        coder()
    elif mod == 2:
        decoder()
    else:
        print("Wrong code")

if __name__ == "__main__":
    main()