# OgbonLab Notebooks

Runnable seismic modelling notebooks from the [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) at [ogbonlab.com](https://ogbonlab.com).

<p align="center">
  <img src="assets/ssm_field_realistic_section.png" width="820"
       alt="Two panels. Left: the field earth's impedance in depth, 3.6 km across and 1.6 km deep, a folded and faulted package of sand and shale beds cut by an angular unconformity beneath a draped overburden with a channel. Right: the seismic section it produces in two-way time, with a Ricker whose frequency falls with time and noise in the band of the data, showing the anticline, fault breaks, truncated reflectors, the channel, and a gas bright spot with a flat spot at its base on the flank of the crest, both labelled.">
  <br>
  <sub>What <a href="notebooks/ssm_field_realistic_section.ipynb">ssm_field_realistic_section</a> computes: the field earth every notebook shares, and the seismic section it produces. numpy and matplotlib only, unedited output of running the notebook.</sub>
</p>

Each notebook is self-contained: it generates its own data, needs only numpy and matplotlib, and runs top to bottom in under a minute on the free Colab tier. All eight together compute in about a second and a half on an ordinary laptop CPU (about 11 s with a fresh Jupyter kernel started for each). Edit the parameters cell and run again; every value is yours to change.

## One field earth, in every notebook

Every notebook builds on one seeded **field earth**, defined once and carried whole by each: thin sand and shale beds over a regional dip, folded into an asymmetric anticline; normal faults, the largest a listric growth fault whose throw grows with depth and whose hanging wall rolls over into it; uplift and an angular unconformity that cuts the crest; a reservoir sand that subcrops beneath the unconformity, wedges out against it, shales out to the left and is sealed by a shale cap and holds gas over a flat contact; and a draped overburden with a channel. Each rock's velocity follows the compaction trend at its deepest burial, so the uplifted rocks under the unconformity are faster than their depth alone would make them, and sands are soft when shallow and hard when deep; density is Gardner's, and the reservoir and its seal are the course's standard rocks. The sections are imaged with a Ricker whose peak falls with time as a constant Q says, plus noise in the band of the data.

Each notebook first prints the numbers the course's Ask Ogbon advisor computes for the same answers (as `name = value`), then puts the same physics to work in the field earth and prints what it measures there (as `[field] name = value`).

## The notebooks

| Notebook | What it does | Run it |
|---|---|---|
| [ssm_field_realistic_section](notebooks/ssm_field_realistic_section.ipynb) | The flagship: build the field earth in the open, stage by stage, then image it | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_field_realistic_section.ipynb) |
| [ssm_convolutional_synthetic](notebooks/ssm_convolutional_synthetic.ipynb) | A well drilled into the gas: its logs, its synthetic, and the tie that finds a datum shift | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_convolutional_synthetic.ipynb) |
| [ssm_wedge_tuning](notebooks/ssm_wedge_tuning.ipynb) | Tuning along the reservoir's real pinch-out against the unconformity, against the wedge's curve | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_wedge_tuning.ipynb) |
| [ssm_fault_ml_dataset](notebooks/ssm_fault_ml_dataset.ipynb) | Sections from the field earth's family with pixel-exact fault, horizon or facies labels, saved as .npz | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fault_ml_dataset.ipynb) |
| [ssm_avo_gassmann_dhi](notebooks/ssm_avo_gassmann_dhi.ipynb) | Gassmann puts gas in the trap: near and far stacks with the bright spot and flat spot, and the AVO curves | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_avo_gassmann_dhi.ipynb) |
| [ssm_timelapse_4d_co2](notebooks/ssm_timelapse_4d_co2.ipynb) | A CO2 plume fills the trap: baseline, monitor and difference, the NRMS and the time shifts beneath | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_timelapse_4d_co2.ipynb) |
| [ssm_acoustic_fd_lab](notebooks/ssm_acoustic_fd_lab.ipynb) | A finite-difference shot through a window of the field earth, and what its structure adds to the record | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_acoustic_fd_lab.ipynb) |
| [ssm_fracture_avaz_hti](notebooks/ssm_fracture_avaz_hti.ipynb) | Cracks that strike with the faults: the AVAz swing along the reservoir, and the strike recovered | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fracture_avaz_hti.ipynb) |

## What they produce

Every figure below is the unedited output of running its notebook top to bottom (`tools/render_assets.py` executes the notebooks and saves what they draw; `tools/render_fd_gif.py` animates the finite-difference notebook's own arrays).

<p align="center">
  <img src="assets/fd-lab-wavefield.gif" width="760"
       alt="An animation of a finite-difference acoustic wavefield in a 1.4 km window of the field earth around its crest: the wavefront expands from a surface source over the faint velocity layering, crosses the unconformity and the crest, and sends reflections back up, while beside it the record of what the structure adds, the shot minus the same shot through the smoothed earth, builds down in time as reflection hyperbolas appear.">
  <br>
  <sub>What <a href="notebooks/ssm_acoustic_fd_lab.ipynb">ssm_acoustic_fd_lab</a> computes, animated: the notebook's own model, stencil, sponge and source, its wavefield captured as its time loop runs.</sub>
</p>

<p align="center">
  <img src="assets/ssm_acoustic_fd_lab.png" width="760" alt="Three panels from the finite-difference notebook: the wavefield at 379 ms over the contours of the window's layering, the wavefront crossing the crest with a reflection rising from it; the shot record with its direct wave and reflection hyperbolas, gained by time squared; and the record minus the record of the smoothed earth, muted above the direct wave, leaving the reflections and the diffraction tails the structure makes.">
  <br>
  <sub><a href="notebooks/ssm_acoustic_fd_lab.ipynb">ssm_acoustic_fd_lab</a> · the shot, the record, and what the structure adds to it</sub>
</p>

<p align="center">
  <img src="assets/ssm_convolutional_synthetic.png" width="760" alt="Three panels of the well tie: the acoustic impedance log of a well through the gas in two-way time, with the gas sand's low impedance near 650 ms; the synthetic against the seismic trace at the well, untied (dotted, correlation -0.21) and shifted 12 ms (solid, correlation 0.97); and the field section with the tied synthetic drawn as a red wiggle at the borehole.">
  <br>
  <sub><a href="notebooks/ssm_convolutional_synthetic.ipynb">ssm_convolutional_synthetic</a> · the well tie in its section, the datum shift found by correlation</sub>
</p>

<p align="center">
  <img src="assets/ssm_wedge_tuning.png" width="760" alt="Two panels: the field section where the gas-filled reservoir wedges out against the unconformity, its top marked trace by trace; and the amplitude at the top of the sand against the bed's two-way thickness, brightest at the 13.0 ms tuning time marked with a dashed line, not at the quarter wavelength; the field's points peak at 0.24 against the 1D wedge's 0.20 and follow a second curve, the same wedge with the field's own top and base coefficients (the shale under the sand is harder than the cap above it).">
  <br>
  <sub><a href="notebooks/ssm_wedge_tuning.ipynb">ssm_wedge_tuning</a> · tuning along a real pinch-out</sub>
</p>

<p align="center">
  <img src="assets/ssm_fault_ml_dataset.png" width="760" alt="Four synthetic sections in the top row, each a different member of the field earth's family, with its own crest, fold, dip, one to three normal faults, an unconformity or none, and its own signal-to-noise, and their pixel-exact fault-mask labels in the bottom row.">
  <br>
  <sub><a href="notebooks/ssm_fault_ml_dataset.ipynb">ssm_fault_ml_dataset</a> · varied, faulted, noisy sections with exact labels, saved for training</sub>
</p>

<p align="center">
  <img src="assets/ssm_avo_gassmann_dhi.png" width="760" alt="Three panels: the near stack at 8 degrees and the far stack at 30 degrees of the trap, at one clip, with the top of the gas and the flat spot at the gas-brine contact labelled, the gas brighter on the far stack; and the reflection coefficient against incidence angle for the brine and gas sands under the standard shale, with the field's crest and downdip points, read from the earth's own cells under its shale seal, lying on those curves.">
  <br>
  <sub><a href="notebooks/ssm_avo_gassmann_dhi.ipynb">ssm_avo_gassmann_dhi</a> · a bright spot, a flat spot, and AVO at the crest and downdip</sub>
</p>

<p align="center">
  <img src="assets/ssm_timelapse_4d_co2.png" width="760" alt="Three panels over the trap: the baseline section with brine in the reservoir, the monitor section with CO2 in 40 percent of its pore space, and their difference at the same clip, in which the plume stands out on both flanks of the crest above the repeat noise, with time-shift stripes beneath it.">
  <br>
  <sub><a href="notebooks/ssm_timelapse_4d_co2.ipynb">ssm_timelapse_4d_co2</a> · the plume fills the trap; the difference shows it, and the time shifts beneath it</sub>
</p>

<p align="center">
  <img src="assets/ssm_fracture_avaz_hti.png" width="760" alt="Three panels: the field earth in depth with its reservoir coloured by crack density, densest beside the faults drawn in cyan; the swing of the reflection coefficient at 30 degrees, across minus along the fractures, along the reservoir, peaking at the major fault; and the coefficient against acquisition azimuth at the most fractured trace, noisy measurements with a fitted cos 2(azimuth) curve whose minimum marks the strike found, 28.3 degrees against the true 30.">
  <br>
  <sub><a href="notebooks/ssm_fracture_avaz_hti.ipynb">ssm_fracture_avaz_hti</a> · fractures that strike with the faults, and the strike from azimuthal AVO</sub>
</p>

<p align="center">
  <img src="assets/ssm_field_realistic_section_geology.png" width="760" alt="Four panels building the field earth: the beds with their regional dip and asymmetric anticline; the same beds cut by normal faults drawn in red, the largest a growth fault; the finished earth, with the angular unconformity in gold, the reservoir outlined in white, its gas in magenta, the channel in orange, and labels for the unconformity, the gas over a flat contact, the wedge-out, the shale-out, the channel and the growth fault; and P velocity against depth through the gas and down the right flank, against the compaction trend.">
  <br>
  <sub><a href="notebooks/ssm_field_realistic_section.ipynb">ssm_field_realistic_section</a> · the field earth, built in geological order, before it is imaged</sub>
</p>

## Three ways to run

1. **One click**: press an Open in Colab badge above. Colab loads the notebook straight from this repository.
2. **Your own copy**: the [Ask Ogbon advisor](https://ogbonlab.com/textbooks/synthetic-seismic-modeling/part-12-the-modeling-lab/whats-next) on ogbonlab.com generates a personalized notebook from your answers. Download it, then upload at [colab.research.google.com/upload](https://colab.research.google.com/upload).
3. **Locally**: `pip install numpy matplotlib jupyter`, then open any notebook.

## Where these come from

The [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) teaches the forward problem in 13 parts: wavelets, reflectivity, the convolutional model, finite differences, elastic AVO, anisotropy, fracture physics, earth models, and a Modeling Lab. The course's closing advisor generates these starter programs; the notebooks here are the curated set with course defaults, plus the flagship field-realistic section built for this repository.

Note: most sections here are the processed, migrated-image idealization, 1D convolution trace by trace in time, with noise in the band of the data; they have no diffractions. The finite-difference lab is the exception: it propagates the full acoustic wavefield, diffractions and all. Each notebook says which it is.

The through-line of the course, and of every notebook here: use the cheapest engine that carries the physics your question depends on.

## License

MIT. Use them in courses, workshops, or your own research.
