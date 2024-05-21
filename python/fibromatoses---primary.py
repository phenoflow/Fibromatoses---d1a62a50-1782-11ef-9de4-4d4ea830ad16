# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"50915.0","system":"readv2"},{"code":"44537.0","system":"readv2"},{"code":"21080.0","system":"readv2"},{"code":"743.0","system":"readv2"},{"code":"28831.0","system":"readv2"},{"code":"44504.0","system":"readv2"},{"code":"53902.0","system":"readv2"},{"code":"25701.0","system":"readv2"},{"code":"26216.0","system":"readv2"},{"code":"22546.0","system":"readv2"},{"code":"11899.0","system":"readv2"},{"code":"10142.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fibromatoses-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fibromatoses---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fibromatoses---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fibromatoses---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
