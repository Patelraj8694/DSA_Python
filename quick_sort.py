# Quick Sort Algorithm

def Quick_Sort(arr: list):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i >= pivot]

        return Quick_Sort(smaller) + [pivot] + Quick_Sort(larger)

# passing data
data = [1, 5, 3, 2, 4]
sorted_data = Quick_Sort(data)
print("Sorted Data: ", sorted_data) 
