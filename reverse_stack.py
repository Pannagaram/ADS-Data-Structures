class reversed_file:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.stack = []
    
    def reverse_file_content(self):
        with open (self.input_file, 'r') as file:
            content = file.read()

            for char in content:
                self.stack.append(char)
            
            reversed_content = ''

            while self.stack:
                reversed_content += self.stack.pop()

        with open (self.output_file, 'w') as file:
            file.write(reversed_content)


reverse = reversed_file('original.txt', 'reverse.txt')
reverse.reverse_file_content()