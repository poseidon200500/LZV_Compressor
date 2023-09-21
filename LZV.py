# export PROMPT_DIRTRIM=1
string = "aaabcbbacbcabccbbacbcabcbcbbacbcabccbbacb"
codes = {}
alphabet = "0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ" #36-ая система

def to_36(num):
    output = ""
    while num != 0:
        print(num%36,alphabet[num%36])
        output += alphabet[num%36-1]
        num //= 36
    return output[::-1]

def from_36(string):
    string = string[::-1]
    otv = 0
    for ind,sym in enumerate(string):
        otv += (alphabet.find(sym)+1) * (36**ind)
    return otv

def new_check(string,ind):
    now_string = ""
    ind2 = ind
    while ind2 != len(string):
        now_string += string[ind]
        if codes.get(now_string) == None:
            codes_len += 1
            codes[now_string] = to_36(codes_len)
            if now_string != "":
                string = string[:ind]+codes[now_string] + string[ind2-1:]
            
        ind2+=1

    return ind,ind2 


def main():
    codes = {}
    ind = 0
    dict_len = 0
    while ind != len(string):
        
        
            
    pass
if __name__ == "__main__":
    main()