import numpy as np

def filter_thickness(mat, mu):
    """
    Calculate the filter thickness that can reduce the intensity of the 
    beam to 1% based on its macroscopic cross section.

    Parameters:
    mat : material name
    mu : macroscopic cross section

    Returns:
    thickness of the filter
    """
    #Convert barn to cm-2 
    x = (2 * np.log(10)) / mu

    print(f"\nMaterial : {mat}")
    print(f"Macroscopic cross section : {mu:.2e} cm^-2")
    #print(f"Filter thickness : {x:.3f} cm\n")
    
    return x
