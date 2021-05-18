# H dibaryon from lattice QCD

This repository is a supplementary analysis of the finite volume method in lattice QCD
based on the data from "Weakly bound H dibaryon from SU(3)-flavor-symmetric QCD", 
J. R. Green, A. D. Hanlon, P. M. Junnarkar, H. Wittig,  [arXiv:2103.01054](https://arxiv.org/abs/2103.01054).

- [H dibaryon from lattice QCD](#h-dibaryon-from-lattice-qcd)
- [To Do List](#to-do-list)
- [Gauge configurations](#gauge-configurations)
- [Energy levels & $p\cot\delta$ vs $p^2$](#energy-levels--pcotdelta-vs-p2)
  - [$L = 3.1$ fm](#l--31-fm)
  - [$L = 2.8$ fm](#l--28-fm)
  - [$L = 2.4$ fm](#l--24-fm)
  - [$L = 2.1$ fm](#l--21-fm)
  - [Nf = 2](#nf--2)
- [Summary of phase shifts](#summary-of-phase-shifts)
  - [$La$ : fixed](#la--fixed)
  - [$a$ : fixed](#a--fixed)

# To Do List
- [ ] ERE fitting & binding energy
- [ ] Consistency check between root mean square distance of a shallow bound state and a finite volume box
- [ ] Square well potential demo & finite volume method from eigenvalues

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

# Energy levels & $p\cot\delta$ vs $p^2$

Interactive plots are also available.
(see figs/pcot_vs_p2/{label}_pcot_vs_p2.html)

![plotly figure](figs/pcot_vs_p2/plotly_pcot_vs_p2_sample.png)

The relation between negative squared momentum vs B.E.
for baryon mass 1.2 GeV and pion mass 420 MeV.
![BE](figs/../notebook/BE_vs_p_square.png)

## $L = 3.1$ fm
* $a = 0.0642$ fm

![N202 ensemble](figs/energy_levels/N202_spin_zero.png)
![N202 ensemble](figs/pcot_vs_p2/N202_pcot_vs_p2.png)
![N202 ensemble](figs/pcot_vs_p2/N202_pcot_vs_p2_neg.png)

## $L = 2.8$ fm
* $a = 0.0865$ fm

![H101 ensemble](figs/energy_levels/H101_spin_zero.png)
![H101 ensemble](figs/pcot_vs_p2/H101_pcot_vs_p2.png)
![H101 ensemble](figs/pcot_vs_p2/H101_pcot_vs_p2_neg.png)

## $L = 2.4$ fm
* $a = 0.0498$ fm

![N300 ensemble](figs/energy_levels/N300_spin_zero.png)
![N300 ensemble](figs/pcot_vs_p2/N300_pcot_vs_p2.png)
![N300 ensemble](figs/pcot_vs_p2/N300_pcot_vs_p2_neg.png)

* $a = 0.0762$ fm

![B450 ensemble](figs/energy_levels/B450_spin_zero.png)
![B450 ensemble](figs/pcot_vs_p2/B450_pcot_vs_p2.png)
![B450 ensemble](figs/pcot_vs_p2/B450_pcot_vs_p2_neg.png)

* $a = 0.0992$ fm

![A653 ensemble](figs/energy_levels/A653_spin_zero.png)
![A653 ensemble](figs/pcot_vs_p2/A653_pcot_vs_p2.png)
![A653 ensemble](figs/pcot_vs_p2/A653_pcot_vs_p2_neg.png)

## $L = 2.1$ fm
* $a = 0.0642$ fm

![H200 ensemble](figs/energy_levels/H200_spin_zero.png)
![H200 ensemble](figs/pcot_vs_p2/H200_pcot_vs_p2.png)
![H200 ensemble](figs/pcot_vs_p2/H200_pcot_vs_p2_neg.png)

* $a = 0.0865$ fm

![U103 ensemble](figs/energy_levels/U103_spin_zero.png)
![U103 ensemble](figs/pcot_vs_p2/U103_pcot_vs_p2.png)
![U103 ensemble](figs/pcot_vs_p2/U103_pcot_vs_p2_neg.png)


## Nf = 2

![E5 ensemble](figs/energy_levels/E5_spin_zero.png)
![E5 ensemble](figs/pcot_vs_p2/E5_pcot_vs_p2.png)
![E5 ensemble](figs/pcot_vs_p2/E5_pcot_vs_p2_neg.png)

![E1 ensemble](figs/energy_levels/E1_spin_zero.png)
![E1 ensemble](figs/pcot_vs_p2/E1_pcot_vs_p2.png)
![E1 ensemble](figs/pcot_vs_p2/E1_pcot_vs_p2_neg.png)


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
