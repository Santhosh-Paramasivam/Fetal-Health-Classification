import papermill

for i in range(1,2,1):
    papermill.execute_notebook("scripts/robust_scaler.ipynb","scripts/out/normalizer.ipynb")
    print(str(i) + " iterations")