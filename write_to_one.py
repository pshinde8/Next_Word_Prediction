import os

folder = R"D:\Github\Next_Word_Prediction\data file\20news-bydate-test\alt.atheism"
tgt_file = R'D:\Github\Next_Word_Prediction\data file\Main corpus.txt'

for item in os.listdir(folder):
    with open(item, "r") as infile:
        content = infile.readlines()
        lines = content[5] + "\n" + content[6] + "\n" + content[7] + "\n" + content[8] + "\n" + content[9] + "\n" + \
                content[10] + "\n" + content[11]
    with open(tgt_file, "w") as outfile:
        outfile.write(lines)



