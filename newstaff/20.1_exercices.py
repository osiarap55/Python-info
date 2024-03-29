class stadistic:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2)
        else:
            return sorted_data[n // 2]

    def mode(self):
        from collections import Counter
        counts = Counter(self.data)
        mode_values = [k for k, v in counts.items() if v == max(counts.values())]
        return mode_values

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean_value = self.mean()
        squared_diff = [(x - mean_value) ** 2 for x in self.data]
        return sum(squared_diff) / len(self.data)
    

    def standard_deviation(self):
        import math
        return math.sqrt(self.variance())

    def minimun(self):
        return min(self.data)

    def maximun(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile (self, percentile_value):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        index = int((percentile_value / 100) * (n - 1))
        return sorted_data[index]

    def frequency_distribution(self):
        from collections import Counter
        return Counter(self.data)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = stadistic(ages)

print("mean:", data.mean())
print("media", data.median())
print("mode:", data.mode())
print("Range:", data.range())
print("variance:", data.variance())
print("standard deviation:", data.standard_deviation())
print("minimun:", data.minimun())
print("maximun:", data.maximun())
print("count:", data.count())
print("25 percentile", data.percentile(25))
print("75 percentile", data.percentile(75))
print("frequency_distribution:", data.frequency_distribution())



# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
