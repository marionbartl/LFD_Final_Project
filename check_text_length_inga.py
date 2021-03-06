import pandas as pd


data = pd.read_csv('hyperp-training-grouped.csv.xz',
                   compression='xz', sep='\t',
                   encoding='utf-8', index_col=0).dropna()

empty_text_counter = 0
# To count characters
for row in data.itertuples(index=True, name='Pandas'):
    if len(getattr(row, "text")) < 70:
        print(getattr(row, "text"))
        print("NEXT")
        empty_text_counter += 1
        
        
# To count words
#for row in data.itertuples(index=True, name='Pandas'):
#    words = getattr(row, "text").split(" ")
#    if len(words) < 70:
#        print(getattr(row, "text"))
#        print("NEXT")
#        empty_text_counter += 1

print(empty_text_counter)
