function solution(participant, completion) {
    var answer = '';
  	let part = {}
  	for (let x of participant){
      if(part.hasOwnProperty(x)){
        part[x] += 1
      }else{
        part[x] = 1
      }
    }
  	// console.log(part)
    for (let x of completion){
        part[x] -= 1
    }
    // console.log(part)
    for (let x in part){
      if(part[x]>0){
        answer += x;
      }
    }
    return answer;
}