# Simulation for testing speciation in envirionments
# como e o caso dos OCBILs
#------------------------------------------------------------------------------
# Duas populacoes com fluxos de gametas masculinos e femininos entre si.
# Cada individuo e definido por duas sequencias que representam seu material
# genetico: uma para o nucleo e uma para o citoplasma.
#

# size of encoding sequences
SEQ_SIZE = 100

# tamanhos populacionais
P1 = 10
P2 = 10

# taxa de mutacao
m = 0.01

# probabilidade do gameta masculino(feminino) migrar
fn = 0.5
fc = 0.5

INITIAL_SEQ = [0]*SEQ_SIZE

# Nuclear sequences
N1 = [INITIAL_SEQ]*P1
N2 = [INITIAL_SEQ]*P2

# Citoplasmatic sequences
C1 = [INITIAL_SEQ]*P1
C2 = [INITIAL_SEQ]*P2
