import markdown

file1 = open("demo.md", "r")

file1_string = file1.read()

output = markdown.markdown(file1_string)

print(output)

output_file = open("demo2.html", "w")
output_file.write(output)
output_file.close()