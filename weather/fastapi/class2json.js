// import  './city.js'
import { city_data } from './city.js'
import fs from 'fs'
// city_data
//console.log(city_data)

const data = JSON.stringify(city_data)
console.log(data)

// fs.write(JSON.parse(data))

fs.writeFile('./city.json', data, function (err) {
    if (err) {
        console.error(err);
    }
    console.log('success');
})

