import Code.Nanoparticle as NP
import Code.FCCLattice as FCC
import Code.EnergyCalculator as EC

if __name__ == '__main__':
    #lattice = FCC.FCCLattice(15, 15, 15, 2)

    #p = NP.Nanoparticle(lattice)
    #p.kozlov_sphere(5, ['Pt', 'Au'], [23, 79 - 23])

    #emt_calculator = EC.EMTCalculator()
    #emt_calculator.compute_energy(p)
    #p.save('hi')
    p = NP.Nanoparticle(None)
    p.load('hi.pcl')
    print(p.lattice.width)



