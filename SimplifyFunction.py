
class SimplifyFraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")
        # to get the gcd and simplified fraction, the fraction is simplified
        # with both the numerator and denominator positive.
        # self._is_negative tracks the original signage of the fraction
        self._numerator = abs(numerator)
        self._denominator = abs(denominator)
        self.is_negative = (numerator < 0) ^ (denominator < 0)
        self.gcd = self._gcd_algorithm()
        self.simplified = self._simplify()

    def _gcd_algorithm(self) -> int:
        # Euclidian Algorithm
        dividend = (
            self._numerator if self._numerator > self._denominator
            else self._denominator)  # bigger number
        divisor = (
            self._numerator if self._numerator < self._denominator
            else self._denominator)  # smaller number
        remainder = dividend % divisor
        while remainder > 0:
            dividend = divisor
            divisor = remainder
            remainder = dividend % remainder
        return divisor

    def _simplify(self) -> tuple[int, int]:
        s_numerator = self._numerator // self.gcd
        s_denominator = self._denominator // self.gcd
        # account for original signage of fraction
        if self.is_negative:
            s_numerator = -s_numerator
        return (s_numerator, s_denominator)

    def get_simplified_fraction(self) -> tuple[int, int]:
        """Returns the simplified fraction as a string"""
        (new_numerator, new_denominator) = self.simplified
        #if new_denominator == 1:
            #return new_numerator
        return (new_numerator, new_denominator)

    def get_gcd(self) -> int:
        """Returns the greatest common divisor"""
        return self.gcd

def get_fraction() -> tuple[int, int]:
    nums_str = input("\nEnter numerator, denominator separated by /: ")
    if len(nums_str) == 1:
        return 'q'
    separator = "," if "," in nums_str else "/"
    nums = nums_str.split(separator)
    numerator = int(nums[0].strip())
    denominator = int(nums[1].strip())
    return (numerator, denominator)

"""if __name__ == "__main__":
    while (fraction := get_fraction()) != 'q':
        numerator, denominator = fraction
        simplified_fraction = SimplifyFraction(numerator, denominator).get_simplified_fraction()
        print(f"\tSimplified fraction: {simplified_fraction}")
    print("\nGoodbye!\n")"""
