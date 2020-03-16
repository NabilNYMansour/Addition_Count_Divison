def ManDivQR(Numerator, Denominator):
    '''
    - Divides the Numerator{int} with the Denominator{int} using Addition Count Division algorithm (Mansourian Division algorithm).
    - returns (Quotient{int}, NumeratorRemainder{int}, DenominatorRemainder{int}) where Remainder = NumeratorRemainder/DenominatorRemainder.
    '''
    # If division by zero.
    if Denominator == 0:
        return None
    # Initializing the return values.
    Quotient, NumeratorRemainder, DenominatorRemainder = 0, 0, 0
    # Initializing the algorithm values.
    Count, Check, Result = 0, 0, 0
    if Denominator > Numerator:
        NumeratorRemainder = Numerator
        DenominatorRemainder = Denominator
    elif Denominator == Numerator:
        Quotient = 1
    else:
        Done = False
        while not Done:
            Result += 1
            if Result == Denominator:
                Check += Result
                Result = 0
                Count += 1
            if Check == Numerator:
                Quotient = Count
                DenominatorRemainder = Denominator
                Done = True
            elif Check > Numerator:
                Quotient = Count - 1
                NumeratorRemainder = Numerator + Denominator - Check
                DenominatorRemainder = Denominator
                Done = True
    return Quotient, NumeratorRemainder, DenominatorRemainder


def ManDivPoint(Numerator, Denominator, numberOfDecimalPoint):
    '''
    - Divides the Numerator{int} with the Denominator{int} using Addition Count Division algorithm (Mansourian Division algorithm).
    - Utilizes ManDivQR(Numerator, Denominator).
    - returns a decimal representation up to numberOfDecimalPoint{int} as a String.
    '''
    (Quotient, NumeratorRemainder) = ManDivQR(Numerator, Denominator)[0:2]
    if NumeratorRemainder == 0:
        return str(Quotient) + ".0"
    else:
        ToReturn = str(Quotient) + "."
        for _ in range(numberOfDecimalPoint):
            (Quotient, NumeratorRemainder) = ManDivQR(
                NumeratorRemainder * 10, Denominator)[0:2]
            ToReturn += str(Quotient)
        return ToReturn


# Testing:
print(ManDivQR(50, 43))
print(ManDivPoint(50, 43, 10))
