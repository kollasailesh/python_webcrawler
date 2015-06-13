fw = open('sample.txt', 'w')
fw.write("Hello World !! \n")
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

