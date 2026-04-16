from abaqus import *
from abaqusConstants import *
import __main__
import numpy as np
from inputParams import *  # Import all parameters
import time

from UCModel import UCModel
import numpy as np
import csv

# Assuming that UCModel and necessary modules are imported above


# Define a range of values for t_t
prestress_vals = np.linspace(0, 10, 5)

# Open CSV file for recording results
with open('t_t_simulation_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['prestress', 'inflection_status', 'radius']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write header
    
    # Loop through defined t_t values and run the simulation
    for i in range(len(prestress_vals)):

        prestress = prestress_vals[i]
        
        # Run the model with the current parameters
        inflection_status, radius = UCModel(
            L, w_f, E1_FRP, E2_FRP, nu12_FRP,
            G12_FRP, G13_FRP, G23_FRP, rho_FRP, 
            rho_m, C10_m, D1_m, rho_t, E_t, nu_t, t_t, 
            t_FRP, layup, meshSize, prestress, uz_pull, cpus)

        # Write results to CSV
        writer.writerow({
            'prestress': prestress,
            'inflection_status': inflection_status,
            'radius': radius,
        })

print("All simulations completed. Results saved in 't_t_simulation_results.csv'.")