#!/usr/bin/node
// Reverses a list

exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;
  while (left <= right) {
    const temp = list[right];
    list[right] = list[left];
    list[left] = temp;
    left++;
    right--;
  }
  return (list);
};
