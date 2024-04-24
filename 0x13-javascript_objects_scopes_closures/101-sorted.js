exports.callMeMoby = function (x, theFunction) {
  // Validate the parameters
  if (typeof x !== 'number' || !Number.isInteger(x) || x <= 0) {
    throw new Error('The first parameter must be a positive integer.');
  }
  if (typeof theFunction !== 'function') {
    throw new Error('The second parameter must be a function.');
  }

  // Call the function x times
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
