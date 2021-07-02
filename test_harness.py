from Exercise_Visualizer import cell_to_list

# Test harness

# Testing cell_to_list function
assert cell_to_list("[]") == []
assert cell_to_list("[10101010100]") == [10101010100]
assert cell_to_list("[1,2,3,4]") == [1,2,3,4]
assert cell_to_list("[1,2,3,4,5,6,7,8]") == [1,2,3,4,5,6,7,8]
assert cell_to_list("[10,2,38,900,1000000]") == [10,2,38,900,1000000]
