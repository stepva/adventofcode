package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func load_input(path string) ([]string) { 
	f, err := os.Open(path)
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

	var input []string 

    // read the file line by line using scanner
    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
        // do something with a line
        input = append(input, scanner.Text())
	}

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	return input
}

func main() {
	input := load_input("2022/input_01.txt")

	var calories []int
	currentElf := 0

	for _, c := range input {
		if c == "" {
			calories = append(calories, currentElf)
			currentElf = 0
		} else {
			cal, _ := strconv.Atoi(c)
			currentElf = currentElf + cal
		}
	}

	sort.Ints(calories)

	// ANSWER 1
	fmt.Println(calories[len(calories)-1])

	top_three := 0
	for _, c := range calories[len(calories)-3:] {
		top_three = top_three + c
	}

	// ANSWER 2
	fmt.Println(top_three)

}
