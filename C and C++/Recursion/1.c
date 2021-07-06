void fun(int n){
    if (n>0){
    fun(n-1);
    printf("%d ",n);
    
    }
}
int main(){
    int x;
    x=3;
    fun(x);
    return 0;
}

// function call before print- 123
// function call after print- 321
