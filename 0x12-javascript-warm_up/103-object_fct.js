#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const incr = (object) => {
  let object = myObject.value + 1;
  return object;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
