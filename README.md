# HDRchallenge

Supporting code for the A3D3 HDR challenge.

---

## Introduction

Gravitational waves are ripples in spacetime caused by the acceleration of massive objects. Predicted by Einstein in 1916, they travel at the speed of light, carrying information about their origins and the nature of gravity. The Laser Interferometer Gravitational-wave Observatory (LIGO) detects these waves using laser interferometers in Hanford, Washington, and Livingston, Louisiana.

Having two LIGO interferometers is crucial because it allows for the verification of signals, distinguishing them from local noise and artifacts that are uncorrelated between the two locations. This dual setup also improves the localization of gravitational wave sources by comparing the arrival times of signals at each detector.

To identify transient gravitational waves, scientists use matched filtering, comparing LIGO data with known templates from systems whose gravitational-wave emission can be analytically or numerically calculated (e.g., merging black holes). This method is effective for well-understood sources but less so for unknown phenomena where signal morphologies are poorly modeled or completely unknown.

---

## Problem Setting

The Anomaly Detection Challenge focuses on data from LIGO's O3 observations — gravitational-wave strain h(t) time series recorded by two LIGO interferometers. We provide several datasets, including whitened, bandpass-filtered data from O3, with known GW events corresponding to binary coalescences removed. The dataset also contains simulated signals injected into real instrument data.

Participants are tasked with training their models primarily on the instrument data to detect anomalies, and may also leverage information from the simulated signals to enhance their detection methods.

---

## Gravitational Wave Sources

### Known transient GW sources (detectable with matched-filtering pipelines)

1. **Binary Black Hole (BBH) Mergers** — Two black holes orbiting and eventually merging. Produce strong, detectable gravitational waves during the final moments of merger.
2. **Binary Neutron Star (BNS) Mergers** — Two neutron stars spiraling together and merging. Emit gravitational waves as they orbit and merge, followed by electromagnetic signals including gamma-ray bursts.
3. **Black Hole - Neutron Star (BHNS) Mergers** — A black hole and neutron star in a binary system merging. Create gravitational waves and potentially a variety of electromagnetic emissions.

### Unmodeled transient GW sources / "anomalies" (not yet detected with matched-filtering pipelines)

1. **Supernovae** — Explosive deaths of massive stars. Can produce gravitational waves, especially in cases of asymmetric explosions.
2. **Neutron Star Glitches** — Sudden, small changes in the spin frequency of pulsars may be associated with transient gravitational-wave emission.
3. **Cosmic Strings** — Hypothetical one-dimensional topological defects in spacetime. Could produce bursts of gravitational waves when they interact or oscillate.
4. **Fast Radio Bursts / Gamma-Ray Bursts** — Astrophysical phenomena energetic enough to be plausibly associated with gravitational-wave emission, but with incomplete progenitor models.
5. **Completely unknown sources** — GW detectors are fairly new instruments and the GW sky is largely unexplored; completely new astrophysical systems remain a possibility.

---

## Challenge Goal

Develop machine learning algorithms capable of identifying anomalous (transient) gravitational-wave signals from unknown sources. Participants train models on the provided LIGO O3 datasets, focusing on detecting unusual patterns in strain data without relying on pre-defined templates. The challenge concludes with testing on a held-out sample containing "secret" anomalies not included in the training data.

---

## Questions

Please open an issue on the [GitHub issues page](https://github.com/a3d3-institute/HDRchallenge/issues).

---

## License

This project is licensed under the [MIT License](LICENSE).
