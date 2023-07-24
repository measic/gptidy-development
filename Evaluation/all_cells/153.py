# Pauli X gate to qubit 1 in the Quantum Register "qr" 
circuit.x(quantum_r[1])

# Pauli Y gate to qubit 2 in the Quantum Register "qr" 
circuit.y(quantum_r[2])

# Pauli Z gate to qubit 3 in the Quantum Register "qr" 
circuit.z(quantum_r[3])

# CNOT (Controlled-NOT) gate from qubit 0 to qubit 2
circuit.cx(quantum_r[0], quantum_r[2])

# add a barrier to your circuit
circuit.barrier()

# H (Hadamard) gate to qubit 0 in the Quantum Register "qr" 
circuit.h(quantum_r[0])

# S Phase gate to qubit 0
circuit.s(quantum_r[0])

# T Phase gate to qubit 1
circuit.t(quantum_r[1])

# identity gate to qubit 1
circuit.iden(quantum_r[1])

# first physical gate: u1(lambda) to qubit 0
circuit.u1(0.3, quantum_r[0])

# second physical gate: u2(phi,lambda) to qubit 1
circuit.u2(0.3, 0.2, quantum_r[1])

# second physical gate: u3(theta,phi,lambda) to qubit 2
circuit.u3(0.3, 0.2, 0.1, quantum_r[2])

# rotation around the x-axis to qubit 0
circuit.rx(0.2, quantum_r[0])

# rotation around the y-axis to qubit 1
circuit.ry(0.2, quantum_r[1])

# rotation around the z-axis to qubit 2
circuit.rz(0.2, quantum_r[2])

# Classical if, from qubit2 gate Z to classical bit 1
# circuit.z(quantum_r[2]).c_if(classical_r, 0)

# measure gate from qubit 0 to classical bit 0
circuit.measure(quantum_r[0], classical_r[0])
circuit.measure(quantum_r[1], classical_r[1])
circuit.measure(quantum_r[2], classical_r[2])