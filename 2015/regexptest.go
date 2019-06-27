package main

import (
	"fmt"
	"regexp"
)

func main() {
	r, err := regexp.Compile(`All (.*) go to (.*)`)
	if err != nil {
		fmt.Println("There was an error")
	}
	fmt.Println(r.FindAllStringSubmatch("All dogs go to heaven", -1)[0])
}
