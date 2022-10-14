import shutil

file = R"D:\Github\Next_Word_Prediction\data file\20news-bydate.tar.gz"
tgt_dir = R'D:\Github\Next_Word_Prediction\data file'


if __name__ == "__main__":
    shutil.unpack_archive(file, tgt_dir)
