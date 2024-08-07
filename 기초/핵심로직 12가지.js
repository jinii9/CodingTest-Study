// 1. 배열 순회
a = [1, 3, 45, 2, 10]
a.forEach((e, i) => {
    console.log(e, i)
    // 1 0
    // 3 1
    // 45 2
    // 2 3
    // 10 4
})

/////////////////////////////////////////////////////
// 2. 문자열분해
// 문자열 -> 배열
const str = "Hello World";
const ret = str.split(" ")
console.log(ret) // [ 'Hello', 'World' ]

// 배열 -> 문자열
const b = ret.join('')
console.log(b) // HelloWorld

// find, findIndex, includes, substring, slice, Object.keys, Object.values, Object.entries, Math.round, Math.ceil, Math.floor, Math.abs

/////////////////////////////////////////////////////
// 3. 정렬
/////////////////////////////////////////////////////
// 02:18 필터링
/////////////////////////////////////////////////////
// 02:52 배열재가공
/////////////////////////////////////////////////////
// 03:55 reduce
/////////////////////////////////////////////////////
// 04:42 그외 기본문법
/////////////////////////////////////////////////////
// 04:46 DFS
/////////////////////////////////////////////////////
// 07:06 이분탐색 
/////////////////////////////////////////////////////
// 12:06 배열생성팁
/////////////////////////////////////////////////////
// 13:20 DP - 피보나치
/////////////////////////////////////////////////////
// 15:54 스와핑