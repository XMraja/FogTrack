import os
from eval.eval import eval

dataset_path = "./datasets/fogmvt/inhomogeneous-fog/test"
out_path = "./fog_track_results/fogtrack/fogmvt"
exp_name = "test"

seqmap = "./datasets/fogmvt/seqmaps/test-all.txt"

HOTA,IDF1,MOTA,AssA = eval(dataset_path,out_path, seqmap, exp_name,1,False)


