function solution(nums) {
  let dic = {};
  for (let i of nums) {
    if (dic.hasOwnProperty(i)) {
      dic[i] += 1;
    } else {
      dic[i] = 1;
    }
  }
  console.log(Object.keys(dic).length);
  if (Object.keys(dic).length >= nums.length / 2) {
    return nums.length / 2;
  } else {
    return Object.keys(dic).length;
  }
}
