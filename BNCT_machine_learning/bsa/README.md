# Analytical Estimation of Beam Shaping Assembly Parts Thickness
- **[Rio Agustian Gilang Fernando]**

## What it does?
Calculate the thickness estimation of BSA parts. Specifically: moderator, fast neutron filter, thermal neutron filter, gamma filter, and gamma shielding.

## Why it's important?
See, when you calculate this kind of stuff, you need the microscopic cross section and a bunch of constans. If you don't use a well structured way, it is very easy to make mistake. This code is created to make MY work easier.

## Theory
### 1. Filter Mode

Fast neutron filter, thermal neutron filter, gamma filter, and gamma shielding is considered as filter. So, we just using the Beer–Lambert law:

$$I = I_0 e^{-\sigma x}$$

I chose the maximum thickness as a thickness where $I_0=1%$ the initial intensity. It works pretty well when I compare it with some journal that is talking about BSA optimization. The energy that use is always the upper bound energy. Why? Because mostly high energy particle has considerably low microscopic cross section, which mean that can penetrate the material very easy. Note that this code is meant to generate hundreds of BSA configurations for machine learning dataset. We need to explore this region. We want our model learn for the lowest possible thickness to the physically possible thickness.

### 2. Moderator Mode

Moderator's job is to moderate the neutron. In this case, we need special technique to estimate the ma
