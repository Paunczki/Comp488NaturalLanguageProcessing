'''
I plan to do a simple classifier that only judges good or bad based on how many characters in a sentence
I will count the avearge number of characters and do a binary choice
'''

# need to do while loops to loop through

i=0
tot =0
avg_pos=0
f_pos=open('Homework/Homework 1/rt-polarity.pos','r')
for line in f_pos.readlines():
    tot+=len(line)
    i+=1
avg_pos = tot / i
print(avg_pos)


j=0
tot=0
avg_neg=0
f_neg=open('Homework/Homework 1/rt-polarity.neg', 'r')
for line in f_neg.readlines():
    tot+=len(line)
    j+=1
avg_neg = tot / j
print(avg_neg)


avg = 0
res_pos = -1
res_neg = -1
check = False
if avg_pos > avg_neg:
    avg = avg_pos
    res_pos = 1
    res_neg = 0
    check = True
else:
    avg = avg_neg
    res_pos = 0
    res_neg = 1
    check = False


# Now create a random dataset and test classifier
ds = []
b = []
i = 0
f_pos=open('Homework/Homework 1/rt-polarity.pos','r')
for line in f_pos.readlines():
    ds.append(line)
    b.append(res_pos)
    i += 1
    if i == 5331:
        break

f_neg=open('Homework/Homework 1/rt-polarity.neg', 'r')
for line in f_neg.readlines():
    ds.append(line)
    b.append(res_neg)
    i += 1
    if i == 5331:
        break

# Test and see percent correct
j = 0
num_correct = 0
num_wrong = 0
for line in ds:
    a = line.split(" ")
    if "awful" in a or "terrible" in a or "bad" in a or "no" in a:
        if b[j] == res_neg:
            num_correct += 1
        else:
            num_wrong += 1
        j += 1
        continue
    if "amazing" in a or "great" in a or "good" in a or "yes" in a:
        if b[j] == res_pos:
            num_correct += 1
        else:
            num_wrong += 1
        j += 1
        continue   
    
    if len(line) > avg and check:
        if b[j] == res_pos:
            num_correct += 1
        else: 
            num_wrong += 1
    elif len(line) < avg and not check:
        if b[j] == res_neg:
            num_correct += 1
        else: 
            num_wrong += 1
    else:
        if b[j] == res_neg:
            num_correct += 1
        else: 
            num_wrong += 1
    j += 1

print(num_correct)
print(num_wrong)

# Results from entire dataset
# Number correct -> 5590
# Number wrong -> 5072
# Percentage -> 52.43%
# So pretty much it is as good as guessing
