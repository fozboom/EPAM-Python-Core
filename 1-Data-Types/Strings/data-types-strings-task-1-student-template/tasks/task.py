def get_fractions(a_b: str, c_b: str) -> str:
    numerator1, denominator1 = map(int, a_b.split('/'))
    numerator2, denominator2 = map(int, c_b.split('/'))
    result_denominator = denominator1
    return f'{a_b} + {c_b} = {numerator1 + numerator2}/{result_denominator}'
