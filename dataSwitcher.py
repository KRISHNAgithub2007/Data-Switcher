def SwapData():
    filePath1 = input("Enter File Path 1 : ")
    filePath2 = input("Enter File Path 2 : ")

    file1 = open(filePath1,'r')
    fileData1 = file1.read()
    file1.close()

    file2 = open(filePath2,'r')
    fileData2 = file2.read()
    file2.close()

    file2 = open(filePath2, 'w')
    file2.write(fileData1)
    file2.close()

    file1 = open(filePath1, 'w')
    file1.write(fileData2)
    file1.close()

SwapData()