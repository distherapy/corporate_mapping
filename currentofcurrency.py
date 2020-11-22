#!usr/bin/env python
#
#<sixie6e@paracosmoclast>
#
#pseudolayout
#
import pandas as pd
import matplotlib as plt
import ezodf

banks = pd.read_excel("/home/sixie6e/Documents/corporate_mapping/banks.ods")

nasdaq = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/nasdaq.ods")

djia = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/djia.ods")

crudeoil = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/crudeoil.ods")

snp500 = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/snp500.ods")

russell2000 = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/russell2000.ods")
