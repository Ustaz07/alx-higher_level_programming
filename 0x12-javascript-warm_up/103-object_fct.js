#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

myObject.value += 1;
myObject.incr = function () {
  myObject.value += 1;
};

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
