# LELEC1360-Labs

Repository for the laboratories of the telecommunication course LELEC1360 @UCLouvain (attended in 25-26)
Laboratories subjects includes : 
- Lab1 : AM Modulations (A3 & DSB-SC)
- Lab2 : FM Modulation
- Lab3 : Grouping in symboles and decision rules in numerical modulations
- Lab4 : subject to be completed

To run the python file of a lab run : python labs/labX.py
By default, all the pertinent graphs for the laboratories are saved in a the figures/labX folder. 

## Contributing to the project

Contributions to this project are highly encouraged. You can find in this section information about the way to contribute in order to keep the code readable. 

### Structure of the project

The project is structured as follows:
 
```
LELEC1360-Labs/
├── lib/
│   ├── signals.py          # Time axis and signal generation
│   ├── modulations.py      # Modulation functions (A3, DSB-SC, FM, ...)
│   ├── demodulations.py    # Demodulation functions
│   └── plotting.py         # Plotting utilities
├── labs/
│   ├── lab1-AM.py
│   ├── lab2-FM.py
│   └── ...
└── figures/
    ├── lab1/
    └── ...
```
### Adding a new lab
 
1. Create the main script at `labs/labX.py`.
2. Add any new signal processing functions to the appropriate `lib/` module (`modulations.py`, `demodulations.py`, etc.) rather than defining them locally in the lab script.
3. Make sure figures are saved to `figures/labX/` — the directory is created automatically at runtime via `os.makedirs`.

### Adding to the lib
 
- Each function must have a docstring describing its parameters and return value.
- Use `fs` (sampling frequency) as a direct parameter rather than recomputing it from a time array inside the function.
- Keep modulation and demodulation functions side-effect free (no plotting, no `print`).

### Code presentation 

- Please use meaningful parameter names (`message`, `carrier` rather than `signal1`, `signal2`).
- Physical quantities should ideally carry their unit in a comment or docstring. 
