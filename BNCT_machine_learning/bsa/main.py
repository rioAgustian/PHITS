import numpy as np
from params import Params
from src.moderator import moderator_thickness
from src.filter import filter_thickness

def main():

    const = Params()

    MODERATOR_THICKNESS = moderator_thickness(const.moderator_mat,
                                               const.moderator_rho,
                                               const.moderator_sig,
                                               const.moderator_M)
    print(f"Estimated moderator thickness: {MODERATOR_THICKNESS:.2f} cm\n")
    
    FNF_THICKNESS = filter_thickness(const.FNF_mat,
                                     const.FNF_mu)
    print(f"Estimated fast neutron filter thickness {FNF_THICKNESS:.2f} cm\n")
    
    TNF_THICKNESS = filter_thickness(const.TNF_mat,
                                     const.TNF_mu)
    print(f"Estimated thermal neutron filter thickness {TNF_THICKNESS:.2f} cm\n")
    
    GF_THICKNESS = filter_thickness(const.GF_mat,
                                    const.GF_mu)
    print(f"Estimated gamma filter thickness {GF_THICKNESS} cm\n")
    
    GS_THICKNESS = filter_thickness(const.GS_mat,
                                    const.GS_mu)
    print(f"Estimated gamma shielding thickness {GS_THICKNESS} cm\n")

if __name__ == "__main__":
    main()
