from bubble_sort import bubble
from insertion_sort import insertion
from selection_sort import selection
from my_algo import my_bubble
from merge_sort import merge_split
from quick_sort import sort_quick
import random
import time
li = [random.randint(1, 10000) for i in range(1, 10000)]

st = time.time()
bu = bubble(li)
print(f"bubble, {time.time()-st}")

st = time.time()
bu = bubble(li)
print(f"bubble, {time.time()-st}")

st = time.time()
ins = insertion(li)
print(f"insertion, {time.time()-st}")

st = time.time()
sel = selection(li)
print(f"selection, {time.time()-st}")


st = time.time()
merge = merge_split(li)
print(f"merge, {time.time()-st}")

st = time.time()
merge = sort_quick(li, 0, len(li)-1)
print(f"merge, {time.time()-st}")




if bu == ins == sel == merge:
    print("oho")
