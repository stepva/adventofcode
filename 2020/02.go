package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
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
	input := load_input("2020/input_02.txt")

	valid := 0

	for _, l := range input {
		s := strings.Split(l, " ")
		
		borders := strings.Split(s[0], "-")

		min_n, _ := strconv.Atoi(borders[0])
		max_n, _ := strconv.Atoi(borders[1])

		letter := string(string(s[1])[0])
		password := string(s[2])

		n := strings.Count(password, letter)
		if n >= min_n && n <= max_n {
			valid = valid + 1
		}
	}

	// ANSWER 1
	fmt.Println(valid)

	valid_two := 0

	for _, l := range input {
		s := strings.Split(l, " ")
		
		positions := strings.Split(s[0], "-")

		pos_a, _ := strconv.Atoi(positions[0])
		pos_b, _ := strconv.Atoi(positions[1])

		letter := string(string(s[1])[0])
		password := string(s[2])

		both := (letter == string(password[pos_a-1])) && (letter == string(password[pos_b-1]))
		at_least_one := (letter == string(password[pos_a-1])) || (letter == string(password[pos_b-1]))

		if at_least_one && !both {
			valid_two = valid_two + 1
		}
	}
	
	// ANSWER 2
	fmt.Println(valid_two)

}

// notes:
// fmt.Sscanf(l, "%d-%d %1s: %s", &lower, &upper, &char, &pw) cool way to parse a string of some format, instead of spliting multiple times!
// doing letter == string(password[pos_a-1]) twice is a waste
// go can do valid++ instead of valid = valid + 1