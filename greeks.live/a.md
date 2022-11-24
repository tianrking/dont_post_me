```bash
curl 'https://www.greeks.live/ddh/strategy/edit' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: ph_phc_UlbOZqDIVLNVC2uoyTfUBMZ2gGvjUOc1fG9xHTKCbjZ_posthog=%7B%22distinct_id%22%3A%22266545%22%2C%22%24device_id%22%3A%22184a9651f8a94e-0558faaedec802-7d5d5471-144000-184a9651f8b16fc%22%2C%22%24user_id%22%3A%22266545%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24initial_referring_domain%22%3A%22greeks.live%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fgreeks.live%2F%22%2C%22%24referring_domain%22%3A%22greeks.live%22%2C%22%24sesid%22%3A%5B1669289287564%2C%22184a9651e80172c-02feb6c927e662-7d5d5471-144000-184a9651e811bf8%22%2C1669289287296%5D%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D; session=eyJrZXkiOiJ2eGZCUnJ0aSJ9.Y39aGw.NyYcdENpsmeB3YvsyEh26WfOfGU; lang=zh' \
  -H 'Origin: https://www.greeks.live' \
  -H 'Referer: https://www.greeks.live/ddh/strategy/list' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"type":"AdvancedDynamicDeltaStrategy","curr":"ETH","subId":266545,"param":{"isRun":true,"maxPositiveCoinDelta":1,"maxNegativeCoinDelta":1,"maxPositiveUsdDelta":1000,"maxNegativeUsdDelta":1000,"positiveHedgeRatio":100,"negativeHedgeRatio":100,"coinTargetDelta":0,"usdTargetDelta":0,"eachOrderSize":2,"makerEachOrderSize":20,"longFuture":"ETH-PERPETUAL","shortFuture":"ETH-PERPETUAL","coinDeltaMode":false,"orderType":"taker"}}' \
  --compressed
```