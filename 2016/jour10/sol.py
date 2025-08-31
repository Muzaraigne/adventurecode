import re, collections



if __name__ == "__main__" : 
    print("--- Jour 10 : Solution ---") 
    with open(".\\2016\\jour10\\input.txt","r") as f : 
       data = f.read().splitlines() 
    bot = collections.defaultdict(list)
    output = collections.defaultdict(list)



    pipeline = {}
    for line in data:
        if line.startswith('value'):
            n, b = map(int,re.findall(r'-?\d+', line))
            bot[b].append(n)
        if line.startswith('bot'):
            who, n1, n2 = map(int,re.findall(r'-?\d+', line))
            t1, t2 = re.findall(r' (bot|output)', line)
            pipeline[who] = (t1,n1),(t2,n2)


    while bot:
        for k,v in dict(bot).items():
            if len(v) == 2:
                v1, v2 = sorted(bot.pop(k))
                if v1==17 and v2==61: print(k)
                (t1,n1),(t2,n2) = pipeline[k]
                if t1 == 'bot':
                    bot[n1].append(v1)
                else:
                    output[n1].append(v1)

                if t2 == 'bot':
                    bot[n2].append(v2)
                else:
                    output[n2].append(v2)

    a,b,c = (output[k][0] for k in [0,1,2])
    print(a*b*c)