import os
import pandas as pd

COLUMNNAMES = ["Saldo Devedor", "Parcela", "Juros", "Amortizacao"]
OUTPUT = os.path.join(".", "outputs")


class AmortizationSystems(object):
    """ """

    def __init__(self, principal, time, rate):
        """ """
        self.principal = float(principal)
        self.time = int(time)
        self.rate = float(rate) / 1200

        self.df = pd.DataFrame(index=range(self.time + 1), columns=COLUMNNAMES)

    def __setAmortization(self):
        """ """
        self.df["Amortizacao"] = self.principal / self.time
        self.df.loc[0, "Amortizacao"] = 0

    def __setDevedor(self):
        """ """
        self.df.loc[0, "Saldo Devedor"] = self.principal
        for i in range(self.time):
            self.df.loc[i + 1, "Saldo Devedor"] = (
                self.df.loc[i, "Saldo Devedor"] - self.principal / self.time
            )

    def __setJuros(self):
        """ """
        self.df["Juros"] = self.df["Saldo Devedor"] * self.rate
        self.df["Juros"] = self.df["Juros"].shift(1)
        self.df.loc[0, "Juros"] = 0

    def __setParcelas(self):
        """ """
        self.df["Parcela"] = self.df["Juros"] + self.df["Amortizacao"]

    def __evaluateSAC(self):
        """ """
        self.__setAmortization()
        self.__setDevedor()
        self.__setJuros()
        self.__setParcelas()

    def __saveToFile(self):
        """ """
        try:
            self.df.to_csv(os.path.join(OUTPUT, "output.csv"))

        except:
            raise RuntimeError()

    def evaluateSAC(self):
        """ """
        self.__evaluateSAC()
        self.__saveToFile()

    def getDf(self):
        return self.df
