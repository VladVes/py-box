def div_mod(divisible: int, divisor: int) -> tuple[float, float]:
    quotient = divisible // divisor
    remainder = divisible % divisor
    return (quotient, remainder)