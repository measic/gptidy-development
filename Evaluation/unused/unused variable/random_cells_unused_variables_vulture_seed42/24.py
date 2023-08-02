backend = 'ibmqx2'   # Backend where you execute your program; in this case, on the Real Quantum Chip online 
circuits = ['Circuit']   # Group of circuits to execute
shots = 1024           # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 3          # Maximum number of credits to spend on executions. 
qp.set_api(Qconfig.APItoken, Qconfig.config['url']) # set the APIToken and API url

result_real = qp.execute(circuits, backend, shots=shots, max_credits=3, wait=10, timeout=240)