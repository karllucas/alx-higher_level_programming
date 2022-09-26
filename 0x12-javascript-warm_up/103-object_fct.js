#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);
const incr = myObject.map(object => {
  return object.value += 1;
});
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
