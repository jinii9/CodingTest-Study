const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
    
}).on('close', function () {
    str = input[0]; 
    n = Number(input[1]); // str 개수
    answer = ''
    
    // 1번째 방법
    // for (let i=0; i<n; i++){
    //     answer += str;
    // }
    
    // 2번째 방법
    // 문자열 n번 반복
    answer = str.repeat(n);
    
    console.log(answer)
});