from Evolve.creature import Creature
from time import perf_counter


start = perf_counter()

creature1 = Creature(num_of_genomes=11)
creature1.Create_Genome()

creature2 = Creature(num_of_genomes=11)
creature2.Create_Genome()

creature3 = Creature(num_of_genomes=11)
creature3.Inherite(creature1.genome, creature2.genome)

print()
print(f"Parent1: {'|'.join(item for item in creature1.genome)}", end='|\n')
print(f"Parent2: {'|'.join(item for item in creature2.genome)}", end='|\n')
print()
print(f"Child: {'|'.join(item for item in creature3.genome)}", end='|\n')

print(f"\ntime: {perf_counter()-start} sec")