import pandas as pd

counts = [pd.read_table(f, index_col=0, usecols=[0, 1], header=None, skiprows=0)
          for f in snakemake.input]

for t, (sample) in zip(counts, snakemake.params.units.index):
    t.columns = ["%s" % (sample)]
matrix = pd.concat(counts, axis=1)
matrix=matrix.drop(matrix.index[[-5,-4,-3,-2,-1]]) #delete last 5 rows
matrix.index.name = "gene"
print(matrix)
matrix.to_csv(snakemake.output[0], sep=",")



python /data1/script/CountMatrix.py list > out.matrix


WR180755S 1.Mapping/WR180755S_clean_CountNum.txt
WR180756S 1.Mapping/WR180756S_clean_CountNum.txt
WR180757S 1.Mapping/WR180757S_clean_CountNum.txt