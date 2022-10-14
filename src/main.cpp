#include <Arduino.h>
#include <U8x8lib.h>
#include <PCF8563.h>
PCF8563 pcf;
#include <Wire.h>


U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* clock=*/PIN_WIRE_SCL, /* data=*/PIN_WIRE_SDA, /* reset=*/U8X8_PIN_NONE); // OLEDs without Reset of the Display
const int buttonPin = 1;
const int RRPin = 7;

// const int RECV_PIN = 7; // set pin 2 as IR control
// IRrecv irrecv(RECV_PIN);
// decode_results results;

#define ROTARY_ANGLE_SENSOR A0

int dis_val;
String val_case[10] = {"=         ","==        ","===       ","====      ","=====     ","======    ","=======   ","========  ","========= ","=========="};

void setup()
{
    Serial.begin(115200);
    u8x8.begin();
    u8x8.setFlipMode(1);
    Wire.begin();
    pcf.init();       // initialize the clock
    pcf.stopClock();  // stop the clock
    pcf.setYear(20);  // set year
    pcf.setMonth(10); // set month
    pcf.setDay(23);   // set dat
    pcf.setHour(17);  // set hour
    pcf.setMinut(33); // set minut
    pcf.setSecond(0); // set second
    pcf.startClock(); // start the clock

    pinMode(ROTARY_ANGLE_SENSOR, INPUT);
    pinMode(RRPin, OUTPUT);

    // Serial.begin(9600);
    // Serial.println("Enabling IRin"); // remind enabling IR
    // irrecv.enableIRIn();             // Start the receiver
    // Serial.println("Enabled IRin");
}

void loop()
{
    Time nowTime = pcf.getTime(); // get current time
    int sensor_value = analogRead(ROTARY_ANGLE_SENSOR);

    if(sensor_value>500){
        digitalWrite(RRPin, HIGH);
        u8x8.setCursor(5, 3);
        u8x8.print("On ");
    }
    if(sensor_value<500){
        u8x8.setCursor(5, 3);
        digitalWrite(RRPin, LOW);
        u8x8.print("OFF");
    }

    u8x8.setFont(u8x8_font_chroma48medium8_r); // choose a suitable font
    u8x8.setCursor(0, 0);
    u8x8.print(nowTime.day);
    u8x8.print("/");
    u8x8.print(nowTime.month);
    u8x8.print("/");
    u8x8.print("20");
    u8x8.print(nowTime.year);
    u8x8.setCursor(0, 1);
    u8x8.print(nowTime.hour);
    u8x8.print(":");
    u8x8.print(nowTime.minute);
    u8x8.print(":");
    u8x8.println(nowTime.second);

    u8x8.setCursor(0, 3);
    dis_val = sensor_value >= 1000 ? 999 : sensor_value;
    u8x8.print(dis_val);

    // u8x8.setCursor(0, 5);
    // u8x8.print("");

    u8x8.setCursor(3, 5);
    u8x8.println(val_case[dis_val/100]);


    delay(1000);
}
