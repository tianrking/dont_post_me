//go mod init 
//
package main

import (
	"fmt"
	"io/ioutil"
	// "log"
	"encoding/json"
	"net/http"
	"github.com/gin-gonic/gin"
	"strings"
)



func main() {

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.GET("/news", func(c *gin.Context) {

		// https://mholt.github.io/json-to-go/  JSON-to-Go
		// 先構造json s 再利用 json.Unmarshal(body, &s) 解析
		type Jin10 struct {
			IP                 string      `json:"ip"`
			Version            string      `json:"version"`
			City               string      `json:"city"`
			Region             string      `json:"region"`
			RegionCode         string      `json:"region_code"`
			Country            string      `json:"country"`
			CountryName        string      `json:"country_name"`
			CountryCode        string      `json:"country_code"`
			CountryCodeIso3    string      `json:"country_code_iso3"`
			CountryCapital     string      `json:"country_capital"`
			CountryTld         string      `json:"country_tld"`
			ContinentCode      string      `json:"continent_code"`
			InEu               bool        `json:"in_eu"`
			Postal             interface{} `json:"postal"`
			Latitude           float64     `json:"latitude"`
			Longitude          float64     `json:"longitude"`
			Timezone           string      `json:"timezone"`
			UtcOffset          string      `json:"utc_offset"`
			CountryCallingCode string      `json:"country_calling_code"`
			Currency           string      `json:"currency"`
			CurrencyName       string      `json:"currency_name"`
			Languages          string      `json:"languages"`
			CountryArea        float64     `json:"country_area"`
			CountryPopulation  int         `json:"country_population"`
			Asn                string      `json:"asn"`
			Org                string      `json:"org"`
			CityCode           string      `json:"city_code"`
			Weather            string      `json:"weather"`
		}

		
		response, err := http.Get("http://49.234.208.23:1234/")
    	if err != nil || response.StatusCode != http.StatusOK {
         	c.Status(http.StatusServiceUnavailable)
        	return
      	}
		// response := `{"servers":[{"serverName":"Shanghai_VPN","serverIP":"127.0.0.1"},{"serverName":"Beijing_VPN","serverIP":"127.0.0.2"}]}`
		
		// defer resp.Body.Close()  //不關閉怎麽樣？
		body, _ := ioutil.ReadAll(response.Body)
    	var s Jin10
		
		json.Unmarshal(body, &s)
		// json.Unmarshal(response, &s)、


		// fmt.Println(s)

		fmt.Printf("%T\n", response)
		fmt.Printf("%T\n", response.Body)
		fmt.Printf("%T\n", body)
		fmt.Printf("%T\n", s)

		c.JSON(200,s)

		// response, err := http.Get("http://49.234.208.23:1234/")
    	// if err != nil || response.StatusCode != http.StatusOK {
        //  	c.Status(http.StatusServiceUnavailable)
        // 	return
      	// }

		// reader := response.Body
		// contentLength := response.ContentLength
		// contentType := response.Header.Get("Content-Type")
	
		// extraHeaders := map[string]string{
		// 	 //"Content-Disposition": `attachment; filename="gopher.png"`,
		// }
	
		// c.DataFromReader(http.StatusOK, contentLength, contentType, reader, extraHeaders)
	
		// c.JSON(200,bodyText)
		// c.JSON(200, gin.H{"message": bodyText})
		// fmt.Println(contentLength)
		// fmt.Println(contentType)
			
	

		// c.JSON(200, gin.H{"a":"aa"})
	})


	r.GET("/jin10_diy", func(c *gin.Context) {

		// var ss Jin10_diy

		rsps, err := http.Get("http://49.234.208.23:1234/jin10/3")
		if err != nil {
			fmt.Println("Request failed:", err)
			return
		}
		defer rsps.Body.Close()
	
		body, err := ioutil.ReadAll(rsps.Body) //uint8
		if err != nil {
			fmt.Println("Read body failed:", err)
			return
		}


		// json.Unmarshal(body, &ss)
		// c.JSON(200,gin.H{
		// 	"message": body,
		// })
		// c.String(200,string(body))
		gg_body := strings.Split(string(body), "]")[0]
		gg_body = strings.Split(string(gg_body), "[")[1]
		gg_body = strings.Trim(gg_body, "\"")
		bb := strings.Split(string(gg_body), ",")

		for i,s := range bb{
			bb[i]=strings.Trim(s, "\"")
		}
		
		fmt.Printf("%T\n",bb)
		fmt.Printf("%s\n",bb)
		c.JSON(200,gin.H{"1":bb[0],"2":bb[1],"3":bb[2]})
		fmt.Println(string(body))
	})

	r.Run(":8088")
}