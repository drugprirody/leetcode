package main

func singleNumber(nums []int) int {
	numsMap := map[int]bool{}
	for _, num := range nums {
		val, ok := numsMap[num]
		if ok && val == true {
			numsMap[num] = false
		} else if !ok {
			numsMap[num] = true
		}
	}
	for key, val := range numsMap {
		if val {
			return key
		}
	}
	return 0
}
