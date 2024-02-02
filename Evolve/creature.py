from random import choice, randint


hex_digits = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f'
]


class Creature:
    def __init__(self, genome:list=[], num_of_genomes:int=10001) -> None:
        self.num_of_genomes = num_of_genomes
        self.genome=genome


    def Create_Genome(self):
        self.genome=[]
        for _ in range(self.num_of_genomes):
            gene = []
            for _ in range(11):
                gene.append(choice(hex_digits))
            self.genome.append(''.join(item for item in gene))

    def Inherite(self, parent1:list, parent2:list):
        index = 0
        for _ in range(self.num_of_genomes):
            parent = randint(0, 1)

            if parent == 0:
                gene = self.Mutation(parent=parent1, index=index)
                self.genome.append(gene)
            elif parent == 1:
                gene = self.Mutation(parent=parent2, index=index)
                self.genome.append(gene)

            index += 1

        return parent1, parent2
    
    def Mutation(self, parent:list, index:int=0):
        gene_index = 0
        gene = []
        try:
            for item in parent[index]:
                gene.append(item)
        except IndexError:
            pass
        for item in gene:
            mutation = randint(1, 1001)
            if mutation <= 10:
                gene[gene_index] = choice(hex_digits)
                gene_index += 1

        return ''.join(item for item in gene)