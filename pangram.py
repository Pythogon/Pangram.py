import time
blacklist = ''' !?:;"'.()[]{}-+_=~#/\,<>@|¬`'''
whitelist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    sentencebackup = input('Input the sentence for the pangram checker.').lower()
    sentence = sentencebackup.translate({ord(i): None for i in blacklist})
    # print(sentence) # Debug
    arr = list()
    for x in range(len(whitelist)):
        a = whitelist[x]
        if sentence.replace(a, '', 1) != sentence:
            arr.append(a)
        else:
            break
        print(a.upper(), 'filter active.')
    # print(arr) # Debug
    arr = ''.join(arr)
    print({'abcdefghijklmnopqrstuvwxyz':'Your sentence is a pangram.'}.get(arr,'Your sentence is not a pangram'))
