#define NUM_SAMPLES 10

int sum1 = 0;                    // sum of samples taken
int sum2 = 0;
int sum3 = 0;
int sum4 = 0;
int sum5 = 0;
unsigned char sample_count = 0; // current sample number
float voltage1 = 0.0;            // calculated voltage
float voltage2 = 0.0;
float voltage3 = 0.0;
float voltage4 = 0.0;
float voltage5 = 0.0;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    delay(1000);
    // take a number of analog samples and add them up
    while (sample_count < NUM_SAMPLES) {
        sum1 += analogRead(A0);
        sum2 += analogRead(A1);
        sum3 += analogRead(A2);
        sum4 += analogRead(A3);
        sum5 += analogRead(A4);
        sample_count++;
        delay(10);
    }
    // calculate the voltage
    // use 5.0 for a 5.0V ADC reference voltage
    // 5.015V is the calibrated reference voltage
    voltage1 = ((float)sum1 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    voltage2 = ((float)sum2 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    voltage3 = ((float)sum3 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    voltage4 = ((float)sum4 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    voltage5 = ((float)sum5 / (float)NUM_SAMPLES * 5.015) / 1024.0;
    // send voltage for display on Serial Monitor
    // voltage multiplied by 11 when using voltage divider that
    // divides by 11. 11.132 is the calibrated voltage divide
    // value
    Serial.print(voltage1 * 11.0);
    Serial.print(" ");
    Serial.print(voltage2 * 11.0);
    Serial.print(" ");
    Serial.print(voltage3 * 11.0);
    Serial.print(" ");
    Serial.print(voltage4 * 11.0);
    Serial.print(" ");
    Serial.println(voltage5 * 11.0);
    sample_count = 0;
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    sum5 = 0;    
}
