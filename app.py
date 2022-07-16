# write[w],read[r],append[a], reading/writtin[r+] and open a file
# readable,readline,readlines
# loop inside a file
count_file = open('countries.txt', 'r')
for files in count_file.readlines():
    print(files)
count_file.close()


count_file = open('write.txt', 'w')
count_file.write('woow')


