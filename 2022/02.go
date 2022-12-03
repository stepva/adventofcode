package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	input := load_input("2022/input_02.txt")

	equivalent := map[string]string{
		"X": "A",
		"Y": "B",
		"Z": "C",
	}

	wins := map[string]string{
		"A": "C",
		"B": "A",
		"C": "B",
	}

	loses := map[string]string{
		"C": "A",
		"A": "B",
		"B": "C",
	}

	scores := map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
	}

	score_1, score_2 := 0, 0

	for _, l := range input {
		var elf string
		var me string

		fmt.Sscanf(l, "%s %s", &elf, &me)
		
		meAbc := equivalent[me]
		gameScore := 0
		if wins[meAbc] == elf {
			gameScore = 6
		} else if meAbc == elf {
			gameScore = 3
		}
		score_1 = score_1 + gameScore + scores[meAbc]

		if me == "X" {
			meShould := wins[elf]
			score_2 = score_2 + scores[meShould]
		} else if me == "Y" {
			score_2 = score_2 + scores[elf] + 3
		} else if me == "Z" {
			meShould := loses[elf]
			score_2 = score_2 + scores[meShould] + 6
		}

	}

	// ANSWER 1
	fmt.Println((score_1))

	// ANSWER 2
	fmt.Println((score_2))
}