import random

class MeerSchwein:
    def __init__(self, genotype, generation):
        genotype_sorted = {}
        for feature, genes in genotype.items():
            genotype_sorted[feature] = ''.join(sorted(genes))
        self.genotype = genotype_sorted
        self.generation = generation
    def print(self):
        print("My generation is " + str(self.generation) + ", and my genotype is " + str(self.genotype))
    def phaenotype(self):
        # calculate phaenotype from genotype
        genotype = self.genotype
        phaeno_type = {}            
        for feature, gene in genotype.items():
            phaeno_type[feature] = sorted(gene)[0]
        return phaeno_type
            
def mate(mama_meerschwein, papa_meerschwein):
        # main function - generate n babys with random genotypes from parents
        litter_size = random.randint(1,6)
        litter = [None]*litter_size
        for i in range(litter_size):
            litter[i] = MeerSchwein({},None)
            litter[i].generation = mama_meerschwein.generation + 1
            for feature, genes in mama_meerschwein.genotype.items():
                # we assume that mama and papa meerschwein features match
                mama_random = mama_meerschwein.genotype[feature][random.randint(0,1)]
                papa_random = papa_meerschwein.genotype[feature][random.randint(0,1)]
                litter[i].genotype[feature] = ''.join(sorted([mama_random, papa_random]))
        return litter






