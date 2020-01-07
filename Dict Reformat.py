filename = 'NFL_C Copy.txt'

with open(filename) as f:
    content = f.readlines()
    
for line in content:
    line.replace('\n', '')
    print(line)
        
print(content)