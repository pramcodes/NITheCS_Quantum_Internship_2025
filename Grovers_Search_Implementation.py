import pennylane as qml

# Task 2

dev = qml.device('default.qubit', wires = 2 + 1)

def Uf():
    qml.MultiControlledX(wires = [0,1,2], control_values = [1,1])
    
@qml.qnode(dev)
def mycircuit():
    
    qml.PauliX(2)
    
    qml.Hadamard(2)
    
    Uf()
    
    qml.Hadamard(2)
    
    qml.PauliX(2)
    
    return qml.state()

u = qml.matrix(mycircuit, wire_order = [2,1,0])()

for i in range(4):
    s=""
    for j in range(4):
        val = str(round(u[i][j].real, 3))
        while(len(val)<5): val  = " "+val
        s = s + val
    print(s)
    
###########################################

# Task 3

def inversion():
    
    
    qml.Hadamard(1)
    qml.Hadamard(0)
    
    qml.PauliX(1)
    qml.PauliX(0)

    qml.MultiControlledX(wires = [1,0,2], control_values = [1,1])

    qml.PauliX(1)
    qml.PauliX(0)
    
    qml.PauliX(2)
    
    qml.Hadamard(1)
    qml.Hadamard(0)
    
dev_inv = qml.device('default.qubit', wires = 3)

@qml.qnode(dev_inv)
def mycircuit1():
    qml.PauliX(2)
    qml.Hadamard(2)
    inversion()
    qml.Hadamard(2)
    qml.PauliX(2)
    return qml.state()

u_inv = qml.matrix(mycircuit1, wire_order = [2,1,0])()

for i in range(4):
    s=""
    for j in range(4):
        val = str(round(u_inv[i][j].real, 3))
        while(len(val)<5): val  = " "+val
        s = s + val
    print(s)

###########################################

# Task 5

def big_inversion():
    for i in range(3):
        qml.Hadamard(i)
        qml.PauliX(i)
    qml.MultiControlledX(wires = [1,0,4], control_values = [1,1])
    qml.MultiControlledX(wires = [2,4,3], control_values = [1,1])
    qml.MultiControlledX(wires = [1,0,4], control_values = [1,1])
    for i in range(3):
        qml.PauliX(i)
        qml.Hadamard(i)
    qml.PauliX(3)

big_dev = qml.device('default.qubit', wires = 5)

@qml.qnode(big_dev)
def big_mycircuit2():
    qml.PauliX(3)
    qml.Hadamard(3)
    big_inversion()
    qml.Hadamard(3)
    qml.PauliX(3)
    return qml.state()
    
u_big = qml.matrix(big_mycircuit2, wire_order = [4,3,2,1,0])()

for i in range(8):
    s=""
    for j in range(8):
        val = str(round(u_big[i][j].real, 3))
        while(len(val)<6): val  = " "+val
        s = s + val
    print(s)

###########################################

# Generalised Inversion Gate

Num_qubits = 4
dev_g = qml.device('default.qubit', wires = Num_qubits + 1)

@qml.qnode(dev_g)
def general_inversion():
    for i in range(Num_qubits):
        qml.Hadamard(i)
        qml.PauliX(i)
    qml.PauliX(Num_qubits)
    qml.Hadamard(Num_qubits)
    qml.MultiControlledX(wires = [n for n in range(Num_qubits+1)])
    qml.PauliX(Num_qubits)
    qml.Hadamard(Num_qubits)
    qml.PauliX(Num_qubits)
    for i in range(Num_qubits):
        qml.PauliX(i)
        qml.Hadamard(i)
    return qml.state()

order = [(Num_qubits - p) for p in range(Num_qubits+1)]
unit = qml.matrix(general_inversion, wire_order = order)()

for i in range(2**Num_qubits):
    s=""
    for j in range(2**Num_qubits):
        val = str(round(unit[i][j].real, 3))
        while(len(val)<6): val  = " "+val
        s = s + val
    print(s)
    