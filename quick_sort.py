# Quick Sort Algorithm

def Quick_Sort(arr: list):
    # Base case if array is empty or has only one element
    if len(arr) <=1:
        return arr
    else:
        # Selecting pivot element
        pivot = arr[0]
        # Creating two lists to store elements smaller and larger than pivot element
        smaller = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i >= pivot]
        # Recursively calling Quick_Sort function on smaller and larger list
        return Quick_Sort(smaller) + [pivot] + Quick_Sort(larger)

# passing data
data = [1, 5, 3, 2, 4]
sorted_data = Quick_Sort(data)
print("Sorted Data: ", sorted_data) 
