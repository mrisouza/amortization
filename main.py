from System.AmortizationSystems import AmortizationSystems
from Inputs.params import *


def main():
    """ """
    A = AmortizationSystems(
        principal=params["principal"], time=params["time"], rate=params["rate"]
    )
    A.evaluateSAC()
    print(A.getDf())


if __name__ == "__main__":
    main()
