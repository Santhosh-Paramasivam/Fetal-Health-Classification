import papermill

for i in range(1,10,1):
    papermill.execute_notebook("scripts/unnormalized.ipynb","scripts/out/unnormalized.ipynb")
    papermill.execute_notebook("scripts/standard_scaler.ipynb","scripts/out/standard_scaler.ipynb")
    papermill.execute_notebook("scripts/minmax_scaler.ipynb","scripts/out/minmax_scaler.ipynb")
    papermill.execute_notebook("scripts/maxabs_scaler.ipynb","scripts/out/maxabs_scaler.ipynb")
    papermill.execute_notebook("scripts/robust_scaler.ipynb","scripts/out/robust_scaler.ipynb")
    papermill.execute_notebook("scripts/normalizer.ipynb","scripts/out/normalizer.ipynb")
    papermill.execute_notebook("scripts/quantile_transformer.ipynb","scripts/out/quantile_transformer.ipynb")
    print(i+1,"iterations done")
