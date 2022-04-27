package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"github.com/gin-gonic/gin"
)

func main() {

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.GET("/news", func(c *gin.Context) {

		client := &http.Client{}
		req, err := http.NewRequest("GET", "https://www.cls.cn/nodeapi/refreshTelegraphList?app=CailianpressWeb&lastTime=1646659780&os=web&sv=7.7.5&sign=639d4a54e68a1270edb70d96f13b9112", nil)
		if err != nil {
			log.Fatal(err)
		}
		req.Header.Set("Connection", "keep-alive")
		req.Header.Set("sec-ch-ua", " Not A;Brand;v=99, Chromium;v=99, Google Chrome;v=99")
		req.Header.Set("Accept", "application/json, text/plain, */*")
		req.Header.Set("Content-Type", "application/json;charset=utf-8")
		req.Header.Set("sec-ch-ua-mobile", "?0")
		req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
		req.Header.Set("sec-ch-ua-platform", "Windows")
		req.Header.Set("Sec-Fetch-Site", "same-origin")
		req.Header.Set("Sec-Fetch-Mode", "cors")
		req.Header.Set("Sec-Fetch-Dest", "empty")
		req.Header.Set("Referer", "https://www.cls.cn/telegraph")
		req.Header.Set("Accept-Language", "zh-TW,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5,en-US;q=0.4")
		req.Header.Set("If-None-Match", "W/28c2-X0O5ToV+Bo+BEkphYl8yKLoLPac")
		req.Header.Set("Cookie", "HWWAFSESID=3a3d276fad28eb8931; HWWAFSESTIME=1646659798349; hasTelegraphRemind=on; hasTelegraphSound=on; vipNotificationState=on; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1646659764,1646659766; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1646659766; hasTelegraphNotification=off")
		resp, err := client.Do(req)
		if err != nil {
			log.Fatal(err)
		}
		defer resp.Body.Close()
		bodyText, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%s\n", bodyText)

		// c.JSON(200,bodyText)
		// c.JSON(200, gin.H{"message": bodyText})
		c.JSON(http.StatusOK,bodyText)
	})

	r.Run(":8088")
}