import os
import numpy as np
from scipy.stats import qmc
from pathlib import Path

template = "template.inp"
base_folder = "data"

#Read the template file
with open(template, "r") as f:
    content = f.read()
    
def generate_samples():
    
    # Initialization
    n_dim = 6
    m_pow = 3
    N = 2**m_pow
    
    #Mod1, mod2, FNF, TNF, GF, GS
    low_bounds = [15,  5, 0.01, 0.01, 0.01, 0.01]
    upp_bounds = [40, 20,   25,    1,   10,   10]

    #Generate 
    sampler = qmc.Sobol(d=n_dim, scramble=True)
    sample_unit = sampler.random_base2(m=m_pow)

    #Scale it
    sample_scaled = qmc.scale(sample_unit, low_bounds, upp_bounds)
    
    j = 1

    for i in sample_scaled:
        #New parameter based on sobol sampling
        MOD_1 = round(i[0], 1) 
        MOD_2 = round(i[1], 1)
        FNF = round(i[2], 1) 
        TNF = round(i[3], 1)
        GF = round(i[4], 1)
        GS = round(i[5], 1)
        
        #Copy template file
        new_file = content
        
        #Find and replace
        new_file = new_file.replace("{MOD_1}", str(MOD_1))
        new_file = new_file.replace("{MOD_2}", str(MOD_2))
        new_file = new_file.replace("{FNF}", str(FNF))
        new_file = new_file.replace("{TNF}", str(TNF))
        new_file = new_file.replace("{GF}", str(GF))
        new_file = new_file.replace("{GS}", str(GS))

        #ID
        run_id = f"{j:03d}"
        
        #Make folder
        folder_name = f"run_{run_id}"
    
        #Full path
        new_file_name = f"run_{run_id}.inp"
        full_folder_path = os.path.join(base_folder, folder_name)
        full_file_path = os.path.join(full_folder_path, new_file_name)
        os.makedirs(full_folder_path, exist_ok=True)

        #Write the file
        with open(full_file_path, "w") as out_file:
            out_file.write(new_file)
    
        print(f"[{j}/{N} File created: {full_file_path}]")
        
        j += 1

    print("Finished!")
        
if __name__ == "__main__":
    generate_samples()

