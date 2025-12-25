package main

import (
	"fmt"
)

func main() {
	count := 0
	for i := range 1_000_000_000 {
		if i%2 == 0 {
			count++
		}
	}
	fmt.Println(count)
}
