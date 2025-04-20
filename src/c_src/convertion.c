
int convert_and_add_one_time(float x) {
    return (int)x + 1;
}

int convert_and_add_one_million(float x) {
    volatile int a =0;
    for(int i=0; i<1000000; i++){
        a += ((int)x + 1);
    }
    return a;
}
