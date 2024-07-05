const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
    // split 메서드 : 문자열을 특정 구분자를 기준으로 분리하여 배열로 만들어 주는 함수
    // console.log("line:", line) // line: 4 5
    // console.log("input:", input) // input: [ '4', '5' ]
    
}).on('close', function () {
    // console.log(Number(input[0]) + Number(input[1]));
    console.log("a =", input[0])
    console.log("b =", input[1])
});