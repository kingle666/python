import csv
def read_csv_demo1():
    with open('test.csv','r') as fp:
        reader = csv.reader(fp)
        # next(reader)
        for x in reader:
            # leibie = x[1]
            # name = x[-3]
            print(x)# ({'name':name,'leibie':leibie})
            break
def read_csv_deam2():
    with open('test.csv','r') as fp:
        reader = csv.DictReader(fp)
        for x in reader:
            print(x)
if __name__ == "__main__":
    read_csv_deam2()