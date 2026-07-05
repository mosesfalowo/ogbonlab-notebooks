# OgbonLab Notebooks

Runnable seismic modelling notebooks from the [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) at [ogbonlab.com](https://ogbonlab.com).

Each notebook is self-contained: it generates its own data, needs only numpy and matplotlib, and runs top to bottom in under a minute on the free Colab tier. Edit the parameters cell and run again; every value is yours to change.

## The notebooks

| Notebook | What it does | Run it |
|---|---|---|
| [ssm_convolutional_synthetic](notebooks/ssm_convolutional_synthetic.ipynb) | Logs to reflectivity to trace: the standard well tie | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_convolutional_synthetic.ipynb) |
| [ssm_wedge_tuning](notebooks/ssm_wedge_tuning.ipynb) | The wedge model: tuning thickness and vertical resolution | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_wedge_tuning.ipynb) |
| [ssm_fault_ml_dataset](notebooks/ssm_fault_ml_dataset.ipynb) | Synthetic sections with exact fault masks: ML training data | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fault_ml_dataset.ipynb) |
| [ssm_avo_gassmann_dhi](notebooks/ssm_avo_gassmann_dhi.ipynb) | Gassmann fluid substitution and AVO: is the bright spot real? | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_avo_gassmann_dhi.ipynb) |
| [ssm_timelapse_4d_co2](notebooks/ssm_timelapse_4d_co2.ipynb) | Baseline vs monitor for a CO2 plume, judged against repeatability | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_timelapse_4d_co2.ipynb) |
| [ssm_acoustic_fd_lab](notebooks/ssm_acoustic_fd_lab.ipynb) | A finite-difference acoustic wavefield you can watch propagate | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_acoustic_fd_lab.ipynb) |
| [ssm_fracture_avaz_hti](notebooks/ssm_fracture_avaz_hti.ipynb) | HTI rock physics and azimuthal AVO: recover fracture strike | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mosesfalowo/ogbonlab-notebooks/blob/main/notebooks/ssm_fracture_avaz_hti.ipynb) |

## Three ways to run

1. **One click**: press an Open in Colab badge above. Colab loads the notebook straight from this repository.
2. **Your own copy**: the [Ask Ogbon advisor](https://ogbonlab.com/textbooks/synthetic-seismic-modeling/part-12-the-modeling-lab/whats-next) on ogbonlab.com generates a personalized notebook from your answers. Download it, then upload at [colab.research.google.com/upload](https://colab.research.google.com/upload).
3. **Locally**: `pip install numpy matplotlib jupyter`, then open any notebook.

## Where these come from

The [Synthetic Seismic Modeling course](https://ogbonlab.com/textbooks/synthetic-seismic-modeling) teaches the forward problem in 13 parts: wavelets, reflectivity, the convolutional model, finite differences, elastic AVO, anisotropy, fracture physics, earth models, and a Modeling Lab. The course's closing advisor generates these starter programs; the notebooks here are the curated set with course defaults.

The through-line of the course, and of every notebook here: use the cheapest engine that carries the physics your question depends on.

## License

MIT. Use them in courses, workshops, or your own research.
