#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
};
console.log(myObject);
const incr = myObject.map(object => {
  const increased = object.value += 1;
  return increased;
});
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
