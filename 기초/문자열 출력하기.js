// [모듈 불러오기]
// readline 변수로 readline 모듈을 불러온다.
// readline 모듈은 콘솔에서 입력을 읽고 출력하는 기능을 제공한다.
const readline = require('readline');

// [interface 객체 만들기] : interface 객체를 이용하여 콘솔에서 표준 입출력 처리
// rl 변수로 input과 output interface를 생성한다.
// 이 인터페이스 객체 rl을 통해 콘솔에서 입력을 받고 출력할 수 있다.
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = []; // 입력받은 데이터를 저장할 배열 input을 선언

// [입출력 코드 작성하기]
// rl.on이 연속으로 붙어 있는데 각 라인마다 실행 후 종료, 실행 후 종료를 반복한다.

// line 이벤트는 사용자가 Enter 키를 눌러 한 줄을 입력할 때마다 발생한다.
// function (line) 콜백 함수가 실행되며, line에는 입력된 문자열이 담긴다.
// input = [line];을 통해 입력된 값을 input 배열에 저장한다. (이 경우, 항상 최신 입력값 하나만 저장된다.)

// close 이벤트는 입력이 끝났을 때 발생한다.
// function() 콜백 함수가 실행되며, input[0]에 저장된 첫 번째 입력값을 변수 str에 저장한다.

rl.on('line', function (line) {
    // 입력 받은 값을 처리하는 코드
    input = [line]; // [ 'HelloWorld!' ]
}).on('close',function(){
    // 입력이 끝나고 실행하는 코드
    str = input[0];
    console.log(str)
});