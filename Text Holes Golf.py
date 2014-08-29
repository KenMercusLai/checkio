def golf(t):
    c=0
    for r in range(1,len(t)-1):
        for i in range(1,len(t[r])-1):
            try:
                if t[r][i]==' 'and' 'not in[t[r][i-1],t[r][i+1],t[r-1][i],t[r+1][i],t[r+1][i+1],t[r-1][i-1],t[r+1][i-1],t[r-1][i+1]]:
                    c+=1
            except:pass
    return c

print golf([
    "How are you doing?",
    "I'm fine. OK.",
    "Lorem Ipsum?",
    "Of course!!!",
    "1234567890",
    "0        0",
    "1234567890",
    "Fine! good buy!"])

print golf([
    "Lorem ipsum dolor",
    "sit amet,",
    "consectetuer",
    "adipiscing elit.",
    "Aenean commodo",
    "ligula eget dolor.",
    "Aenean massa. Cum",
    "sociis natoque",
    "penatibus et magnis",
    "dis parturient",
    "montes, nascetur",
    "ridiculus mus. Donec",
    "quam felis,",
    "ultricies nec,",
    "pellentesque eu,",
    "pretium quis, sem.",
    "Nulla consequat",
    "massa quis enim.",
    "Donec pede justo,",
    "fringilla vel,"])

print golf([
    "Lorem ipsum dolor",
    "sit amet,",
    "consectetuer",
    "adipiscing elit.",
    "Aenean commodo",
    "ligula eget dolor.",
    "Aenean massa. Cum",
    "sociis natoque",
    "penatibus et magnis",
    "dis parturient",
    "montes, nascetur",
    "ridiculus mus. Donec",
    "quam felis,",
    "ultricies nec,",
    "pellentesque eu,",
    "pretium quis, sem.",
    "Nulla consequat",
    "massa quis enim.",
    "Donec pede justo,",
    "fringilla vel,"])
