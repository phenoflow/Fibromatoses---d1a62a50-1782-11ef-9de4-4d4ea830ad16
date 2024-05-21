# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N236800","system":"readv2"},{"code":"N236400","system":"readv2"},{"code":"N236200","system":"readv2"},{"code":"N236300","system":"readv2"},{"code":"N236500","system":"readv2"},{"code":"7H32011","system":"readv2"},{"code":"N236000","system":"readv2"},{"code":"N236.00","system":"readv2"},{"code":"N236100","system":"readv2"},{"code":"7H34012","system":"readv2"},{"code":"N236700","system":"readv2"},{"code":"N236600","system":"readv2"},{"code":"M72.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fibromatoses-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fibromatoses-dupuytren---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fibromatoses-dupuytren---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fibromatoses-dupuytren---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
