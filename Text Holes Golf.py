def golf(t):
 c=0
 for j in range(0,len(t)-2):
  for i in range(0,min(map(len,t[j:j+3]))-1):
   x,y,z=t[j:j+3];u=x[i:i+3]+y[i:i+3]+z[i:i+3]
   if all([y[i+1]==' ',u.count(' ')*9==len(u)]):c+=1
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

print golf([
 "How are you doing?",
 "I'm fine. OK.",
 "Lorem Ipsum?",
 "Of course!!!",
 "1234567890",
 "0        0",
 "1234567890",
 "Fine! good buy!"])
