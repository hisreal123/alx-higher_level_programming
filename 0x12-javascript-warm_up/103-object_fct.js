#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// myObject.push((incr = () => this.value++));
// function () {
//   this.value++;
// };

const incr = () => {
  myObject.value++;
};

myObject.incr = incr;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
