package main

func singleNumber(nums []int) int {
	var result int

	for _, n := range nums {
		result ^= n
	}

	return result
}
