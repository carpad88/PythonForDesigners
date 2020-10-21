# Estándar US
valor = 2345.67
f'{valor:n}'
# 2,345.67

# Estándar Italiano
import locale
locale.setlocale(locale.LC_ALL, 'it_IT')
f'{valor:n}'
# 2345,67
