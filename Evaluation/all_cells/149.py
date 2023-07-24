# Creating Programs
# create your first QuantumProgram object instance.
qp = QuantumProgram()

# Creating Registers
# create your first Quantum Register called "qr" with 2 qubits 
qr = qp.create_quantum_register('qr', 2)
# create your first Classical Register  called "cr" with 2 bits
cr = qp.create_classical_register('cr', 2)

# Creating Circuits
# create your first Quantum Circuit called "qc" involving your Quantum Register "qr"
# and your Classical Register "cr"
qc = qp.create_circuit('qc', [qr], [cr])