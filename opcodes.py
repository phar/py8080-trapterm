FLAGS_BASE = 0xb00000010
FLAGS_SIGN_FLAG     = 0b10000000
FLAGS_ZERO_FLAG     = 0b01000000
FLAGS_AUXCARRY_FLAG = 0b00100000
FLAGS_PARITY_FLAG   = 0b00000100
FLAGS_CARRY_FLAG    = 0b00000001

TYPE_MISC		= 0
TYPE_BRANCH		= 1
TYPE_MOVE_8		= 2
TYPE_MOVE_16	= 3
TYPE_LOGIC_8	= 4
TYPE_LOGIC_16	= 5
TYPE_COMPARE	= 6


ARG_TYPE_A  = 0
ARG_TYPE_B  = 1
ARG_TYPE_C  = 2
ARG_TYPE_H  = 3
ARG_TYPE_L  = 4
ARG_TYPE_D  = 5
ARG_TYPE_E  = 6
ARG_TYPE_SP  = 7
ARG_TYPE_M  = 8
ARG_TYPE_0  = 9
ARG_TYPE_1  = 10
ARG_TYPE_2  = 11
ARG_TYPE_3  = 12
ARG_TYPE_4  = 13
ARG_TYPE_5  = 14
ARG_TYPE_6  = 15
ARG_TYPE_7  = 16
ARG_TYPE_d8  = 17
ARG_TYPE_d16  = 18
ARG_TYPE_a16  = 19
ARG_TYPE_PSW  = 20






Opcodes8080 = [{'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   0,
  'opstr': 'NOP'},
 {'arg': ['B', 'd16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   1,
  'opstr': 'LXI'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   2,
  'opstr': 'STAX'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   3,
  'opstr': 'INX'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   4,
  'opstr': 'INR'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   5,
  'opstr': 'DCR'},
 {'arg': ['B', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   6,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   7,
  'opstr': 'RLC'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   8,
  'opstr': 'NOP'},
 {'arg': ['B'],
  'l': 1,
  'f': {   'C': True,    },
  'c': [10,10],
  'type':TYPE_LOGIC_16,
  'op':   9,
  'opstr': 'DAD'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MISC,
  'op':   10,
  'opstr': 'LDAX'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   11,
  'opstr': 'DCX'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   12,
  'opstr': 'INR'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   13,
  'opstr': 'DCR'},
 {'arg': ['C', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   14,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   15,
  'opstr': 'RRC'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   16,
  'opstr': 'NOP'},
 {'arg': ['D', 'd16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   17,
  'opstr': 'LXI'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   18,
  'opstr': 'STAX'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   19,
  'opstr': 'INX'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   20,
  'opstr': 'INR'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   21,
  'opstr': 'DCR'},
 {'arg': ['D', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   22,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   23,
  'opstr': 'RAL'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   24,
  'opstr': 'NOP'},
 {'arg': ['D'],
  'l': 1,
  'f': {   'C': True,    },
  'c': [10,10],
  'type':TYPE_LOGIC_16,
  'op':   25,
  'opstr': 'DAD'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MISC,
  'op':   26,
  'opstr': 'LDAX'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   27,
  'opstr': 'DCX'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   28,
  'opstr': 'INR'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   29,
  'opstr': 'DCR'},
 {'arg': ['E', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   30,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   31,
  'opstr': 'RAR'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   32,
  'opstr': 'NOP'},
 {'arg': ['H', 'd16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   33,
  'opstr': 'LXI'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [16,16],
  'type':TYPE_MOVE_16,
  'op':   34,
  'opstr': 'SHLD'},
 {'arg': ['H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   35,
  'opstr': 'INX'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   36,
  'opstr': 'INR'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   37,
  'opstr': 'DCR'},
 {'arg': ['H', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   38,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   39,
  'opstr': 'DAA'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   40,
  'opstr': 'NOP'},
 {'arg': ['H'],
  'l': 1,
  'f': {   'C': True,    },
  'c': [10,10],
  'type':TYPE_LOGIC_16,
  'op':   41,
  'opstr': 'DAD'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [16,16],
  'type':TYPE_MOVE_16,
  'op':   42,
  'opstr': 'LHLD'},
 {'arg': ['H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   43,
  'opstr': 'DCX'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   44,
  'opstr': 'INR'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   45,
  'opstr': 'DCR'},
 {'arg': ['L', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   46,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   47,
  'opstr': 'CMA'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   48,
  'opstr': 'NOP'},
 {'arg': ['SP', 'd16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   49,
  'opstr': 'LXI'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [13,13],
  'type':TYPE_MOVE_8,
  'op':   50,
  'opstr': 'STA'},
 {'arg': ['SP'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   51,
  'opstr': 'INX'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [10,10],
  'type':TYPE_LOGIC_8,
  'op':   52,
  'opstr': 'INR'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [10,10],
  'type':TYPE_LOGIC_8,
  'op':   53,
  'opstr': 'DCR'},
 {'arg': ['M', 'd8'],
  'l': 2,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_8,
  'op':   54,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   55,
  'opstr': 'STC'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   56,
  'opstr': 'NOP'},
 {'arg': ['SP'],
  'l': 1,
  'f': {   'C': True,    },
  'c': [10,10],
  'type':TYPE_LOGIC_16,
  'op':   57,
  'opstr': 'DAD'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [13,13],
  'type':TYPE_MISC,
  'op':   58,
  'opstr': 'LDA'},
 {'arg': ['SP'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_LOGIC_16,
  'op':   59,
  'opstr': 'DCX'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   60,
  'opstr': 'INR'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,    'S': True,  'Z': True, 'P': True},
  'c': [5,5],
  'type':TYPE_LOGIC_8,
  'op':   61,
  'opstr': 'DCR'},
 {'arg': ['A', 'd8'],
  'l': 2,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   62,
  'opstr': 'MVI'},
 {'arg': [],
  'l': 1,
  'f': {   'C': True,    },
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   63,
  'opstr': 'CMC'},
 {'arg': ['B', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   64,
  'opstr': 'MOV'},
 {'arg': ['B', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   65,
  'opstr': 'MOV'},
 {'arg': ['B', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   66,
  'opstr': 'MOV'},
 {'arg': ['B', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   67,
  'opstr': 'MOV'},
 {'arg': ['B', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   68,
  'opstr': 'MOV'},
 {'arg': ['B','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   69,
  'opstr': 'MOV'},
 {'arg': ['B', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   70,
  'opstr': 'MOV'},
 {'arg': ['B', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   71,
  'opstr': 'MOV'},
 {'arg': ['C', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   72,
  'opstr': 'MOV'},
 {'arg': ['C', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   73,
  'opstr': 'MOV'},
 {'arg': ['C', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   74,
  'opstr': 'MOV'},
 {'arg': ['C', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   75,
  'opstr': 'MOV'},
 {'arg': ['C', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   76,
  'opstr': 'MOV'},
 {'arg': ['C','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   77,
  'opstr': 'MOV'},
 {'arg': ['C', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   78,
  'opstr': 'MOV'},
 {'arg': ['C', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   79,
  'opstr': 'MOV'},
 {'arg': ['D', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   80,
  'opstr': 'MOV'},
 {'arg': ['D', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   81,
  'opstr': 'MOV'},
 {'arg': ['D', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   82,
  'opstr': 'MOV'},
 {'arg': ['D', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   83,
  'opstr': 'MOV'},
 {'arg': ['D', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   84,
  'opstr': 'MOV'},
 {'arg': ['D','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   85,
  'opstr': 'MOV'},
 {'arg': ['D', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   86,
  'opstr': 'MOV'},
 {'arg': ['D', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   87,
  'opstr': 'MOV'},
 {'arg': ['E', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   88,
  'opstr': 'MOV'},
 {'arg': ['E', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   89,
  'opstr': 'MOV'},
 {'arg': ['E', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   90,
  'opstr': 'MOV'},
 {'arg': ['E', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   91,
  'opstr': 'MOV'},
 {'arg': ['E', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   92,
  'opstr': 'MOV'},
 {'arg': ['E','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   93,
  'opstr': 'MOV'},
 {'arg': ['E', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   94,
  'opstr': 'MOV'},
 {'arg': ['E', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   95,
  'opstr': 'MOV'},
 {'arg': ['H', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   96,
  'opstr': 'MOV'},
 {'arg': ['H', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   97,
  'opstr': 'MOV'},
 {'arg': ['H', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   98,
  'opstr': 'MOV'},
 {'arg': ['H', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   99,
  'opstr': 'MOV'},
 {'arg': ['H', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   100,
  'opstr': 'MOV'},
 {'arg': ['H','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   101,
  'opstr': 'MOV'},
 {'arg': ['H', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   102,
  'opstr': 'MOV'},
 {'arg': ['H', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   103,
  'opstr': 'MOV'},
 {'arg': ['L', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   104,
  'opstr': 'MOV'},
 {'arg': ['L', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   105,
  'opstr': 'MOV'},
 {'arg': ['L', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   106,
  'opstr': 'MOV'},
 {'arg': ['L', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   107,
  'opstr': 'MOV'},
 {'arg': ['L', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   108,
  'opstr': 'MOV'},
 {'arg': ['L','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   109,
  'opstr': 'MOV'},
 {'arg': ['L', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   110,
  'opstr': 'MOV'},
 {'arg': ['L', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   111,
  'opstr': 'MOV'},
 {'arg': ['M', 'B'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   112,
  'opstr': 'MOV'},
 {'arg': ['M', 'C'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   113,
  'opstr': 'MOV'},
 {'arg': ['M', 'D'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   114,
  'opstr': 'MOV'},
 {'arg': ['M', 'E'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   115,
  'opstr': 'MOV'},
 {'arg': ['M', 'H'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   116,
  'opstr': 'MOV'},
 {'arg': ['M','L'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   117,
  'opstr': 'MOV'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MISC,
  'op':   118,
  'opstr': 'HLT'},
 {'arg': ['M', 'A'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   119,
  'opstr': 'MOV'},
 {'arg': ['A', 'B'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   120,
  'opstr': 'MOV'},
 {'arg': ['A', 'C'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   121,
  'opstr': 'MOV'},
 {'arg': ['A', 'D'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   122,
  'opstr': 'MOV'},
 {'arg': ['A', 'E'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   123,
  'opstr': 'MOV'},
 {'arg': ['A', 'H'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   124,
  'opstr': 'MOV'},
 {'arg': ['A','L'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   125,
  'opstr': 'MOV'},
 {'arg': ['A', 'M'],
  'l': 1,
  'f': { },
  'c': [7,7],
  'type':TYPE_MOVE_8,
  'op':   126,
  'opstr': 'MOV'},
 {'arg': ['A', 'A'],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_8,
  'op':   127,
  'opstr': 'MOV'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   128,
  'opstr': 'ADD'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   129,
  'opstr': 'ADD'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   130,
  'opstr': 'ADD'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   131,
  'opstr': 'ADD'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   132,
  'opstr': 'ADD'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   133,
  'opstr': 'ADD'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   134,
  'opstr': 'ADD'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   135,
  'opstr': 'ADD'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   136,
  'opstr': 'ADC'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   137,
  'opstr': 'ADC'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   138,
  'opstr': 'ADC'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   139,
  'opstr': 'ADC'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   140,
  'opstr': 'ADC'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   141,
  'opstr': 'ADC'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   142,
  'opstr': 'ADC'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   143,
  'opstr': 'ADC'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   144,
  'opstr': 'SUB'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   145,
  'opstr': 'SUB'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   146,
  'opstr': 'SUB'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   147,
  'opstr': 'SUB'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   148,
  'opstr': 'SUB'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   149,
  'opstr': 'SUB'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   150,
  'opstr': 'SUB'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   151,
  'opstr': 'SUB'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   152,
  'opstr': 'SBB'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   153,
  'opstr': 'SBB'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   154,
  'opstr': 'SBB'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   155,
  'opstr': 'SBB'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   156,
  'opstr': 'SBB'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   157,
  'opstr': 'SBB'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   158,
  'opstr': 'SBB'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   159,
  'opstr': 'SBB'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   160,
  'opstr': 'ANA'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   161,
  'opstr': 'ANA'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   162,
  'opstr': 'ANA'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   163,
  'opstr': 'ANA'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   164,
  'opstr': 'ANA'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   165,
  'opstr': 'ANA'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   166,
  'opstr': 'ANA'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   167,
  'opstr': 'ANA'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   168,
  'opstr': 'XRA'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   169,
  'opstr': 'XRA'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   170,
  'opstr': 'XRA'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   171,
  'opstr': 'XRA'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   172,
  'opstr': 'XRA'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   173,
  'opstr': 'XRA'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   174,
  'opstr': 'XRA'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   175,
  'opstr': 'XRA'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   176,
  'opstr': 'ORA'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   177,
  'opstr': 'ORA'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   178,
  'opstr': 'ORA'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   179,
  'opstr': 'ORA'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   180,
  'opstr': 'ORA'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   181,
  'opstr': 'ORA'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   182,
  'opstr': 'ORA'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_LOGIC_8,
  'op':   183,
  'opstr': 'ORA'},
 {'arg': ['B'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   184,
  'opstr': 'CMP'},
 {'arg': ['C'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   185,
  'opstr': 'CMP'},
 {'arg': ['D'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   186,
  'opstr': 'CMP'},
 {'arg': ['E'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   187,
  'opstr': 'CMP'},
 {'arg': ['H'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   188,
  'opstr': 'CMP'},
 {'arg': ['L'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   189,
  'opstr': 'CMP'},
 {'arg': ['M'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_COMPARE,
  'op':   190,
  'opstr': 'CMP'},
 {'arg': ['A'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [4,4],
  'type':TYPE_COMPARE,
  'op':   191,
  'opstr': 'CMP'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   192,
  'opstr': 'RNZ'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   193,
  'opstr': 'POP'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   194,
  'opstr': 'JNZ'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   195,
  'opstr': 'JMP'},
 {'arg': ['a16'],
  'f': { },
  'c':[17,11],
  'l': 3,
  'type':TYPE_BRANCH,
  'op':   196,
  'opstr': 'CNZ'},
 {'arg': ['B'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_MOVE_16,
  'op':   197,
  'opstr': 'PUSH'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   198,
  'opstr': 'ADI'},
 {'arg': ['0'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   199,
  'opstr': 'RST'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   200,
  'opstr': 'RZ'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   201,
  'opstr': 'RET'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   202,
  'opstr': 'JZ'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   203,
  'opstr': 'JMP'},
 {'arg': ['a16'],
  'f': { },
  'type':TYPE_BRANCH,
  'l': 3,
  'op':   204,
  'c':[17,11],
  'opstr': 'CZ'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [17,17],
  'type':TYPE_BRANCH,
  'op':   205,
  'opstr': 'CALL'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   206,
  'opstr': 'ACI'},
 {'arg': ['1'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   207,
  'opstr': 'RST'},
 {'arg': [],
  'f': { },
 'l': 1,
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   208,
  'opstr': 'RNC'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   209,
  'opstr': 'POP'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   210,
  'opstr': 'JNC'},
 {'arg': ['d8'],
  'l': 2,
  'f': { },
  'c': [10,10],
  'type':TYPE_MISC,
  'op':   211,
  'opstr': 'OUT'},
 {'arg': ['a16'],
  'f': { },
  'c':[17,11],
  'l': 3,
  'type':TYPE_BRANCH,
  'op':   212,
  'opstr': 'CNC'},
 {'arg': ['D'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_MOVE_16,
  'op':   213,
  'opstr': 'PUSH'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   214,
  'opstr': 'SUI'},
 {'arg': ['2'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   215,
  'opstr': 'RST'},
 {'arg': [],
   'l': 1,
  'f': { },
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   216,
  'opstr': 'RC'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   217,
  'opstr': 'RET'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   218,
  'opstr': 'JC'},
 {'arg': ['d8'],
  'l': 2,
  'f': { },
  'c': [10,10],
  'type':TYPE_MISC,
  'op':   219,
  'opstr': 'IN'},
 {'arg': ['a16'],
  'f': { },
  'l': 3,
  'type':TYPE_BRANCH,
  'op':   220,
  'c':[17,11],
  'opstr': 'CC'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [17,17],
  'type':TYPE_BRANCH,
  'op':   221,
  'opstr': 'CALL'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   222,
  'opstr': 'SBI'},
 {'arg': ['3'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   223,
  'opstr': 'RST'},
 {'arg': [],
  'f': { },
  'l': 1,
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   224,
  'opstr': 'RPO'},
 {'arg': ['H'],
  'l': 1,
  'f': { },
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   225,
  'opstr': 'POP'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   226,
  'opstr': 'JPO'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [18,18],
  'type':TYPE_MOVE_16,
  'op':   227,
  'opstr': 'XTHL'},
 {'arg': ['a16'],
  'f': { },
  'l': 3,
  'c':[17,11],
  'type':TYPE_BRANCH,
  'op':   228,
  'opstr': 'CPO'},
 {'arg': ['H'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_MISC,
  'op':   229,
  'opstr': 'PUSH'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   230,
  'opstr': 'ANI'},
 {'arg': ['4'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   231,
  'opstr': 'RST'},
 {'arg': [],
  'f': { },
  'l': 1,
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   232,
  'opstr': 'RPE'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_BRANCH,
  'op':   233,
  'opstr': 'PCHL'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   234,
  'opstr': 'JPE'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_16,
  'op':   235,
  'opstr': 'XCHG'},
 {'arg': ['a16'],
  'f': { },
  'type':TYPE_BRANCH,
  'l': 3,
  'op':   236,
  'c':[17,11],
  'opstr': 'CPE'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [17,17],
  'type':TYPE_BRANCH,
  'op':   237,
  'opstr': 'CALL'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   238,
  'opstr': 'XRI'},
 {'arg': ['5'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   239,
  'opstr': 'RST'},
 {'arg': [],
  'f': { },
  'l': 1,
  'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   240,
  'opstr': 'RP'},
 {'arg': ['PSW'],
  'l': 1,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [10,10],
  'type':TYPE_MOVE_16,
  'op':   241,
  'opstr': 'POP'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   242,
  'opstr': 'JP'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   243,
  'opstr': 'DI'},
 {'arg': ['a16'],
  'f': { },
  'l': 3,
  'c':[17,11],
  'type':TYPE_BRANCH,
  'op':   244,
  'opstr': 'CP'},
 {'arg': ['PSW'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_MOVE_16,
  'op':   245,
  'opstr': 'PUSH'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_LOGIC_8,
  'op':   246,
  'opstr': 'ORI'},
 {'arg': ['6'],
  'l': 1,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   247,
  'opstr': 'RST'},
 {'arg': [],
  'l': 1,
  'f': { },
'c':[11,5],
  'type':TYPE_BRANCH,
  'op':   248,
  'opstr': 'RM'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [5,5],
  'type':TYPE_MOVE_16,
  'op':   249,
  'opstr': 'SPHL'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [10,10],
  'type':TYPE_BRANCH,
  'op':   250,
  'opstr': 'JM'},
 {'arg': [],
  'l': 1,
  'f': { },
  'c': [4,4],
  'type':TYPE_MISC,
  'op':   251,
  'opstr': 'EI'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'type':TYPE_BRANCH,
  'op':   252,
  'opstr': 'CM'},
 {'arg': ['a16'],
  'l': 3,
  'f': { },
  'c': [17,17],
  'type':TYPE_BRANCH,
  'op':   253,
  'opstr': 'CALL'},
 {'arg': ['d8'],
  'l': 2,
  'f': { 'A': True,  'C': True,  'S': True,  'Z': True, 'P': True},
  'c': [7,7],
  'type':TYPE_COMPARE,
  'op':   254,
  'opstr': 'CPI'},
 {'arg': ['7'],
  'l': 1		,
  'f': { },
  'c': [11,11],
  'type':TYPE_BRANCH,
  'op':   255,
  'opstr': 'RST'}]



