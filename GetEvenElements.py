def separate_even_odd_indexes(elements):
    # Separate elements with even and odd indexes
    even_index_elements = [elements[i] for i in range(len(elements)) if i % 2 == 0]
    odd_index_elements = [elements[i] for i in range(len(elements)) if i % 2 != 0]
    
    # Return the separated elements
    return even_index_elements, odd_index_elements

def separate_even_indexes(elements):
    # Separate elements with even and odd indexes
    even_index_elements = [elements[i] for i in range(len(elements)) if i % 2 == 0]
    # odd_index_elements = [elements[i] for i in range(len(elements)) if i % 2 != 0]   
    # Return the separated elements
    return even_index_elements

def separate_odd_indexes(elements):
    # Separate elements with even and odd indexes
    # even_index_elements = [elements[i] for i in range(len(elements)) if i % 2 == 0]
    odd_index_elements = [elements[i] for i in range(len(elements)) if i % 2 != 0]
    
    # Return the separated elements
    return odd_index_elements

# Test the function with a list of elements
elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
even_index_elements, odd_index_elements = separate_even_odd_indexes(elements)

# Print the results
print(f"Elements with even indexes: {even_index_elements}")
print(f"Elements with odd indexes: {odd_index_elements}")
