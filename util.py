import argparse

circuitGen = None
jsonFile = None
qubitsPerChain = None
numQubits = -1
q1latency = -1
q2latency = -1
num1qGates = -1
num2qGates = -1
weaklink = -1

verbose = False
debug = False

def check_args(args=None):
    parser = argparse.ArgumentParser(description='Arguments')
    parser.add_argument('-c', '--circuit',
                        help="Input circuit ('random', 'json', 'cmd')",
                        default='random',
                        )

    parser.add_argument('-j', '--json',
                        help="Input json file for circuit",
                        default="",
                        )

    parser.add_argument('-s', '--chainsize',
                        help="Number of qubits in a chain",
                        type=int,
                        default=4,
                        )

    parser.add_argument('-q', '--qubits',
                        help="Total number of qubits",
                        type=int,
                        default=4, #BUG: if this is 16, it doesn't produce a valid circuit
                        )

    parser.add_argument('-q1', '--q1latency',
                        help="1-Qubit gate latency",
                        type=int,
                        default=16,
                        )

    parser.add_argument('-q2', '--q2latency',
                        help="2-Qubit gate latency",
                        type=int,
                        default=12,
                        )

    parser.add_argument('-g1', '--gates1',
                        help="Total 1-Qubit gates",
                        type=int,
                        default=16,
                        )

    parser.add_argument('-g2', '--gates2',
                        help="Total 2-Qubit gates ",
                        type=int,
                        default=16,
                        )

    parser.add_argument('-w', '--weaklink',
                        help="Weak Link scale factor penalty",
                        type=int,
                        default=16,
                        )

    parser.add_argument('-v', '--verbose',
                        help="Include print statements",
                        nargs='?',
                        const=True,
                        default=False
                        )

    parser.add_argument('-d', '--debug',
                        help="Debug mode",
                        nargs='?',
                        const=True,
                        default=False
                        )



    results = parser.parse_args(args)

    # access to globals
    global circuitGen, jsonFile, qubitsPerChain, numQubits, q1latency, q2latency, weaklink, \
            num1qGates, num2qGates, \
            verbose

    # assign parsed arg to global
    circuitGen = results.circuit
    jsonFile = results.json
    qubitsPerChain = results.chainsize
    numQubits = results.qubits
    q1latency = results.q1latency
    q2latency = results.q2latency
    num1qGates = results.gates1
    num2qGates = results.gates2
    weaklink = results.weaklink
    verbose = results.verbose


# access variables
def getCircuitInput(): return circuitGen
def getJsonFile(): return jsonFile
def getChainSize(): return qubitsPerChain
def getNumQubits(): return numQubits
def getq1latency(): return q1latency
def getq2latency(): return q2latency
def getnum1qGates(): return num1qGates
def getnum2qGates(): return num2qGates
def getWeakLinkPen(): return weaklink
def getVerbose(): return verbose
def getDebug(): return debug

def printArgs():
    print("Command Line Args:")
    print("\tCircuit: ", getCircuitInput())
    print("\tJsonFile: ", getJsonFile())
    print("\tChain Size: ", getChainSize() )
    print("\tNum Qubits: ", getNumQubits())
    print("\tq1 Latency: ", getq1latency())
    print("\tq2 Latency: ", getq2latency())
    print("\t1-Qubit Gates: ", getnum1qGates())
    print("\t2-Qubit Gates: ", getnum2qGates())
    print("\tWeakLink Penalty: ", getWeakLinkPen())
    print("\tVerbose: ", getVerbose())
    print("\tDebug: ", getDebug())

