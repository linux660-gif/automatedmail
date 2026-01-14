import pandas as pd
import os

class HandleExcel:
    def __init__(self):
        path = None

    def form_details_to_excel(self, path):
        df = pd.read_json(path)
        return  df.to_excel('formdetailsexcel.xlsx', index=False)
  



