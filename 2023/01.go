package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func load_input(path string) ([]string) { 
	f, err := os.Open(path)
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

	var input []string 
    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
        input = append(input, scanner.Text())
	}

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	return input
}

var numbers = map[string]string{
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
}

func stringToNumString(r string) string {
	if d, ok := numbers[r]; ok {
		return d
	}
	return r
}

func main() {
	input := load_input("2023/input_01.txt")

	calibrationValue := 0
	var reg = regexp.MustCompile(`(\d)`)

	for _, l := range input {
		foundDigits := reg.FindAllString(l, -1)
		digits := strings.Join([]string {foundDigits[0], foundDigits[len(foundDigits)-1]}, "")
		num, _ := strconv.Atoi(digits)
		calibrationValue += num
	}

	// ANSWER 1
	fmt.Println(calibrationValue)


	// bullshit, go regexp doesn't support overlapping characters, I give up with this language
	calibrationValue2 := 0
	var reg2 = regexp.MustCompile(`(?=(\d|one|two|three|four|five|six|seven|eight|nine))`)

	for _, l := range input {
		foundDigitStrings := reg2.FindAllString(l, -1)
		foundDigitStrings = []string {foundDigitStrings[0], foundDigitStrings[len(foundDigitStrings)-1]}
		var foundDigits []string
		for _, r := range foundDigitStrings {
			foundDigits = append(foundDigits, stringToNumString(r))
		}
		digits := strings.Join(foundDigits, "")
		num, _ := strconv.Atoi(digits)
		calibrationValue2 += num
	}

	fmt.Println(calibrationValue2)
}
