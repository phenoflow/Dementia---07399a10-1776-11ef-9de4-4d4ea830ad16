# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"1461.00","system":"readv2"},{"code":"8CMZ.00","system":"readv2"},{"code":"6AB..00","system":"readv2"},{"code":"E004.11","system":"readv2"},{"code":"Eu01100","system":"readv2"},{"code":"ZS7C500","system":"readv2"},{"code":"11175.0","system":"readv2"},{"code":"38438.0","system":"readv2"},{"code":"16797.0","system":"readv2"},{"code":"33707.0","system":"readv2"},{"code":"8934.0","system":"readv2"},{"code":"55467.0","system":"readv2"},{"code":"11379.0","system":"readv2"},{"code":"38678.0","system":"readv2"},{"code":"56912.0","system":"readv2"},{"code":"15249.0","system":"readv2"},{"code":"59122.0","system":"readv2"},{"code":"1350.0","system":"readv2"},{"code":"9565.0","system":"readv2"},{"code":"43346.0","system":"readv2"},{"code":"4357.0","system":"readv2"},{"code":"25704.0","system":"readv2"},{"code":"31016.0","system":"readv2"},{"code":"32057.0","system":"readv2"},{"code":"27759.0","system":"readv2"},{"code":"48501.0","system":"readv2"},{"code":"18386.0","system":"readv2"},{"code":"4693.0","system":"readv2"},{"code":"1917.0","system":"readv2"},{"code":"8634.0","system":"readv2"},{"code":"2882.0","system":"readv2"},{"code":"44674.0","system":"readv2"},{"code":"25386.0","system":"readv2"},{"code":"42602.0","system":"readv2"},{"code":"29386.0","system":"readv2"},{"code":"46762.0","system":"readv2"},{"code":"19393.0","system":"readv2"},{"code":"46488.0","system":"readv2"},{"code":"1916.0","system":"readv2"},{"code":"15165.0","system":"readv2"},{"code":"21887.0","system":"readv2"},{"code":"7323.0","system":"readv2"},{"code":"60059.0","system":"readv2"},{"code":"19477.0","system":"readv2"},{"code":"6578.0","system":"readv2"},{"code":"37015.0","system":"readv2"},{"code":"7664.0","system":"readv2"},{"code":"49263.0","system":"readv2"},{"code":"8195.0","system":"readv2"},{"code":"47619.0","system":"readv2"},{"code":"43292.0","system":"readv2"},{"code":"43089.0","system":"readv2"},{"code":"27677.0","system":"readv2"},{"code":"27935.0","system":"readv2"},{"code":"30706.0","system":"readv2"},{"code":"55313.0","system":"readv2"},{"code":"61528.0","system":"readv2"},{"code":"51494.0","system":"readv2"},{"code":"30032.0","system":"readv2"},{"code":"34944.0","system":"readv2"},{"code":"55838.0","system":"readv2"},{"code":"42279.0","system":"readv2"},{"code":"41089.0","system":"readv2"},{"code":"49513.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('dementia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dementia-dementium---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dementia-dementium---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dementia-dementium---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
