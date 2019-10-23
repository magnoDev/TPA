def QuickSort(X, IniVet, FimVet):

        i = IniVet
        j = FimVet
        pivo = X[(IniVet + FimVet) // 2]

        while (i <= j):
            while (X[i] < pivo):
                i = i + 1
            # fimEnquanto
            while (X[j] > pivo):
                j = j - 1
            # fimEnquanto
            if (i <= j):
                aux = X[i]
                X[i] = X[j]
                X[j] = aux
                i = i + 1
                j = j - 1
            # fimSe
            # fimEnquanto

            if (IniVet < j):
                QuickSort(X, IniVet, j)
            # fimSe
            if (i < FimVet):
                QuickSort(X, i, FimVet)
            # fimSe
# fimProcedimento