import json

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ATLAS Open Data Exploration\n",
    "\n",
    "This notebook demonstrates how to use the `atlasopenmagic` package to access and analyze CERN ATLAS Open Data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import atlasopenmagic as atom\n",
    "import uproot\n",
    "import awkward as ak\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Setup Data Release\n",
    "\n",
    "First, we check available releases and set the active one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "releases = atom.available_releases()\n",
    "print(f\"Available releases: {releases}\")\n",
    "\n",
    "# Set to a common release\n",
    "atom.set_release('2024r-pp')\n",
    "print(\"Release set to 2024r-pp\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Retrieve Metadata\n",
    "\n",
    "Let's look at the metadata for a specific sample. Sample ID `361106` is often used for Z boson studies (Z -> mu mu)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "sid = '361106'\n",
    "metadata = atom.get_metadata(sid)\n",
    "print(f\"Metadata for {sid}:\")\n",
    "for key, value in metadata.items():\n",
    "    print(f\"{key}: {value}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Get Data URLs\n",
    "\n",
    "We can get the URLs to stream the data directly using `uproot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "urls = atom.get_urls(sid)\n",
    "print(f\"Found {len(urls)} files.\")\n",
    "if urls:\n",
    "    print(f\"Streaming from: {urls[0]}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Next Steps\n",
    "\n",
    "You can now use `uproot` to open these files and perform analysis:\n",
    "\n",
    "```python\n",
    "events = uproot.open(urls[0] + \":CollectionTree\")\n",
    "# Explore branches\n",
    "print(events.keys())\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_light_style": "long",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

with open('notebooks/exploration.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)
