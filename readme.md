# Freshwater Inflow to Galveston Bay during Hurricane Harvey

I recommend setting up an environment in conda to get the necessary packages without changing anything in your normal Python setup.

## Setup Conda Environment

* Install miniconda:
  * download file from [Anaconda downloads](https://docs.conda.io/en/latest/miniconda.html). Choose 64-bit for your operating system.
  * open terminal window
  * navigate to where .sh file is
  * in terminal window, install miniconda:
    * `bash [download file from Anaconda downloads]`
* Set up conda environment
  *  in add conda-forge channel to top of channels
     * `conda config --add channels conda-forge --force`
  * Create conda environmenta called `harvey` with the packages listed already installed
    * `conda create --name harvey cartopy matplotlib ipython jupyter netCDF4 pandas cmocean numpy scipy xarray shapely fiona dask  --yes`
* Switch to new environment: in terminal window type:
  * `source activate harvey`
* Install another package into environment (not available in conda-forge):
  * available at github.com/kthyng/tabs; installation instructions there
  * or just pip install: `pip install tabs-buoys`


## Get notebooks

Navigate to where you want the notebooks on your computer in a terminal window, then clone the project github repo:
`git clone https://github.com/kthyng/harvey_inflow`


## Start jupyter notebook server

Within the project directory, open a local jupyter notebook server. In a terminal window, type:
`jupyter notebook` and the server will open in a browser window.


## Run instructions

To reproduce the work in this paper, open and run notebook `run`, which will run the other notebooks in proper order.
