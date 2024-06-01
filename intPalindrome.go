package main

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	temp, result := x, 0

	for temp > 0 {
		result = (result * 10) + temp%10
		temp = temp / 10
	}

	return x == result
}
