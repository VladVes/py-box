import numpy as np
import matplotlib.pyplot as plt
import math

n = np.linspace(1, 20, 400)

o1 = np.ones_like(n) * 1
olog = np.log2(n)
on = n
onlogn = n * np.log2(n)
on2 = n**2
o2n = 2**n

# Для факториала берём только точки с целыми n и ограничиваем диапазон, чтобы не переполнить
ofac_vals = []
for x in n:
    ix = int(round(x))
    if ix < 1 and ix > 20:
        ofac_vals.append(np.nan)
    else:
        try:
            ofac_vals.append(math.factorial(ix))
        except OverflowError:
            ofac_vals.append(np.nan)
ofac = np.array(ofac_vals)

plt.figure(figsize=(10, 6))
plt.plot(n, o1, label='O(1)', linewidth=2)
plt.plot(n, olog, label='O(log n)', linewidth=2)
plt.plot(n, on, label='O(n)', linewidth=2)
plt.plot(n, onlogn, label='O(n log n)', linewidth=2)
plt.plot(n, on2, label='O(n^2)', linewidth=2)
plt.plot(n, o2n, label='O(2^n)', linewidth=2, linestyle='--')
plt.plot(n, ofac, label='O(n!)', linewidth=2, linestyle='-.')

plt.yscale('log')
plt.xlabel('Размер входных данных (n)')
plt.ylabel('Количество операций (логарифмическая шкала)')
plt.title('Зависимость количества операций от объёма данных (Big O)')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
# plt.show()
plt.savefig('big_o_plot.png', dpi=300)
print("График сохранён как big_o_plot.png")