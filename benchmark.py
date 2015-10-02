import timeit


print( "Quick Sort" )

print( "One thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(1000)]
from quickSort import quickSort
'''

print( min( timeit.Timer('a=s[:]; quickSort(0, 1000, a)', setup=setup).repeat(10, 100) ) )

print( "Ten thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(10000)]
from quickSort import quickSort
'''

print( min( timeit.Timer('a=s[:]; quickSort(0, 10000, a)', setup=setup).repeat(10, 100) ) )

print( "One hundred thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(100000)]
from quickSort import quickSort
'''

print( min( timeit.Timer('a=s[:]; randomQuickSort(0, 100000, a)', setup=setup).repeat(10, 100) ) )



print( "Random Quick Sort" )

print( "One thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(1000)]
from randomQuickSort import randomQuickSort
'''

print( min( timeit.Timer('a=s[:]; randomQuickSort(0, 1000, a)', setup=setup).repeat(10, 100) ) )

print( "Ten thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(10000)]
from randomQuickSort import randomQuickSort
'''

print( min( timeit.Timer('a=s[:]; randomQuickSort(0, 10000, a)', setup=setup).repeat(10, 100) ) )

print( "One hundred thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(100000)]
from randomQuickSort import randomQuickSort
'''

print( min( timeit.Timer('a=s[:]; randomQuickSort(0, 100000, a)', setup=setup).repeat(10, 100) ) )



print( "Median Random Quick Sort" )

print( "One thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(1000)]
from medianRandomQuickSort import medianRandomQuickSort
'''

print( min( timeit.Timer('a=s[:]; medianRandomQuickSort(0, 1000, a)', setup=setup).repeat(10, 100) ) )

print( "Ten thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(10000)]
from medianRandomQuickSort import medianRandomQuickSort
'''

print( min( timeit.Timer('a=s[:]; medianRandomQuickSort(0, 10000, a)', setup=setup).repeat(10, 100) ) )

print( "One hundred thousand elements" )

setup = '''
import random
random.seed('12345')
s = [random.random() for i in range(100000)]
from medianRandomQuickSort import medianRandomQuickSort
'''

print( min( timeit.Timer('a=s[:]; medianRandomQuickSort(0, 100000, a)', setup=setup).repeat(10, 100) ) )