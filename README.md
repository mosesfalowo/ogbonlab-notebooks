# OgbonLab Notebooks

Runnable seismic modelling notebooks from the [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) at [ogbonlab.com](https://ogbonlab.com).

<p align="center">
  <img src="assets/ssm_field_realistic_section.png" width="820"
       alt="Two panels: a field-realistic 2D impedance model in depth, with a folded and faulted deep package truncated by an angular unconformity beneath a draped overburden, and the seismic image it produces in two-way time, with band-limited noise, a fold crest, fault breaks, and truncating reflectors.">
  <br>
  <sub>What <a href="notebooks/ssm_field_realistic_section.ipynb">ssm_field_realistic_section</a> computes: a geologically built earth, folded, faulted, truncated, and draped, and the seismic image it produces. numpy and matplotlib only, unedited output of running the notebook.</sub>
</p>

Each notebook is self-contained: it generates its own data, needs only numpy and matplotlib, and runs top to bottom in under a minute on the free Colab tier (all eight together take under ten seconds on an ordinary laptop CPU). Edit the parameters cell and run again; every value is yours to change.

Four of the notebooks share one **field-realistic earth model**: a deep package of thin beds carrying regional dip and an asymmetric anticline, cut by three normal faults, truncated by an angular unconformity with a reservoir sand subcropping at the crest, then draped by a post-unconformity package with a channel. The well tie sits in it, the wavefield propagates through it, the CO2 plume fills its trap, and the flagship builds it in the open.

## The notebooks

| Notebook | What it does | Run it |
|---|---|---|
| [ssm_field_realistic_section](notebooks/ssm_field_realistic_section.ipynb) | The flagship: build the field-realistic earth, then image it | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_field_realistic_section.ipynb) |
| [ssm_convolutional_synthetic](notebooks/ssm_convolutional_synthetic.ipynb) | Logs to reflectivity to trace: the well tie, shown in its section | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_convolutional_synthetic.ipynb) |
| [ssm_wedge_tuning](notebooks/ssm_wedge_tuning.ipynb) | The wedge model: tuning thickness and vertical resolution | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_wedge_tuning.ipynb) |
| [ssm_fault_ml_dataset](notebooks/ssm_fault_ml_dataset.ipynb) | Folded, faulted sections with pixel-exact masks: ML training data | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fault_ml_dataset.ipynb) |
| [ssm_avo_gassmann_dhi](notebooks/ssm_avo_gassmann_dhi.ipynb) | Gassmann fluid substitution and AVO: is the bright spot real? | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_avo_gassmann_dhi.ipynb) |
| [ssm_timelapse_4d_co2](notebooks/ssm_timelapse_4d_co2.ipynb) | Baseline vs monitor for a CO2 plume filling the field model's trap | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_timelapse_4d_co2.ipynb) |
| [ssm_acoustic_fd_lab](notebooks/ssm_acoustic_fd_lab.ipynb) | A finite-difference wavefield propagating through the field model | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_acoustic_fd_lab.ipynb) |
| [ssm_fracture_avaz_hti](notebooks/ssm_fracture_avaz_hti.ipynb) | HTI rock physics and azimuthal AVO: recover fracture strike | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fracture_avaz_hti.ipynb) |

## What they produce

Every figure below is the unedited output of running its notebook top to bottom (`tools/render_assets.py` executes the notebooks and saves what they draw).

<p align="center">
  <img src="assets/fd-lab-wavefield.gif" width="740"
       alt="A finite-difference acoustic wavefield propagating through the folded and faulted field model, its wavefront crossing the unconformity and fault as backscattered reflections trail behind, next to the surface record building one time sample per step as diffraction hyperbolas appear.">
  <br>
  <sub>What <a href="notebooks/ssm_acoustic_fd_lab.ipynb">ssm_acoustic_fd_lab</a> computes, animated: the same arrays the notebook plots, rendered as its time loop runs, through the field model's fold, faults, and unconformity.</sub>
</p>

| | |
|:---:|:---:|
| <img src="assets/ssm_convolutional_synthetic.png" width="430" alt="Three panels of the well tie: an acoustic impedance log in two-way time, the synthetic trace it produces after convolution, and the full field-realistic section with the well marked and the synthetic wiggle overlaid in place at the borehole."> | <img src="assets/ssm_fracture_avaz_hti.png" width="370" alt="A polar plot of the azimuthal AVO gradient: a fitted ellipse whose long axis aligns with the fracture strike, with noisy measurements scattered around it."> |
| [ssm_convolutional_synthetic](notebooks/ssm_convolutional_synthetic.ipynb) · the well tie, in its section | [ssm_fracture_avaz_hti](notebooks/ssm_fracture_avaz_hti.ipynb) · fracture strike from azimuthal AVO |
| <img src="assets/ssm_wedge_tuning.png" width="450" alt="The tuning curve: peak amplitude against bed thickness, rising to a maximum below the predicted 25 m tuning thickness marked by a dashed line."> | <img src="assets/ssm_avo_gassmann_dhi.png" width="392" alt="Two AVO curves, reflection coefficient against incidence angle: a brine baseline and the gas-substituted case diverging below it; the deviation from brine is the fluid signal."> |
| [ssm_wedge_tuning](notebooks/ssm_wedge_tuning.ipynb) · where thin beds stop being resolvable | [ssm_avo_gassmann_dhi](notebooks/ssm_avo_gassmann_dhi.ipynb) · is the bright spot fluid or lithology? |

<p align="center">
  <img src="assets/ssm_fault_ml_dataset.png" width="760" alt="Four synthetic seismic sections in the top row, each with folded or dipping beds cut by normal faults at varying signal-to-noise, and their pixel-exact fault-mask labels in the bottom row.">
  <br>
  <sub><a href="notebooks/ssm_fault_ml_dataset.ipynb">ssm_fault_ml_dataset</a> · folded, faulted, noisy sections with pixel-exact labels, ready for training</sub>
</p>

<p align="center">
  <img src="assets/ssm_timelapse_4d_co2.png" width="760" alt="Three panels: a baseline section of the field model, a monitor section, and their difference, in which a CO2 plume anomaly conformal to the fold crest stands out above repeatability noise with time-shift stripes beneath it.">
  <br>
  <sub><a href="notebooks/ssm_timelapse_4d_co2.ipynb">ssm_timelapse_4d_co2</a> · the plume fills the trap; the difference shows it, plus the time shifts every real 4D carries</sub>
</p>

<p align="center">
  <img src="assets/ssm_field_realistic_section_geology.png" width="760" alt="The field model annotated: an angular unconformity in gold truncating folded beds, the reservoir sand in red subcropping at the fold crest, a channel, and a growth fault, over the impedance image in depth.">
  <br>
  <sub><a href="notebooks/ssm_field_realistic_section.ipynb">ssm_field_realistic_section</a> · the geology, assembled and annotated, before it is imaged</sub>
</p>

## Three ways to run

1. **One click**: press an Open in Colab badge above. Colab loads the notebook straight from this repository.
2. **Your own copy**: the [Ask Ogbon advisor](https://ogbonlab.com/textbooks/synthetic-seismic-modeling/part-12-the-modeling-lab/whats-next) on ogbonlab.com generates a personalized notebook from your answers. Download it, then upload at [colab.research.google.com/upload](https://colab.research.google.com/upload).
3. **Locally**: `pip install numpy matplotlib jupyter`, then open any notebook.

## Where these come from

The [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) teaches the forward problem in 13 parts: wavelets, reflectivity, the convolutional model, finite differences, elastic AVO, anisotropy, fracture physics, earth models, and a Modeling Lab. The course's closing advisor generates these starter programs; the notebooks here are the curated set with course defaults, plus the flagship field-realistic section built for this repository.

Note: the sections here are the processed, migrated-image idealization (per-trace 1D convolution in time), with band-limited noise at survey-quality S/N. The finite-difference lab is the exception; it propagates the full acoustic wavefield, diffractions and all. Each notebook says which it is.

The through-line of the course, and of every notebook here: use the cheapest engine that carries the physics your question depends on.

## License

MIT. Use them in courses, workshops, or your own research.
