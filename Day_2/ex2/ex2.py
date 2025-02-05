with open('./input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
    
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, world!\n')
    file.write('This is a test file.')