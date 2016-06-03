package main

import (
	"log"
	"io/ioutil"
	"strings"
	"fmt"
	"regexp"
)

func main() {

	m := make(map[string]string)
	
	m["View"] = "div"
	m["Text"] = "div"
	m["NavigatorIOS"] = "div"
	m["AppRegistry"] = "div"
	m["StyleSheet"] = "div"
	
	var reg1 string
	reg1 = "[\t]*?[ \t]*?<"

	//  Read input file
	fi, err := ioutil.ReadFile("index.ios.js")
	if err != nil {
					log.Fatalln(err)
	}
	//fmt.Println(fi)
	lines := strings.Split(string(fi))

	for i, line := range lines{
			for key, value := range m{
				match, _ := regexp.MatchString(line,reg1)
				if(match == true){
					if(strings.Contains(line, key)){
						lines[i] = strings.Replace(line, key, value, -1)	
						fmt.Println(i,key,value)
						
					}
					//fmt.Println(match , key)
				}
			}
		}
		output := strings.Join(lines, "\n")
		err = ioutil.WriteFile("index.line.js", []byte(output), 0644)
		if err != nil {
						log.Fatalln(err)
		}
}
