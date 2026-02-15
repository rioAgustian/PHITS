import numpy as np

Na = 6.022e23 #Avogardo number (atom/mol)

class Params:
    def __init__(self):
        #Moderator (Al)
        self.moderator_mat = "Al"
        self.moderator_rho = 2.7 #g/cm^3 
        self.moderator_sig = 1.749994 #For 11.15 MeV neutron (barn)
        self.moderator_M = 26.98

        #Fast neutron filter (LiF)
        self.FNF_mat = "LiF"
        self.FNF_rho = 2.64 #g/cm^3 
        self.calculate_FNF_mu()
        
        #Thermal neutron filter (B4C)
        self.TNF_mat = "B4C"
        self.TNF_rho = 2.51 #g/cm^3
        self.calculate_TNF_mu()

        #Gamma filter (Bi)
        self.GF_mat = "Bi"
        self.GF_rho = 9.757 #g/cm^3
        self.calculate_GF_mu()

        #Gamma shielding (Pb)
        self.GS_mat = "Pb"
        self.GS_rho = 11.35 #g/cm^3
        self.calculate_GS_mu()

    def calculate_FNF_mu(self):
        #Relative atom mass
        M_Li = 6.94
        M_F = 18.99
        M_LiF = M_Li + M_F 

        #Atomic density (atom/cm^3)
        n_LiF = (self.FNF_rho * Na) / M_LiF

        #Microscopic cross section
        sig_6Li = 1.6383042 #For 11.15 MeV neutron (barn)
        sig_7Li = 1.598664  #For 11.15 MeV neutron (barn)
        sig_F = 1.7255831 #For 11.15 MeV neutron (barn)
        frac_6Li = 0.075 #Natural occurance of isotope 6Li
        frac_7Li = 0.925 #Natural occurance of isotope 7Li
        sig_Li = (frac_6Li * sig_6Li) + (frac_7Li * sig_7Li)
        
        #Convert from barn to cm^-2 by 1.0e-24
        #Macroscopic cross section
        self.FNF_mu = n_LiF * (sig_Li + sig_F) * 1.0e-24

    def calculate_TNF_mu(self):
        #Relative mass
        M_B = 10.81
        M_C = 12.01
        M_B4C = 4*M_B + M_C

        #Atomic density
        n_B4C = (self.TNF_rho * Na) / M_B4C

        #Microscopic cross section
        sig_10B = 3835 #For thermal neutron (barn)
        sig_11B = 0.005 #For thermal neutron (barn)
        sig_C = 4.7592974 #For 0.5 eV thermal neutron (barn)
        frac_10B = 0.189
        frac_11B = 0.796
        sig_B = (frac_10B * sig_10B) + (frac_11B * sig_11B)

        #Convert from barn to cm^-2 by a factor of 1.0e-24
        #Macroscopic cross section
        self.TNF_mu = n_B4C * (4*sig_B + sig_C) * 1.0e-24
    
    def calculate_GF_mu(self):
        #Atomic mass
        M_Bi = 208.98

        #Mass attenuation coefficient
        mu_rho_Bi = 4.725E-02 #Mass attenuation coefficient Bi for photon 8MeV (27Al(n,gamma)28Al -> gamma 7.5 MeV)

        #Macroscopic cross section
        self.GF_mu = mu_rho_Bi * self.GF_rho

    def calculate_GS_mu(self):
        #Atomic mass
        M_Pb = 207.2

        #Mass attenuation coefficient
        mu_rho_Pb = 4.675E-02 #Mass attenuatioin coefficient Pb for photon 8 MeV
        #Macroscopic cross section
        self.GS_mu = mu_rho_Pb * self.GS_rho

