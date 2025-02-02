from components import *
import pandas as pd
import os


HsCodes = pdf_extractor(pdf_name = "PAKISTANCUSTOMSTARIFF-2023-24.pdf", count=10, newExtraction=False, allHsCode=True)
print(HsCodes)
if type(HsCodes) == list:
    # HsCodes.insert(5, "1511.9030")
    # print(HsCodes)
    with open(os.getcwd() + "/Documents/hsCode.txt", "r") as f:
            code = f.read()
            print(code)
    if bool(code):
        run(HsCodes, isAllPages=True, maxPagesAllowed=5, isContinue=True, existingHsCode=code)
    else:
        print("Not Continue")
        run(HsCodes, isAllPages=True, maxPagesAllowed=5, isContinue=False, existingHsCode=None)
        
    
    
    
    
else:
    print(HsCodes)