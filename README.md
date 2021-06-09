# H dibaryon from lattice QCD

This repository is a supplementary analysis of the finite volume method in lattice QCD
based on the data from "Weakly bound H dibaryon from SU(3)-flavor-symmetric QCD", 
J. R. Green, A. D. Hanlon, P. M. Junnarkar, H. Wittig,  [arXiv:2103.01054](https://arxiv.org/abs/2103.01054).

- [H dibaryon from lattice QCD](#h-dibaryon-from-lattice-qcd)
- [To Do List](#to-do-list)
- [Gauge configurations](#gauge-configurations)
- [Energy levels & $p\cot\delta$ vs $p^2$](#energy-levels--pcotdelta-vs-p2)
  - [Effective Range Expansion (ERE) analysis (NLO)](#effective-range-expansion-ere-analysis-nlo)
  - [$L = 3.1$ fm N202 ensemble ($a = 0.0642$ fm)](#l--31-fm-n202-ensemble-a--00642-fm)
    - [ERE analysis](#ere-analysis)
  - [$L = 2.8$ fm H101 ensemble ($a = 0.0865$ fm)](#l--28-fm-h101-ensemble-a--00865-fm)
    - [ERE analysis](#ere-analysis-1)
  - [$L = 2.4$ fm N300 ensemble ($a = 0.0498$ fm)](#l--24-fm-n300-ensemble-a--00498-fm)
    - [ERE analysis](#ere-analysis-2)
  - [$L = 2.4$ fm B450 ensemble ($a = 0.0762$ fm)](#l--24-fm-b450-ensemble-a--00762-fm)
    - [ERE analysis](#ere-analysis-3)
  - [$L = 2.4$ fm A653 ensemble ($a = 0.0992$ fm)](#l--24-fm-a653-ensemble-a--00992-fm)
    - [ERE analysis](#ere-analysis-4)
  - [$L = 2.1$ fm H200 ensemble ($a = 0.0642$ fm)](#l--21-fm-h200-ensemble-a--00642-fm)
    - [ERE analysis](#ere-analysis-5)
  - [$L = 2.1$ fm U103 ensemble ($a = 0.0865$ fm)](#l--21-fm-u103-ensemble-a--00865-fm)
    - [ERE analysis](#ere-analysis-6)
  - [Nf = 2 E5 ensemble ($La = 2.1$ fm, $a = 0.0658$ fm, $m_\pi = 436$ MeV)](#nf--2-e5-ensemble-la--21-fm-a--00658-fm-m_pi--436-mev)
    - [ERE analysis](#ere-analysis-7)
  - [Nf = 2 E1 ensemble ($La = 2.1$ fm, $a = 0.0658$ fm, $m_\pi = 978$ MeV)](#nf--2-e1-ensemble-la--21-fm-a--00658-fm-m_pi--978-mev)
    - [ERE analysis](#ere-analysis-8)
- [Summary of phase shifts](#summary-of-phase-shifts)
  - [$La$ : fixed](#la--fixed)
  - [$a$ : fixed](#a--fixed)
- [First excited states for P011 and P111](#first-excited-states-for-p011-and-p111)
- [Finite volume potential](#finite-volume-potential)

# To Do List
- [X] ERE fitting & binding energy
- [X] Check imaginary (?) state P011, P111 first excited state versus ERE
- [X] HAL potential inside a small box

# Gauge configurations

|Label | Nf | L | a [fm] | La [fm] |  m_pi [MeV] |
|------|----|---|--------|---------|-------------|
| N300 | 3  | 48| 0.0498 | 2.4     | 422         |
| N202 | 3  | 48| 0.0642 | 3.1     | 412         |
| H200 | 3  | 32| 0.0642 | 2.1     | 419         |
| B450 | 3  | 32| 0.0762 | 2.4     | 417         |
| H101 | 3  | 32| 0.0865 | 2.8     | 417         |
| U103 | 3  | 24| 0.0865 | 2.1     | 414         |
| A653 | 3  | 24| 0.0992 | 2.4     | 424         |
| E5   | 2  | 32| 0.0658 | 2.1     | 436         |
| E1   | 2  | 32| 0.0658 | 2.1     | 978         |

![SU3 conf.](figs/SU3_ensembles.png)

Summary of binding energies and their cutoff/volume dependence.
![SU3 BE summary](figs/BE_summary_Nf3.png)

* These binding energies are obtained as follows.

1. Calculate the scattering phase shifts $\delta$ of level = 0 states for P000, P001, P011, P111 and P002 frames with total spin-zero. The errors are estimated from 95CI of bootstrap samples.
2. Fit these 5 points using NLO ERE (next leading order effective range expansion) with the finite volume formula constraints correctly. In some ensembles (H200, B450, and U103) P111 level is ignored due to tension between other levels.
3. Measure the intersection between NLO ERE and binding state condition $-\sqrt{-k^2}$, which can be converted into the binding energy.
4. Take continuum limit.

# Energy levels & $p\cot\delta$ vs $p^2$

Interactive plots are also available.
(see figs/pcot_vs_p2/{label}_pcot_vs_p2.html)

![plotly figure](figs/pcot_vs_p2/plotly_pcot_vs_p2_sample.png)

The relation between negative squared momentum vs B.E.
for baryon mass 1.2 GeV and pion mass 420 MeV.
![BE](figs/BE_vs_p_square.png)

## Effective Range Expansion (ERE) analysis (NLO)

NLO order ERE fitting
$k\cot\delta = 1/a_0 + \frac{1}{2}r_\mathrm{eff}k^2$

$a_0$: scattering length
$r_\mathrm{eff}$: effective range

* For the fitting, we employ 5 data points ($n = 0$ level spectra for P000, P001, P011, P111, and P200 frames with total spin-zero.
* We take into account the finite volume constraints correctly.

## $L = 3.1$ fm N202 ensemble ($a = 0.0642$ fm)

![N202 ensemble](figs/energy_levels/N202_spin_zero.png)
![N202 ensemble](figs/pcot_vs_p2/N202_pcot_vs_p2.png)
![N202 ensemble](figs/pcot_vs_p2/N202_pcot_vs_p2_neg.png)

### ERE analysis

![N202 ensemble](figs/ERE/N202_ERE_parameter.png)
![N202 ensemble](figs/ERE/N202_pcot_vs_p2_ERE_fit.png)

## $L = 2.8$ fm H101 ensemble ($a = 0.0865$ fm)

![H101 ensemble](figs/energy_levels/H101_spin_zero.png)
![H101 ensemble](figs/pcot_vs_p2/H101_pcot_vs_p2.png)
![H101 ensemble](figs/pcot_vs_p2/H101_pcot_vs_p2_neg.png)

### ERE analysis

![H101 ensemble](figs/ERE/H101_ERE_parameter.png)
![H101 ensemble](figs/ERE/H101_pcot_vs_p2_ERE_fit.png)

## $L = 2.4$ fm N300 ensemble ($a = 0.0498$ fm)

![N300 ensemble](figs/energy_levels/N300_spin_zero.png)
![N300 ensemble](figs/pcot_vs_p2/N300_pcot_vs_p2.png)
![N300 ensemble](figs/pcot_vs_p2/N300_pcot_vs_p2_neg.png)

### ERE analysis

![N300 ensemble](figs/ERE/N300_ERE_parameter.png)
![N300 ensemble](figs/ERE/N300_pcot_vs_p2_ERE_fit.png)
![N300 ensemble](figs/ERE/N300_pcot_vs_p2_ERE_fit_neg.png)

## $L = 2.4$ fm B450 ensemble ($a = 0.0762$ fm)

![B450 ensemble](figs/energy_levels/B450_spin_zero.png)
![B450 ensemble](figs/pcot_vs_p2/B450_pcot_vs_p2.png)
![B450 ensemble](figs/pcot_vs_p2/B450_pcot_vs_p2_neg.png)

### ERE analysis

Here, we ignore P111 from ERE fitting.

![B450 ensemble](figs/ERE/B450_ERE_parameter.png)
![B450 ensemble](figs/ERE/B450_pcot_vs_p2_ERE_fit.png)
![B450 ensemble](figs/ERE/B450_pcot_vs_p2_ERE_fit_neg.png)

## $L = 2.4$ fm A653 ensemble ($a = 0.0992$ fm)

![A653 ensemble](figs/energy_levels/A653_spin_zero.png)
![A653 ensemble](figs/pcot_vs_p2/A653_pcot_vs_p2.png)
![A653 ensemble](figs/pcot_vs_p2/A653_pcot_vs_p2_neg.png)

### ERE analysis

![A653 ensemble](figs/ERE/A653_ERE_parameter.png)
![A653 ensemble](figs/ERE/A653_pcot_vs_p2_ERE_fit.png)

## $L = 2.1$ fm H200 ensemble ($a = 0.0642$ fm)

![H200 ensemble](figs/energy_levels/H200_spin_zero.png)
![H200 ensemble](figs/pcot_vs_p2/H200_pcot_vs_p2.png)
![H200 ensemble](figs/pcot_vs_p2/H200_pcot_vs_p2_neg.png)

### ERE analysis

Here, we ignore P111 from ERE fitting.

![H200 ensemble](figs/ERE/H200_ERE_parameter.png)
![H200 ensemble](figs/ERE/H200_pcot_vs_p2_ERE_fit.png)
![H200 ensemble](figs/ERE/H200_pcot_vs_p2_ERE_fit_neg.png)

## $L = 2.1$ fm U103 ensemble ($a = 0.0865$ fm)

![U103 ensemble](figs/energy_levels/U103_spin_zero.png)
![U103 ensemble](figs/pcot_vs_p2/U103_pcot_vs_p2.png)
![U103 ensemble](figs/pcot_vs_p2/U103_pcot_vs_p2_neg.png)

### ERE analysis

Here, we ignore P111 from ERE fitting.

![U103 ensemble](figs/ERE/U103_ERE_parameter.png)
![U103 ensemble](figs/ERE/U103_pcot_vs_p2_ERE_fit.png)
![U103 ensemble](figs/ERE/U103_pcot_vs_p2_ERE_fit_neg.png)

## Nf = 2 E5 ensemble ($La = 2.1$ fm, $a = 0.0658$ fm, $m_\pi = 436$ MeV)

![E5 ensemble](figs/energy_levels/E5_spin_zero.png)
![E5 ensemble](figs/pcot_vs_p2/E5_pcot_vs_p2.png)
![E5 ensemble](figs/pcot_vs_p2/E5_pcot_vs_p2_neg.png)

### ERE analysis 

P011 & P111 1st excited states are ignored.

![E5 ensemble](figs/ERE/E5_ERE_parameter.png)
![E5 ensemble](figs/ERE/E5_pcot_vs_p2_ERE_fit.png)
![E5 ensemble](figs/ERE/E5_pcot_vs_p2_ERE_fit_neg.png)

## Nf = 2 E1 ensemble ($La = 2.1$ fm, $a = 0.0658$ fm, $m_\pi = 978$ MeV)

![E1 ensemble](figs/energy_levels/E1_spin_zero.png)
![E1 ensemble](figs/pcot_vs_p2/E1_pcot_vs_p2.png)
![E1 ensemble](figs/pcot_vs_p2/E1_pcot_vs_p2_neg.png)

### ERE analysis 

P011 & P111 1st excited states are ignored.

![E1 ensemble](figs/ERE/E1_ERE_parameter.png)
![E1 ensemble](figs/ERE/E1_pcot_vs_p2_ERE_fit.png)
![E1 ensemble](figs/ERE/E1_pcot_vs_p2_ERE_fit_neg.png)

# Summary of phase shifts

## $La$ : fixed
![Fixed volume](figs/pcot_vs_p2/pcot_vs_p2_La_2_2fm.png)
![Fixed volume](figs/pcot_vs_p2/pcot_vs_p2_La_2_2fm_neg.png)

![Fixed volume](figs/pcot_vs_p2/pcot_vs_p2_La_2_4fm.png)
![Fixed volume](figs/pcot_vs_p2/pcot_vs_p2_La_2_4fm_neg.png)

## $a$ : fixed
![Fixed cutoff](figs/pcot_vs_p2/pcot_vs_p2_lat_spacing_00642fm.png)
![Fixed cutoff](figs/pcot_vs_p2/pcot_vs_p2_lat_spacing_00642fm_neg.png)

![Fixed cutoff](figs/pcot_vs_p2/pcot_vs_p2_lat_spacing_00865fm.png)
![Fixed cutoff](figs/pcot_vs_p2/pcot_vs_p2_lat_spacing_00865fm_neg.png)

# First excited states for P011 and P111

ERE fitting using first excited states for P000 and P001, which works well.
![First excited state for N202](figs/first_excited_state/N202_p2_vs_pcot_with_ERE.png)
![First excited state for N202](figs/first_excited_state/N202_p2_vs_pcot_with_ERE_neg.png)
![First excited state for N202](figs/first_excited_state/N202_ERE_param_with_P000_1_P001_1.png)

# Finite volume potential

To estimate the systematic uncertainties of finite volume and cutoff,  
we use flavor SU(3) potential at $m_\pi = 837$ MeV with a lattice spacing 0.121 fm.
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_1rep_pot.png)

Here, we consider small boxes such as $L = 8, 12, 16$.
![Finite volume potential](figs/hal_pot_finite_volume/finite_volume_potential.png)

The finite volume spectra at $L = 8$ and 12 show discrepancy.

![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_L8_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_L12_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_L16_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_L24_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_L32_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/su3_mpi837MeV_kcot_vs_k2_L_dep_neg.png)


Next, we consider a cutoff dependence of the finite volume eigenvalues.
(Here, we assume the interpolated potential in a = 0.121 fm is consistent with the continuum limit.)

![Finite volume potential](figs/hal_pot_finite_volume/mockup_potentials_in_various_lattice_spacing.png)
![Finite volume potential](figs/hal_pot_finite_volume/mockup_potentials_r2_in_various_lattice_spacing.png)

The eigenvalue using coarse lattices are much deeper than the original ones,
while the spectra using a much finer lattice than the one only show small cutoff dependence.

![Finite volume potential](figs/hal_pot_finite_volume/kcot_vs_k2_lattice_spacing_dependence.png)


The details of the convergence.

![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L24_level_0.png)
![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L24_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L36_level_0.png)
![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L36_level_1.png)
![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L48_level_0.png)
![Finite volume potential](figs/hal_pot_finite_volume/k2mpi2_cut_off_dependence_orig_L48_level_1.png)
