package main

import (
	"fmt"
	"os"
	"log"
	"bufio"
	"strings"
	"strconv"
)

func printusage() {
	fmt.Printf("Usage: %s <packages file>\n\nFind how much wrapping paper is needed to wrap all the packages described in <packages file>\n", os.Args[0])
	log.Fatal("FATAL: no filename given")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func min(is ...int) int {
	min := is[0]
	for _, i := range is[1:] {
		if i < min {
			min = i
		}
	}
	return min
}

func main() {
	total_area := 0

	var fname string

	if (len(os.Args) > 2) || ((len(os.Args) == 2) && (os.Args[1] == "-h")) || ((len(os.Args) == 2) && (os.Args[1] == "--help")) {
		printusage()
	}

	if (len(os.Args) == 2) {
		fname = os.Args[1]
	} else {
		fname = "day2.txt"
	}

	f, err := os.Open(fname)
	check(err)

	s := bufio.NewScanner(f)

	for s.Scan() {
		splitline := strings.Split(s.Text(), "x")
		l, err := strconv.Atoi(splitline[0])
		check(err)
		w, err := strconv.Atoi(splitline[1])
		check(err)
		h, err := strconv.Atoi(splitline[2])
		check(err)
		total_area += 2*l*w+2*w*h+2*h*l+min(l*w,w*h,h*l)
	}

	fmt.Printf("%v square feet of wrapping paper is needed to wrap all the presents\n", total_area)
}
