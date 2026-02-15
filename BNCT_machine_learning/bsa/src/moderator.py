import numpy as np

Na = 6.022e23 #Avogardo number (atom/mol) 
m = 1.008664 #Neutron mass (u)
E_p = 13 #Maximum proton energy (MeV)
E_high = 0.47 * E_p - 2.2 #Average neutron energy generated (MeV)
E_low = 1.0e-2 #Upper bound of epithermal neutron (we want epithermal!) (MeV)

def moderator_thickness(mat, rho, sig, M):
    """
    Estimate the moderator thickness based on the given cross section and
    density of the materials.

    Parameters:
    mat : name of material (str)
    rho : density in g/cm^3

    Returns:
    moderator thickness (cm)
    """
    # Convert cross section to cm^-2
    sig = sig * 1.0e-24

    #Atomic density (atom/cm^3)
    n = (rho * Na) / M

    #Mean free path
    MFP = 1/(n * sig)
    
    #Alpha
    alpha = ((M - m)/(M + m))**2

    #Average logarithmic energy decrement
    xi = 1 + (alpha * np.log(alpha)) / (1 - alpha)
    
    #Number of collision
    N = np.log(E_high/E_low)

    #Crow flight distance
    r = np.sqrt(3 * N) * MFP

    print(f"Material : {mat}")
    print(f"Density : {rho:.3f} g/cm^3")
    print(f"Epithermal neutron cross section : {sig:.2e} cm^2")
    print(f"Mean free path : {MFP:.3f} cm")

    return r



