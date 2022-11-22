package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
    // open file
    f, err := os.Open("2020/input_01.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

	var input []int 

    // read the file line by line using scanner
    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
        // do something with a line
		i, _ := strconv.Atoi(scanner.Text())
        input = append(input, i)
	}

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	var smaller []int
	var larger []int

	for _, i := range input {
		if i < 1010 {
			smaller = append(smaller, i)
		} else {
			larger = append(larger, i)
		}
	}

	var entries [2]int

	for _, s := range smaller {
		for _, l := range larger {
			if s + l == 2020 {
				entries[0] = s
				entries[1] = l
				break
			}
		}
		if entries[0] != 0 {
			break
		}
	}

	// ANSWER 1
	fmt.Println(entries[0] * entries[1])

	var entries_trio [3]int

	for i := 0; i < len(smaller); i++ {
		first := smaller[i]
		for j := i; j < len(smaller); j++ {
			second := smaller[j]
			for k := j; k < len(smaller); k++ {
				third := smaller[k]

				if first + second + third == 2020 {
					entries_trio[0] = first
					entries_trio[1] = second
					entries_trio[2] = third
					break
				}
			}
			if entries_trio[0] == 0 {
				for _, l := range larger {
					if first + second + l == 2020 {
						entries_trio[0] = first
						entries_trio[1] = second
						entries_trio[2] = l
						break
					}
				}
			} 
			if entries_trio[0] != 0 {
				break
			}
		}
		if entries_trio[0] != 0 {
				break
		}
	}
	
	// ANSWER 2
	fmt.Println(entries_trio[0] * entries_trio[1] * entries_trio[2])
}