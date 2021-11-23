import pandas as pd

main_df = pd.DataFrame()

arg = pd.read_csv('VeriSetleri\Argentina\Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_Argentina.txt',
                  sep='\t')
arg = arg.iloc[:, 0:-1]
arg = arg.dropna(axis=0)
arg['Exporter'] = 'Argentina'

ch = pd.read_csv('VeriSetleri/China/Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_China.txt',
                 sep='\t')
ch = ch.iloc[:, 0:-1]
ch = ch.dropna(axis=0)

ch['Exporter'] = 'China'

ger = pd.read_csv('VeriSetleri/Germany/Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_Germany.txt',
                  sep='\t')
ger = ger.iloc[:, 0:-1]
ger = ger.dropna(axis=0)

ger['Exporter'] = 'Germany'

sen = pd.read_csv('VeriSetleri/Senegal/Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_Senegal.txt',
                  sep='\t')
sen = sen.iloc[:, 0:-1]
sen = sen.dropna(axis=0)

sen['Exporter'] = 'Senegal'

tur = pd.read_csv('VeriSetleri/Turkey/Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_Turkey.txt',
                  sep='\t')
tur = tur.iloc[:, 0:-1]
tur = tur.dropna(axis=0)

tur['Exporter'] = 'Turkey'

usa = pd.read_csv(
    'VeriSetleri/USA/Trade_Map_-_List_of_importing_markets_for_a_product_exported_by_United_States_of_America.txt',
    sep='\t')
usa = usa.iloc[:, 0:-1]
usa = usa.dropna(axis=0)

usa['Exporter'] = 'USA'

frames = [arg, ch, ger, sen, tur, usa]

main_df = pd.concat(frames)

main_df.to_csv('import-exported-value.csv', sep='\t', index=False)


del main_df

